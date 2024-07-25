import datetime
import requests
import markdown

GITHUB_API_TOKEN = "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"
GITHUB_RELEASES_API = "https://api.github.com/repos/{ORG}/{REPO}/releases"
NEWSLETTER_NEWS_md = "https://api.github.com/repos/amol-/modern-datascience/contents/NEWS.md"
NOW = datetime.datetime.utcnow()
START_DATE = NOW - datetime.timedelta(days=31)


def fetch_news_entries():
    news_entries = requests.get(NEWSLETTER_NEWS_md,
                                   headers={"Accept": "application/vnd.github.v3+json",
                                           "Authorization": f"token {GITHUB_API_TOKEN}"}).json()
    download_url = news_entries["download_url"]
    content = requests.get(download_url).text
    
    github_releases = []
    blogs = []
    for entry in content.split("\n"):
        if not entry:
            continue
        _, url = entry.split(" ", 1)
        if "github.com" in url:
            repo_url = url[len("https://github.com/"):]
            org, repo, *_ = repo_url.split("/", 3)
            github_releases.append((url, org, repo))
        else:
            blogs.append(url)
    return github_releases, blogs


def fetch_releases(org, repo):
    github_releases = requests.get(GITHUB_RELEASES_API.format(ORG=org, REPO=repo),
                                   headers={"Accept": "application/vnd.github.v3+json",
                                           "Authorization": f"token {GITHUB_API_TOKEN}"}).json()

    release_infos = []
    for release in github_releases:
        release_date = release["published_at"] # "2013-02-27T19:35:32Z"
        release_date = _parse_github_date(release_date)
        if release_date < START_DATE:
            break

        release_name = release["name"]
        release_notes = release["body"]
        release_infos.append((release_date, release_name, release_notes))
    return release_infos


def _parse_github_date(date):
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")


def main():
    mkdown = ""

    github_releases, blogs = fetch_news_entries()
    for releases_url, project_org, project_name in github_releases:
        print(f"Processing {project_org}/{project_name}")
        recent_releases = fetch_releases(project_org, project_name)
        if not recent_releases:
            continue

        mkdown += f"# [{project_org}/{project_name}]({releases_url})\n"
        for recent_release in recent_releases:
            release_date, release_name, release_notes = recent_release
            mkdown += f"## ⇰⇰ {release_name}\n"
            mkdown += release_notes
            mkdown += "\n"

    with open("newsletter.html", "w+") as f:
        f.write(markdown.markdown(mkdown))


if __name__ == "__main__":
    main()
