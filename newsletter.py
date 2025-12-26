import datetime
import webbrowser
import os
import requests
import markdown
import feedparser
from bs4 import BeautifulSoup

# Expires after 1 year as ASF forbids access to their repositories
# with endless tokens.
GITHUB_API_TOKEN = os.environ["TOKEN_GITHUB_API"]
GITHUB_RELEASES_API = "https://api.github.com/repos/{ORG}/{REPO}/releases"
NEWSLETTER_NEWS_md = "https://api.github.com/repos/amol-/monthly-python-dataeng/contents/NEWS.md"
NOW = datetime.datetime.utcnow()
START_DATE = NOW - datetime.timedelta(days=31)


def fetch_news_entries():
    news_entries = requests.get(NEWSLETTER_NEWS_md,
                                   headers={"Accept": "application/vnd.github.v3+json",
                                           "Authorization": f"token {GITHUB_API_TOKEN}"}).json()
    # print(news_entries)
    download_url = news_entries["download_url"]
    content = requests.get(download_url).text
    
    github_releases = []
    html_blogs = []
    xml_feeds = []
    for entry in content.split("\n"):
        if not entry:
            continue
        _, url = entry.split(" ", 1)
        url, *webpage = url.split("|")
        if webpage:
            webpage = ''.join(webpage).strip()
        else:
            webpage = url
        url = url.strip()
        if "github.com" in url:
            repo_url = url[len("https://github.com/"):]
            org, repo, *_ = repo_url.split("/", 3)
            github_releases.append((url, org, repo, webpage))
        elif url.endswith(".xml"):
            xml_feeds.append(url)
        else:
            html_blogs.append(url)
    return github_releases, html_blogs, xml_feeds


def fetch_releases(org, repo):
    github_releases = requests.get(GITHUB_RELEASES_API.format(ORG=org, REPO=repo),
                                   headers={"Accept": "application/vnd.github.v3+json",
                                           "Authorization": f"token {GITHUB_API_TOKEN}"}).json()
    print("RELEASES FOR", org, repo, ":", len(github_releases))

    release_infos = []
    for release in github_releases:
        release_date = release["published_at"] # "2013-02-27T19:35:32Z"
        release_date = _parse_github_date(release_date)
        if release_date < START_DATE:
            break

        release_name = release["name"]
        release_notes = release["body"]
        release_url = release["html_url"]
        release_infos.append((release_date, release_name, release_notes, release_url))
    return release_infos


def _parse_github_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")


def fetch_rss_posts(url):
    content = requests.get(url).text
    feed = feedparser.parse(content)

    blog_url = feed.feed.link
    blog_title = feed.feed.title

    articles = []
    for entry in feed.entries:
        published_date = datetime.datetime(*entry.published_parsed[:6])
        if published_date < START_DATE:
            break

        soup = BeautifulSoup(entry.description)
        content_preview = soup.get_text()
        articles.append((published_date, entry.title, content_preview[:1024], entry.link))

    return blog_url, blog_title, articles

def fetch_html_posts(url):
    content = requests.get(url).text
    
    if "spark.apache.org" in url:
        return _parse_spark_blog(content)
    if "arrow.apache.org" in url:
        return _parse_arrow_blog(content)
    else:
        print(f"\tUNSUPPORTED: {url}")


def _parse_spark_blog(content):
    SPARK_BLOG_BASE_URL = "https://spark.apache.org"

    blog_articles = []

    sp = BeautifulSoup(content, "html5lib")
    articles = sp.find_all('article')
    for article in articles:
        title = article.select_one(".entry-title").text
        article_url = article.select_one(".entry-title > a")["href"]
        date = article.select_one(".entry-date").text
        content = article.select_one(".entry-content > p").text
        date = _parse_USA_date(date)
        if date < START_DATE:
            break
        blog_articles.append((date, title, content, SPARK_BLOG_BASE_URL + article_url))

    return blog_articles


