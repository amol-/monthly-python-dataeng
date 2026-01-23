# Complete List of Projects
 * Project: apache/arrow has 2 releases
 * Project: substrait-io/substrait-python has 1 releases
 * Project: narwhals-dev/narwhals has 1 releases
 * Project: pola-rs/polars has 2 releases
 * Project: pandas-dev/pandas has 2 releases
 * Project: holoviz/panel has 1 releases
 * Project: pyscript/pyscript has 1 releases
 * Project: cython/cython has 2 releases
 * Project: plotly/dash has 2 releases
 * Project: dask/dask has 2 releases
 * Project: delta-io/delta-rs has 4 releases
 * Project: lancedb/lance has 10 releases
 * Project: lancedb/lancedb has 6 releases
 * Project: datafusion-contrib/datafusion-table-providers has 3 releases
 * Project: datafusion-contrib/datafusion-table-providers has 3 releases
 * Project: unionai-oss/pandera has 2 releases
 * Project: https://spark.apache.org/news/index.html has 3 releases
 * Project: https://velox-lib.io/blog/rss.xml has 2 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 1 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 3 articles
### Release: [Spark 3.5.8 released](https://spark.apache.org/news/spark-3-5-8-released.html)

### Release: [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview1-released.html)

### Release: [Spark 4.1.1 released](https://spark.apache.org/news/spark-4-1-1-released.html)

## Project: [Velox Blog](https://velox-lib.io/blog), 2 articles
### Release: [Task Barrier: Efficient Task Reuse and Streaming Checkpoints in Velox](https://velox-lib.io/blog/task-barrier)

### Release: [Why Sort is row-based in Velox — A Quantitative Assessment](https://velox-lib.io/blog/why-row-based-sort)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 1 articles
### Release: [Extending SQL in DataFusion: from ->> to TABLESAMPLE](https://datafusion.apache.org/blog/2026/01/12/extending-sql)

## Project: [apache/arrow](https://arrow.apache.org/docs/python/), 2 releases: ['Apache Arrow 23.0.0', 'Apache Arrow 23.0.0 RC2']
### Release: arrow [Apache Arrow 23.0.0](https://github.com/apache/arrow/releases/tag/apache-arrow-23.0.0)
Release Notes URL: https://arrow.apache.org/release/23.0.0.html
### Release: arrow [Apache Arrow 23.0.0 RC2](https://github.com/apache/arrow/releases/tag/apache-arrow-23.0.0-rc2)
Release Notes: Release Candidate: 23.0.0 RC2
## Project: [substrait-io/substrait-python](https://substrait.io/), 1 releases: ['v0.26.0']
### Release: substrait-python [v0.26.0](https://github.com/substrait-io/substrait-python/releases/tag/v0.26.0)
## What's Changed
* chore: drop support for python 3.9 by @tokoko in https://github.com/substrait-io/substrait-python/pull/122
* feat(cast): add alias for cast expression by @giospada in https://github.com/substrait-io/substrait-python/pull/127
* fix: correct if_then and switch_expression type inference calls by @giospada in https://github.com/substrait-io/substrait-python/pull/128
* feat(write): add write table builder and tests by @giospada in https://github.com/substrait-io/substrait-python/pull/129
* feat: add substrait spec version to plan by @nielspardon in https://github.com/substrait-io/substrait-python/pull/132
* feat(types): add comprehensive type support and stricter validation by @giospada in https://github.com/substrait-io/substrait-python/pull/130
* feat: add select builder by @tokoko in https://github.com/substrait-io/substrait-python/pull/125
* chore(deps): bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/126
* chore(deps): bump actions/download-artifact from 6 to 7 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/133
* chore(deps): bump actions/upload-artifact from 5 to 6 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/134
* feat: narwhals-compliant dataframe setup by @tokoko in https://github.com/substrait-io/substrait-python/pull/112
* chore: move dev extras to dependency-groups by @tokoko in https://github.com/substrait-io/substrait-python/pull/135
* feat: added FunctionType parameter to FunctionEntry by @giospada in https://github.com/substrait-io/substrait-python/pull/136
* chore: remove dependency on protoletariat and update protobuf by @nielspardon in https://github.com/substrait-io/substrait-python/pull/138
* chore: use pixi for codegen environment in ci by @tokoko in https://github.com/substrait-io/substrait-python/pull/137
* fix: added the handling for all the substrait type in cover by @giospada in https://github.com/substrait-io/substrait-python/pull/139
* fix: change protoc version to v29.5 and protobuf to >=5 by @nielspardon in https://github.com/substrait-io/substrait-python/pull/141
* chore: configure ruff to reorder imports by @tokoko in https://github.com/substrait-io/substrait-python/pull/140
* fix: use version from src/substrait/__init__.py by @nielspardon in https://github.com/substrait-io/substrait-python/pull/143
* chore(substrait): bump to v0.79.0 by @tokoko in https://github.com/substrait-io/substrait-python/pull/142

## New Contributors
* @giospada made their first contribution in https://github.com/substrait-io/substrait-python/pull/127

**Full Changelog**: https://github.com/substrait-io/substrait-python/compare/v0.25.0...v0.26.0
## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 1 releases: ['Narwhals v2.15.0']
### Release: narwhals [Narwhals v2.15.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.15.0)
## Changes