def _parse_arrow_blog(content):
    ARROW_BLOG_BASE_URL = "https://arrow.apache.org"

    blog_articles = []

    sp = BeautifulSoup(content, "html5lib")
    article_headers = sp.select('main > h3')
    for article_header in article_headers:
        header_anchor = article_header.select_one("a")
        title = header_anchor.text
        article_url = header_anchor["href"]
        article_header_sibling = article_header.find_next_sibling()
        date_element = article_header_sibling.select_one(".blog-list-date")
        if not date_element:
            continue
        date = date_element.text.strip()
        date = _parse_eng_date(date)
        if date < START_DATE:
            break
        blog_articles.append((date, title, "", ARROW_BLOG_BASE_URL + article_url))

    return blog_articles


def _parse_USA_date(date):
    return datetime.datetime.strptime(date, "%B %d, %Y")


def _parse_eng_date(date):
    return datetime.datetime.strptime(date, "%d %B %Y")


def main():
    mkdown = ""

    github_releases, html_blogs, xml_feeds = fetch_news_entries()
    downloaded_data = {}

    mkdown += "# Complete List of Projects\n"
    for releases_url, project_org, project_name, project_page in github_releases:
        print(f"[GH] Fetching {project_org}/{project_name}")
        recent_releases = fetch_releases(project_org, project_name)
        if not recent_releases:
            continue
        downloaded_data[(project_org, project_name)] = recent_releases
        mkdown += f" * Project: {project_org}/{project_name} has {len(recent_releases)} releases\n"
    for url in html_blogs:
        print(f"[HTML] Fetching {url}")
        recent_articles = fetch_html_posts(url)
        if not recent_articles:
            continue
        downloaded_data[url] = recent_articles
        mkdown += f" * Project: {url} has {len(recent_articles)} releases\n"
    for url in xml_feeds:
        print(f"[RSS] Fetching {url}")
        blog_url, blog_title, recent_articles = fetch_rss_posts(url)
        if not recent_articles:
            continue
        downloaded_data[url] = (blog_url, blog_title, recent_articles)
        mkdown += f" * Project: {url} has {len(recent_articles)} releases\n"
    mkdown += "\n\n"

    mkdown += "# Releases for each project\n"
    
    # Process HTML Blogs without RSS
    for url in html_blogs:
        print(f"[HTML] Processing {url}")
        recent_articles = downloaded_data.get(url)
        if not recent_articles:
            continue

        mkdown += f"## Project: [{url}]({url}), {len(recent_articles)} articles\n"
        for recent_article in recent_articles:
            article_date, article_title, article_content, article_url = recent_article
            mkdown += f"### Release: [{article_title}]({article_url})\n"
            # mkdown += article_content
            mkdown += "\n"

    # Process RSS Blogs
    for url in xml_feeds:
        print(f"[RSS] Processing {url}")
        data = downloaded_data.get(url)
        if not data:
            continue
        
        blog_url, blog_title, recent_articles = data
        mkdown += f"## Project: [{blog_title}]({blog_url}), {len(recent_articles)} articles\n"
        for recent_article in recent_articles:
            article_date, article_title, article_content, article_url = recent_article
            mkdown += f"### Release: [{article_title}]({article_url})\n"
            # mkdown += article_content
            mkdown += "\n"

    # Process GitHub Releases
    for releases_url, project_org, project_name, project_page in github_releases:
        print(f"[GH] Processing {project_org}/{project_name}")
        recent_releases = downloaded_data.get((project_org, project_name))
        if not recent_releases:
            continue

        release_names = [name for _, name, *_ in recent_releases]
        mkdown += f"## Project: [{project_org}/{project_name}]({project_page}), {len(recent_releases)} releases: {release_names}\n"
        for recent_release in recent_releases:
            release_date, release_name, release_notes, release_url = recent_release
            mkdown += f"### Release: {project_name} [{release_name}]({release_url})\n"
            mkdown += release_notes
            mkdown += "\n"

    with open("newsletter.md", "w+") as f:
        f.write(mkdown)
    with open("newsletter.html", "w+") as f:
        f.write(markdown.markdown(mkdown))

    webbrowser.open(f"file://{os.getcwd()}/newsletter.html", new=1)

if __name__ == "__main__":
    main()