- test: unxfail sqlframe tests for list functions (#3383)
- ci: Test fairlearn using pytest marker (#3234)

## ✨ Enhancements

- test: unxfail sqlframe for `list.median` (#3387)
- feat: Add `{Expr,Series}.sin` (#3365)
- feat: add `list.sort` (#3356)

## 🐞 Bug fixes

- test: Various GPU fixes (#3390)
- test: separate numpy array for tests (#3385)
- fix(docs): Keep table filter only in api-completeness page (#3367)
- ci: Fix `hierarchicalforecast` installation (#3362)

## 📖 Documentation

- fix(docs): Keep table filter only in api-completeness page (#3367)

## 🛠️ Other improvements

- chore: Refactor pandas-like pyarrow branching (#3361)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @liamholmes31, @raisadz

## Project: [pola-rs/polars](https://docs.pola.rs/), 2 releases: ['Python Polars 1.37.1', 'Python Polars 1.37.0']
### Release: polars [Python Polars 1.37.1](https://github.com/pola-rs/polars/releases/tag/py-1.37.1)
## 🚀 Performance improvements

- Speed up `SQL` interface "UNION" clauses (#26039)

## 🐞 Bug fixes

- Optimize slicing support on compressed IPC (#26071)
- CPU check for musl builds (#26076)
- Propagate C Stream import errors instead of panicking (#26036)
- Fix slicing on compressed IPC (#26066)

## 📖 Documentation

- Clarify min\_by/max\_by behavior on ties (#26077)

## 🛠️ Other improvements

- Mark top slow normal tests as slow (#26080)
- Update breaking deps (#26055)
- Fix for upstream url bug and update deps (#26052)
- Properly pin chrono (#26051)
- Don't run rust doctests (#26046)
- Update deps (#26042)
- Ignore very slow test (#26041)

Thank you to all our contributors for making this release possible!
@Voultapher, @alexander-beedie, @kdn36, @nameexhaustion, @orlp, @ritchie46 and @wtn

### Release: polars [Python Polars 1.37.0](https://github.com/pola-rs/polars/releases/tag/py-1.37.0)
## 🚀 Performance improvements

- Speed up `SQL` interface "ORDER BY" clauses (#26037)
- Add fast kernel for is\_nan and use it for numpy NaN->null conversion (#26034)
- Optimize ArrayFromIter implementations for ObjectArray (#25712)
- New streaming NDJSON sink pipeline (#25948)
- New streaming CSV sink pipeline (#25900)
- Dispatch partitioned usage of `sink_*` functions to new-streaming by default (#25910)
- Replace ryu with faster zmij (#25885)
- Reduce memory usage for .item() count in grouped first/last (#25787)
- Skip schema inference if schema provided for `scan_csv/ndjson` (#25757)
- Add width-aware chunking to prevent degradation with wide data (#25764)
- Use new sink pipeline for write/sink\_ipc (#25746)
- Reduce memory usage when scanning multiple parquet files in streaming (#25747)
- Don't call cluster\_with\_columns optimization if not needed (#25724)

## ✨ Enhancements

- Add new `pl.PartitionBy` API (#26004)
- ArrowStreamExportable and sink\_delta (#25994)
- Release musl builds (#25894)
- Implement streaming decompression for CSV `COUNT(*)` fast path (#25988)
- Add nulls support for rolling\_mean\_by (#25917)
- Add lazy `collect_all` (#25991)
- Add streaming decompression for NDJSON schema inference (#25992)
- Improved handling of unqualified SQL `JOIN` columns that are ambiguous (#25761)
- Drop Python 3.9 support (#25984)
- Expose record batch size in `{sink,write}_ipc` (#25958)
- Add `null_on_oob` parameter to `expr.get` (#25957)
- Suggest correct timezone if timezone validation fails (#25937)
- Support streaming IPC scan from S3 object store (#25868)
- Implement streaming CSV schema inference (#25911)
- Support hashing of meta expressions (#25916)
- Improve `SQLContext` recognition of possible table objects in the Python globals (#25749)
- Add pl.Expr.(min|max)\_by (#25905)
- Improve MemSlice Debug impl (#25913)
- Implement or fix json encode/decode for (U)Int128, Categorical, Enum, Decimal (#25896)
- Expand scatter to more dtypes (#25874)
- Implement streaming CSV decompression (#25842)
- Add Series `sql` method for API consistency (#25792)
- Mark Polars as safe for free-threading (#25677)
- Support Binary and Decimal in arg\_(min|max) (#25839)
- Allow Decimal parsing in str.json\_decode (#25797)
- Add `shift` support for Object data type (#25769)
- Add missing `Series.arr.mean` (#25774)
- Allow scientific notation when parsing Decimals (#25711)

## 🐞 Bug fixes

- Release GIL on collect\_batches (#26033)
- Missing buffer update in String is\_in Parquet pushdown (#26019)
- Make `struct.with_fields` data model coherent (#25610)
- Incorrect output order for order sensitive operations after join\_asof (#25990)
- Use SeriesExport for pyo3-polars FFI (#26000)
- Add pl.Schema to type signature for DataFrame.cast (#25983)
- Don't write Parquet min/max statistics for i128 (#25986)
- Ensure chunk consistency in in-memory join (#25979)
- Fix varying block metadata length in IPC reader (#25975)
- Implement collect\_batches properly in Rust (#25918)
- Fix panic on arithmetic with bools in list (#25898)
- Convert to index type with strict cast in some places (#25912)
- Empty dataframe in streaming non-strict hconcat (#25903)
- Infer large u64 in json as i128 (#25904)
- Set http client timeouts to 10 minutes (#25902)
- Correct lexicographic ordering for Parquet BYTE\_ARRAY statistics (#25886)
- Raise error on duplicate `group_by` names in `upsample()` (#25811)
- Correctly export view buffer sizes nested in Extension types (#25853)
- Fix `DataFrame.estimated_size` not handling overlapping chunks correctly (#25775)
- Ensure Kahan sum does not introduce NaN from infinities (#25850)
- Trim excess bytes in parquet decode (#25829)
- Fix panic/deadlock sinking parquet with rows larger than 64MB estimated size (#25836)
- Fix quantile `midpoint` interpolation (#25824)
- Don't use cast when converting from physical in list.get (#25831)
- Invalid null count on int -> categorical cast (#25816)
- Update groups in `list.eval` (#25826)
- Use downcast before FFI conversion in PythonScan (#25815)
- Double-counting of row metrics (#25810)
- Cast nulls to expected type in streaming union node (#25802)
- Incorrect slice pushdown into map\_groups (#25809)
- Fix panic writing parquet with single bool column (#25807)
- Fix upsample with `group_by` incorrectly introduced NULLs on group key columns (#25794)
- Panic in top\_k pruning (#25798)
- Fix incorrect `collect_schema` for unpivot followed by join (#25782)
- Verify `arr` namespace is called from array column (#25650)
- Ensure `LazyFrame.serialize()` unchanged after `collect_schema()` (#25780)
- Function map\_(rows|elements) with return\_dtype = pl.Object (#25753)
- Fix incorrect cargo sub-feature (#25738)

## 📖 Documentation

- Fix display of deprecation warning (#26010)
- Document null behaviour for `rank` (#25887)
- Add `QUALIFY` clause and `SUBSTRING` function to the SQL docs (#25779)
- Update mixed-offset datetime parsing example in user guide (#25915)
- Update bare-metal docs for mounted anonymous results (#25801)
- Fix credential parameter name in cloud-storage.py (#25788)
- Configuration options update (#25756)

## 🛠️ Other improvements

- Update rust compiler (#26017)
- Improve csv test coverage (#25980)
- Ramp up CSV read size (#25997)
- Mark `lazy` parameter to `collect_all` as unstable (#25999)
- Update `ruff` action and simplify version handling (#25940)
- Run python lint target as part of pre-commit (#25982)
- Disable HTTP timeout for receiving response body (#25970)
- Fix mypy lint (#25963)
- Add AI contribution policy (#25956)
- Fix failing scan delta S3 test (#25932)
- Improve MemSlice Debug impl (#25913)
- Remove and deprecate batched csv reader (#25884)
- Remove unused AnonymousScan functions (#25872)
- Filter DeprecationWarning from pyparsing indirectly through pyiceberg (#25854)
- Various small improvements (#25835)
- Clear venv with appropriate version of Python (#25851)
- Skip schema inference if schema provided for `scan_csv/ndjson` (#25757)
- Ensure proper async connection cleanup on DB test exit (#25766)
- Ensure we uninstall other Polars runtimes in CI (#25739)
- Make 'make requirements' more robust (#25693)
- Remove duplicate compression level types (#25723)

Thank you to all our contributors for making this release possible!
@AndreaBozzo, @EndPositive, @Kevin-Patyk, @MarcoGorelli, @Voultapher, @alexander-beedie, @anosrepenilno, @arlyon, @azimafroozeh, @carnarez, @dependabot[bot], @dsprenkels, @edizeqiri, @eitanf, @gab23r, @henryharbeck, @hutch3232, @ion-elgreco, @jqnatividad, @kdn36, @lun3x, @m1guelperez, @mcrumiller, @nameexhaustion, @orlp, @ritchie46, @sachinn854, @yonikremer and [dependabot[bot]](https://github.com/apps/dependabot)

## Project: [pandas-dev/pandas](https://pandas.pydata.org/docs/index.html), 2 releases: ['pandas 3.0.0', 'Pandas 3.0.0rc2']
### Release: pandas [pandas 3.0.0](https://github.com/pandas-dev/pandas/releases/tag/v3.0.0)
We are pleased to announce the release of pandas 3.0.0, a major release from the pandas 2.x series. This release includes various new features, bug fixes, and performance improvements, as well as possible breaking changes.  

The pandas 3.0 release removed a functionality that was deprecated in previous releases. It is recommended to first upgrade to pandas 2.3 and to ensure your code is working without warnings, before upgrading to pandas 3.0.

Highlights include:

- [Dedicated string data type by default](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html#whatsnew-300-enhancements-string-dtype)
- [Consistent copy/view behaviour with Copy-on-Write](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html#whatsnew-300-enhancements-copy_on_write) (CoW) (a.k.a. getting rid of the SettingWithCopyWarning)
- [New default resolution for datetime-like data](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html#whatsnew-300-api-breaking-datetime-resolution-inference)
- [Initial support for the new `pd.col` syntax](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html#whatsnew-300-enhancements-col)

See the [announcement blog post](https://pandas.pydata.org/community/blog/pandas-3.0.html) and the [detailed release notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html) for a list of all the changes.

Pandas 3.0.0 supports Python 3.11 and higher. 
The release can be installed from PyPI

    python -m pip install --upgrade pandas==3.0.*

Or from conda-forge

    conda install -c conda-forge pandas=3.0

Please report any issues with the release on the [pandas issue tracker](https://github.com/pandas-dev/pandas/issues/new/choose).

Thanks to all the contributors who made this release possible.
### Release: pandas [Pandas 3.0.0rc2](https://github.com/pandas-dev/pandas/releases/tag/v3.0.0rc2)
ERROR: (datetime.datetime(2026, 1, 14, 22, 17, 15), 'Pandas 3.0.0rc2', '', 'https://github.com/pandas-dev/pandas/releases/tag/v3.0.0rc2')
## Project: [holoviz/panel](https://panel.holoviz.org/), 1 releases: ['Version 1.8.5']
### Release: panel [Version 1.8.5](https://github.com/holoviz/panel/releases/tag/v1.8.5)
This release includes several fixes and enhancements for notebook stability, Tabulator behavior, ESM/ReactiveComponent handling, and Markdown rendering. It also adds documentation updates for FastAPI integration, app conversion guides, and the Panel roadmap.

### 🐛 Bug Fixes

- Fix error in notebook environments causing failure to run apps ([#8334](https://github.com/holoviz/panel/pull/8334))
- Prevent `Tabulator` from unintentionally reverting `show_index=False` back to `True` ([#8333](https://github.com/holoviz/panel/pull/8333))
- Ensure transformed param values are inherited by ESM components ([#8338](https://github.com/holoviz/panel/pull/8338))
- Ensure DataFrame objects can be referenced in Vega `datasets` ([#8330](https://github.com/holoviz/panel/pull/8330))
- Improve handling of code highlighting in `Markdown` pane ([#8331](https://github.com/holoviz/panel/pull/8331))
- Allow replacing child models inside `ReactiveESM` components ([#8348](https://github.com/holoviz/panel/pull/8348))

### 📚 Documentation

* Add **how-to guides** for converting Panel apps to **desktop and mobile apps** ([#8349](https://github.com/holoviz/panel/pull/8349))
* Update **FastAPI integration instructions** ([#8337](https://github.com/holoviz/panel/pull/8337))
* Publish updated **Roadmap for Panel v2 and beyond** ([#8339](https://github.com/holoviz/panel/pull/8339))

### 🧪 Maintenance & Build

* Use **trusted publisher** setup for NPM release
* Bump Node.js version used in build

## Project: [pyscript/pyscript](https://pyscript.com/), 1 releases: ['2026.1.1']
### Release: pyscript [2026.1.1](https://github.com/pyscript/pyscript/releases/tag/2026.1.1)
* Minor fixes in [coincident](https://github.com/WebReflection/coincident/commit/eef4d0831ca47c1fabed3d7e8fa6809d818d729f).
* Removed WebR (for the time being) and improved packages details in [polyscript](https://github.com/pyscript/polyscript/pull/165).
* Updated polyscript module to include latest coincident and latest [Pyodide 0.29.1](https://pyodide.org/en/stable/project/changelog.html).
* **INCLUDES BREAKING CHANGES** API/docstring refactor #2414
    * `magic_js` renamed to `context` (but everything should still only be referenced via the core `pyscript` namespace).
    * A much requested change in `pyscript.web`: use `page["#an-id"]` to get a single element by id (rather than `page.find("#an-id")[0]`).
    * In `pyscript.web` an Element's styles are a Python `dict` and classes a Python `set` (rather than custom objects with a similar API to those Python classes).
    * Explicitly use `update_all` with `ElementCollection` instances. You used to be able to do implicit changes via: `my_collection.innerHTML = "foo"`. Feedback was this felt risky (folks thought they were mutating an element, not an element collection and they were getting strange results). Now you just: `my_collection.update_all(innerHTML="foo")` which also makes it more obvious what's going on.
    * Extensive rewrite of docstrings with examples. These form the basis of our new API docs.
    * Added many more tests for the purpose of coverage and testing edge-cases.
## Project: [cython/cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html), 2 releases: ['3.2.4', '3.1.8']
### Release: cython [3.2.4](https://github.com/cython/cython/releases/tag/3.2.4)
ERROR: (datetime.datetime(2026, 1, 4, 13, 13, 45), '3.2.4', None, 'https://github.com/cython/cython/releases/tag/3.2.4')
### Release: cython [3.1.8](https://github.com/cython/cython/releases/tag/3.1.8)
ERROR: (datetime.datetime(2026, 1, 3, 15, 23, 29), '3.1.8', None, 'https://github.com/cython/cython/releases/tag/3.1.8')
## Project: [plotly/dash](https://plotly.com/dash/), 2 releases: ['Dash Version 3.4.0', 'v4.0.0rc6']
### Release: dash [Dash Version 3.4.0](https://github.com/plotly/dash/releases/tag/v3.4.0)
## Added

- [#3568]((https://github.com/plotly/dash/pull/3568) Added `children` and `copied_children` props to `dcc.Clipboard` to customize the button contents before and after copying.
- [#3534]((https://github.com/plotly/dash/pull/3534) Adds `playsInline` prop to `html.Video`.  Based on [#2338]((https://github.com/plotly/dash/pull/2338)
- [#3541](https://github.com/plotly/dash/pull/3541) Add `attributes` dictionary to be be formatted on script/link (_js_dist/_css_dist) tags of the index, allows for `type="module"` or `type="importmap"`. [#3538](https://github.com/plotly/dash/issues/3538)
- [#3542](https://github.com/plotly/dash/pull/3542) Add hidden=True to dash pages callback.
- [#3564](https://github.com/plotly/dash/pull/3564) Add new parameter `hide_all_callbacks` to `run()`. Closes [#3493](https://github.com/plotly/dash/issues/3493)
- [#3563](https://github.com/plotly/dash/pull/3563) Add hidden to clientside callbacks as configurable parameter

## Fixed
- [#3541](https://github.com/plotly/dash/pull/3541) Remove last reference of deprecated `pkg_resources`.
- [#3548](https://github.com/plotly/dash/pull/3548) Fix devtools overflowing it's container on version update. Fix [#3535](https://github.com/plotly/dash/issues/3535).
- [#3545](https://github.com/plotly/dash/pull/3545) Replace deprecated asyncio.iscoroutinefunction() call with inspect.iscoroutinefunction()

# Changed
- [#3540](https://github.com/plotly/dash/pull/3540) Expose more types for better static typing options.
- [#3520](https://github.com/plotly/dash/pull/3520). Set `pointer-events` to `auto` on `Tooltip` to make it possible to interact with tooltip content when `targetable=True`
### Release: dash [v4.0.0rc6](https://github.com/plotly/dash/releases/tag/v4.0.0rc6)
## Added
- Restored missing implementation for `with_portal` and `with_full_screen_portal` in datepickers

## Changed
- Bugfixes for feedback received in `rc5`: notably, popovers are `position: fixed` once again.

## Project: [dask/dask](https://www.dask.org/), 2 releases: ['2026.1.1', '2026.1.0']
### Release: dask [2026.1.1](https://github.com/dask/dask/releases/tag/2026.1.1)
## Changes

* No changes  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

### Release: dask [2026.1.0](https://github.com/dask/dask/releases/tag/2026.1.0)
## Changes

- Remove the Python 2 Comment @vipinkataria2209 (#12229)
- Bump JamesIves/github-pages-deploy-action from 4.7.6 to 4.8.0 @[dependabot[bot]](https://github.com/apps/dependabot) (#12230)
- Fix changelog: distributed-pr -> pr-distributed @mplough-kobold (#12227)
- Support duck-typed Futures in task graph processing @mrocklin (#12213)
- Bump actions/setup-java from 4 to 5 @[dependabot[bot]](https://github.com/apps/dependabot) (#12057)
- Relax `test_serialization` @crusaderky (#12226)
- [cosmetic] Reorganise dependency groups in CI environment files @crusaderky (#12222)
- Review `_array_expr_enabled()` @crusaderky (#12217)
- Increase coverage; lower codecov threshold to pass @crusaderky (#12214)
- Test array expr on mindeps @crusaderky (#12216)
- Disable some Mac builds @crusaderky (#12218)
- Typing tweaks @crusaderky (#12215)
- [CI] unbreak codecov @crusaderky (#12211)
- Test array expr on Python 3.14 @crusaderky (#12212)
- Fix pickle compatibility for Python 3.14 @mrocklin (#12206)
- Remove deprecated `dask._compatibility.entry_points` @crusaderky (#12202)
- Tweak MacOS CI @crusaderky (#12200)
- Remove obsolete CI pins @crusaderky (#12199)
- Bump JamesIves/github-pages-deploy-action from 4.7.4 to 4.7.6 @[dependabot[bot]](https://github.com/apps/dependabot) (#12196)
- Bump actions/upload-artifact from 5 to 6 @[dependabot[bot]](https://github.com/apps/dependabot) (#12197)
- Bump actions/cache from 4 to 5 @[dependabot[bot]](https://github.com/apps/dependabot) (#12195)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

## Project: [delta-io/delta-rs](https://delta-io.github.io/delta-rs/usage/installation/), 4 releases: ['python-v1.3.2', 'python-v1.3.1: read support deletion vectors, column mapping', 'rust-v0.30.0', 'python-v1.3.0']
### Release: delta-rs [python-v1.3.2](https://github.com/delta-io/delta-rs/releases/tag/python-v1.3.2)
## What's Changed
* ci: correct maturin invocations to call publish by @rtyler in https://github.com/delta-io/delta-rs/pull/4064
* fix: ensure that delete on an empty table works by @rtyler in https://github.com/delta-io/delta-rs/pull/4066
* fix: avoid unnecessary reload of file data by file_views() by @rtyler in https://github.com/delta-io/delta-rs/pull/4067
* feat: expose new table provider in query builder by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4061
* fix: wrap table provider with block_on in scan for python by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4072
* feat: migrate table scans by @roeap in https://github.com/delta-io/delta-rs/pull/4048
* chore: clippy by @roeap in https://github.com/delta-io/delta-rs/pull/4073
* feat: move data validation on a stream by @roeap in https://github.com/delta-io/delta-rs/pull/4050
* fix: handle DV mask exhaustion and short masks in batch_project by @ethan-tyler in https://github.com/delta-io/delta-rs/pull/4058
* fix: use LTO thin for linux ARM release by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4077
* chore: clean up older ignored tests for deletion vectors and column mapping by @rtyler in https://github.com/delta-io/delta-rs/pull/4075
* feat: integrate new table provider with DataSink by @roeap in https://github.com/delta-io/delta-rs/pull/4049
* refactor: remove unused error variants by @roeap in https://github.com/delta-io/delta-rs/pull/4078


**Full Changelog**: https://github.com/delta-io/delta-rs/compare/python-v1.3.1...python-v1.3.2
### Release: delta-rs [python-v1.3.1: read support deletion vectors, column mapping](https://github.com/delta-io/delta-rs/releases/tag/python-v1.3.1)
## What's Changed
* docs: update the changelog for the last couple releases by @rtyler in https://github.com/delta-io/delta-rs/pull/4028
* chore: tidy up the python release by @rtyler in https://github.com/delta-io/delta-rs/pull/4031
* ci: configure python version for windows by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/4033
* feat: improve kernel engine by @roeap in https://github.com/delta-io/delta-rs/pull/4035
* feat: kernel based table scans by @roeap in https://github.com/delta-io/delta-rs/pull/4036
* feat: push predicates into parquet scans by @roeap in https://github.com/delta-io/delta-rs/pull/4039
* fix(catalog-unity): improve error messages for temporary credentials failures by @saivineel in https://github.com/delta-io/delta-rs/pull/4038
* docs: explicitly describe filesystem_check does fix and not only checks it by @SG5 in https://github.com/delta-io/delta-rs/pull/3941
* refactor: remove DataFrame usage in delete operation by @roeap in https://github.com/delta-io/delta-rs/pull/4047
* feat: improve schema and predicate handling in scan planning by @roeap in https://github.com/delta-io/delta-rs/pull/4044
* chore: bump the patch version for a release of catalog-unity by @rtyler in https://github.com/delta-io/delta-rs/pull/4042
* fix: decode paths only during scan_memory_table by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4056
* chore: improve lakefs error msg with unknown errors by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4055
* feat: expose newest table provider to python by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4057
* chore!: remove peek_next_commit from LogStore by @roeap in https://github.com/delta-io/delta-rs/pull/4059
* chore: 1.3.1 release by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4060
* chore(ci): use ubuntu-arm images for linux arm builds by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/4043

## New Contributors
* @saivineel made their first contribution in https://github.com/delta-io/delta-rs/pull/4038
* @SG5 made their first contribution in https://github.com/delta-io/delta-rs/pull/3941

**Full Changelog**: https://github.com/delta-io/delta-rs/compare/python-v1.3.0...python-v1.3.1
### Release: delta-rs [rust-v0.30.0](https://github.com/delta-io/delta-rs/releases/tag/rust-v0.30.0)
## :warning: There are a number of API changes between `0.30.x` and `0.29.4 :warning: 


This release includes [delta_kernel](https://crates.io/crates/delta_kernel) which includes some performance improvements around stats parsing. The 0.30.x release line is expected to have a number of patch releases that incorporate more and more performance improvements with our delta_kernel integration.




[Full Changelog](https://github.com/delta-io/delta-rs/compare/rust-v0.29.4...rust-v0.30.0)

**Merged pull requests:**

- refactor: remove log\_data call sites in find\_files [\#4026](https://github.com/delta-io/delta-rs/pull/4026) ([roeap](https://github.com/roeap))
- chore: remove wildcard dependency for publishing [\#4025](https://github.com/delta-io/delta-rs/pull/4025) ([rtyler](https://github.com/rtyler))
- refactor: use logical type ref when getting stats [\#4019](https://github.com/delta-io/delta-rs/pull/4019) ([roeap](https://github.com/roeap))
- fix: handle stats config in data sink [\#4016](https://github.com/delta-io/delta-rs/pull/4016) ([roeap](https://github.com/roeap))
- fix: null handling when extracting scalars [\#4014](https://github.com/delta-io/delta-rs/pull/4014) ([roeap](https://github.com/roeap))
- fix: between range handling in expression translations [\#4013](https://github.com/delta-io/delta-rs/pull/4013) ([roeap](https://github.com/roeap))
- chore: fix windows uri test [\#4011](https://github.com/delta-io/delta-rs/pull/4011) ([hntd187](https://github.com/hntd187))
- refactor: towards lazier snapshots [\#4010](https://github.com/delta-io/delta-rs/pull/4010) ([roeap](https://github.com/roeap))
- fix: pin pyspark and clear disk space in runners [\#4007](https://github.com/delta-io/delta-rs/pull/4007) ([ion-elgreco](https://github.com/ion-elgreco))
- test: add utilities for asserting DAT scan results [\#4005](https://github.com/delta-io/delta-rs/pull/4005) ([roeap](https://github.com/roeap))
- chore: update delta-kernel to 0.19 [\#4004](https://github.com/delta-io/delta-rs/pull/4004) ([roeap](https://github.com/roeap))
- refactor: simplify kernel extensions [\#4003](https://github.com/delta-io/delta-rs/pull/4003) ([roeap](https://github.com/roeap))
- chore: clippy [\#4002](https://github.com/delta-io/delta-rs/pull/4002) ([roeap](https://github.com/roeap))
- refactor: handle target version when resolving snapshot [\#4001](https://github.com/delta-io/delta-rs/pull/4001) ([roeap](https://github.com/roeap))
- refactor: use rstest for running DAT tests [\#4000](https://github.com/delta-io/delta-rs/pull/4000) ([roeap](https://github.com/roeap))
- feat: kernel expression conversion [\#3998](https://github.com/delta-io/delta-rs/pull/3998) ([roeap](https://github.com/roeap))
- chore: add easier local coverage reporting [\#3995](https://github.com/delta-io/delta-rs/pull/3995) ([rtyler](https://github.com/rtyler))
- feat: expose operations on DeltaTable [\#3987](https://github.com/delta-io/delta-rs/pull/3987) ([roeap](https://github.com/roeap))
- chore: remove some warnigs [\#3986](https://github.com/delta-io/delta-rs/pull/3986) ([roeap](https://github.com/roeap))
- chore: normalize Url going into logstore and update everything to take references [\#3985](https://github.com/delta-io/delta-rs/pull/3985) ([rtyler](https://github.com/rtyler))
- fix: add missing field to snapshot serde [\#3984](https://github.com/delta-io/delta-rs/pull/3984) ([roeap](https://github.com/roeap))
- feat: allow for concurrent deletes in conflict checker if `data_change` is false [\#3982](https://github.com/delta-io/delta-rs/pull/3982) ([abhiaagarwal](https://github.com/abhiaagarwal))
- fix: remove 3.9 from ci matrix [\#3978](https://github.com/delta-io/delta-rs/pull/3978) ([ion-elgreco](https://github.com/ion-elgreco))
- fix: decode path before lookup [\#3976](https://github.com/delta-io/delta-rs/pull/3976) ([ion-elgreco](https://github.com/ion-elgreco))
- chore: remove deprecated pyo3 methods [\#3975](https://github.com/delta-io/delta-rs/pull/3975) ([ion-elgreco](https://github.com/ion-elgreco))
- chore: removing APIs and deprecation warnings: 0.30.x here we come [\#3962](https://github.com/delta-io/delta-rs/pull/3962) ([rtyler](https://github.com/rtyler))
- feat: update to DataFusion 51, arrow 57, delta-kernel 0.18.0, pyo3 26, pyo3-arrow 0.14 [\#3949](https://github.com/delta-io/delta-rs/pull/3949) ([hntd187](https://github.com/hntd187))
- fix: schema evolution for merge operation [\#3945](https://github.com/delta-io/delta-rs/pull/3945) ([JustinRush80](https://github.com/JustinRush80))
- chore: remove Python 3.9 from our build infrastructure [\#3937](https://github.com/delta-io/delta-rs/pull/3937) ([rtyler](https://github.com/rtyler))
- docs: fix small typo issue [\#3935](https://github.com/delta-io/delta-rs/pull/3935) ([bmoreau8](https://github.com/bmoreau8))
- chore: removing references to using `partition_filters` for partition overwrite [\#3912](https://github.com/delta-io/delta-rs/pull/3912) ([zyd14](https://github.com/zyd14))
- feat\(datafusion\): add max\_temp\_directory\_size parameter for z-order and compact operations for DataFusion [\#3847](https://github.com/delta-io/delta-rs/pull/3847) ([fvaleye](https://github.com/fvaleye))

**Fixed bugs:**

- Asked to increase `max_temp_directory_size` in the disk manager configuration when optimizing large table [\#3833](https://github.com/delta-io/delta-rs/issues/3833)

**Closed issues:**

- \[Bug\]: Count / get\_add\_actions exception for an empty table [\#4023](https://github.com/delta-io/delta-rs/issues/4023)
- \[Bug\]: MERGE with schema evolution does not add new columns [\#4009](https://github.com/delta-io/delta-rs/issues/4009)
- \[Bug\]: vacuum does not respect retention\_hours when `full=True` [\#3989](https://github.com/delta-io/delta-rs/issues/3989)
- \[Bug\]: write table by FFI call from go may memory leak? [\#3973](https://github.com/delta-io/delta-rs/issues/3973)
- \[Bug\]: Table merging fails with `merge_schema=True` [\#3943](https://github.com/delta-io/delta-rs/issues/3943)
- \[Bug\]: \_internal.DeltaError: Generic DeltaTable error: Unable to map \_\_delta\_rs\_path to action during `overwrite` with `predicate` [\#3939](https://github.com/delta-io/delta-rs/issues/3939)
- \[Feature\]: update to DataFusion 51.0.0 [\#3920](https://github.com/delta-io/delta-rs/issues/3920)
- \[Bug\]: `get_add_actions()` panics with "index out of bounds" when table has no data files [\#3918](https://github.com/delta-io/delta-rs/issues/3918)
- \[Bug\]: Docs describe `partition_filters` parameter to `write_deltalake` that doesn't exist [\#3904](https://github.com/delta-io/delta-rs/issues/3904)
- \[Feature\]: split `delta-rs` into multiple crates [\#3899](https://github.com/delta-io/delta-rs/issues/3899)
- \[Feature\]: Drop python 3.9 support once EOL [\#3886](https://github.com/delta-io/delta-rs/issues/3886)
- \[Bug\]: PyPi storage limit hit for `deltalake` \[python releases blocked for time-being\] [\#3876](https://github.com/delta-io/delta-rs/issues/3876)**
### Release: delta-rs [python-v1.3.0](https://github.com/delta-io/delta-rs/releases/tag/python-v1.3.0)
## What's Changed
* fix: remove manylinux 217 builds for aarch64 by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3880
* fix: display kernel-rs errors better by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3883
* fix: needs ci release python by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3885
* feat: add multiple constraints at once by @JustinRush80 in https://github.com/delta-io/delta-rs/pull/3879
* chore: create the next release of the rust core package by @rtyler in https://github.com/delta-io/delta-rs/pull/3887
* fix: surface the correct kernel objectstore error by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3888
* feat(memory): optimize collection preallocation where capacity is known by @fvaleye in https://github.com/delta-io/delta-rs/pull/3895
* feat: tracing spans across threadpool by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3894
* chore: reduce wheel size by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/3878
* fix: use the default features of aws-config by @rtyler in https://github.com/delta-io/delta-rs/pull/3898
* perf(snapshot): minor memory allocation and usage reduction without cloning by @fvaleye in https://github.com/delta-io/delta-rs/pull/3903
* feat: generate an Symlink Manifest for External Engines by @JustinRush80 in https://github.com/delta-io/delta-rs/pull/3889
* feat(typed-builder): adopt typed-builder for safer builder pattern in non-core crates by @fvaleye in https://github.com/delta-io/delta-rs/pull/3902
* chore: cleaning up warnings and preparing 0.29.3 by @rtyler in https://github.com/delta-io/delta-rs/pull/3910
* fix: update stats serialization logic for scale-0 decimals by @DrakeLin in https://github.com/delta-io/delta-rs/pull/3916
* feat: add GCS auto-registration via ctor hooks by @ethan-tyler in https://github.com/delta-io/delta-rs/pull/3923
* chore: bump the patch version to release fixes by @rtyler in https://github.com/delta-io/delta-rs/pull/3919
* chore(cargo): unify cargo profiles by @fvaleye in https://github.com/delta-io/delta-rs/pull/3924
* fix: correctly rectify Urls with dots in DeltaTableBuilder by @rtyler in https://github.com/delta-io/delta-rs/pull/3929
* chore(deps): update ctor requirement from 0.2 to 0.6 by @dependabot[bot] in https://github.com/delta-io/delta-rs/pull/3927
* chore: remove proofs/ which are no longer used by @rtyler in https://github.com/delta-io/delta-rs/pull/3930
* chore(deps): update convert_case requirement from 0.8.0 to 0.9.0 by @dependabot[bot] in https://github.com/delta-io/delta-rs/pull/3926
* chore: adding more test coverage to the Gcp crate by @rtyler in https://github.com/delta-io/delta-rs/pull/3931
* fix: handle empty tables in get_add_actions() by @vsmanish1772 in https://github.com/delta-io/delta-rs/pull/3922
* chore: removing references to using `partition_filters` for partition overwrite by @zyd14 in https://github.com/delta-io/delta-rs/pull/3912
* chore: remove Python 3.9 from our build infrastructure by @rtyler in https://github.com/delta-io/delta-rs/pull/3937
* feat: update to DataFusion 51, arrow 57, delta-kernel 0.18.0, pyo3 26, pyo3-arrow 0.14 by @hntd187 in https://github.com/delta-io/delta-rs/pull/3949
* docs: fix small typo issue by @bmoreau8 in https://github.com/delta-io/delta-rs/pull/3935
* fix: retry advancement of `PreparedCommit` into `PostCommit` in case version 0 already exists (created by another writer) by @danielgafni in https://github.com/delta-io/delta-rs/pull/3513
* fix: remove 3.9 from ci matrix by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3978
* chore: remove deprecated pyo3 methods by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3975
* fix: schema evolution for merge operation by @JustinRush80 in https://github.com/delta-io/delta-rs/pull/3945
* chore: removing APIs and deprecation warnings: 0.30.x here we come by @rtyler in https://github.com/delta-io/delta-rs/pull/3962
* fix: add missing field to snapshot serde by @roeap in https://github.com/delta-io/delta-rs/pull/3984
* chore: remove some warnigs by @roeap in https://github.com/delta-io/delta-rs/pull/3986
* feat: expose operations on DeltaTable by @roeap in https://github.com/delta-io/delta-rs/pull/3987
* feat(datafusion): add max_temp_directory_size parameter for z-order and compact operations for DataFusion by @fvaleye in https://github.com/delta-io/delta-rs/pull/3847
* chore: normalize Url going into logstore and update everything to take references by @rtyler in https://github.com/delta-io/delta-rs/pull/3985
* chore: add easier local coverage reporting by @rtyler in https://github.com/delta-io/delta-rs/pull/3995
* refactor: use rstest for running DAT tests by @roeap in https://github.com/delta-io/delta-rs/pull/4000
* refactor: handle target version when resolving snapshot by @roeap in https://github.com/delta-io/delta-rs/pull/4001
* chore: clippy by @roeap in https://github.com/delta-io/delta-rs/pull/4002
* refactor: simplify kernel extensions by @roeap in https://github.com/delta-io/delta-rs/pull/4003
* chore: update delta-kernel to 0.19 by @roeap in https://github.com/delta-io/delta-rs/pull/4004
* test: add utilities for asserting DAT scan results by @roeap in https://github.com/delta-io/delta-rs/pull/4005
* feat: allow for concurrent deletes in conflict checker if `data_change` is false by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/3982
* feat: kernel expression conversion by @roeap in https://github.com/delta-io/delta-rs/pull/3998
* fix: decode path before lookup by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3976
* fix: pin pyspark and clear disk space in runners by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/4007
* refactor: towards lazier snapshots by @roeap in https://github.com/delta-io/delta-rs/pull/4010
* chore: fix windows uri test by @hntd187 in https://github.com/delta-io/delta-rs/pull/4011
* fix: between range handling in expression translations by @roeap in https://github.com/delta-io/delta-rs/pull/4013
* fix: null handling when extracting scalars by @roeap in https://github.com/delta-io/delta-rs/pull/4014
* fix: handle stats config in data sink by @roeap in https://github.com/delta-io/delta-rs/pull/4016
* refactor: use logical type ref when getting stats by @roeap in https://github.com/delta-io/delta-rs/pull/4019
* chore: remove wildcard dependency for publishing by @rtyler in https://github.com/delta-io/delta-rs/pull/4025
* refactor: remove log_data call sites in find_files by @roeap in https://github.com/delta-io/delta-rs/pull/4026

## New Contributors
* @DrakeLin made their first contribution in https://github.com/delta-io/delta-rs/pull/3916
* @ethan-tyler made their first contribution in https://github.com/delta-io/delta-rs/pull/3923
* @zyd14 made their first contribution in https://github.com/delta-io/delta-rs/pull/3912
* @bmoreau8 made their first contribution in https://github.com/delta-io/delta-rs/pull/3935
* @danielgafni made their first contribution in https://github.com/delta-io/delta-rs/pull/3513

**Full Changelog**: https://github.com/delta-io/delta-rs/compare/python-v1.2.1...python-v1.3.0
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 10 releases: ['v1.0.3', 'v1.0.3-rc.1', 'v2.0.0-rc.1', 'v2.0.0-beta.10', 'v2.0.0-beta.9', 'v1.0.2', 'v2.0.0-beta.8', 'v1.0.2-rc.2', 'v1.0.1', 'v2.0.0-beta.5']
### Release: lance [v1.0.3](https://github.com/lance-format/lance/releases/tag/v1.0.3)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.3 -->

## What's Changed
### New Features 🎉
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat: support credentials vending in directory namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5566
* feat: support dynamic context for lance namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5710
### Performance Improvements 🚀
* perf: tighten WAND block score upper bound by @BubbleCal in https://github.com/lance-format/lance/pull/5668
* perf: use LRU cache for session contexts in get_session_context by @wjones127 in https://github.com/lance-format/lance/pull/5736

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.2...v1.0.3
### Release: lance [v1.0.3-rc.1](https://github.com/lance-format/lance/releases/tag/v1.0.3-rc.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.3-rc.1 -->

## What's Changed
### New Features 🎉
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat: support credentials vending in directory namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5566
* feat: support dynamic context for lance namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5710
### Performance Improvements 🚀
* perf: tighten WAND block score upper bound by @BubbleCal in https://github.com/lance-format/lance/pull/5668
* perf: use LRU cache for session contexts in get_session_context by @wjones127 in https://github.com/lance-format/lance/pull/5736

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.2...v1.0.3-rc.1
### Release: lance [v2.0.0-rc.1](https://github.com/lance-format/lance/releases/tag/v2.0.0-rc.1)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-rc.1 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
* feat!: track cumulative wall time in analyze plan by @wkalt in https://github.com/lance-format/lance/pull/5505
* fix!: check metric compatibility before using vector index by @wjones127 in https://github.com/lance-format/lance/pull/5609
* feat!: define default index name and return IndexMetadata after building index by @wjones127 in https://github.com/lance-format/lance/pull/5645
* feat!: make v2 manifest default by @wojiaodoubao in https://github.com/lance-format/lance/pull/5656
* refactor!: introduce storage options accessor by @jackye1995 in https://github.com/lance-format/lance/pull/5728
### New Features 🎉
* feat: support using FTS as a filter in vector search by @wojiaodoubao in https://github.com/lance-format/lance/pull/4928
* feat: support when_matched_delete in merge_insert by @jtuglu1 in https://github.com/lance-format/lance/pull/4939
* feat: add support for large minichunk size (u32) in format v2.2 by @niyue in https://github.com/lance-format/lance/pull/4959
* feat: support GEO RTree index by @ddupg in https://github.com/lance-format/lance/pull/5034
* feat: support global tag retrieval and improve tag api by @majin1102 in https://github.com/lance-format/lance/pull/5088
* feat: support create vector index distributedly by @chenghao-guo in https://github.com/lance-format/lance/pull/5117
* feat: support add sub-column to struct col by @wojiaodoubao in https://github.com/lance-format/lance/pull/5126
* feat: distributed range-based BTree index by @steFaiz in https://github.com/lance-format/lance/pull/5202
* feat: strategized plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5233
* feat: dataset supports deep_clone by @majin1102 in https://github.com/lance-format/lance/pull/5250
* feat: cleanup only scan managed files by @majin1102 in https://github.com/lance-format/lance/pull/5338
* feat: support map data type in lance format version 2.2 by @xloya in https://github.com/lance-format/lance/pull/5349
* feat: add RTree index spec in table format by @ddupg in https://github.com/lance-format/lance/pull/5360
* feat(java): support row lineage and cdf apis by @yanghua in https://github.com/lance-format/lance/pull/5362
* feat: disable default features on internal use by @valkum in https://github.com/lance-format/lance/pull/5372
* feat(cdf): support set start/end timestamp in cdf by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5378
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
* feat(blob_v2): add dedicated blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5406
* feat: fallback to CPU if GPU accelerating is unavailable by @BubbleCal in https://github.com/lance-format/lance/pull/5407
* feat(blob_v2): add packed blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5413
* feat: allow python tracing / logging to be independently configured by @westonpace in https://github.com/lance-format/lance/pull/5415
* feat: add additional index APIs to support count rows split plan by @jackye1995 in https://github.com/lance-format/lance/pull/5447
* feat(java): support multi-bases for writing database by @ddupg in https://github.com/lance-format/lance/pull/5450
* feat(blob_v2): add BlobAray API for user input by @Xuanwo in https://github.com/lance-format/lance/pull/5451
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat(python): support cleanup_with_policy by @ddupg in https://github.com/lance-format/lance/pull/5458
* feat: support dropping sub-column of list(struct) by @wojiaodoubao in https://github.com/lance-format/lance/pull/5469
* feat(blob_v2): add GC support by @Xuanwo in https://github.com/lance-format/lance/pull/5473
* feat: add `py.typed` marker file by @jonded94 in https://github.com/lance-format/lance/pull/5479
* feat(python): expose the `distance_range` param in the Python scanner `nearest` config by @xloya in https://github.com/lance-format/lance/pull/5486
* feat(java): simplify the use of optional in jni by @ddupg in https://github.com/lance-format/lance/pull/5488
* feat(blob_v2): add Python API for Blob v2 by @Xuanwo in https://github.com/lance-format/lance/pull/5491
* feat(python): add DatasetBasePath stub to improve IDE hints by @ddupg in https://github.com/lance-format/lance/pull/5503
* feat(memtest): add macos support by @Xuanwo in https://github.com/lance-format/lance/pull/5510
* feat(java): add full text search api by @wojiaodoubao in https://github.com/lance-format/lance/pull/5563
* feat: support credentials vending in directory namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5566
* feat: upgrade lance-namespace to 0.4.0 by @jackye1995 in https://github.com/lance-format/lance/pull/5568
* feat: add skip_merge for FTS index build by @BubbleCal in https://github.com/lance-format/lance/pull/5570
* feat(java): add builder-style scalar index params by @wojiaodoubao in https://github.com/lance-format/lance/pull/5581
* feat: optimize rle implementation by @Xuanwo in https://github.com/lance-format/lance/pull/5586
* feat: support FixedSizeList<Struct> by @wkalt in https://github.com/lance-format/lance/pull/5593
* feat: add dictionary encoding for 64bit types like int64/double by @Xuanwo in https://github.com/lance-format/lance/pull/5594
* feat: support merge_insert with source dedupe on first seen value by @jackye1995 in https://github.com/lance-format/lance/pull/5603
* feat: support truncate table api by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5604
* feat: add Error::External variant for preserving user errors by @wjones127 in https://github.com/lance-format/lance/pull/5606
* feat: upgrade lance-namespace to 0.4.5 by @jackye1995 in https://github.com/lance-format/lance/pull/5611
* feat: refactor use of Error::io by @lichuang in https://github.com/lance-format/lance/pull/5612
* feat(java): add detached flag to commitTransaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5626
* feat: add parts_searched metrics for FTS by @BubbleCal in https://github.com/lance-format/lance/pull/5627
* feat: improve the random access file benchmark by @westonpace in https://github.com/lance-format/lance/pull/5628
* feat(oss): add sts token support for aliyun oss via storage_options by @hh23485 in https://github.com/lance-format/lance/pull/5632
* feat: merge-insert with primary key dedupe by @jackye1995 in https://github.com/lance-format/lance/pull/5633
* feat(java): expose index description and statistics by @majin1102 in https://github.com/lance-format/lance/pull/5655
* feat: allow configure temp dir size for datafusion exec by @jackye1995 in https://github.com/lance-format/lance/pull/5659
* feat(java): add support for optimizing indices by @majin1102 in https://github.com/lance-format/lance/pull/5663
* feat: make on arg optional for merge insert api by @yanghua in https://github.com/lance-format/lance/pull/5667
* feat: make OneShotPartitionStream pub by @timsaucer in https://github.com/lance-format/lance/pull/5672
* feat: support array_contains in LabelList scalar index by @fenfeng9 in https://github.com/lance-format/lance/pull/5681
* feat: add order to primary key by @touch-of-grey in https://github.com/lance-format/lance/pull/5683
* feat: use independent region manifest for MemWAL by @touch-of-grey in https://github.com/lance-format/lance/pull/5689
* feat: add stats() method to ObjectStoreRegistry by @wkalt in https://github.com/lance-format/lance/pull/5706
* feat: support dynamic context for lance namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5710
* feat: make blob v2 dedicated threshold configurable by @yanghua in https://github.com/lance-format/lance/pull/5719
* feat: cleanup partial idx files when merging distributed vector index by @yanghua in https://github.com/lance-format/lance/pull/5729
### Bug Fixes 🐛
* fix: correct null_count aggregation in boolean statistics collection by @YinZheng-Sun in https://github.com/lance-format/lance/pull/4839
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: fix vector index prewarm index by @xloya in https://github.com/lance-format/lance/pull/5412
* fix: panic unwrap on None in decoder.rs by @camilesing in https://github.com/lance-format/lance/pull/5424
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5464
* fix: make column name lookups case-insensitive by @wjones127 in https://github.com/lance-format/lance/pull/5465
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5499
* fix(java): support FixedSizeList for java LanceField by @fangbo in https://github.com/lance-format/lance/pull/5509
* fix: head external manifest object happend 404 NotFound error by @hushengquan in https://github.com/lance-format/lance/pull/5512
* fix: json's arrow extension metadata missing by @Xuanwo in https://github.com/lance-format/lance/pull/5527
* fix: infer multivector sampling rows by @BubbleCal in https://github.com/lance-format/lance/pull/5534
* fix: support ManifestNamingSchemeV2 with unordered object stores by @wjones127 in https://github.com/lance-format/lance/pull/5539
* fix: merge_insert uses full schema path for reordered columns by @wjones127 in https://github.com/lance-format/lance/pull/5541
* fix: allow storage options provider without expires_at_millis by @jackye1995 in https://github.com/lance-format/lance/pull/5542
* fix(ci): use pull_request_target for fork PR reviews by @wjones127 in https://github.com/lance-format/lance/pull/5544
* fix: restore decrease max_fragment_id in manifest by @majin1102 in https://github.com/lance-format/lance/pull/5554
* fix: improve error handling for environment variable parsing by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5560
* fix: panic when lance.auto_cleanup.interval is set to 0 by @majin1102 in https://github.com/lance-format/lance/pull/5571
* fix(python): correct type hint for to_tensor_fn parameter by @AndreaBozzo in https://github.com/lance-format/lance/pull/5577
* fix: avoid panic while hitting non-null empty multi-vector by @Xuanwo in https://github.com/lance-format/lance/pull/5588
* fix: filter garbage entries from null maps during encoding by @wkalt in https://github.com/lance-format/lance/pull/5591
* fix: reduce verbosity of errors due to string conversion by @wjones127 in https://github.com/lance-format/lance/pull/5600
* fix: remove imports that are not needed by @westonpace in https://github.com/lance-format/lance/pull/5651
* fix: allow nearest applied in default_scan_options by @chenghao-guo in https://github.com/lance-format/lance/pull/5666
* fix: trait Array has been sealed in arrow new version by @Xuanwo in https://github.com/lance-format/lance/pull/5690
* fix: project_by_schema now reorders fields inside List<Struct> types by @wjones127 in https://github.com/lance-format/lance/pull/5703
* fix: allocate too much memory for block max scores by @BubbleCal in https://github.com/lance-format/lance/pull/5718
* docs: in dataset.rs, fix comment for get_fragments by @cmccabe in https://github.com/lance-format/lance/pull/5724
* fix(python): close SQLite connections in BatchUDFCheckpoint by @wjones127 in https://github.com/lance-format/lance/pull/5733
* fix: remove credential vending features from python and java bindings by @jackye1995 in https://github.com/lance-format/lance/pull/5737
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
* docs: fix and improve the description about row id by @yanghua in https://github.com/lance-format/lance/pull/5463
* docs: add specification for handling indices by @wjones127 in https://github.com/lance-format/lance/pull/5543
* docs: fix duplicate words in comments and error messages by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5548
* docs: add research paper link to the landing page by @prrao87 in https://github.com/lance-format/lance/pull/5549
* docs: auto-build refactored namespace integrations doc by @jackye1995 in https://github.com/lance-format/lance/pull/5562
* docs: rename RowIdTreeMap to RowAddrTreeMap in rtree.md by @ddupg in https://github.com/lance-format/lance/pull/5564
* docs: add docs for DuckDB extension by @prrao87 in https://github.com/lance-format/lance/pull/5578
* docs: update Lance-DuckDB docs to latest version 0.4.1 by @prrao87 in https://github.com/lance-format/lance/pull/5613
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
* perf: offload IVF partition build to CPU pool by @BubbleCal in https://github.com/lance-format/lance/pull/5551
* perf: materialize the tokens after WAND done by @BubbleCal in https://github.com/lance-format/lance/pull/5572
* perf: compute HNSW level counts after build by @BubbleCal in https://github.com/lance-format/lance/pull/5590
* perf: improve SQ query speed by @BubbleCal in https://github.com/lance-format/lance/pull/5596
* perf: reuse zstd compressors in encoding by @wkalt in https://github.com/lance-format/lance/pull/5598
* perf: use binary search to skip documents by @BubbleCal in https://github.com/lance-format/lance/pull/5636
* perf: improve FTS indexing perf and reduce memory footprint by @BubbleCal in https://github.com/lance-format/lance/pull/5650
* perf: avoid copying tokens while merging by @BubbleCal in https://github.com/lance-format/lance/pull/5661
* perf: tighten WAND block score upper bound by @BubbleCal in https://github.com/lance-format/lance/pull/5668
* perf: cache global BM25 idf per query by @BubbleCal in https://github.com/lance-format/lance/pull/5727
* perf: use LRU cache for session contexts in get_session_context by @wjones127 in https://github.com/lance-format/lance/pull/5736
* perf: merge partitions in stream style by @BubbleCal in https://github.com/lance-format/lance/pull/5754
### Other Changes
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: rename RowIdMask to RowAddrMask by @yanghua in https://github.com/lance-format/lance/pull/5281
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449
* refactor: add store_prefix to lance-io's ObjectStore by @cmccabe in https://github.com/lance-format/lance/pull/5468
* refactor: expose take_blobs_by_addresses to python by @Xuanwo in https://github.com/lance-format/lance/pull/5474
* refactor: support java 21, drop java 8 by @cmccabe in https://github.com/lance-format/lance/pull/5565
* refactor: allow switching to bitpack inside RLE by @Xuanwo in https://github.com/lance-format/lance/pull/5595
* refactor: introduce RowSetOps and refactor RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5624

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-rc.1
### Release: lance [v2.0.0-beta.10](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.10)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.10 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
* feat!: track cumulative wall time in analyze plan by @wkalt in https://github.com/lance-format/lance/pull/5505
* fix!: check metric compatibility before using vector index by @wjones127 in https://github.com/lance-format/lance/pull/5609
* feat!: define default index name and return IndexMetadata after building index by @wjones127 in https://github.com/lance-format/lance/pull/5645
* feat!: make v2 manifest default by @wojiaodoubao in https://github.com/lance-format/lance/pull/5656
* refactor!: introduce storage options accessor by @jackye1995 in https://github.com/lance-format/lance/pull/5728
### New Features 🎉
* feat: support using FTS as a filter in vector search by @wojiaodoubao in https://github.com/lance-format/lance/pull/4928
* feat: support when_matched_delete in merge_insert by @jtuglu1 in https://github.com/lance-format/lance/pull/4939
* feat: add support for large minichunk size (u32) in format v2.2 by @niyue in https://github.com/lance-format/lance/pull/4959
* feat: support GEO RTree index by @ddupg in https://github.com/lance-format/lance/pull/5034
* feat: support global tag retrieval and improve tag api by @majin1102 in https://github.com/lance-format/lance/pull/5088
* feat: support create vector index distributedly by @chenghao-guo in https://github.com/lance-format/lance/pull/5117
* feat: support add sub-column to struct col by @wojiaodoubao in https://github.com/lance-format/lance/pull/5126
* feat: distributed range-based BTree index by @steFaiz in https://github.com/lance-format/lance/pull/5202
* feat: strategized plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5233
* feat: dataset supports deep_clone by @majin1102 in https://github.com/lance-format/lance/pull/5250
* feat: cleanup only scan managed files by @majin1102 in https://github.com/lance-format/lance/pull/5338
* feat: support map data type in lance format version 2.2 by @xloya in https://github.com/lance-format/lance/pull/5349
* feat: add RTree index spec in table format by @ddupg in https://github.com/lance-format/lance/pull/5360
* feat(java): support row lineage and cdf apis by @yanghua in https://github.com/lance-format/lance/pull/5362
* feat: disable default features on internal use by @valkum in https://github.com/lance-format/lance/pull/5372
* feat(cdf): support set start/end timestamp in cdf by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5378
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
* feat(blob_v2): add dedicated blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5406
* feat: fallback to CPU if GPU accelerating is unavailable by @BubbleCal in https://github.com/lance-format/lance/pull/5407
* feat(blob_v2): add packed blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5413
* feat: allow python tracing / logging to be independently configured by @westonpace in https://github.com/lance-format/lance/pull/5415
* feat: add additional index APIs to support count rows split plan by @jackye1995 in https://github.com/lance-format/lance/pull/5447
* feat(java): support multi-bases for writing database by @ddupg in https://github.com/lance-format/lance/pull/5450
* feat(blob_v2): add BlobAray API for user input by @Xuanwo in https://github.com/lance-format/lance/pull/5451
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat(python): support cleanup_with_policy by @ddupg in https://github.com/lance-format/lance/pull/5458
* feat: support dropping sub-column of list(struct) by @wojiaodoubao in https://github.com/lance-format/lance/pull/5469
* feat(blob_v2): add GC support by @Xuanwo in https://github.com/lance-format/lance/pull/5473
* feat: add `py.typed` marker file by @jonded94 in https://github.com/lance-format/lance/pull/5479
* feat(python): expose the `distance_range` param in the Python scanner `nearest` config by @xloya in https://github.com/lance-format/lance/pull/5486
* feat(java): simplify the use of optional in jni by @ddupg in https://github.com/lance-format/lance/pull/5488
* feat(blob_v2): add Python API for Blob v2 by @Xuanwo in https://github.com/lance-format/lance/pull/5491
* feat(python): add DatasetBasePath stub to improve IDE hints by @ddupg in https://github.com/lance-format/lance/pull/5503
* feat(memtest): add macos support by @Xuanwo in https://github.com/lance-format/lance/pull/5510
* feat(java): add full text search api by @wojiaodoubao in https://github.com/lance-format/lance/pull/5563
* feat: support credentials vending in directory namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5566
* feat: upgrade lance-namespace to 0.4.0 by @jackye1995 in https://github.com/lance-format/lance/pull/5568
* feat: add skip_merge for FTS index build by @BubbleCal in https://github.com/lance-format/lance/pull/5570
* feat(java): add builder-style scalar index params by @wojiaodoubao in https://github.com/lance-format/lance/pull/5581
* feat: optimize rle implementation by @Xuanwo in https://github.com/lance-format/lance/pull/5586
* feat: support FixedSizeList<Struct> by @wkalt in https://github.com/lance-format/lance/pull/5593
* feat: add dictionary encoding for 64bit types like int64/double by @Xuanwo in https://github.com/lance-format/lance/pull/5594
* feat: support merge_insert with source dedupe on first seen value by @jackye1995 in https://github.com/lance-format/lance/pull/5603
* feat: support truncate table api by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5604
* feat: add Error::External variant for preserving user errors by @wjones127 in https://github.com/lance-format/lance/pull/5606
* feat: upgrade lance-namespace to 0.4.5 by @jackye1995 in https://github.com/lance-format/lance/pull/5611
* feat: refactor use of Error::io by @lichuang in https://github.com/lance-format/lance/pull/5612
* feat(java): add detached flag to commitTransaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5626
* feat: add parts_searched metrics for FTS by @BubbleCal in https://github.com/lance-format/lance/pull/5627
* feat: improve the random access file benchmark by @westonpace in https://github.com/lance-format/lance/pull/5628
* feat(oss): add sts token support for aliyun oss via storage_options by @hh23485 in https://github.com/lance-format/lance/pull/5632
* feat: merge-insert with primary key dedupe by @jackye1995 in https://github.com/lance-format/lance/pull/5633
* feat: allow configure temp dir size for datafusion exec by @jackye1995 in https://github.com/lance-format/lance/pull/5659
* feat(java): add support for optimizing indices by @majin1102 in https://github.com/lance-format/lance/pull/5663
* feat: make on arg optional for merge insert api by @yanghua in https://github.com/lance-format/lance/pull/5667
* feat: make OneShotPartitionStream pub by @timsaucer in https://github.com/lance-format/lance/pull/5672
* feat: support array_contains in LabelList scalar index by @fenfeng9 in https://github.com/lance-format/lance/pull/5681
* feat: add order to primary key by @touch-of-grey in https://github.com/lance-format/lance/pull/5683
* feat: use independent region manifest for MemWAL by @touch-of-grey in https://github.com/lance-format/lance/pull/5689
* feat: add stats() method to ObjectStoreRegistry by @wkalt in https://github.com/lance-format/lance/pull/5706
* feat: support dynamic context for lance namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5710
* feat: cleanup partial idx files when merging distributed vector index by @yanghua in https://github.com/lance-format/lance/pull/5729
### Bug Fixes 🐛
* fix: correct null_count aggregation in boolean statistics collection by @YinZheng-Sun in https://github.com/lance-format/lance/pull/4839
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: fix vector index prewarm index by @xloya in https://github.com/lance-format/lance/pull/5412
* fix: panic unwrap on None in decoder.rs by @camilesing in https://github.com/lance-format/lance/pull/5424
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5464
* fix: make column name lookups case-insensitive by @wjones127 in https://github.com/lance-format/lance/pull/5465
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5499
* fix(java): support FixedSizeList for java LanceField by @fangbo in https://github.com/lance-format/lance/pull/5509
* fix: head external manifest object happend 404 NotFound error by @hushengquan in https://github.com/lance-format/lance/pull/5512
* fix: json's arrow extension metadata missing by @Xuanwo in https://github.com/lance-format/lance/pull/5527
* fix: infer multivector sampling rows by @BubbleCal in https://github.com/lance-format/lance/pull/5534
* fix: support ManifestNamingSchemeV2 with unordered object stores by @wjones127 in https://github.com/lance-format/lance/pull/5539
* fix: merge_insert uses full schema path for reordered columns by @wjones127 in https://github.com/lance-format/lance/pull/5541
* fix: allow storage options provider without expires_at_millis by @jackye1995 in https://github.com/lance-format/lance/pull/5542
* fix(ci): use pull_request_target for fork PR reviews by @wjones127 in https://github.com/lance-format/lance/pull/5544
* fix: restore decrease max_fragment_id in manifest by @majin1102 in https://github.com/lance-format/lance/pull/5554
* fix: improve error handling for environment variable parsing by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5560
* fix: panic when lance.auto_cleanup.interval is set to 0 by @majin1102 in https://github.com/lance-format/lance/pull/5571
* fix(python): correct type hint for to_tensor_fn parameter by @AndreaBozzo in https://github.com/lance-format/lance/pull/5577
* fix: avoid panic while hitting non-null empty multi-vector by @Xuanwo in https://github.com/lance-format/lance/pull/5588
* fix: filter garbage entries from null maps during encoding by @wkalt in https://github.com/lance-format/lance/pull/5591
* fix: reduce verbosity of errors due to string conversion by @wjones127 in https://github.com/lance-format/lance/pull/5600
* fix: remove imports that are not needed by @westonpace in https://github.com/lance-format/lance/pull/5651
* fix: allow nearest applied in default_scan_options by @chenghao-guo in https://github.com/lance-format/lance/pull/5666
* fix: trait Array has been sealed in arrow new version by @Xuanwo in https://github.com/lance-format/lance/pull/5690
* fix: project_by_schema now reorders fields inside List<Struct> types by @wjones127 in https://github.com/lance-format/lance/pull/5703
* fix: allocate too much memory for block max scores by @BubbleCal in https://github.com/lance-format/lance/pull/5718
* docs: in dataset.rs, fix comment for get_fragments by @cmccabe in https://github.com/lance-format/lance/pull/5724
* fix(python): close SQLite connections in BatchUDFCheckpoint by @wjones127 in https://github.com/lance-format/lance/pull/5733
* fix: remove credential vending features from python and java bindings by @jackye1995 in https://github.com/lance-format/lance/pull/5737
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
* docs: fix and improve the description about row id by @yanghua in https://github.com/lance-format/lance/pull/5463
* docs: add specification for handling indices by @wjones127 in https://github.com/lance-format/lance/pull/5543
* docs: fix duplicate words in comments and error messages by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5548
* docs: add research paper link to the landing page by @prrao87 in https://github.com/lance-format/lance/pull/5549
* docs: auto-build refactored namespace integrations doc by @jackye1995 in https://github.com/lance-format/lance/pull/5562
* docs: rename RowIdTreeMap to RowAddrTreeMap in rtree.md by @ddupg in https://github.com/lance-format/lance/pull/5564
* docs: add docs for DuckDB extension by @prrao87 in https://github.com/lance-format/lance/pull/5578
* docs: update Lance-DuckDB docs to latest version 0.4.1 by @prrao87 in https://github.com/lance-format/lance/pull/5613
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
* perf: offload IVF partition build to CPU pool by @BubbleCal in https://github.com/lance-format/lance/pull/5551
* perf: materialize the tokens after WAND done by @BubbleCal in https://github.com/lance-format/lance/pull/5572
* perf: compute HNSW level counts after build by @BubbleCal in https://github.com/lance-format/lance/pull/5590
* perf: improve SQ query speed by @BubbleCal in https://github.com/lance-format/lance/pull/5596
* perf: reuse zstd compressors in encoding by @wkalt in https://github.com/lance-format/lance/pull/5598
* perf: use binary search to skip documents by @BubbleCal in https://github.com/lance-format/lance/pull/5636
* perf: improve FTS indexing perf and reduce memory footprint by @BubbleCal in https://github.com/lance-format/lance/pull/5650
* perf: avoid copying tokens while merging by @BubbleCal in https://github.com/lance-format/lance/pull/5661
* perf: tighten WAND block score upper bound by @BubbleCal in https://github.com/lance-format/lance/pull/5668
* perf: cache global BM25 idf per query by @BubbleCal in https://github.com/lance-format/lance/pull/5727
* perf: use LRU cache for session contexts in get_session_context by @wjones127 in https://github.com/lance-format/lance/pull/5736
### Other Changes
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: rename RowIdMask to RowAddrMask by @yanghua in https://github.com/lance-format/lance/pull/5281
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449
* refactor: add store_prefix to lance-io's ObjectStore by @cmccabe in https://github.com/lance-format/lance/pull/5468
* refactor: expose take_blobs_by_addresses to python by @Xuanwo in https://github.com/lance-format/lance/pull/5474
* refactor: support java 21, drop java 8 by @cmccabe in https://github.com/lance-format/lance/pull/5565
* refactor: allow switching to bitpack inside RLE by @Xuanwo in https://github.com/lance-format/lance/pull/5595

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.10
### Release: lance [v2.0.0-beta.9](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.9)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.9 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
* feat!: track cumulative wall time in analyze plan by @wkalt in https://github.com/lance-format/lance/pull/5505
* fix!: check metric compatibility before using vector index by @wjones127 in https://github.com/lance-format/lance/pull/5609
* feat!: make v2 manifest default by @wojiaodoubao in https://github.com/lance-format/lance/pull/5656
### New Features 🎉
* feat: support using FTS as a filter in vector search by @wojiaodoubao in https://github.com/lance-format/lance/pull/4928
* feat: support when_matched_delete in merge_insert by @jtuglu1 in https://github.com/lance-format/lance/pull/4939
* feat: add support for large minichunk size (u32) in format v2.2 by @niyue in https://github.com/lance-format/lance/pull/4959
* feat: support GEO RTree index by @ddupg in https://github.com/lance-format/lance/pull/5034
* feat: support global tag retrieval and improve tag api by @majin1102 in https://github.com/lance-format/lance/pull/5088
* feat: support create vector index distributedly by @chenghao-guo in https://github.com/lance-format/lance/pull/5117
* feat: support add sub-column to struct col by @wojiaodoubao in https://github.com/lance-format/lance/pull/5126
* feat: distributed range-based BTree index by @steFaiz in https://github.com/lance-format/lance/pull/5202
* feat: strategized plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5233
* feat: dataset supports deep_clone by @majin1102 in https://github.com/lance-format/lance/pull/5250
* feat: cleanup only scan managed files by @majin1102 in https://github.com/lance-format/lance/pull/5338
* feat: support map data type in lance format version 2.2 by @xloya in https://github.com/lance-format/lance/pull/5349
* feat: add RTree index spec in table format by @ddupg in https://github.com/lance-format/lance/pull/5360
* feat(java): support row lineage and cdf apis by @yanghua in https://github.com/lance-format/lance/pull/5362
* feat: disable default features on internal use by @valkum in https://github.com/lance-format/lance/pull/5372
* feat(cdf): support set start/end timestamp in cdf by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5378
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
* feat(blob_v2): add dedicated blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5406
* feat: fallback to CPU if GPU accelerating is unavailable by @BubbleCal in https://github.com/lance-format/lance/pull/5407
* feat(blob_v2): add packed blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5413
* feat: allow python tracing / logging to be independently configured by @westonpace in https://github.com/lance-format/lance/pull/5415
* feat: add additional index APIs to support count rows split plan by @jackye1995 in https://github.com/lance-format/lance/pull/5447
* feat(java): support multi-bases for writing database by @ddupg in https://github.com/lance-format/lance/pull/5450
* feat(blob_v2): add BlobAray API for user input by @Xuanwo in https://github.com/lance-format/lance/pull/5451
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat(python): support cleanup_with_policy by @ddupg in https://github.com/lance-format/lance/pull/5458
* feat: support dropping sub-column of list(struct) by @wojiaodoubao in https://github.com/lance-format/lance/pull/5469
* feat(blob_v2): add GC support by @Xuanwo in https://github.com/lance-format/lance/pull/5473
* feat: add `py.typed` marker file by @jonded94 in https://github.com/lance-format/lance/pull/5479
* feat(python): expose the `distance_range` param in the Python scanner `nearest` config by @xloya in https://github.com/lance-format/lance/pull/5486
* feat(java): simplify the use of optional in jni by @ddupg in https://github.com/lance-format/lance/pull/5488
* feat(blob_v2): add Python API for Blob v2 by @Xuanwo in https://github.com/lance-format/lance/pull/5491
* feat(python): add DatasetBasePath stub to improve IDE hints by @ddupg in https://github.com/lance-format/lance/pull/5503
* feat(memtest): add macos support by @Xuanwo in https://github.com/lance-format/lance/pull/5510
* feat(java): add full text search api by @wojiaodoubao in https://github.com/lance-format/lance/pull/5563
* feat: support credentials vending in directory namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5566
* feat: upgrade lance-namespace to 0.4.0 by @jackye1995 in https://github.com/lance-format/lance/pull/5568
* feat: add skip_merge for FTS index build by @BubbleCal in https://github.com/lance-format/lance/pull/5570
* feat(java): add builder-style scalar index params by @wojiaodoubao in https://github.com/lance-format/lance/pull/5581
* feat: optimize rle implementation by @Xuanwo in https://github.com/lance-format/lance/pull/5586
* feat: support FixedSizeList<Struct> by @wkalt in https://github.com/lance-format/lance/pull/5593
* feat: add dictionary encoding for 64bit types like int64/double by @Xuanwo in https://github.com/lance-format/lance/pull/5594
* feat: support merge_insert with source dedupe on first seen value by @jackye1995 in https://github.com/lance-format/lance/pull/5603
* feat: support truncate table api by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5604
* feat: add Error::External variant for preserving user errors by @wjones127 in https://github.com/lance-format/lance/pull/5606
* feat: upgrade lance-namespace to 0.4.5 by @jackye1995 in https://github.com/lance-format/lance/pull/5611
* feat: refactor use of Error::io by @lichuang in https://github.com/lance-format/lance/pull/5612
* feat(java): add detached flag to commitTransaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5626
* feat: add parts_searched metrics for FTS by @BubbleCal in https://github.com/lance-format/lance/pull/5627
* feat(oss): add sts token support for aliyun oss via storage_options by @hh23485 in https://github.com/lance-format/lance/pull/5632
* feat: merge-insert with primary key dedupe by @jackye1995 in https://github.com/lance-format/lance/pull/5633
* feat: allow configure temp dir size for datafusion exec by @jackye1995 in https://github.com/lance-format/lance/pull/5659
* feat(java): add support for optimizing indices by @majin1102 in https://github.com/lance-format/lance/pull/5663
* feat: make on arg optional for merge insert api by @yanghua in https://github.com/lance-format/lance/pull/5667
* feat: make OneShotPartitionStream pub by @timsaucer in https://github.com/lance-format/lance/pull/5672
* feat: add order to primary key by @touch-of-grey in https://github.com/lance-format/lance/pull/5683
* feat: use independent region manifest for MemWAL by @touch-of-grey in https://github.com/lance-format/lance/pull/5689
* feat: add stats() method to ObjectStoreRegistry by @wkalt in https://github.com/lance-format/lance/pull/5706
* feat: support dynamic context for lance namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5710
### Bug Fixes 🐛
* fix: correct null_count aggregation in boolean statistics collection by @YinZheng-Sun in https://github.com/lance-format/lance/pull/4839
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: fix vector index prewarm index by @xloya in https://github.com/lance-format/lance/pull/5412
* fix: panic unwrap on None in decoder.rs by @camilesing in https://github.com/lance-format/lance/pull/5424
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5464
* fix: make column name lookups case-insensitive by @wjones127 in https://github.com/lance-format/lance/pull/5465
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5499
* fix(java): support FixedSizeList for java LanceField by @fangbo in https://github.com/lance-format/lance/pull/5509
* fix: head external manifest object happend 404 NotFound error by @hushengquan in https://github.com/lance-format/lance/pull/5512
* fix: json's arrow extension metadata missing by @Xuanwo in https://github.com/lance-format/lance/pull/5527
* fix: infer multivector sampling rows by @BubbleCal in https://github.com/lance-format/lance/pull/5534
* fix: support ManifestNamingSchemeV2 with unordered object stores by @wjones127 in https://github.com/lance-format/lance/pull/5539
* fix: merge_insert uses full schema path for reordered columns by @wjones127 in https://github.com/lance-format/lance/pull/5541
* fix: allow storage options provider without expires_at_millis by @jackye1995 in https://github.com/lance-format/lance/pull/5542
* fix(ci): use pull_request_target for fork PR reviews by @wjones127 in https://github.com/lance-format/lance/pull/5544
* fix: restore decrease max_fragment_id in manifest by @majin1102 in https://github.com/lance-format/lance/pull/5554
* fix: panic when lance.auto_cleanup.interval is set to 0 by @majin1102 in https://github.com/lance-format/lance/pull/5571
* fix(python): correct type hint for to_tensor_fn parameter by @AndreaBozzo in https://github.com/lance-format/lance/pull/5577
* fix: avoid panic while hitting non-null empty multi-vector by @Xuanwo in https://github.com/lance-format/lance/pull/5588
* fix: filter garbage entries from null maps during encoding by @wkalt in https://github.com/lance-format/lance/pull/5591
* fix: reduce verbosity of errors due to string conversion by @wjones127 in https://github.com/lance-format/lance/pull/5600
* fix: remove imports that are not needed by @westonpace in https://github.com/lance-format/lance/pull/5651
* fix: allow nearest applied in default_scan_options by @chenghao-guo in https://github.com/lance-format/lance/pull/5666
* fix: trait Array has been sealed in arrow new version by @Xuanwo in https://github.com/lance-format/lance/pull/5690
* fix: project_by_schema now reorders fields inside List<Struct> types by @wjones127 in https://github.com/lance-format/lance/pull/5703
* fix: allocate too much memory for block max scores by @BubbleCal in https://github.com/lance-format/lance/pull/5718
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
* docs: fix and improve the description about row id by @yanghua in https://github.com/lance-format/lance/pull/5463
* docs: add specification for handling indices by @wjones127 in https://github.com/lance-format/lance/pull/5543
* docs: fix duplicate words in comments and error messages by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5548
* docs: add research paper link to the landing page by @prrao87 in https://github.com/lance-format/lance/pull/5549
* docs: auto-build refactored namespace integrations doc by @jackye1995 in https://github.com/lance-format/lance/pull/5562
* docs: rename RowIdTreeMap to RowAddrTreeMap in rtree.md by @ddupg in https://github.com/lance-format/lance/pull/5564
* docs: add docs for DuckDB extension by @prrao87 in https://github.com/lance-format/lance/pull/5578
* docs: update Lance-DuckDB docs to latest version 0.4.1 by @prrao87 in https://github.com/lance-format/lance/pull/5613
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
* perf: offload IVF partition build to CPU pool by @BubbleCal in https://github.com/lance-format/lance/pull/5551
* perf: materialize the tokens after WAND done by @BubbleCal in https://github.com/lance-format/lance/pull/5572
* perf: compute HNSW level counts after build by @BubbleCal in https://github.com/lance-format/lance/pull/5590
* perf: improve SQ query speed by @BubbleCal in https://github.com/lance-format/lance/pull/5596
* perf: reuse zstd compressors in encoding by @wkalt in https://github.com/lance-format/lance/pull/5598
* perf: use binary search to skip documents by @BubbleCal in https://github.com/lance-format/lance/pull/5636
* perf: improve FTS indexing perf and reduce memory footprint by @BubbleCal in https://github.com/lance-format/lance/pull/5650
* perf: avoid copying tokens while merging by @BubbleCal in https://github.com/lance-format/lance/pull/5661
* perf: tighten WAND block score upper bound by @BubbleCal in https://github.com/lance-format/lance/pull/5668
### Other Changes
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: rename RowIdMask to RowAddrMask by @yanghua in https://github.com/lance-format/lance/pull/5281
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449
* refactor: add store_prefix to lance-io's ObjectStore by @cmccabe in https://github.com/lance-format/lance/pull/5468
* refactor: expose take_blobs_by_addresses to python by @Xuanwo in https://github.com/lance-format/lance/pull/5474
* refactor: support java 21, drop java 8 by @cmccabe in https://github.com/lance-format/lance/pull/5565
* refactor: allow switching to bitpack inside RLE by @Xuanwo in https://github.com/lance-format/lance/pull/5595

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.9
### Release: lance [v1.0.2](https://github.com/lance-format/lance/releases/tag/v1.0.2)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.2 -->

## What's Changed
### Performance Improvements 🚀
* perf: reuse session context by @jackye1995 in https://github.com/lance-format/lance/pull/5696

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.1...v1.0.2
### Release: lance [v2.0.0-beta.8](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.8)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.8 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
* feat!: track cumulative wall time in analyze plan by @wkalt in https://github.com/lance-format/lance/pull/5505
### New Features 🎉
* feat: support using FTS as a filter in vector search by @wojiaodoubao in https://github.com/lance-format/lance/pull/4928
* feat: support when_matched_delete in merge_insert by @jtuglu1 in https://github.com/lance-format/lance/pull/4939
* feat: add support for large minichunk size (u32) in format v2.2 by @niyue in https://github.com/lance-format/lance/pull/4959
* feat: support GEO RTree index by @ddupg in https://github.com/lance-format/lance/pull/5034
* feat: support global tag retrieval and improve tag api by @majin1102 in https://github.com/lance-format/lance/pull/5088
* feat: support create vector index distributedly by @chenghao-guo in https://github.com/lance-format/lance/pull/5117
* feat: support add sub-column to struct col by @wojiaodoubao in https://github.com/lance-format/lance/pull/5126
* feat: distributed range-based BTree index by @steFaiz in https://github.com/lance-format/lance/pull/5202
* feat: strategized plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5233
* feat: dataset supports deep_clone by @majin1102 in https://github.com/lance-format/lance/pull/5250
* feat: cleanup only scan managed files by @majin1102 in https://github.com/lance-format/lance/pull/5338
* feat: support map data type in lance format version 2.2 by @xloya in https://github.com/lance-format/lance/pull/5349
* feat: add RTree index spec in table format by @ddupg in https://github.com/lance-format/lance/pull/5360
* feat(java): support row lineage and cdf apis by @yanghua in https://github.com/lance-format/lance/pull/5362
* feat: disable default features on internal use by @valkum in https://github.com/lance-format/lance/pull/5372
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
* feat(blob_v2): add dedicated blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5406
* feat: fallback to CPU if GPU accelerating is unavailable by @BubbleCal in https://github.com/lance-format/lance/pull/5407
* feat(blob_v2): add packed blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5413
* feat: allow python tracing / logging to be independently configured by @westonpace in https://github.com/lance-format/lance/pull/5415
* feat: add additional index APIs to support count rows split plan by @jackye1995 in https://github.com/lance-format/lance/pull/5447
* feat(java): support multi-bases for writing database by @ddupg in https://github.com/lance-format/lance/pull/5450
* feat(blob_v2): add BlobAray API for user input by @Xuanwo in https://github.com/lance-format/lance/pull/5451
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat(python): support cleanup_with_policy by @ddupg in https://github.com/lance-format/lance/pull/5458
* feat: support dropping sub-column of list(struct) by @wojiaodoubao in https://github.com/lance-format/lance/pull/5469
* feat(blob_v2): add GC support by @Xuanwo in https://github.com/lance-format/lance/pull/5473
* feat: add `py.typed` marker file by @jonded94 in https://github.com/lance-format/lance/pull/5479
* feat(python): expose the `distance_range` param in the Python scanner `nearest` config by @xloya in https://github.com/lance-format/lance/pull/5486
* feat(java): simplify the use of optional in jni by @ddupg in https://github.com/lance-format/lance/pull/5488
* feat(blob_v2): add Python API for Blob v2 by @Xuanwo in https://github.com/lance-format/lance/pull/5491
* feat(python): add DatasetBasePath stub to improve IDE hints by @ddupg in https://github.com/lance-format/lance/pull/5503
* feat(memtest): add macos support by @Xuanwo in https://github.com/lance-format/lance/pull/5510
* feat(java): add full text search api by @wojiaodoubao in https://github.com/lance-format/lance/pull/5563
* feat: support credentials vending in directory namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5566
* feat: upgrade lance-namespace to 0.4.0 by @jackye1995 in https://github.com/lance-format/lance/pull/5568
* feat: add skip_merge for FTS index build by @BubbleCal in https://github.com/lance-format/lance/pull/5570
* feat(java): add builder-style scalar index params by @wojiaodoubao in https://github.com/lance-format/lance/pull/5581
* feat: optimize rle implementation by @Xuanwo in https://github.com/lance-format/lance/pull/5586
* feat: support FixedSizeList<Struct> by @wkalt in https://github.com/lance-format/lance/pull/5593
* feat: add dictionary encoding for 64bit types like int64/double by @Xuanwo in https://github.com/lance-format/lance/pull/5594
* feat: support merge_insert with source dedupe on first seen value by @jackye1995 in https://github.com/lance-format/lance/pull/5603
* feat: upgrade lance-namespace to 0.4.5 by @jackye1995 in https://github.com/lance-format/lance/pull/5611
* feat(java): add detached flag to commitTransaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5626
* feat: add parts_searched metrics for FTS by @BubbleCal in https://github.com/lance-format/lance/pull/5627
* feat(oss): add sts token support for aliyun oss via storage_options by @hh23485 in https://github.com/lance-format/lance/pull/5632
* feat: merge-insert with primary key dedupe by @jackye1995 in https://github.com/lance-format/lance/pull/5633
* feat: allow configure temp dir size for datafusion exec by @jackye1995 in https://github.com/lance-format/lance/pull/5659
* feat: add order to primary key by @touch-of-grey in https://github.com/lance-format/lance/pull/5683
### Bug Fixes 🐛
* fix: correct null_count aggregation in boolean statistics collection by @YinZheng-Sun in https://github.com/lance-format/lance/pull/4839
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: fix vector index prewarm index by @xloya in https://github.com/lance-format/lance/pull/5412
* fix: panic unwrap on None in decoder.rs by @camilesing in https://github.com/lance-format/lance/pull/5424
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5464
* fix: make column name lookups case-insensitive by @wjones127 in https://github.com/lance-format/lance/pull/5465
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5499
* fix: head external manifest object happend 404 NotFound error by @hushengquan in https://github.com/lance-format/lance/pull/5512
* fix: json's arrow extension metadata missing by @Xuanwo in https://github.com/lance-format/lance/pull/5527
* fix: infer multivector sampling rows by @BubbleCal in https://github.com/lance-format/lance/pull/5534
* fix: support ManifestNamingSchemeV2 with unordered object stores by @wjones127 in https://github.com/lance-format/lance/pull/5539
* fix: merge_insert uses full schema path for reordered columns by @wjones127 in https://github.com/lance-format/lance/pull/5541
* fix: allow storage options provider without expires_at_millis by @jackye1995 in https://github.com/lance-format/lance/pull/5542
* fix(ci): use pull_request_target for fork PR reviews by @wjones127 in https://github.com/lance-format/lance/pull/5544
* fix: restore decrease max_fragment_id in manifest by @majin1102 in https://github.com/lance-format/lance/pull/5554
* fix: panic when lance.auto_cleanup.interval is set to 0 by @majin1102 in https://github.com/lance-format/lance/pull/5571
* fix: avoid panic while hitting non-null empty multi-vector by @Xuanwo in https://github.com/lance-format/lance/pull/5588
* fix: filter garbage entries from null maps during encoding by @wkalt in https://github.com/lance-format/lance/pull/5591
* fix: remove imports that are not needed by @westonpace in https://github.com/lance-format/lance/pull/5651
* fix: allow nearest applied in default_scan_options by @chenghao-guo in https://github.com/lance-format/lance/pull/5666
* fix: trait Array has been sealed in arrow new version by @Xuanwo in https://github.com/lance-format/lance/pull/5690
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
* docs: fix and improve the description about row id by @yanghua in https://github.com/lance-format/lance/pull/5463
* docs: add specification for handling indices by @wjones127 in https://github.com/lance-format/lance/pull/5543
* docs: fix duplicate words in comments and error messages by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5548
* docs: add research paper link to the landing page by @prrao87 in https://github.com/lance-format/lance/pull/5549
* docs: auto-build refactored namespace integrations doc by @jackye1995 in https://github.com/lance-format/lance/pull/5562
* docs: rename RowIdTreeMap to RowAddrTreeMap in rtree.md by @ddupg in https://github.com/lance-format/lance/pull/5564
* docs: add docs for DuckDB extension by @prrao87 in https://github.com/lance-format/lance/pull/5578
* docs: update Lance-DuckDB docs to latest version 0.4.1 by @prrao87 in https://github.com/lance-format/lance/pull/5613
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
* perf: offload IVF partition build to CPU pool by @BubbleCal in https://github.com/lance-format/lance/pull/5551
* perf: materialize the tokens after WAND done by @BubbleCal in https://github.com/lance-format/lance/pull/5572
* perf: compute HNSW level counts after build by @BubbleCal in https://github.com/lance-format/lance/pull/5590
* perf: improve SQ query speed by @BubbleCal in https://github.com/lance-format/lance/pull/5596
* perf: reuse zstd compressors in encoding by @wkalt in https://github.com/lance-format/lance/pull/5598
* perf: improve FTS indexing perf and reduce memory footprint by @BubbleCal in https://github.com/lance-format/lance/pull/5650
* perf: tighten WAND block score upper bound by @BubbleCal in https://github.com/lance-format/lance/pull/5668
### Other Changes
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: rename RowIdMask to RowAddrMask by @yanghua in https://github.com/lance-format/lance/pull/5281
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449
* refactor: add store_prefix to lance-io's ObjectStore by @cmccabe in https://github.com/lance-format/lance/pull/5468
* refactor: expose take_blobs_by_addresses to python by @Xuanwo in https://github.com/lance-format/lance/pull/5474
* refactor: support java 21, drop java 8 by @cmccabe in https://github.com/lance-format/lance/pull/5565
* refactor: allow switching to bitpack inside RLE by @Xuanwo in https://github.com/lance-format/lance/pull/5595

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.8
### Release: lance [v1.0.2-rc.2](https://github.com/lance-format/lance/releases/tag/v1.0.2-rc.2)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.2-rc.2 -->

## What's Changed
### Performance Improvements 🚀
* perf: reuse session context by @jackye1995 in https://github.com/lance-format/lance/pull/5696

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.1...v1.0.2-rc.2
### Release: lance [v1.0.1](https://github.com/lance-format/lance/releases/tag/v1.0.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.1 -->

## What's Changed
### Bug Fixes 🐛
* fix: make column name lookups case-insensitive by @wjones127 in https://github.com/lance-format/lance/pull/5465
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5495
* fix: panic unwrap on None in decoder.rs by @jackye1995 in https://github.com/lance-format/lance/pull/5498
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5500
* fix: head external manifest object happend 404 NotFound error by @hushengquan in https://github.com/lance-format/lance/pull/5512
* fix: json's arrow extension metadata missing by @Xuanwo in https://github.com/lance-format/lance/pull/5527
* fix: infer multivector sampling rows by @BubbleCal in https://github.com/lance-format/lance/pull/5534
* fix: support ManifestNamingSchemeV2 with unordered object stores by @wjones127 in https://github.com/lance-format/lance/pull/5539
* fix: merge_insert uses full schema path for reordered columns by @wjones127 in https://github.com/lance-format/lance/pull/5541
### Other Changes
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.0...v1.0.1
### Release: lance [v2.0.0-beta.5](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.5)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.5 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
* feat!: track cumulative wall time in analyze plan by @wkalt in https://github.com/lance-format/lance/pull/5505
### New Features 🎉
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
* feat: fallback to CPU if GPU accelerating is unavailable by @BubbleCal in https://github.com/lance-format/lance/pull/5407
* feat: disable default features on internal use by @valkum in https://github.com/lance-format/lance/pull/5372
* feat(blob_v2): add dedicated blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5406
* feat(blob_v2): add packed blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5413
* feat: strategized plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5233
* feat: support add sub-column to struct col by @wojiaodoubao in https://github.com/lance-format/lance/pull/5126
* feat: distributed range-based BTree index by @steFaiz in https://github.com/lance-format/lance/pull/5202
* feat: upgrade lance-namespace to 0.3.1 and add missing apis by @jackye1995 in https://github.com/lance-format/lance/pull/5457
* feat: add additional index APIs to support count rows split plan by @jackye1995 in https://github.com/lance-format/lance/pull/5447
* feat(blob_v2): add BlobAray API for user input by @Xuanwo in https://github.com/lance-format/lance/pull/5451
* feat: support using FTS as a filter in vector search by @wojiaodoubao in https://github.com/lance-format/lance/pull/4928
* feat(java): support multi-bases for writing database by @ddupg in https://github.com/lance-format/lance/pull/5450
* feat: add `py.typed` marker file by @jonded94 in https://github.com/lance-format/lance/pull/5479
* feat: support map data type in lance format version 2.2 by @xloya in https://github.com/lance-format/lance/pull/5349
* feat(blob_v2): add GC support by @Xuanwo in https://github.com/lance-format/lance/pull/5473
* feat(python): support cleanup_with_policy by @ddupg in https://github.com/lance-format/lance/pull/5458
* feat(java): simplify the use of optional in jni by @ddupg in https://github.com/lance-format/lance/pull/5488
* feat(python): add DatasetBasePath stub to improve IDE hints by @ddupg in https://github.com/lance-format/lance/pull/5503
* feat: cleanup only scan managed files by @majin1102 in https://github.com/lance-format/lance/pull/5338
* feat(java): support row lineage and cdf apis by @yanghua in https://github.com/lance-format/lance/pull/5362
* feat(memtest): add macos support by @Xuanwo in https://github.com/lance-format/lance/pull/5510
* feat: add support for large minichunk size (u32) in format v2.2 by @niyue in https://github.com/lance-format/lance/pull/4959
* feat(blob_v2): add Python API for Blob v2 by @Xuanwo in https://github.com/lance-format/lance/pull/5491
* feat: support global tag retrieval and improve tag api by @majin1102 in https://github.com/lance-format/lance/pull/5088
* feat: add RTree index spec in table format by @ddupg in https://github.com/lance-format/lance/pull/5360
* feat: dataset supports deep_clone by @majin1102 in https://github.com/lance-format/lance/pull/5250
### Bug Fixes 🐛
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
* fix: fix vector index prewarm index by @xloya in https://github.com/lance-format/lance/pull/5412
* fix: panic unwrap on None in decoder.rs by @camilesing in https://github.com/lance-format/lance/pull/5424
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5464
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5499
* fix: head external manifest object happend 404 NotFound error by @hushengquan in https://github.com/lance-format/lance/pull/5512
* fix: infer multivector sampling rows by @BubbleCal in https://github.com/lance-format/lance/pull/5534
* fix: json's arrow extension metadata missing by @Xuanwo in https://github.com/lance-format/lance/pull/5527
* fix: support ManifestNamingSchemeV2 with unordered object stores by @wjones127 in https://github.com/lance-format/lance/pull/5539
* fix: allow storage options provider without expires_at_millis by @jackye1995 in https://github.com/lance-format/lance/pull/5542
* fix(ci): use pull_request_target for fork PR reviews by @wjones127 in https://github.com/lance-format/lance/pull/5544
* fix: make column name lookups case-insensitive by @wjones127 in https://github.com/lance-format/lance/pull/5465
* fix: merge_insert uses full schema path for reordered columns by @wjones127 in https://github.com/lance-format/lance/pull/5541
* fix: correct null_count aggregation in boolean statistics collection by @YinZheng-Sun in https://github.com/lance-format/lance/pull/4839
* fix: restore decrease max_fragment_id in manifest by @majin1102 in https://github.com/lance-format/lance/pull/5554
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
* docs: fix and improve the description about row id by @yanghua in https://github.com/lance-format/lance/pull/5463
* docs: fix duplicate words in comments and error messages by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5548
* docs: auto-build refactored namespace integrations doc by @jackye1995 in https://github.com/lance-format/lance/pull/5562
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
* perf: offload IVF partition build to CPU pool by @BubbleCal in https://github.com/lance-format/lance/pull/5551
* perf: materialize the tokens after WAND done by @BubbleCal in https://github.com/lance-format/lance/pull/5572
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449
* refactor: expose take_blobs_by_addresses to python by @Xuanwo in https://github.com/lance-format/lance/pull/5474
* refactor: add store_prefix to lance-io's ObjectStore by @cmccabe in https://github.com/lance-format/lance/pull/5468
* refactor: rename RowIdMask to RowAddrMask by @yanghua in https://github.com/lance-format/lance/pull/5281
* refactor: support java 21, drop java 8 by @cmccabe in https://github.com/lance-format/lance/pull/5565

## New Contributors
* @mackrorysd made their first contribution in https://github.com/lance-format/lance/pull/5315
* @valkum made their first contribution in https://github.com/lance-format/lance/pull/5372
* @rongou made their first contribution in https://github.com/lance-format/lance/pull/5439
* @camilesing made their first contribution in https://github.com/lance-format/lance/pull/5424
* @hfutatzhanghb made their first contribution in https://github.com/lance-format/lance/pull/5470
* @jonded94 made their first contribution in https://github.com/lance-format/lance/pull/5479
* @hushengquan made their first contribution in https://github.com/lance-format/lance/pull/5512
* @XuQianJin-Stars made their first contribution in https://github.com/lance-format/lance/pull/5548
* @YinZheng-Sun made their first contribution in https://github.com/lance-format/lance/pull/4839

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.5
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 6 releases: ['Node/Rust LanceDB v0.24.0', 'Python LanceDB v0.27.0', 'Node/Rust LanceDB v0.24.0-beta.0', 'Python LanceDB v0.27.0-beta.0', 'Node/Rust LanceDB v0.23.1', 'Python LanceDB v0.26.1']
### Release: lancedb [Node/Rust LanceDB v0.24.0](https://github.com/lancedb/lancedb/releases/tag/v0.24.0)
## 🛠 Breaking Changes

- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912

## 🎉 New Features

- feat: voyage-multimodal-3.5 by @fzowl in https://github.com/lancedb/lancedb/pull/2887
- feat: support remote ivf rq by @LuQQiu in https://github.com/lancedb/lancedb/pull/2863
- feat: parallelize embedding computations by @ex172000 in https://github.com/lancedb/lancedb/pull/2896
- feat: enable huggingface feature by default by @Xuanwo in https://github.com/lancedb/lancedb/pull/2910
- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912
- feat: expose table uri by @rpgreen in https://github.com/lancedb/lancedb/pull/2922
- feat: update lance dependency to v1.0.3 by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2932

## 🐛 Bug Fixes

- fix(python): require explicit region for S3 buckets with dots by @Angryrou in https://github.com/lancedb/lancedb/pull/2892
- fix: support `exist_ok` in `RemoteDBConnection.create_table` by @cmccabe in https://github.com/lancedb/lancedb/pull/2901

## 📚 Documentation

- docs: address styling and aesthetics issues with banner and links by @prrao87 in https://github.com/lancedb/lancedb/pull/2878

## 🔧 Build and CI

- ci: fix codex version bump title and summary by @jackye1995 in https://github.com/lancedb/lancedb/pull/2931


### Release: lancedb [Python LanceDB v0.27.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.27.0)
## 🛠 Breaking Changes

- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912

## 🎉 New Features

- feat: voyage-multimodal-3.5 by @fzowl in https://github.com/lancedb/lancedb/pull/2887
- feat: support remote ivf rq by @LuQQiu in https://github.com/lancedb/lancedb/pull/2863
- feat: parallelize embedding computations by @ex172000 in https://github.com/lancedb/lancedb/pull/2896
- feat: enable huggingface feature by default by @Xuanwo in https://github.com/lancedb/lancedb/pull/2910
- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912
- feat: expose table uri by @rpgreen in https://github.com/lancedb/lancedb/pull/2922
- feat: update lance dependency to v1.0.3 by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2932

## 🐛 Bug Fixes

- fix(python): require explicit region for S3 buckets with dots by @Angryrou in https://github.com/lancedb/lancedb/pull/2892
- fix: support `exist_ok` in `RemoteDBConnection.create_table` by @cmccabe in https://github.com/lancedb/lancedb/pull/2901

## 📚 Documentation

- docs: address styling and aesthetics issues with banner and links by @prrao87 in https://github.com/lancedb/lancedb/pull/2878

## 🔧 Build and CI

- ci: fix codex version bump title and summary by @jackye1995 in https://github.com/lancedb/lancedb/pull/2931


### Release: lancedb [Node/Rust LanceDB v0.24.0-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.24.0-beta.0)
## 🛠 Breaking Changes

- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912

## 🎉 New Features

- feat: voyage-multimodal-3.5 by @fzowl in https://github.com/lancedb/lancedb/pull/2887
- feat: support remote ivf rq by @LuQQiu in https://github.com/lancedb/lancedb/pull/2863
- feat: parallelize embedding computations by @ex172000 in https://github.com/lancedb/lancedb/pull/2896
- feat: enable huggingface feature by default by @Xuanwo in https://github.com/lancedb/lancedb/pull/2910
- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912
- feat: expose table uri by @rpgreen in https://github.com/lancedb/lancedb/pull/2922

## 🐛 Bug Fixes

- fix(python): require explicit region for S3 buckets with dots by @Angryrou in https://github.com/lancedb/lancedb/pull/2892
- fix: support `exist_ok` in `RemoteDBConnection.create_table` by @cmccabe in https://github.com/lancedb/lancedb/pull/2901

## 📚 Documentation

- docs: address styling and aesthetics issues with banner and links by @prrao87 in https://github.com/lancedb/lancedb/pull/2878


### Release: lancedb [Python LanceDB v0.27.0-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.27.0-beta.0)
## 🛠 Breaking Changes

- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912

## 🎉 New Features

- feat: voyage-multimodal-3.5 by @fzowl in https://github.com/lancedb/lancedb/pull/2887
- feat: support remote ivf rq by @LuQQiu in https://github.com/lancedb/lancedb/pull/2863
- feat: parallelize embedding computations by @ex172000 in https://github.com/lancedb/lancedb/pull/2896
- feat: enable huggingface feature by default by @Xuanwo in https://github.com/lancedb/lancedb/pull/2910
- feat(rust)!: remove default features by @wjones127 in https://github.com/lancedb/lancedb/pull/2912
- feat: expose table uri by @rpgreen in https://github.com/lancedb/lancedb/pull/2922

## 🐛 Bug Fixes

- fix(python): require explicit region for S3 buckets with dots by @Angryrou in https://github.com/lancedb/lancedb/pull/2892
- fix: support `exist_ok` in `RemoteDBConnection.create_table` by @cmccabe in https://github.com/lancedb/lancedb/pull/2901

## 📚 Documentation

- docs: address styling and aesthetics issues with banner and links by @prrao87 in https://github.com/lancedb/lancedb/pull/2878


### Release: lancedb [Node/Rust LanceDB v0.23.1](https://github.com/lancedb/lancedb/releases/tag/v0.23.1)
## 🐛 Bug Fixes

- fix: use post for describe_namespace and allow access to underlying client by @jackye1995 in https://github.com/lancedb/lancedb/pull/2871
- fix: pass namespace storage options provider into native table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2873
- fix: add to_lance() and to_polars() stub methods for type-checkers by @prrao87 in https://github.com/lancedb/lancedb/pull/2876

## 📚 Documentation

- docs: remove incorrect "LanceDb Cloud only" from table_names params by @jmhsieh in https://github.com/lancedb/lancedb/pull/2893


### Release: lancedb [Python LanceDB v0.26.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.26.1)
## 🐛 Bug Fixes

- fix: use post for describe_namespace and allow access to underlying client by @jackye1995 in https://github.com/lancedb/lancedb/pull/2871
- fix: pass namespace storage options provider into native table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2873
- fix: add to_lance() and to_polars() stub methods for type-checkers by @prrao87 in https://github.com/lancedb/lancedb/pull/2876

## 📚 Documentation

- docs: remove incorrect "LanceDb Cloud only" from table_names params by @jmhsieh in https://github.com/lancedb/lancedb/pull/2893


## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers?tab=readme-ov-file#datafusion-table-providers), 3 releases: ['v0.9.3', 'v0.9.2', 'v0.9.1']
### Release: datafusion-table-providers [v0.9.3](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.3)
## What's Changed
* Bump bb8 from 0.9.0 to 0.9.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/514
* Bump bytes from 1.10.1 to 1.11.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/515
* Bump arrow-schema from 57.0.0 to 57.2.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/524
* Bump insta from 1.43.2 to 1.46.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/523
* Update the README file to include a development section. by @hozan23 in https://github.com/datafusion-contrib/datafusion-table-providers/pull/526
* Prevent invalid INSERT statements with empty batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/528


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.2...v0.9.3
### Release: datafusion-table-providers [v0.9.2](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.2)
## What's Changed
* Add write support for Decimal32 and Decimal64 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/519


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.1...v0.9.2
### Release: datafusion-table-providers [v0.9.1](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.1)
## What's Changed
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/505
* Prevent `InsertBuilder` from taking ownership of record batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/518


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.0...v0.9.1
## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers), 3 releases: ['v0.9.3', 'v0.9.2', 'v0.9.1']
### Release: datafusion-table-providers [v0.9.3](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.3)
## What's Changed
* Bump bb8 from 0.9.0 to 0.9.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/514
* Bump bytes from 1.10.1 to 1.11.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/515
* Bump arrow-schema from 57.0.0 to 57.2.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/524
* Bump insta from 1.43.2 to 1.46.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/523
* Update the README file to include a development section. by @hozan23 in https://github.com/datafusion-contrib/datafusion-table-providers/pull/526
* Prevent invalid INSERT statements with empty batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/528


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.2...v0.9.3
### Release: datafusion-table-providers [v0.9.2](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.2)
## What's Changed
* Add write support for Decimal32 and Decimal64 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/519


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.1...v0.9.2
### Release: datafusion-table-providers [v0.9.1](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.1)
## What's Changed
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/505
* Prevent `InsertBuilder` from taking ownership of record batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/518


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.0...v0.9.1
## Project: [unionai-oss/pandera](https://pandera.readthedocs.io/en/stable/index.html), 2 releases: ['v0.28.1: Fix regressions in Check behavior', 'Release 0.28.0: Add support for Pyspark 4']
### Release: pandera [v0.28.1: Fix regressions in Check behavior](https://github.com/unionai-oss/pandera/releases/tag/v0.28.1)
## What's Changed
* fix bugs in Check interface and Field by @cosmicBboy in https://github.com/unionai-oss/pandera/pull/2203


**Full Changelog**: https://github.com/unionai-oss/pandera/compare/v0.28.0...v0.28.1
### Release: pandera [Release 0.28.0: Add support for Pyspark 4](https://github.com/unionai-oss/pandera/releases/tag/v0.28.0)
## ⭐️ Highlight

Pandera now supports Pyspark 4 🚀

## What's Changed
* refactor(pyspark): restructure pyspark components by @ELC in https://github.com/unionai-oss/pandera/pull/2007
* add support for pyspark 4 by @cosmicBboy in https://github.com/unionai-oss/pandera/pull/2193
* Decouple import dependencies for io serialization formats by @cosmicBboy in https://github.com/unionai-oss/pandera/pull/2195
* Use `get_annotations` instead of direct `__annotations__` access by @amerberg in https://github.com/unionai-oss/pandera/pull/2196
* Re-implement improvements to str_length check by @cosmicBboy in https://github.com/unionai-oss/pandera/pull/2198
* Support the `Decimal` data type in the Ibis engine by @deepyaman in https://github.com/unionai-oss/pandera/pull/2194
* Update .git-blame-ignore-revs to add Ruff refactor by @deepyaman in https://github.com/unionai-oss/pandera/pull/2199
* Avoid full materialization of levels in failing MultiIndex validations by @amerberg in https://github.com/unionai-oss/pandera/pull/2187
* schema descriptor should raise AttributeError if build_schema_ is not implemented by @amerberg in https://github.com/unionai-oss/pandera/pull/2197

## New Contributors
* @ELC made their first contribution in https://github.com/unionai-oss/pandera/pull/2007

**Full Changelog**: https://github.com/unionai-oss/pandera/compare/v0.27.1...v0.28.0
