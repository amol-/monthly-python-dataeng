# Complete List of Projects
 * Project: posit-dev/py-shiny has 1 releases
 * Project: substrait-io/substrait-python has 1 releases
 * Project: narwhals-dev/narwhals has 4 releases
 * Project: pola-rs/polars has 6 releases
 * Project: pandas-dev/pandas has 1 releases
 * Project: holoviz/panel has 2 releases
 * Project: cython/cython has 1 releases
 * Project: plotly/dash has 3 releases
 * Project: dask/dask has 2 releases
 * Project: rapidsai/cudf has 1 releases
 * Project: lancedb/lance has 10 releases
 * Project: lancedb/lancedb has 16 releases
 * Project: datafusion-contrib/datafusion-table-providers has 2 releases
 * Project: duckdb/duckdb has 1 releases
 * Project: trinodb/trino has 1 releases
 * Project: datafusion-contrib/datafusion-table-providers has 2 releases
 * Project: https://spark.apache.org/news/index.html has 4 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 4 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 4 articles
### Release: [Preview release of Spark 4.1.0](https://spark.apache.org/news/spark-4-1-0-preview2-released.html)

### Release: [Spark 3.5.7 released](https://spark.apache.org/news/spark-3-5-7-released.html)

### Release: [Spark 4.0.1 released](https://spark.apache.org/news/spark-4-0-1-released.html)

### Release: [Preview release of Spark 4.1.0](https://spark.apache.org/news/spark-4-1-0-preview1-released.html)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 4 articles
### Release: [Apache DataFusion 50.0.0 Released](https://datafusion.apache.org/blog/2025/09/29/datafusion-50.0.0)

### Release: [Implementing User Defined Types and Custom Metadata in DataFusion](https://datafusion.apache.org/blog/2025/09/21/custom-types-using-metadata)

### Release: [Apache DataFusion Comet 0.10.0 Release](https://datafusion.apache.org/blog/2025/09/16/datafusion-comet-0.10.0)

### Release: [Dynamic Filters: Passing Information Between Operators During Execution for 25x Faster Queries](https://datafusion.apache.org/blog/2025/09/10/dynamic-filters)

## Project: [posit-dev/py-shiny](https://shiny.posit.co/py/), 1 releases: ['shiny 1.5.0']
### Release: py-shiny [shiny 1.5.0](https://github.com/posit-dev/py-shiny/releases/tag/v1.5.0)
### New features

* Added AI-powered test generator for Shiny applications. Use `shiny add test` to automatically generate comprehensive Playwright tests for your apps using AI models from Anthropic or OpenAI. (#2041)

* `ui.sidebar()` is now interactively resizable. (#2020)

* `ui.sidebar()` gains a `fillable` argument to support vertical fill behavior in sidebars. (#2077)

* Added `ui.insert_nav_panel()`, `ui.remove_nav_panel()`, and `ui.update_nav_panel()` to support dynamic navigation. (#90)

* `navset_card_*()` now gains a `full_screen` option. (#1451)

* `ui.update_*()` functions now accept `ui.TagChild` (i.e., HTML) as input to the `label` and `icon` arguments. (#2020)

* The `.output_*()` methods of the `ClientData` class (e.g., `session.clientdata.output_height()`) can now be called without an `id` when called inside a `@render` function. (#1978)

* `playwright.controller.InputActionButton` gains a `expect_icon()` method. As a result, the already existing `expect_label()` no longer includes the icon. (#2020)

### Breaking changes

* The `ui.Chat` and `ui.MarkdownStream` components are now imported from the new `shinychat` library. Future versions of `shinychat` will likely deprecate and remove some features from `Chat`. If you still want to use those features with the latest Shiny, we suggest pinning `shinychat` to it's initial release (v0.1.0). (#2051)

* `express.ui.insert_accordion_panel()`'s function signature has changed to be more ergonomic. Now you can pass the `panel_title` and `panel_contents` directly instead of `ui.hold()`ing the `ui.accordion_panel()` context manager. (#2042)

### Improvements

* Improved the styling and readability of markdown tables rendered by `ui.Chat()` and `ui.MarkdownStream()`. (#1973)

* `input_date()`, `input_date_range()`, `update_date()`, and `update_date_range()` now support `""` for values, mins, and maxes. In this case, no date will be specified on the client. (#1713) (#1689)

* Restricted the allowable types of the `choices` parameter of `input_select()`, `input_selectize()`, `update_select()`, and `update_selectize()` to actual set of allowable types (previously, the type was suggesting HTML-like values were supported). (#2048)

* Added module support for `session.clientdata` methods. This allows you to access client data values in Shiny modules without needing to namespace the keys explicitly. (#1978)

* Added `timeout_secs` parameter to `create_app_fixture` to allow testing apps with longer startup times. (#2033)

* Add support for selecting menu items in `Navset` controllers to improve dropdown navigation test coverage. (#2066)

* Python 3.13 is now offically supported and tested. (#1711)

### Bug fixes

* Fixed issue where apps run in Workbench were unexpectedly crashing. Apps running in Workbench will now have `ws_per_message_deflate=False` enforced. (#2005)

* `include_js()` and `include_css()` now work as expected in multi-user settings and also when multiple files from the same directory are included. (#2061, #2069)

* Fixed numerous issues related to programmatically updating selectize options. (#2053)
   * `update_selectize(options=...)` no longer gets ignored when `server=False` (the default).
   * `update_selectize(options=...)` now works as expected in a module.

* Fixed an issue with `update_selectize(server=True)` not properly displaying labels with HTML reserved characters like "&" (#1330)

* Fixed an issue with `ui.Chat()` sometimes wanting to scroll a parent element. (#1996)

* Fix several issues with bookmarking error reporting and documentation. (#2076, #1984, #1983)

* `input_date()` and `input_date_range()` once again use the client's (not the server) current date as the default `value`. (#2060)

* Fixed false positive warning in `layout_columns()` about number of widths vs elements. (#1704)

* Fixed `set()` method of the `InputSelectize` test controller so it clears existing selections before applying new values. (#2024)

### Deprecations

* `ui.update_navs()` is deprecated in favor of `ui.update_navset()`. (#2047)

* `ui.panel_well()` is deprecated in favor of `ui.card()`. (#2038)

* `selectize`, `remove_button`, and `options` parameters of `ui.input_select()` have been deprecated; use `ui.input_selectize()` instead. (Thanks, @ErdaradunGaztea!) (#1947)

## Project: [substrait-io/substrait-python](https://substrait.io/), 1 releases: ['v0.24.2']
### Release: substrait-python [v0.24.2](https://github.com/substrait-io/substrait-python/releases/tag/v0.24.2)
## What's Changed
* chore(deps): bump actions/download-artifact from 4 to 5 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/88
* chore(deps): bump actions/checkout from 4 to 5 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/89
* chore(deps): bump actions/setup-python from 5 to 6 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/92
* chore(deps): bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/93
* chore(deps): bump actions/setup-node from 4 to 5 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/94
* feat: pretty-printer for plan and expr by @Clonkk in https://github.com/substrait-io/substrait-python/pull/90

## New Contributors
* @Clonkk made their first contribution in https://github.com/substrait-io/substrait-python/pull/90

**Full Changelog**: https://github.com/substrait-io/substrait-python/compare/v0.24.1...v0.24.2
## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 4 releases: ['Narwhals v2.6.0', 'Narwhals v2.5.0', 'Narwhals v2.4.0', 'Narwhals v2.3.0']
### Release: narwhals [Narwhals v2.6.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.6.0)
## Changes

## ✨ Enhancements

- enh: support `skew` with `over` (#3161)
- fix: Align division by zero behavior across all backends (#2761)
- enh: support `n_unique` with `over` across all backends (#3159)
- enh: support non-elementwise (but length-preserving) keys in group-by (#3157)

## 🐞 Bug fixes

- fix: preserve nulls in cumulative functions (#3156)

## 🛠️ Other improvements

- chore(typing): pyright ignore `pl.UInt128` (#3144)
- ci: ban click 8.3.0 (#3146)
- chore: Support `@requires.backend_version` in namespaces (#3127)
- ci: Temporary pin duckdb for ibis (#3136)
- test: fix `version_test` failing on old `venv` (#3134)
- test(typing): fix `pickle_test` using `Sequence` (#3135)
- refactor: Simplify `maybe_convert_dtypes` (#3141)
- chore: Add `CompliantFrame._with_native` (#3140)
- refactor(typing): Remove now-unused `isinstance_or_issubclass` overloads (#3139)
- chore: Upgrade ruff to `v0.13.0` and fix related issues in `tests/` (#3126)
- tests: more `modern polars` tests (#3087)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @dangotbanned and @skritsotalakis

### Release: narwhals [Narwhals v2.5.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.5.0)
## Changes

## ✨ Enhancements

- feat: Allow `os.PathLike[str]` in `{read,scan}_*` functions (#3112)
- enh: Support `keep={'first', 'last'}` in `{DataFrame,LazyFrame}.unique` (#3118)

## 🐞 Bug fixes

- fix: Handle duckdb breaking change in `arrow` (#3119)

## 📖 Documentation

- docs: Add python version support to backcompat (#3115)
- docs: Nan non compliance (#3093)

## 🛠️ Other improvements

- test: add extra test for dataframe.rename (#3123)
- chore(typing): Add `CompliantNamespace.from_native` (#3114)

Thank you to all our contributors for making this release possible!
@MarcoGorelli, @dangotbanned and @ym-pett

### Release: narwhals [Narwhals v2.4.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.4.0)
## Changes

## ✨ Enhancements

- enh: support diagonal concatenation for duckdb (https://github.com/narwhals-dev/narwhals/pull/3108) 

## 🐞 Bug fixes

- fix: allow for fill_null with aggregate expression (https://github.com/narwhals-dev/narwhals/pull/3105)

## 🛠️ Other improvements

- tests: Add backcompat for time_unit (https://github.com/narwhals-dev/narwhals/pull/3098)
- Several internal / maintenance changes

Thank you to all our contributors for making this release possible!
### Release: narwhals [Narwhals v2.3.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.3.0)
## Changes

## ✨ Enhancements

- feat: Raise on mismatched `*Frame` joins (#3055)
- feat: Add `Schema.from_{native,<backend>}` (#2957)
- feat: add multivalue replacement in `.str.replace[_all]` (#2886)
- feat: Allow spark-like backends in `.lazy(backend=...)` (#3032)

## 🐞 Bug fixes

- fix: duckdb `Lazyframe.unique` was raising when column name was "group" (#3070)

## 📖 Documentation

- docs: update image to include duck (#3049)
- docs: reorder "narwhals and sql" page (#3047)

## 🛠️ Other improvements

- refactor: Organizing `Compliant*` APIs (#3045)
- refactor: Add `CompliantFrame` protocol (#3056)
- chore: use `with_callable` in `fill_nan` (#3052)
- chore: remove (internal) `ExprKind.NARY` (#3050)
- chore: fixup duckdb nightly (#3051)
- refactor: Allow `None` in `object_native_to_narwhals_dtype` (#3038)
- refactor(typing): Remove `CompliantDataFrame.collect` (#3041)
- chore(typing): Ignore inferred type in `dask_expr.Series.mask` (#3039)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @camriddell and @dangotbanned

## Project: [pola-rs/polars](https://docs.pola.rs/), 6 releases: ['Python Polars 1.34.0-beta.4', 'Python Polars 1.34.0-beta.3', 'Python Polars 1.34.0-beta.1', 'Rust Polars 0.51.0', 'Python Polars 1.33.1', 'Python Polars 1.33.0']
### Release: polars [Python Polars 1.34.0-beta.4](https://github.com/pola-rs/polars/releases/tag/py-1.34.0-beta.4)
## 🏆 Highlights

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)

## 🚀 Performance improvements

- Skip files in `scan_iceberg` with filter based on metadata statistics (#24547)
- Push row\_index predicate for all scan types (#24537)
- Perform integer in-filtering for Parquet inequality predicates (#24525)
- Stop caching Parquet metadata after 8 files (#24513)
- Native streaming `.mode()` expression (#24459)

## ✨ Enhancements

- Support scanning from `file:/path` URIs (#24603)
- Log which file the schema was sourced from, and which file caused an extra column error (#24621)
- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)
- Add support to display lazy query plan in marimo notebooks without needing to install matplotlib or mermaid (#24540)
- Add unstable `hidden_file_prefix` parameter to `scan_parquet` (#24507)
- Use fixed-scale Decimals (#24542)
- Add support for unsigned 128-bit integers (#24346)
- Add unstable `pl.Config.set_default_credential_provider` (#24434)
- Roundtrip `BinaryOffset` type through Parquet (#24344)
- Add opt-in unstable functionality to load interval types as `Struct` (#24320)
- Support reading parquet metadata from cloud storage (#24443)
- Add user guide section on AWS role assumption (#24421)
- Support `unique` / `n_unique` / `arg_unique` for `array` columns (#24406)

## 🐞 Bug fixes

- Widen `from_dicts` to `Iterable[Mapping[str, Any]]` (#24584)
- Fix `unsupported arrow type Dictionary` error in `scan_iceberg()` (#24573)
- Raise Exception instead of panic when unnest on non-struct column (#24471)
- Include missing feature dependency from `polars-stream/diff` to `polars-plan/abs` (#24613)
- Newline escaping in streaming show\_graph (#24612)
- Do not allow inferring (`-1`) the dimension on any `Expr.reshape` dimension except the first (#24591)
- Sink batches early stop on in-memory engine (#24585)
- More precisely model expression ordering requirements (#24437)
- Panic in zero-weight rolling mean/var (#24596)
- Decimal \<-> literal arithmetic supertype rules (#24594)
- Match various aggregation return types in the streaming engine with the in-memory engine (#24501)
- Validate list type for list expressions in planner (#24589)
- Fix `scan_iceberg()` storage options not taking effect (#24574)
- Have `log()` prioritize the leftmost dtype for its output dtype (#24581)
- CSV pl.len() was incorrect (#24587)
- Add support for float inputs for duration types (#24529)
- Roundtrip empty string through hive partitioning (#24546)
- Fix potential OOB writes in unaligned IPC read (#24550)
- Fix regression error when scanning AWS presigned URL (#24530)
- Make `PlPath::join` for cloud paths replace on absolute paths (#24514)
- Correct dtype for cum\_agg in streaming engine (#24510)
- Restore support for np.datetime64() in pl.lit() (#24527)
- Ignore Iceberg list element ID if missing (#24479)
- Fix panic on streaming full join with coalesce (#23409)
- Fix `AggState` on `all_literal` in `BinaryExpr` (#24461)
- Show IR sort options in `explain` (#24465)
- Benchmark CI import (#24463)
- Fix schema on `ApplyExpr` with single row `literal` in agg context (#24422)
- Fix planner schema for dividing `pl.Float32` by int (#24432)
- Fix panic scanning from AWS legacy global endpoint URL (#24450)
- Fix `iterable_to_pydf(..., infer_schema_length=None)` to scan all data (#23405)
- Do not propagate struct of nulls with null (#24420)
- Be stricter with invalid NDJSON input when `ignore_errors=False` (#24404)
- Implement `approx_n_unique` for temporal dtypes and Null (#24417)

## 📖 Documentation

- Fix syntax error in data-types-and-structures.md (#24606)
- Rename `avg_birthday` -> `avg_age` in examples aggregation (#23726)
- Update Polars Cloud user guide (#24366)
- Fix typo in `set_expr_depth_warning` docstring (#24427)

## 📦 Build system

- Use cargo-run to call dsl-schema script (#24607)

## 🛠️ Other improvements

- Remove dist/ from release python workflow (#24639)
- Escape `sed` ampersand in release script (#24631)
- Remove PyOdide from release for now (#24630)
- Fix sed in-place in release script (#24628)
- Release script pyodide wheel (#24627)
- Release script pyodide wheel (#24626)
- Update release script for runtimes (#24610)
- Remove unused `UnknownKind::Ufunc` (#24614)
- Use cargo-run to call dsl-schema script (#24607)
- Cleanup and prepare `to_field` for element and struct field context (#24592)
- Resolve nightly clippy hints (#24593)
- Rename pl.dependencies to pl.\_dependencies (#24595)
- More release scripting (#24582)
- Again a minor fix for the setup script (#24580)
- Minor fix in release script (#24579)
- Correct release python beta version check (#24578)
- Python dependency failure (#24576)
- Always install yq (#24570)
- Deterministic import order for Python Polars package variants (#24531)
- Check Arrow FFI pointers with an assert (#24564)
- Add a couple of missing type definitions in python (#24561)
- Fix quickstart example in Polars Cloud user guide (#24554)
- Add implementations for loading min/max statistics for Iceberg (#24496)
- Update versions (#24508)
- Add additional unit tests for `pl.concat` (#24487)
- Refactor parametric tests for `as_struct` on aggstates (#24493)
- Use `PlanCallback` in `name.map_*` (#24484)
- Pin `xlsvwriter` to `3.2.5` or before (#24485)
- Add dataclass to hold resolved iceberg scan data (#24418)
- Fix iceberg test failure in CI (#24456)
- Move CompressionUtils to polars-utils (#24430)
- Update github template to dispatch to cloud client (#24416)

Thank you to all our contributors for making this release possible!
@Gusabary, @Kevin-Patyk, @Matt711, @MoizesCBF, @alonsosilvaallende, @borchero, @c-peters, @camriddell, @coastalwhite, @dangotbanned, @deanm0000, @dongchao-1, @dsprenkels, @itamarst, @jan-krueger, @joshuamarkovic, @juansolm, @kdn36, @nameexhaustion, @orlp, @r-brink, @ritchie46 and @stijnherfst

### Release: polars [Python Polars 1.34.0-beta.3](https://github.com/pola-rs/polars/releases/tag/py-1.34.0-beta.3)
## 🏆 Highlights

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)

## 🚀 Performance improvements

- Skip files in `scan_iceberg` with filter based on metadata statistics (#24547)
- Push row\_index predicate for all scan types (#24537)
- Perform integer in-filtering for Parquet inequality predicates (#24525)
- Stop caching Parquet metadata after 8 files (#24513)
- Native streaming `.mode()` expression (#24459)

## ✨ Enhancements

- Support scanning from `file:/path` URIs (#24603)
- Log which file the schema was sourced from, and which file caused an extra column error (#24621)
- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)
- Add support to display lazy query plan in marimo notebooks without needing to install matplotlib or mermaid (#24540)
- Add unstable `hidden_file_prefix` parameter to `scan_parquet` (#24507)
- Use fixed-scale Decimals (#24542)
- Add support for unsigned 128-bit integers (#24346)
- Add unstable `pl.Config.set_default_credential_provider` (#24434)
- Roundtrip `BinaryOffset` type through Parquet (#24344)
- Add opt-in unstable functionality to load interval types as `Struct` (#24320)
- Support reading parquet metadata from cloud storage (#24443)
- Add user guide section on AWS role assumption (#24421)
- Support `unique` / `n_unique` / `arg_unique` for `array` columns (#24406)

## 🐞 Bug fixes

- Widen `from_dicts` to `Iterable[Mapping[str, Any]]` (#24584)
- Fix `unsupported arrow type Dictionary` error in `scan_iceberg()` (#24573)
- Raise Exception instead of panic when unnest on non-struct column (#24471)
- Include missing feature dependency from `polars-stream/diff` to `polars-plan/abs` (#24613)
- Newline escaping in streaming show\_graph (#24612)
- Do not allow inferring (`-1`) the dimension on any `Expr.reshape` dimension except the first (#24591)
- Sink batches early stop on in-memory engine (#24585)
- More precisely model expression ordering requirements (#24437)
- Panic in zero-weight rolling mean/var (#24596)
- Decimal \<-> literal arithmetic supertype rules (#24594)
- Match various aggregation return types in the streaming engine with the in-memory engine (#24501)
- Validate list type for list expressions in planner (#24589)
- Fix `scan_iceberg()` storage options not taking effect (#24574)
- Have `log()` prioritize the leftmost dtype for its output dtype (#24581)
- CSV pl.len() was incorrect (#24587)
- Add support for float inputs for duration types (#24529)
- Roundtrip empty string through hive partitioning (#24546)
- Fix potential OOB writes in unaligned IPC read (#24550)
- Fix regression error when scanning AWS presigned URL (#24530)
- Make `PlPath::join` for cloud paths replace on absolute paths (#24514)
- Correct dtype for cum\_agg in streaming engine (#24510)
- Restore support for np.datetime64() in pl.lit() (#24527)
- Ignore Iceberg list element ID if missing (#24479)
- Fix panic on streaming full join with coalesce (#23409)
- Fix `AggState` on `all_literal` in `BinaryExpr` (#24461)
- Show IR sort options in `explain` (#24465)
- Benchmark CI import (#24463)
- Fix schema on `ApplyExpr` with single row `literal` in agg context (#24422)
- Fix planner schema for dividing `pl.Float32` by int (#24432)
- Fix panic scanning from AWS legacy global endpoint URL (#24450)
- Fix `iterable_to_pydf(..., infer_schema_length=None)` to scan all data (#23405)
- Do not propagate struct of nulls with null (#24420)
- Be stricter with invalid NDJSON input when `ignore_errors=False` (#24404)
- Implement `approx_n_unique` for temporal dtypes and Null (#24417)

## 📖 Documentation

- Fix syntax error in data-types-and-structures.md (#24606)
- Rename `avg_birthday` -> `avg_age` in examples aggregation (#23726)
- Update Polars Cloud user guide (#24366)
- Fix typo in `set_expr_depth_warning` docstring (#24427)

## 📦 Build system

- Use cargo-run to call dsl-schema script (#24607)

## 🛠️ Other improvements

- Remove dist/ from release python workflow (#24639)
- Escape `sed` ampersand in release script (#24631)
- Remove PyOdide from release for now (#24630)
- Fix sed in-place in release script (#24628)
- Release script pyodide wheel (#24627)
- Release script pyodide wheel (#24626)
- Update release script for runtimes (#24610)
- Remove unused `UnknownKind::Ufunc` (#24614)
- Use cargo-run to call dsl-schema script (#24607)
- Cleanup and prepare `to_field` for element and struct field context (#24592)
- Resolve nightly clippy hints (#24593)
- Rename pl.dependencies to pl.\_dependencies (#24595)
- More release scripting (#24582)
- Again a minor fix for the setup script (#24580)
- Minor fix in release script (#24579)
- Correct release python beta version check (#24578)
- Python dependency failure (#24576)
- Always install yq (#24570)
- Deterministic import order for Python Polars package variants (#24531)
- Check Arrow FFI pointers with an assert (#24564)
- Add a couple of missing type definitions in python (#24561)
- Fix quickstart example in Polars Cloud user guide (#24554)
- Add implementations for loading min/max statistics for Iceberg (#24496)
- Update versions (#24508)
- Add additional unit tests for `pl.concat` (#24487)
- Refactor parametric tests for `as_struct` on aggstates (#24493)
- Use `PlanCallback` in `name.map_*` (#24484)
- Pin `xlsvwriter` to `3.2.5` or before (#24485)
- Add dataclass to hold resolved iceberg scan data (#24418)
- Fix iceberg test failure in CI (#24456)
- Move CompressionUtils to polars-utils (#24430)
- Update github template to dispatch to cloud client (#24416)

Thank you to all our contributors for making this release possible!
@Gusabary, @Kevin-Patyk, @Matt711, @MoizesCBF, @alonsosilvaallende, @borchero, @c-peters, @camriddell, @coastalwhite, @dangotbanned, @deanm0000, @dongchao-1, @dsprenkels, @itamarst, @jan-krueger, @joshuamarkovic, @juansolm, @kdn36, @nameexhaustion, @orlp, @r-brink, @ritchie46 and @stijnherfst

### Release: polars [Python Polars 1.34.0-beta.1](https://github.com/pola-rs/polars/releases/tag/py-1.34.0-beta.1)
## 🏆 Highlights

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)

## 🚀 Performance improvements

- Skip files in `scan_iceberg` with filter based on metadata statistics (#24547)
- Push row\_index predicate for all scan types (#24537)
- Perform integer in-filtering for Parquet inequality predicates (#24525)
- Stop caching Parquet metadata after 8 files (#24513)
- Native streaming `.mode()` expression (#24459)

## ✨ Enhancements

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)
- Add support to display lazy query plan in marimo notebooks without needing to install matplotlib or mermaid (#24540)
- Add unstable `hidden_file_prefix` parameter to `scan_parquet` (#24507)
- Use fixed-scale Decimals (#24542)
- Add support for unsigned 128-bit integers (#24346)
- Add unstable `pl.Config.set_default_credential_provider` (#24434)
- Roundtrip `BinaryOffset` type through Parquet (#24344)
- Add opt-in unstable functionality to load interval types as `Struct` (#24320)
- Support reading parquet metadata from cloud storage (#24443)
- Add user guide section on AWS role assumption (#24421)
- Support `unique` / `n_unique` / `arg_unique` for `array` columns (#24406)

## 🐞 Bug fixes

- Add support for float inputs for duration types (#24529)
- Roundtrip empty string through hive partitioning (#24546)
- Fix potential OOB writes in unaligned IPC read (#24550)
- Fix regression error when scanning AWS presigned URL (#24530)
- Make `PlPath::join` for cloud paths replace on absolute paths (#24514)
- Correct dtype for cum\_agg in streaming engine (#24510)
- Restore support for np.datetime64() in pl.lit() (#24527)
- Ignore Iceberg list element ID if missing (#24479)
- Fix panic on streaming full join with coalesce (#23409)
- Fix `AggState` on `all_literal` in `BinaryExpr` (#24461)
- Show IR sort options in `explain` (#24465)
- Benchmark CI import (#24463)
- Fix schema on `ApplyExpr` with single row `literal` in agg context (#24422)
- Fix planner schema for dividing `pl.Float32` by int (#24432)
- Fix panic scanning from AWS legacy global endpoint URL (#24450)
- Fix `iterable_to_pydf(..., infer_schema_length=None)` to scan all data (#23405)
- Do not propagate struct of nulls with null (#24420)
- Be stricter with invalid NDJSON input when `ignore_errors=False` (#24404)
- Implement `approx_n_unique` for temporal dtypes and Null (#24417)

## 📖 Documentation

- Rename `avg_birthday` -> `avg_age` in examples aggregation (#23726)
- Update Polars Cloud user guide (#24366)
- Fix typo in `set_expr_depth_warning` docstring (#24427)

## 🛠️ Other improvements

- More release scripting (#24582)
- Again a minor fix for the setup script (#24580)
- Minor fix in release script (#24579)
- Correct release python beta version check (#24578)
- Python dependency failure (#24576)
- Always install yq (#24570)
- Deterministic import order for Python Polars package variants (#24531)
- Check Arrow FFI pointers with an assert (#24564)
- Add a couple of missing type definitions in python (#24561)
- Fix quickstart example in Polars Cloud user guide (#24554)
- Add implementations for loading min/max statistics for Iceberg (#24496)
- Update versions (#24508)
- Add additional unit tests for `pl.concat` (#24487)
- Refactor parametric tests for `as_struct` on aggstates (#24493)
- Use `PlanCallback` in `name.map_*` (#24484)
- Pin `xlsvwriter` to `3.2.5` or before (#24485)
- Add dataclass to hold resolved iceberg scan data (#24418)
- Fix iceberg test failure in CI (#24456)
- Move CompressionUtils to polars-utils (#24430)
- Update github template to dispatch to cloud client (#24416)

Thank you to all our contributors for making this release possible!
@Gusabary, @Kevin-Patyk, @Matt711, @alonsosilvaallende, @borchero, @c-peters, @camriddell, @coastalwhite, @dongchao-1, @dsprenkels, @itamarst, @jan-krueger, @joshuamarkovic, @juansolm, @kdn36, @nameexhaustion, @orlp, @r-brink, @ritchie46 and @stijnherfst

### Release: polars [Rust Polars 0.51.0](https://github.com/pola-rs/polars/releases/tag/rs-0.51.0)
## 💥 Breaking changes

- Remove, deprecate or change eager `Expr`s to be lazy compatible (#24027)

## 🚀 Performance improvements

- Use specialized decoding for all predicates for Parquet dictionary encoding (#24403)
- Allocate only for read items when reading Parquet with predicate (#24401)
- Don't aggregate groups for strict cast if original len (#24381)
- Allocate only for read items when reading Parquet with predicate (#24324)
- Native streaming `int_range` with `len` or `count` (#24280)
- Lower `arg_unique` natively to the streaming engine (#24279)
- Move unordering optimization to end (#24286)
- Do ordering simplification step after common sub-plan elimination (#24269)
- Always simplify order requirements in IR (#24192)
- Basic de-duplication of filter expressions (#24220)
- Cache the IR in `pipe_with_schema` (#24213)
- Lower `arg_where` natively to streaming engine (#24088)
- Lower Expr.shift to streaming engine (#24106)
- Lower order-preserving groupby to streaming engine (#24053)
- Lower .sort(maintain\_order=True).head() to streaming top\_k (#24014)
- Lower top-k to streaming engine (#23979)
- Allow order pass through Filters and relax to row-seperable instead of elementwise (#23969)

## ✨ Enhancements

- Roundtrip `BinaryOffset` type through Parquet (#24344)
- Add opt-in unstable functionality to load interval types as `Struct` (#24320)
- Add user guide section on AWS role assumption (#24421)
- Support `unique` / `n_unique` / `arg_unique` for `array` columns (#24406)
- Support S3 virtual-hosted–style URI (#24405)
- Remove explicit file create for local async writes (#24358)
- Support Partitioning sinks in cloud (#24399)
- User-friendly error message on empty path expansion (#24337)
- Add Polars security policy (#24314)
- Allow pl.Expr.log to take in an expression (#24226)
- Implement diff() in streaming engine (#24189)
- Enable Expr.diff(n) for negative n (#24200)
- Allow upcasting null-typed columns to nested column types in scans (#24185)
- Log pyarrow predicate conversion result in sensitive verbose logs (#24186)
- Add a deprecation warning for pl.Series.shift(Null) (#24114)
- Improve Debug formatting of DataType (#24056)
- Add `cum_*` as native streaming nodes (#23977)
- Add peak\_{min,max} support for booleans (#24068)
- Add `DataFrame.map_columns` for eager evaluation (#23821)
- Add native streaming for `peaks_{min,max}` (#24039)
- IR graph arrows, monospace font, box nodes (#24021)
- Add `DataTypeExpr.default_value` (#23973)
- Lower `rle` to a native streaming engine node (#23929)
- Add support for `Int128` to pyo3-polars (#23959)
- Lower `rle_id` to a native streaming node (#23894)
- Pass `endpoint_url` loaded from `CredentialProviderAWS` to `scan/write_delta` (#23812)
- Dispatch `scan_iceberg` to native by default (#23912)
- Lower `unique_counts` and `value_counts` to streaming engine (#23890)
- Implement `dt.days_in_month` function (#23119)
- Fix errors on native `scan_iceberg` (#23811)
- Reinterpret binary data to fixed size numerical array (#22840)
- Make `rolling_map` serializable (#23848)

## 🐞 Bug fixes

- Fix `AggState` on `all_literal` in `BinaryExpr` (#24461)
- Replace unsafe with collect (#24494)
- Show IR sort options in `explain` (#24465)
- Benchmark CI import (#24463)
- Fix schema on `ApplyExpr` with single row `literal` in agg context (#24422)
- Fix planner schema for dividing `pl.Float32` by int (#24432)
- Fix panic scanning from AWS legacy global endpoint URL (#24450)
- Emit proper tuple for Log in expression nodes (#24426)
- Do not propagate struct of nulls with null (#24420)
- Be stricter with invalid NDJSON input when `ignore_errors=False` (#24404)
- Implement `approx_n_unique` for temporal dtypes and Null (#24417)
- Correct `sink_ipc` overload for compression (#24398)
- Enable all integer dtypes for `by` parameter in `join_asof` (#24384)
- Fix Group-By + filter aggregation performs subsequent operations on all data instead of only filtered data (#24373)
- Fix incorrect output ordering for row-separable exprs (#24354)
- Fix `Series.__arrow_c_stream__` for Decimal and other logical types (#24120)
- Match output type to engine for `Struct` arithmetic (#23805)
- Make mmap use MAP\_PRIVATE rather than MAP\_SHARED (#24343)
- Fix cloud iceberg scan DATASET\_PROVIDER\_VTABLE error (#24338)
- Incorrect logic in negative streaming slice (#24326)
- Do not error on non-list `Sequence` for `columns` parameter in `read_excel` (#23967)
- Invalid conversion from non-bit numpy bools (#24312)
- Make `dt.epoch('s')` serializable (#24302)
- Make `Expr.rechunk` serializable (#24303)
- Schema mismatch for 'log' operation (#24300)
- Incorrect first/last aggregate in streaming engine (#24289)
- Fix group offsets in sliced groups (#24274)
- Panic in inexact date(time) conversion (#24268)
- The `index_of` feature should not depends on the `object` feature (#24256)
- Keep DSL cache after serialization and deserialization (#24265)
- Sanitize and warn about eval usage (#24262)
- Unique with keep="none" in new optimization pass (#24261)
- Correct size limits for Decimal cast (#24252)
- Unordered unions in check order observing pass (#24253)
- Fix dtype for `slice` on `Literal` in agg context (#24137)
- Fix incorrect `filter(lit(True))` when scanning hive (#24237)
- In-memory group\_by on 128-bit integers (#24242)
- Fix panic in `gather` inside groupby with invalid indices (#24182)
- Release the GIL in map\_groups (#24225)
- Remove extra explode in `LazyGroupBy.{head,tail}` (#24221)
- Fix panic in polars cloud CSV scan (#24197)
- Fix panic when loading categorical columns from IO plugin (#24205)
- Fix engine type for `concat_list` on AggScalar `implode` (#24160)
- Rolling\_mean handle centered weights with len(values) \< window\_size (#24158)
- Reading `is_in` predicate for Parquet plain strings (#24184)
- Make PyCategories pickleable (#24170)
- Remove unused unsound function `to_mutable_slice` (#24173)
- PyO3 extension types giving compat\_level errors (#24166)
- Allow non-elementwise by in top\_k (#24164)
- Fix `sort_by` for `group_by_dynamic` context (#24152)
- Input-independent length aggregations in streaming (#24153)
- Release GIL when iterating df in to\_arrow (#24151)
- Respect non-elementwise join\_where conditions (#24135)
- Resolve schema mismatch for div on Boolean (#24111)
- Keep name when doing empty group-aware aggregation (#24098)
- Implode instead of `reshape_list` (#24078)
- Rolling mean with weights incorrect when min\_samples \< window\_size (#23485)
- Allow `merge_sorted` for all types (#24077)
- Include datatypes in `row_encode` expression (#24074)
- Include UDF materialized type in serialization (#24073)
- Correct `.rolling()` output type for non-aggregations (#24072)
- Correct planner output schema for `join_asof` (#24071)
- Allow %B to work without specifying day (#24009)
- Correct output for `fold` and `reduce` (#24069)
- Expr.meta.output\_name for struct fields (#24064)
- Ensure upcast operations on `pl.Date` default to microsecond precision (#23981)
- Add peak\_{min,max} support for booleans (#24068)
- Planner output type for `mean` with strange input type (#24052)
- Remove, deprecate or change eager `Expr`s to be lazy compatible (#24027)
- Scan of multiple sources with `null` datatype (#24065)
- Categorical in nested data in row encoding (#24051)
- Missing length update in builder for pl.Array repetition (#24055)
- Race condition in global categories init (#24045)
- Revert "fix: Don't encode entire CategoricalMapping when going to Arrow (#24036)" (#24044)
- Error when using named functions (#24041)
- Don't encode entire CategoricalMapping when going to Arrow (#24036)
- Fix cast on arithmetic with `lit` (#23941)
- Incorrect slice-slice pushdown (#24032)
- Dedup common cache subplan in IR graph (#24028)
- Allow join on Decimal in in-memory engine (#24026)
- Fix datatypes for `eval.list` in aggregation context (#23911)
- Allocator capsule fallback panic (#24022)
- Accept another zlib "magic header" file signature (#24013)
- Fix `truediv` dtypes so `cast` in `list.eval` is not dropped (#23936)
- Don't reuse cached `return_dtype` for expanded map expressions (#24010)
- Cache id is not a valid dot node id (#24005)
- Align `map_elements` with and without `return_dtype` (#24007)
- Fix column dtype lifetime for `csv_write` segfault on `Categorical` (#23986)
- Allow serializing `LazyGroupBy.map_groups` (#23964)
- Correct allocator name in `PyCapsule` (#23968)
- Mismatched types for `write` function for windows (#23915)
- Fix `unpivot` panic when `index=` column not found (#23958)
- Fix `assert_frame_equal` with `check_dtypes=False` for all-null series with different types (#23943)
- Return correct python package version (#23951)
- Categorical namespace functions fail on `Enum` columns (#23925)
- Properly set sumwise complete on filter for missing columns (#23877)
- Restore Arrow-FFI-based Python\<->Rust conversion in pyo3-polars (#23881)
- Group By with filters (#23917)
- Fix `read_csv` ignoring Decimal schema for header-only data (#23886)
- Ensure `collect()` native Iceberg always scans latest when no `snapshot_id` is given (#23907)
- Writing List(Array) columns to JSON without panic (#23875)
- Fill Iceberg missing fields with partition values if present in metadata (#23900)
- Create file for streaming sink even if unspawned (#23672)
- Update cloud testing environment (#23908)
- Parquet filtering on multiple RGs with literal predicate (#23903)
- Incorrect datatype passed to libc::write (#23904)
- Properly feature gate TZ\_AWARE\_RE usage (#23888)
- Improve identification of "non group-key" aggregates in SQL `GROUP BY` queries (#23191)
- Spawning tokio task outside reactor (#23884)
- Correctly raise DuplicateError on asof\_join with suffix="" (#23864)
- Fix errors on native `scan_iceberg` (#23811)
- Fix index out of bounds panic filtering parquet (#23850)
- Fix error on empty range requests (#23844)
- Fix handling of hive partitioning `hive_start_idx` parameter (#23843)

## 📖 Documentation

- Rename `avg_birthday` -> `avg_age` in examples aggregation (#23726)
- Update Polars Cloud user guide (#24366)
- Update to Polars Cloud user guide (#24187)
- Update distributed page (#24323)
- Add Polars security policy (#24314)
- Fix few typos (#24305)
- Add missing reference to `LazyFrame.pipe_with_schema()` on the website (#24285)
- Fix formatting of Series.value\_counts examples (#24245)
- Add `DataFrame.map_columns` to API (#24128)
- Update multiple pages in the Polars Cloud user guide (#23661)
- Improve StackOverflow links in contributing guide (#23895)
- Fix `pyo3` documentation page link (#23839)
- Document the pureness requirements of udfs (#23787)

## 📦 Build system

- Re-enable macos-x86-64 (#24266)
- Drop binary support for macos\_x86-64 (#24257)

## 🛠️ Other improvements

- Use `PlanCallback` in `name.map_*` (#24484)
- Replace unsafe with collect (#24494)
- Move dataset expansion to end and refactor not to use stack optimizer (#24457)
- Pin `xlsvwriter` to `3.2.5` or before (#24485)
- Add methods to `EnumUnitVec` and shorten name (#24415)
- Move CompressionUtils to polars-utils (#24430)
- Update github template to dispatch to cloud client (#24416)
- Bump c-api (#24412)
- Add a regression test for #7631 (#24363)
- Update cloud test `InteractiveQuery` to `DirectQuery` (#24287)
- Mark some tests as slow (#24327)
- Mark more tests as ready for cloud (#24315)
- Remove unnecessary stable\_features for AVX512 (#24321)
- Remove PDS-H code (#24301)
- Get ready for even more cloud tests (#24292)
- Add tests for slices with caches (#24288)
- Readd ordering tests (#24284)
- Expand BitRepr to u8/u16 and use in in\_memory group\_by (#24248)
- Fix Makefile venv path (#24251)
- Remove unnecessary parentheses (#24244)
- Remove some transmutes (#24246)
- Wrap Py\* data structures in polars-python in locks (#24209)
- Make non-nested shift{,\_and\_fill} ops generic (#24224)
- Remove unused `Wrap` (#24214)
- Propagate some python feature flags (#24201)
- Allow upcasting null-typed columns to nested column types in scans (#24185)
- Automatically label a few more types of PR (#24147)
- Update toolchain (#24156)
- InMemoryJoin should be coloured as InMemoryFallback (#24154)
- Fool-proof retrieve\_error\_msg (#24132)
- Add `order_sensitive` property for `AExpr` (#24116)
- Mark more tests as not possible on cloud (#24103)
- Turn `AggExpr::Count` from tuple to struct (#24096)
- Mark tests that may fail in cloud (#24067)
- Make CI perf failures more lenient (#24066)
- Fix hive partition string encoding in CI by upgrading `deltalake` (#24018)
- Avoid unreachable if dtype feature is not enabled (#24062)
- Make tests with sinks run on cloud again (#24048)
- Update pyo3-polars versions (#24031)
- Remove insert\_error\_function (#24023)
- Remove cache hits, clean up in-mem prefill (#24019)
- Use .venv instead of venv in pyo3-polars examples (#24024)
- Fix test failing mypy (#24017)
- Remove outdated comment (#23998)
- Add a `_plr.pyi` to remove `mypy` issues (#23970)
- Don't define CountStar as dyn OptimizationRule (#23976)
- Rename `atol` and `rtol` to `abs_tol` and `rel_tol` (#23961)
- Introduce `Row{Encode,Decode}` as FunctionExpr (#23933)
- Dispatch through `pl.map_batches` and `AnonymousColumnsUdf` (#23867)
- Ensure `clippy` and `rustfmt` run in CI when changing `pyo3-polars` (#23930)
- Split `column_selector.rs` (#23921)
- Fix pyo3-polars proc-macro re-exports (#23918)
- Make `GetBatchState` polling functions unsafe (#23795)
- Rewrite `evaluate_on_groups` for `.gather` / `.get` (#23700)
- Remove `Context` from logical layer (#23863)
- Add `proptest` strategy for Polars `DataType` schemas (#23854)
- Move Python C API to `python-polars` (#23876)
- Refactor directory structure of streaming multi-scan (#23865)
- Add subphase and query task spawning to StreamingExecState (#23725)
- Update Rust Polars versions (#23861)
- Make polars-parquet optional (#23860)
- Relax constraint on maximum Python version for `numba` (#23838)

Thank you to all our contributors for making this release possible!
@Gusabary, @JakubValtar, @Kevin-Patyk, @MarcoGorelli, @Matt711, @NeejWeej, @VictorAtIfInsurance, @agossard, @alexander-beedie, @aparna2198, @borchero, @c-peters, @camriddell, @cgevans, @cmdlineluser, @coastalwhite, @deanm0000, @dsprenkels, @eitsupi, @etiennebacher, @gab23r, @gfvioli, @henryharbeck, @iishutov, @itamarst, @jarondl, @jimmmmmmmmmmmy, @jjurm, @joshuamarkovic, @juansolm, @kdn36, @kuril, @math-hiyoko, @mcrumiller, @mpasa, @mrkn, @mroeschke, @nameexhaustion, @nesb1, @orlp, @pka, @pomo-mondreganto, @r-brink, @rawhuul, @ritchie46, @stijnherfst, @vdrn and @wence-

### Release: polars [Python Polars 1.33.1](https://github.com/pola-rs/polars/releases/tag/py-1.33.1)
## 🚀 Performance improvements

- Use specialized decoding for all predicates for Parquet dictionary encoding (#24403)
- Allocate only for read items when reading Parquet with predicate (#24401)
- Don't aggregate groups for strict cast if original len (#24381)
- Allocate only for read items when reading Parquet with predicate (#24324)

## ✨ Enhancements

- Support S3 virtual-hosted–style URI (#24405)
- Remove explicit file create for local async writes (#24358)
- Add PyCapsule `__arrow_c_schema__` interface to `pl.Schema` (#24365)
- Support Partitioning sinks in cloud (#24399)
- User-friendly error message on empty path expansion (#24337)
- Add unstable `pre_execution_query` parameter to `read_database_uri` (#23634)
- Add Polars security policy (#24314)

## 🐞 Bug fixes

- Correct `sink_ipc` overload for compression (#24398)
- Enable all integer dtypes for `by` parameter in `join_asof` (#24384)
- Fix Group-By + filter aggregation performs subsequent operations on all data instead of only filtered data (#24373)
- Wrap deprecated top-level imports in TYPE\_CHECKING (#24340)
- Fix incorrect output ordering for row-separable exprs (#24354)
- Fix `Series.__arrow_c_stream__` for Decimal and other logical types (#24120)
- Match output type to engine for `Struct` arithmetic (#23805)
- Make mmap use MAP\_PRIVATE rather than MAP\_SHARED (#24343)
- Fix cloud iceberg scan DATASET\_PROVIDER\_VTABLE error (#24338)
- Don't throw away type information for NumPy numeric values when using lit() (#24229)
- Incorrect logic in negative streaming slice (#24326)
- Ensure `read_database_uri` with ADBC works as expected with DuckDB URIs (#24097)
- Do not error on non-list `Sequence` for `columns` parameter in `read_excel` (#23967)

## 📖 Documentation

- Document newly added `is_pure` parameter for `register_io_source` (#24311)
- Create a module docstring for the public `polars` module (#24332)
- Update to Polars Cloud user guide (#24187)
- Update distributed page (#24323)
- Add a note and example about exporting unformatted `Excel` sheet data (#24145)
- Add detail about server-side cursor behaviour for SQLAlchemy in the "iter\_batches" parameter of `read_database` (#24094)
- Add Polars security policy (#24314)

## 🛠️ Other improvements

- Bump c-api (#24412)
- Add a regression test for #7631 (#24363)
- Update cloud test `InteractiveQuery` to `DirectQuery` (#24287)
- Mark some tests as slow (#24327)
- Mark more tests as ready for cloud (#24315)
- Add hint to update `PYPOLARS_VERSION` on version assert test (#24313)

Thank you to all our contributors for making this release possible!
@Kevin-Patyk, @VictorAtIfInsurance, @alexander-beedie, @coastalwhite, @dsprenkels, @itamarst, @kdn36, @kuril, @mcrumiller, @nameexhaustion, @nesb1, @orlp, @r-brink and @ritchie46

### Release: polars [Python Polars 1.33.0](https://github.com/pola-rs/polars/releases/tag/py-1.33.0)
## 💥 Breaking changes

- Remove, deprecate or change eager `Expr`s to be lazy compatible (#24027)

## 🚀 Performance improvements

- Native streaming `int_range` with `len` or `count` (#24280)
- Lower `arg_unique` natively to the streaming engine (#24279)
- Move unordering optimization to end (#24286)
- Do ordering simplification step after common sub-plan elimination (#24269)
- Always simplify order requirements in IR (#24192)
- Basic de-duplication of filter expressions (#24220)
- Cache the IR in `pipe_with_schema` (#24213)
- Lower `arg_where` natively to streaming engine (#24088)
- Lower Expr.shift to streaming engine (#24106)
- Lower order-preserving groupby to streaming engine (#24053)

## ✨ Enhancements

- Add CSE for custom io sources using pointer for hashing (#24297)
- Allow pl.Expr.log to take in an expression (#24226)
- Add caching to user credential providers (#23789)
- Expose `mkdir` parameter on `write_parquet` (#24239)
- Implement diff() in streaming engine (#24189)
- Enable Expr.diff(n) for negative n (#24200)
- Allow upcasting null-typed columns to nested column types in scans (#24185)
- Log pyarrow predicate conversion result in sensitive verbose logs (#24186)
- Drop PyArrow requirement for `write_database` with the ADBC engine (#24136)
- Add a deprecation warning for pl.Series.shift(Null) (#24114)
- Improve Debug formatting of DataType (#24056)
- Add `LazyFrame.pipe_with_schema` (#24075)
- Catch additional temporal attributes in `BytecodeParser` function analysis (#24076)
- Add `cum_*` as native streaming nodes (#23977)
- Add peak\_{min,max} support for booleans (#24068)
- Add `DataFrame.map_columns` for eager evaluation (#23821)

## 🐞 Bug fixes

- Invalid conversion from non-bit numpy bools (#24312)
- Make `dt.epoch('s')` serializable (#24302)
- Make `Expr.rechunk` serializable (#24303)
- Schema mismatch for 'log' operation (#24300)
- Incorrect first/last aggregate in streaming engine (#24289)
- Fix group offsets in sliced groups (#24274)
- Panic in inexact date(time) conversion (#24268)
- Keep DSL cache after serialization and deserialization (#24265)
- Sanitize and warn about eval usage (#24262)
- Correct incorrect default in `from_pandas` overload for `include_index` (#24258)
- Unique with keep="none" in new optimization pass (#24261)
- Correct size limits for Decimal cast (#24252)
- Unordered unions in check order observing pass (#24253)
- Fix dtype for `slice` on `Literal` in agg context (#24137)
- Fix incorrect `filter(lit(True))` when scanning hive (#24237)
- In-memory group\_by on 128-bit integers (#24242)
- Fix panic in `gather` inside groupby with invalid indices (#24182)
- Release the GIL in map\_groups (#24225)
- Remove extra explode in `LazyGroupBy.{head,tail}` (#24221)
- Fix panic in polars cloud CSV scan (#24197)
- Fix panic when loading categorical columns from IO plugin (#24205)
- Fix credential provider did not auto-init on partition sinks (#24188)
- Fix engine type for `concat_list` on AggScalar `implode` (#24160)
- Rolling\_mean handle centered weights with len(values) \< window\_size (#24158)
- Reading `is_in` predicate for Parquet plain strings (#24184)
- Support native DuckDB connection in read\_database (#24177)
- Make PyCategories pickleable (#24170)
- Remove unused unsound function `to_mutable_slice` (#24173)
- PyO3 extension types giving compat\_level errors (#24166)
- Allow non-elementwise by in top\_k (#24164)
- Fix `sort_by` for `group_by_dynamic` context (#24152)
- Input-independent length aggregations in streaming (#24153)
- Release GIL when iterating df in to\_arrow (#24151)
- Respect non-elementwise join\_where conditions (#24135)
- Fix mismatched pytest test collection error (#24133)
- Resolve schema mismatch for div on Boolean (#24111)
- Fix from\_repr parsing of negative durations (#24115)
- Make `group_by`/`partition_by` iterator keys `tuple[Any, ...]` to enable tuple-unpacking (#24113)
- Keep name when doing empty group-aware aggregation (#24098)
- Implode instead of `reshape_list` (#24078)
- Rolling mean with weights incorrect when min\_samples \< window\_size (#23485)
- Allow `merge_sorted` for all types (#24077)
- Include datatypes in `row_encode` expression (#24074)
- Include UDF materialized type in serialization (#24073)
- Correct `.rolling()` output type for non-aggregations (#24072)
- Correct planner output schema for `join_asof` (#24071)
- Correct output for `fold` and `reduce` (#24069)
- Expr.meta.output\_name for struct fields (#24064)
- Ensure upcast operations on `pl.Date` default to microsecond precision (#23981)
- Add peak\_{min,max} support for booleans (#24068)
- Planner output type for `mean` with strange input type (#24052)
- Remove, deprecate or change eager `Expr`s to be lazy compatible (#24027)

## 📖 Documentation

- Fix few typos (#24305)
- Add missing reference to `LazyFrame.pipe_with_schema()` on the website (#24285)
- Automatically register `doctest.ELLIPSIS` so we don't have to add the inline directive each time (#24146)
- Update categorical comparison documentation in user guide (#24249)
- Add missing references for `Seriers.rolling_*_by` methods (#24254)
- Fix formatting of Series.value\_counts examples (#24245)
- Add hint to use `DataFrame/Series` constructors in `from_arrow` docstring (#22942)
- Update GPU un/supported features (#24195)
- Add `DataFrame.map_columns` to API (#24128)
- Update multiple pages in the Polars Cloud user guide (#23661)
- Fix `str.find_many()` docstring example (#24092)

## 📦 Build system

- Re-enable macos-x86-64 (#24266)
- Drop binary support for macos\_x86-64 (#24257)

## 🛠️ Other improvements

- Remove PDS-H code (#24301)
- Get ready for even more cloud tests (#24292)
- Add tests for slices with caches (#24288)
- Readd ordering tests (#24284)
- Fix Makefile venv path (#24251)
- Remove unnecessary parentheses (#24244)
- Make non-nested shift{,\_and\_fill} ops generic (#24224)
- Remove unused `Wrap` (#24214)
- Allow upcasting null-typed columns to nested column types in scans (#24185)
- Automatically label a few more types of PR (#24147)
- Update toolchain (#24156)
- Add `order_sensitive` property for `AExpr` (#24116)
- Mark more tests as not possible on cloud (#24103)
- Turn `AggExpr::Count` from tuple to struct (#24096)
- Mark tests that may fail in cloud (#24067)
- Extend read database tests to capture more ADBC functionality (#24002)
- Make CI perf failures more lenient (#24066)
- Fix hive partition string encoding in CI by upgrading `deltalake` (#24018)
- Make tests with sinks run on cloud again (#24048)

Thank you to all our contributors for making this release possible!
@Kevin-Patyk, @MarcoGorelli, @NeejWeej, @agossard, @alexander-beedie, @aparna2198, @borchero, @coastalwhite, @deanm0000, @dsprenkels, @eitsupi, @etiennebacher, @gab23r, @henryharbeck, @jjurm, @kdn36, @math-hiyoko, @mcrumiller, @mroeschke, @nameexhaustion, @orlp, @r-brink, @ritchie46, @stijnherfst, @vdrn and @wence-

## Project: [pandas-dev/pandas](https://pandas.pydata.org/docs/index.html), 1 releases: ['Pandas 2.3.3']
### Release: pandas [Pandas 2.3.3](https://github.com/pandas-dev/pandas/releases/tag/v2.3.3)
We are pleased to announce the release of pandas 2.3.3.
This release includes some improvements and fixes to the future string data type (preview feature for the upcoming pandas 3.0). We recommend that all users upgrade to this version.

See the [full whatsnew](https://pandas.pydata.org/pandas-docs/version/2.3/whatsnew/v2.3.3.html) for a list of all the changes.
Pandas 2.3.3 supports Python 3.9 and higher, and is the first release to support Python 3.14.

The release will be available on the conda-forge channel:

    conda install pandas --channel conda-forge

Or via PyPI:

    python3 -m pip install --upgrade pandas

Please report any issues with the release on the [pandas issue tracker](https://github.com/pandas-dev/pandas/issues).

Thanks to all the contributors who made this release possible.
## Project: [holoviz/panel](https://panel.holoviz.org/), 2 releases: ['Version 1.8.1', 'Version 1.8.0']
### Release: panel [Version 1.8.1](https://github.com/holoviz/panel/releases/tag/v1.8.1)
Many thanks to [@ATL2001](https://github.com/ATL2001) (first contribution), [@Coderambling](https://github.com/Coderambling), [@philippjfr](https://github.com/philippjfr), and [@hoxbro](https://github.com/hoxbro) for their contributions.

### Enhancements

- Add configuration to disable container popup ([#8200](https://github.com/holoviz/panel/pull/8200))

### Bug Fixes

- Ensure Tabulator empty column has no width ([#8193](https://github.com/holoviz/panel/pull/8193))
- Add UTC timezone to default time for croniter ([#8199](https://github.com/holoviz/panel/pull/8199))

### Documentation

- Update indicators_performance.md to fix typo ([#8192](https://github.com/holoviz/panel/pull/8192))

### Release: panel [Version 1.8.0](https://github.com/holoviz/panel/releases/tag/v1.8.0)
This release brings a wide range of new features, enhancements, and compatibility improvements. Highlights include support for `JSCode` in ECharts and Tabulator, reworked WebSocket reconnection, and the ability to bundle resources into WASM apps, and numerous bug fixes to improve stability across components and templates. It also includes compatibility updates for **Bokeh 3.8** and several improvements for use in **Pyodide**, **JupyterLite**, and **authentication-based deployments**. Many thanks to our returning contributors @dalthviz and @etihwo, a very warm welcome to our new contributors @c-meier and @flxmr and as usual many thanks to our core team including @maximlt, @hoxbro, @ahuang11, @MarcSkovMadsen and @philippjfr.

### 🚀 Features

- Support for inline JavaScript functions in `ECharts` and `Tabulator` via `JSCode` wrapper ([#8162](https://github.com/holoviz/panel/pull/8162))
- Add support for reconnecting to a session after network disruption ([#8120](https://github.com/holoviz/panel/pull/8120))
- Add support for `AVIF` images ([#8164](https://github.com/holoviz/panel/pull/8164))
- Add support for bundling local resources into WASM apps ([#8181](https://github.com/holoviz/panel/pull/8181))

### ✨ Enhancements

- Improve `.from_param()` behavior and error messages ([#8047](https://github.com/holoviz/panel/pull/8047), [#8079](https://github.com/holoviz/panel/pull/8079))
- Add `--reuse-sessions warm` option to reduce session cold starts ([#8087](https://github.com/holoviz/panel/pull/8087))
- Enable event dispatch immediately after WebSocket connect ([#8101](https://github.com/holoviz/panel/pull/8101))
- Improve error message display in `LiteralInput` ([#8102](https://github.com/holoviz/panel/pull/8102))
- Allow `hold` usage from a thread ([#8113](https://github.com/holoviz/panel/pull/8113))
- Improve uniformity and consistency in `Tabulator` column configuration ([#8127](https://github.com/holoviz/panel/pull/8127))
- Trigger `param.Event` correctly on value change ([#8148](https://github.com/holoviz/panel/pull/8148))
- Allow registering external `extension_cdn` for JS resources ([#8175](https://github.com/holoviz/panel/pull/8175))
- Allow overriding the `default_widgets` on `HoloViews` pane ([#8186](https://github.com/holoviz/panel/pull/8186))

### 🐛 Bug Fixes

- Ensure `Terminal` resizes correctly ([#8109](https://github.com/holoviz/panel/pull/8109))
- Bundle correct `AceEditor` version ([#8111](https://github.com/holoviz/panel/pull/8111))
- Remove `bokeh-sampledata` dependency from Pyodide builds ([#8138](https://github.com/holoviz/panel/pull/8138))
- Correct resource handling when resources are symlinked ([#8143](https://github.com/holoviz/panel/pull/8143))
- Correct behavior when `FileDownload` resets cursor before reading ([#8154](https://github.com/holoviz/panel/pull/8154))
- Fix handling of `NaT` values ([#8156](https://github.com/holoviz/panel/pull/8156))
- Apply template design after rendering template ([#8155](https://github.com/holoviz/panel/pull/8155))
- Prevent `select-all` checkbox from being hidden in Material theme ([#8147](https://github.com/holoviz/panel/pull/8147))
- Fix handling of exclusive bounds in `Param` widgets ([#8165](https://github.com/holoviz/panel/pull/8165))
- Fix layout of `Card` headers with `row` flex mode ([#8166](https://github.com/holoviz/panel/pull/8166))
- Uncap height of children in scrollable `Column` layouts ([#8167](https://github.com/holoviz/panel/pull/8167))
- Fix errors in `ECharts` when chart has already been destroyed ([#8168](https://github.com/holoviz/panel/pull/8168))
- Fix `Tabulator` filter behavior with list-based filters ([#8169](https://github.com/holoviz/panel/pull/8169))
- Allow `Card` to overflow container ([#8170](https://github.com/holoviz/panel/pull/8170))
- Fix `pyodide` model syncing ([#8174](https://github.com/holoviz/panel/pull/8174))

### ⚠️ Deprecations

- Removed `panel.io.model.hold` (was moved to `panel.io.document.hold` in 1.6.0) ([#8188](https://github.com/holoviz/panel/pull/8188))
- Deprecated `panel.chat.langchain.PanelCallbackHandler` (to be removed in 1.9.0) ([#8188](https://github.com/holoviz/panel/pull/8188))

### 📦 Compatibility & Infrastructure

- Update component versions ([#7447](https://github.com/holoviz/panel/pull/7447))
  - `DeckGL` version from 9.0.20 to 9.1.14
  - `ECharts` version from 5.6.0 to 6.0.0
  - `KaTeX` version from 0.6.0 to 0.16.22
  - `Perspective` version from 3.6.1 to 3.8.0
  - `Plotly` version from 3.0.1 to 3.1.0
  - `Vega` version from 5 to 6.1.2 and vega-lite dependency from 5 to 6.3.0
  - `Vizzu` version from 0.15 to 0.17.1
- Drop support for Bokeh 3.5 and 3.6 ([#8116](https://github.com/holoviz/panel/pull/8116))
- Full compatibility with **Bokeh 3.8** ([#8160](https://github.com/holoviz/panel/pull/8160))

### 📚 Documentation

- Add guide for using WebSocket comms ([#7952](https://github.com/holoviz/panel/pull/7952))
- Update links for Tabulator ([#8126](https://github.com/holoviz/panel/pull/8126))
- Align component parameter reference documentation ([#8152](https://github.com/holoviz/panel/pull/8152))

## Project: [cython/cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html), 1 releases: ['3.1.4']
### Release: cython [3.1.4](https://github.com/cython/cython/releases/tag/3.1.4)

## Project: [plotly/dash](https://plotly.com/dash/), 3 releases: ['Dash Version 3.3.0rc0', 'v4.0.0rc1', 'v4.0.0rc0']
### Release: dash [Dash Version 3.3.0rc0](https://github.com/plotly/dash/releases/tag/v3.3.0rc0)
## Added
- [#3395](https://github.com/plotly/dash/pull/3396) Add position argument to hooks.devtool
- [#3403](https://github.com/plotly/dash/pull/3403) Add app_context to get_app, allowing to get the current app in routes.
- [#3407](https://github.com/plotly/dash/pull/3407) Add `hidden` to callback arguments, hiding the callback from appearing in the devtool callback graph.
- [#3424](https://github.com/plotly/dash/pull/3424) Adds support for `Patch` on clientside callbacks class `dash_clientside.Patch`, as well as supporting side updates, eg: (Running, SetProps).
- [#3347](https://github.com/plotly/dash/pull/3347) Added 'api_endpoint' to `callback` to expose api endpoints at the provided path for use to be executed directly without dash.

## Fixed
- [#3395](https://github.com/plotly/dash/pull/3395) Fix Components added through set_props() cannot trigger related callback functions. Fix [#3316](https://github.com/plotly/dash/issues/3316)
- [#3397](https://github.com/plotly/dash/pull/3397) Add optional callbacks, suppressing callback warning for missing component ids for a single callback.
- [#3415](https://github.com/plotly/dash/pull/3415) Fix the error triggered when only a single no_update is returned for client-side callback functions with multiple Outputs. Fix [#3366](https://github.com/plotly/dash/issues/3366)
- [#3416](https://github.com/plotly/dash/issues/3416) Fix DeprecationWarning in dash/_jupyter.py by migrating from deprecated ipykernel.comm.Comm to comm module
### Release: dash [v4.0.0rc1](https://github.com/plotly/dash/releases/tag/v4.0.0rc1)
## Added
- [#3440](https://github.com/plotly/dash/pull/3440) Modernize dcc.Dropdown

### Release: dash [v4.0.0rc0](https://github.com/plotly/dash/releases/tag/v4.0.0rc0)
- [#3398](https://github.com/plotly/dash/pull/3398) Modernize dcc.Input
- [#3414](https://github.com/plotly/dash/pull/3414) Modernize dcc.Slider
## Project: [dask/dask](https://www.dask.org/), 2 releases: ['2025.9.1', '2025.9.0']
### Release: dask [2025.9.1](https://github.com/dask/dask/releases/tag/2025.9.1)
## Changes

- Bump scientific-python/issue-from-pytest-log-action from 1.3.0 to 1.4.0 @[dependabot[bot]](https://github.com/apps/dependabot) (#12077)
- Avoid unconditional pyarrow dependency in dataframe.backends @TomAugspurger (#12075)
- pandas 3.x compatibility for `.groups` @TomAugspurger (#12071)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

### Release: dask [2025.9.0](https://github.com/dask/dask/releases/tag/2025.9.0)
## Changes

- Bump actions/stale from 9 to 10 @[dependabot[bot]](https://github.com/apps/dependabot) (#12070)
- Bump actions/setup-python from 5 to 6 @[dependabot[bot]](https://github.com/apps/dependabot) (#12069)
- fix: `0` scalar setting for `scipy.sparse` @ilan-gold (#12027)
- Get upstream-dev CI passing @TomAugspurger (#12061)
- avoid instantiating a potentially very large arange in `take` @keewis (#11998)
- MAINT: address NumPy deprecation in `np.minimum` @MarcoGorelli (#12059)
- CI fixes @TomAugspurger (#12058)
- MAINT: Address NumPy DeprecationWarning @MarcoGorelli (#12056)
- TST: Fix test\_enforce\_columns on Python 3.14 @QuLogic (#12047)
- Bump actions/checkout from 4 to 5 @[dependabot[bot]](https://github.com/apps/dependabot) (#12046)
- Fix "th" --> "the" typo in DataFrame SQL docs @pjonsson (#12038)
- Advance rng state in permutation @jrbourbeau (#12031)
- Fix ``pyarrow`` chunked array conversion @jrbourbeau (#12034)
- Fix ``xfail`` condition for ``pyarrow`` ``large\_string`` issue @jrbourbeau (#12032)
- pandas 3.x compatibility @TomAugspurger (#12025)
- (fix): `name` not passed to `blockwise` in `map_blocks` @ilan-gold (#11952)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

## Project: [rapidsai/cudf](https://docs.rapids.ai/api/cudf/stable/user_guide/10min/), 1 releases: ['[NIGHTLY] v25.12.00']
### Release: cudf [[NIGHTLY] v25.12.00](https://github.com/rapidsai/cudf/releases/tag/v25.12.00a)
## 🔗 Links

- [Development Branch](https://github.com/rapidsai/cudf/tree/branch-25.12)
- [Compare with `main` branch](https://github.com/rapidsai/cudf/compare/main...branch-25.12)

## 🚨 Breaking Changes

- Rewrite JNI functions to use `JNI_TRY`/`JNI_CATCH` (#19053) @ttnghia

## 🐛 Bug Fixes

- Fix arrow timestamp frequency cases in `cudf.pandas` (#20128) @galipremsagar
- Fix cudf.date_range with non-iso start and end date strings (#20116) @mroeschke
- Unproxy few unnecessary testing utilities in pandas (#20088) @galipremsagar
- Fix create_distinct_rows_column to create non-nullable columns (#20082) @davidwendt
- Handle missing nightly runs in pandas tests job (#20081) @galipremsagar
- Copy `attrs` at correct place in `DataFrame` constructor (#20074) @galipremsagar
- Fix numpy ufunc for `DataFrame` (#20070) @galipremsagar
- Fix libcudf groupby benchmarks to not include internal cache (#20038) @davidwendt

## 🚀 New Features

- Add memory resources to reduce, column, column_factories, and contiguous_split (#20135) @vyasr
- Add memory resource to all strings modules (#20123) @vyasr
- Add memory resources to all nvtext APIs (#20119) @vyasr
- Add memory resources to groupby, datetime, and lists modules (#20102) @vyasr
- Add memory resources to search, reshape, and partitioning module (#20101) @vyasr
- Add memory resources to rolling, sorting, and quantiles modules (#20099) @vyasr
- Add memory resources to binaryop, copying, and stream_compaction (#20059) @vyasr
- Add memory resources to unary, transform, and filling modules (#20054) @vyasr
- [FEA] Implement JIT Filter for read_parquet (#19831) @lamarrr
- Rewrite JNI functions to use `JNI_TRY`/`JNI_CATCH` (#19053) @ttnghia

## 🛠️ Improvements

- Fix slowdown in cudf-polars distributed tests (#20137) @TomAugspurger
- Disable async MR priming in cudf.pandas (#20133) @bdice
- Add pyarrow stubs to mypy environment and fix associated errors (#20118) @vyasr
- Avoid running pandas unit tests for private functionality with cudf.pandas (#20115) @mroeschke
- Remove MultiIndex.from_pandas pytest benchmark (#20112) @mroeschke
- Use 8 processes for pandas tests, show top 10 test times (#20109) @bdice
- Reduce verbosity of running the pandas test suite (#20107) @vyasr
- Switch host_vector and host_span dependency (#20106) @davidwendt
- Have ListColumn.from_sequence go through pylibcudf (#20098) @mroeschke
- Fix `RAPIDS_BRANCH` version and update script (#20091) @galipremsagar
- Avoid direct CategoricalColumn calls in dask_cudf (#20080) @mroeschke
- Avoid shadowing module names (#20071) @vyasr
- Fix typing issues in pylibcudf (#20069) @vyasr
- Cleanup of some libcudf aggregation code (#20053) @davidwendt
- Prune entries in Sphinx nitpick_ignore (#20045) @mroeschke
- Deprecate .from_pandas constructor (#19996) @mroeschke
- Improve performance of string column size computation during parquet reads. (#19986) @nvdbaranec
- Run cudf-polars conda unit tests with more than 1 process (#19980) @mroeschke
- Clean up detail device atomic logic using atomic_ref (#19924) @PointKernel
- Update nvbench (#19619) @bdice
- Remove calling to `purge_nonempty_nulls` in `make_lists_column` (#12873) @ttnghia
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 10 releases: ['v0.37.1-beta.1', 'v0.37.0', 'v0.36.0-beta.2', 'v0.36.0', 'v0.36.0-beta.1', 'v0.35.0-beta.3', 'v0.35.0-beta.2', 'v0.35.0-beta.1', 'v0.35.0', 'v0.34.0-beta.4']
### Release: lance [v0.37.1-beta.1](https://github.com/lancedb/lance/releases/tag/v0.37.1-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v0.37.1-beta.1 -->

## What's Changed
### New Features 🎉
* feat: support manifeset summary and get it from Version by @majin1102 in https://github.com/lancedb/lance/pull/4754
* feat: implement blob encoding for 2.1 by @westonpace in https://github.com/lancedb/lance/pull/4802
* feat(java): expose additional Operation::Update fields to bindings by @wayneli-vt in https://github.com/lancedb/lance/pull/4788
* feat(index/fts): build fst at write time instead of read time by @Xuanwo in https://github.com/lancedb/lance/pull/4811
* feat: support RabitQ quantization by @BubbleCal in https://github.com/lancedb/lance/pull/4344
* feat: add scalar and system index spec by @jackye1995 in https://github.com/lancedb/lance/pull/4736
### Bug Fixes 🐛
* fix: propagate span in filtered read by @wjones127 in https://github.com/lancedb/lance/pull/4790
* fix: add incremental metrics in FilteredRead by @wjones127 in https://github.com/lancedb/lance/pull/4798
### Performance Improvements 🚀
* perf: move cpu heavy fst building into blocking threads by @Xuanwo in https://github.com/lancedb/lance/pull/4803

## New Contributors
* @wayneli-vt made their first contribution in https://github.com/lancedb/lance/pull/4788

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.37.0...v0.37.1-beta.1
### Release: lance [v0.37.0](https://github.com/lancedb/lance/releases/tag/v0.37.0)
<!-- Release notes generated using configuration in .github/release.yml at v0.37.0 -->

## What's Changed
### Breaking Changes 🛠
* feat: add table metadata, support incremental updates of all metadata by @wjones127 in https://github.com/lancedb/lance/pull/4350
### New Features 🎉
* feat: optimize bitmap index with lazy loading and column projection by @LuQQiu in https://github.com/lancedb/lance/pull/4699
* feat: add LanceFileSession.open_writer for sharing object store by @jmhsieh in https://github.com/lancedb/lance/pull/4722
* feat: apply bitpacking on rep/def for compression by @Xuanwo in https://github.com/lancedb/lance/pull/4537
* feat: support create btree index distributedly by @xloya in https://github.com/lancedb/lance/pull/4667
* feat: add LANCE_LOG_FILE environment variable for file logging by @yanghua in https://github.com/lancedb/lance/pull/4721
* feat: optimize file name for s3 throughput by @jackye1995 in https://github.com/lancedb/lance/pull/4737
* feat(rust): support refresh frag bitmap for index after updating when… by @yanghua in https://github.com/lancedb/lance/pull/4589
* feat(java): supports do compaction distributedly by @steFaiz in https://github.com/lancedb/lance/pull/4706
* feat: exposing option to provide a serialized manifest to the Java SDK by @morales-t-netflix in https://github.com/lancedb/lance/pull/4764
* feat: allow out-of-line bitpacking supports tail chunk by @Xuanwo in https://github.com/lancedb/lance/pull/4740
* feat: add udtf for fts query by @wojiaodoubao in https://github.com/lancedb/lance/pull/4684
* feat: support nested field for index operations by @jackye1995 in https://github.com/lancedb/lance/pull/4682
### Bug Fixes 🐛
* fix: refine SIMD support detection for AArch64 on iOS/tvOS by @felix-schultz in https://github.com/lancedb/lance/pull/4725
* fix: fix various 2.1 writer issues by @westonpace in https://github.com/lancedb/lance/pull/4713
* fix: correct underestimate of Bloom filter epsilon by @jbapple in https://github.com/lancedb/lance/pull/4734
* fix: fix the preview release is wrong for preview versions by @Xuanwo in https://github.com/lancedb/lance/pull/4750
* fix(rust): fix rechunk sequences bug and refactor for better readability by @yanghua in https://github.com/lancedb/lance/pull/4695
* fix(FlatMatchQuery): add support for List of Utf8 by @wojiaodoubao in https://github.com/lancedb/lance/pull/4742
* fix: fts boolean query and boost query do not support phrase by @wojiaodoubao in https://github.com/lancedb/lance/pull/4766
* fix: speed up generating ProjectionPlan for full schema by @timsaucer in https://github.com/lancedb/lance/pull/4743
* fix: don't create an empty chunk when values are evenly divisible by @westonpace in https://github.com/lancedb/lance/pull/4775
* fix: fix decoder bugs in 2.1 list handling, expand test coverage by @westonpace in https://github.com/lancedb/lance/pull/4784
* fix: move indexes back to table.proto to avoid forward compat. issues by @westonpace in https://github.com/lancedb/lance/pull/4786
### Documentation 📚
* docs: update performance.md for index cache section by @chenghao-guo in https://github.com/lancedb/lance/pull/4738
* docs: make duckdb example runnable by @eddyxu in https://github.com/lancedb/lance/pull/4770
### Performance Improvements 🚀
* perf: avoid per-iop clone of filename by @westonpace in https://github.com/lancedb/lance/pull/4714
* perf: hierarchical clustering by @BubbleCal in https://github.com/lancedb/lance/pull/4726
* perf: cache num_cpus::get by @westonpace in https://github.com/lancedb/lance/pull/4768
### Other Changes
* refactor: rename lance_table::format::Index to lance_table::format::IndexMetadata by @westonpace in https://github.com/lancedb/lance/pull/4760
* refactor(rust): distinguish row id and row addr part-1 by @yanghua in https://github.com/lancedb/lance/pull/4352

## New Contributors
* @jmhsieh made their first contribution in https://github.com/lancedb/lance/pull/4722
* @felix-schultz made their first contribution in https://github.com/lancedb/lance/pull/4725
* @xloya made their first contribution in https://github.com/lancedb/lance/pull/4667
* @morales-t-netflix made their first contribution in https://github.com/lancedb/lance/pull/4764

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.36.0...v0.37.0
### Release: lance [v0.36.0-beta.2](https://github.com/lancedb/lance/releases/tag/v0.36.0-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v0.36.0-beta.2 -->

## What's Changed
### New Features 🎉
* feat: optimize bitmap index with lazy loading and column projection by @LuQQiu in https://github.com/lancedb/lance/pull/4699
* feat: add LanceFileSession.open_writer for sharing object store by @jmhsieh in https://github.com/lancedb/lance/pull/4722

## New Contributors
* @jmhsieh made their first contribution in https://github.com/lancedb/lance/pull/4722

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.36.0-beta.1...v0.36.0-beta.2
### Release: lance [v0.36.0](https://github.com/lancedb/lance/releases/tag/v0.36.0)
<!-- Release notes generated using configuration in .github/release.yml at v0.36.0 -->

## What's Changed
### Breaking Changes 🛠
* feat!: add target_partition_size vector index param by @BubbleCal in https://github.com/lancedb/lance/pull/4616
* feat!: add MERGED state to MemWAL index by @jackye1995 in https://github.com/lancedb/lance/pull/4673
### New Features 🎉
* feat: build type-aware index for JSON by @Xuanwo in https://github.com/lancedb/lance/pull/4626
* feat: add json parser for FtsQuery by @wojiaodoubao in https://github.com/lancedb/lance/pull/4605
* feat: build Linux wheels with debug symbols for GitHub releases by @wjones127 in https://github.com/lancedb/lance/pull/4647
* feat(java): supports fragment-level mergeColumn interface by @steFaiz in https://github.com/lancedb/lance/pull/4649
* feat: support build FTS index distributedly by @chenghao-guo in https://github.com/lancedb/lance/pull/4578
* feat: merge indices with provided unindexed fragments by @jackye1995 in https://github.com/lancedb/lance/pull/4659
* feat: simplify wheel builds with debug parameter for workflow_dispatch by @wjones127 in https://github.com/lancedb/lance/pull/4655
* feat: add LanceFileSession for sharing object store amongst file readers by @westonpace in https://github.com/lancedb/lance/pull/4670
* feat(java): extends WriteParams in java with `enable_stable_row_ids` option by @steFaiz in https://github.com/lancedb/lance/pull/4674
* feat: add timestamp precision control to logging and document logging by @westonpace in https://github.com/lancedb/lance/pull/4669
* feat: add new cleanup policy to retain latest n versions by @wojiaodoubao in https://github.com/lancedb/lance/pull/4614
* feat: add bloom filter filter support by @HaochengLIU in https://github.com/lancedb/lance/pull/4530
* feat: allow using bitpacking in zero chunk by @Xuanwo in https://github.com/lancedb/lance/pull/4694
* feat: add scalar index support in Java/JNI interface by @beinan in https://github.com/lancedb/lance/pull/4683
* feat: create indexes from another source dataset by @jackye1995 in https://github.com/lancedb/lance/pull/4658
* feat: add compact functionality to Java/JNI interface by @beinan in https://github.com/lancedb/lance/pull/4703
* feat(java): expose merge_insert api by @fangbo in https://github.com/lancedb/lance/pull/4685
* feat: add plan summary to `lance::execution` events by @wjones127 in https://github.com/lancedb/lance/pull/4700
* feat: add traces for file level IO by @jaystarshot in https://github.com/lancedb/lance/pull/4697
* feat: add `use_index` option for merge insert by @wjones127 in https://github.com/lancedb/lance/pull/4688
* feat(python): pass `Session` when opening dataset by @wjones127 in https://github.com/lancedb/lance/pull/3927
### Bug Fixes 🐛
* fix: correctly decode lists with all nulls by @westonpace in https://github.com/lancedb/lance/pull/4679
* fix: circular reference in index caching leaks memory by @wkalt in https://github.com/lancedb/lance/pull/4680
* fix: resolve deadlock when multiple threads access a single LanceFileWriter by @lorinlee in https://github.com/lancedb/lance/pull/4600
* fix(rust): fix duplicated source rows when merge insert by @yanghua in https://github.com/lancedb/lance/pull/4687
* fix: use consistent naming for rows_per_zone in zone map index by @jackye1995 in https://github.com/lancedb/lance/pull/4692
* fix: don't fail reading variable width full-zip with repetition but no definition by @westonpace in https://github.com/lancedb/lance/pull/4698
### Documentation 📚
* docs: polish docs for JSON data types by @Xuanwo in https://github.com/lancedb/lance/pull/4640
* docs: non-optional enum fields in proto3 do not have explicit presence by @jbapple in https://github.com/lancedb/lance/pull/4642
* docs: fix vector search add columns issue by @erik-wang-lancedb in https://github.com/lancedb/lance/pull/4690
### Other Changes
* refactor(python): refactor take bench and support parametrize compression by @yanghua in https://github.com/lancedb/lance/pull/4636
* refactor: remove the 2.2 version requirement for using JSON features by @Xuanwo in https://github.com/lancedb/lance/pull/4641

## New Contributors
* @steFaiz made their first contribution in https://github.com/lancedb/lance/pull/4649
* @jaystarshot made their first contribution in https://github.com/lancedb/lance/pull/4697
* @erik-wang-lancedb made their first contribution in https://github.com/lancedb/lance/pull/4690

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.35.0...v0.36.0
### Release: lance [v0.36.0-beta.1](https://github.com/lancedb/lance/releases/tag/v0.36.0-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v0.36.0-beta.1 -->



**Full Changelog**: https://github.com/lancedb/lance/compare/v0.36.0...v0.36.0-beta.1
### Release: lance [v0.35.0-beta.3](https://github.com/lancedb/lance/releases/tag/v0.35.0-beta.3)
<!-- Release notes generated using configuration in .github/release.yml at v0.35.0-beta.3 -->

## What's Changed
### Breaking Changes 🛠
* feat!: add target_partition_size vector index param by @BubbleCal in https://github.com/lancedb/lance/pull/4616
### New Features 🎉
* feat(java): supports fragment-level mergeColumn interface by @steFaiz in https://github.com/lancedb/lance/pull/4649
* feat: support build FTS index distributedly by @chenghao-guo in https://github.com/lancedb/lance/pull/4578
* feat: merge indices with provided unindexed fragments by @jackye1995 in https://github.com/lancedb/lance/pull/4659
* feat: simplify wheel builds with debug parameter for workflow_dispatch by @wjones127 in https://github.com/lancedb/lance/pull/4655
* feat: add LanceFileSession for sharing object store amongst file readers by @westonpace in https://github.com/lancedb/lance/pull/4670

## New Contributors
* @steFaiz made their first contribution in https://github.com/lancedb/lance/pull/4649

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.35.0-beta.2...v0.35.0-beta.3
### Release: lance [v0.35.0-beta.2](https://github.com/lancedb/lance/releases/tag/v0.35.0-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v0.35.0-beta.2 -->

## What's Changed
### New Features 🎉
* feat: build Linux wheels with debug symbols for GitHub releases by @wjones127 in https://github.com/lancedb/lance/pull/4647


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.35.0-beta.1...v0.35.0-beta.2
### Release: lance [v0.35.0-beta.1](https://github.com/lancedb/lance/releases/tag/v0.35.0-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v0.35.0-beta.1 -->

## What's Changed
### New Features 🎉
* feat: build type-aware index for JSON by @Xuanwo in https://github.com/lancedb/lance/pull/4626
* feat: add json parser for FtsQuery by @wojiaodoubao in https://github.com/lancedb/lance/pull/4605
### Documentation 📚
* docs: polish docs for JSON data types by @Xuanwo in https://github.com/lancedb/lance/pull/4640
### Other Changes
* refactor(python): refactor take bench and support parametrize compression by @yanghua in https://github.com/lancedb/lance/pull/4636
* refactor: remove the 2.2 version requirement for using JSON features by @Xuanwo in https://github.com/lancedb/lance/pull/4641


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.35.0...v0.35.0-beta.1
### Release: lance [v0.35.0](https://github.com/lancedb/lance/releases/tag/v0.35.0)
<!-- Release notes generated using configuration in .github/release.yml at v0.35.0 -->

## What's Changed
### Breaking Changes 🛠
* feat!: add storage options to wrapping object store by @wkalt in https://github.com/lancedb/lance/pull/4509
* feat!: shallow_clone supports index by @majin1102 in https://github.com/lancedb/lance/pull/4553
### New Features 🎉
* feat: add lance-tools command by @cmccabe in https://github.com/lancedb/lance/pull/4545
* feat: add JSONB read/write support by @Xuanwo in https://github.com/lancedb/lance/pull/4566
* feat(java): add deleteRows for Fragment by @fangbo in https://github.com/lancedb/lance/pull/4528
* feat: inverted index for contains_tokens by @wojiaodoubao in https://github.com/lancedb/lance/pull/4489
* feat: add cumulative_cpu output to analyze_plan string by @cmccabe in https://github.com/lancedb/lance/pull/4519
* feat(rust): support update stable row id for overlapping by @yanghua in https://github.com/lancedb/lance/pull/4496
* feat: add UDFs for json by @Xuanwo in https://github.com/lancedb/lance/pull/4577
* feat: allow using opendal to access s3, azblob and gcs by @jackye1995 in https://github.com/lancedb/lance/pull/4597
* feat: expose open_session in python by @wojiaodoubao in https://github.com/lancedb/lance/pull/4581
* feat: add a scalar index for JSON by @westonpace in https://github.com/lancedb/lance/pull/4621
### Bug Fixes 🐛
* fix: include base_id in DeletionFile serialization by @pimdh in https://github.com/lancedb/lance/pull/4580
* fix: tagged_old_versions should only track tagged and old versions by @wojiaodoubao in https://github.com/lancedb/lance/pull/4592
* fix: index out of bounds caused by exhausted posting iterator by @BubbleCal in https://github.com/lancedb/lance/pull/4587
* fix: validate operations in transaction commit by @majin1102 in https://github.com/lancedb/lance/pull/4532
* fix: disable default features from jsonb to avoid changing serde-json behavior by @Xuanwo in https://github.com/lancedb/lance/pull/4601
* fix: shallow_clone multiple times refering to wrong base path by @majin1102 in https://github.com/lancedb/lance/pull/4617
* fix: can't train vector index with cosine distance on GPU by @BubbleCal in https://github.com/lancedb/lance/pull/4623
### Documentation 📚
* docs: add docs for JSON and JSON UDFs by @Xuanwo in https://github.com/lancedb/lance/pull/4599
### Performance Improvements 🚀
* perf: add dataset random take benchmark by @yanghua in https://github.com/lancedb/lance/pull/4113
* perf: improve FTS performance for long query by @BubbleCal in https://github.com/lancedb/lance/pull/4576
### Other Changes
* refactor: rework scalar index loading, training, and parsing into a plugin trait by @westonpace in https://github.com/lancedb/lance/pull/4584

## New Contributors
* @pimdh made their first contribution in https://github.com/lancedb/lance/pull/4580
* @ebyhr made their first contribution in https://github.com/lancedb/lance/pull/4606

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.34.0...v0.35.0
### Release: lance [v0.34.0-beta.4](https://github.com/lancedb/lance/releases/tag/v0.34.0-beta.4)
<!-- Release notes generated using configuration in .github/release.yml at v0.34.0-beta.4 -->

## What's Changed
### Breaking Changes 🛠
* feat!: add storage options to wrapping object store by @wkalt in https://github.com/lancedb/lance/pull/4509
* feat!: shallow_clone supports index by @majin1102 in https://github.com/lancedb/lance/pull/4553
### New Features 🎉
* feat: add lance-tools command by @cmccabe in https://github.com/lancedb/lance/pull/4545
* feat: add JSONB read/write support by @Xuanwo in https://github.com/lancedb/lance/pull/4566
* feat(java): add deleteRows for Fragment by @fangbo in https://github.com/lancedb/lance/pull/4528
* feat: inverted index for contains_tokens by @wojiaodoubao in https://github.com/lancedb/lance/pull/4489
* feat: add cumulative_cpu output to analyze_plan string by @cmccabe in https://github.com/lancedb/lance/pull/4519
* feat(rust): support update stable row id for overlapping by @yanghua in https://github.com/lancedb/lance/pull/4496
* feat: add UDFs for json by @Xuanwo in https://github.com/lancedb/lance/pull/4577
* feat: allow using opendal to access s3, azblob and gcs by @jackye1995 in https://github.com/lancedb/lance/pull/4597
### Bug Fixes 🐛
* fix: include base_id in DeletionFile serialization by @pimdh in https://github.com/lancedb/lance/pull/4580
* fix: tagged_old_versions should only track tagged and old versions by @wojiaodoubao in https://github.com/lancedb/lance/pull/4592
* fix: index out of bounds caused by exhausted posting iterator by @BubbleCal in https://github.com/lancedb/lance/pull/4587
* fix: validate operations in transaction commit by @majin1102 in https://github.com/lancedb/lance/pull/4532
* fix: disable default features from jsonb to avoid changing serde-json behavior by @Xuanwo in https://github.com/lancedb/lance/pull/4601
* fix: shallow_clone multiple times refering to wrong base path by @majin1102 in https://github.com/lancedb/lance/pull/4617
### Documentation 📚
* docs: add docs for JSON and JSON UDFs by @Xuanwo in https://github.com/lancedb/lance/pull/4599
### Performance Improvements 🚀
* perf: add dataset random take benchmark by @yanghua in https://github.com/lancedb/lance/pull/4113
* perf: improve FTS performance for long query by @BubbleCal in https://github.com/lancedb/lance/pull/4576
### Other Changes
* refactor: rework scalar index loading, training, and parsing into a plugin trait by @westonpace in https://github.com/lancedb/lance/pull/4584

## New Contributors
* @pimdh made their first contribution in https://github.com/lancedb/lance/pull/4580
* @ebyhr made their first contribution in https://github.com/lancedb/lance/pull/4606

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.34.0...v0.34.0-beta.4
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 16 releases: ['Node/Rust LanceDB v0.22.2-beta.0', 'Python LanceDB v0.25.2-beta.0', 'Node/Rust LanceDB v0.22.1', 'Python LanceDB v0.25.1', 'Node/Rust LanceDB v0.22.1-beta.3', 'Python LanceDB v0.25.1-beta.3', 'Node/Rust LanceDB v0.22.1-beta.2', 'Python LanceDB v0.25.1-beta.2', 'Node/Rust LanceDB v0.22.1-beta.1', 'Node/Rust LanceDB v0.22.1-beta.0', 'Python LanceDB v0.25.1-beta.1', 'Python LanceDB v0.25.1-beta.0', 'Node/Rust LanceDB v0.22.0', 'Python LanceDB v0.25.0', 'Node/Rust LanceDB v0.22.0-beta.1', 'Python LanceDB v0.25.0-beta.1']
### Release: lancedb [Node/Rust LanceDB v0.22.2-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.22.2-beta.0)
## 🎉 New Features

- feat: add use_index parameter to merge insert operations by @wjones127 in https://github.com/lancedb/lancedb/pull/2674
- feat(rust): support namespace backed database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2664

## 🔧 Build and CI

- ci(nodejs): lint for unused imports by @wjones127 in https://github.com/lancedb/lancedb/pull/2673
- ci: fix test failure on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2677


### Release: lancedb [Python LanceDB v0.25.2-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.2-beta.0)
## 🎉 New Features

- feat: add use_index parameter to merge insert operations by @wjones127 in https://github.com/lancedb/lancedb/pull/2674
- feat(rust): support namespace backed database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2664

## 🔧 Build and CI

- ci(nodejs): lint for unused imports by @wjones127 in https://github.com/lancedb/lancedb/pull/2673
- ci: fix test failure on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2677


### Release: lancedb [Node/Rust LanceDB v0.22.1](https://github.com/lancedb/lancedb/releases/tag/v0.22.1)
## 🎉 New Features

- feat: support mTLS for remote database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2638
- feat: support per-request header override by @jackye1995 in https://github.com/lancedb/lancedb/pull/2631
- feat: add 'target_partition_size' param by @BubbleCal in https://github.com/lancedb/lancedb/pull/2642
- feat: support shallow clone by @jackye1995 in https://github.com/lancedb/lancedb/pull/2653
- feat: support mean reciprocal rank reranker by @AyushExel in https://github.com/lancedb/lancedb/pull/2671
- feat: upgrade Lance to v0.37.0 by @wjones127 in https://github.com/lancedb/lancedb/pull/2672

## 🐛 Bug Fixes

- fix: add partition statistics to MetadataEraser by @LuQQiu in https://github.com/lancedb/lancedb/pull/2637
- fix: use create to resolve variables by @manhld0206 in https://github.com/lancedb/lancedb/pull/2640
- fix: add missing validations to namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2659
- fix(node): handle undefined vector fields with embedding functions by @naaa760 in https://github.com/lancedb/lancedb/pull/2655
- fix(node): handle null values in nullable boolean fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2657
- fix: undefined values should become null in nullable fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2658

## Other Changes

- refactor: remove catalog implementation now that we have namespaces in database by @westonpace in https://github.com/lancedb/lancedb/pull/2662


### Release: lancedb [Python LanceDB v0.25.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.1)
## 🎉 New Features

- feat: support mTLS for remote database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2638
- feat: support per-request header override by @jackye1995 in https://github.com/lancedb/lancedb/pull/2631
- feat: add 'target_partition_size' param by @BubbleCal in https://github.com/lancedb/lancedb/pull/2642
- feat: support shallow clone by @jackye1995 in https://github.com/lancedb/lancedb/pull/2653
- feat: support mean reciprocal rank reranker by @AyushExel in https://github.com/lancedb/lancedb/pull/2671
- feat: upgrade Lance to v0.37.0 by @wjones127 in https://github.com/lancedb/lancedb/pull/2672

## 🐛 Bug Fixes

- fix: add partition statistics to MetadataEraser by @LuQQiu in https://github.com/lancedb/lancedb/pull/2637
- fix: use create to resolve variables by @manhld0206 in https://github.com/lancedb/lancedb/pull/2640
- fix: add missing validations to namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2659
- fix(node): handle undefined vector fields with embedding functions by @naaa760 in https://github.com/lancedb/lancedb/pull/2655
- fix(node): handle null values in nullable boolean fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2657
- fix: undefined values should become null in nullable fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2658

## Other Changes

- refactor: remove catalog implementation now that we have namespaces in database by @westonpace in https://github.com/lancedb/lancedb/pull/2662


### Release: lancedb [Node/Rust LanceDB v0.22.1-beta.3](https://github.com/lancedb/lancedb/releases/tag/v0.22.1-beta.3)
## 🎉 New Features

- feat: support shallow clone by @jackye1995 in https://github.com/lancedb/lancedb/pull/2653

## 🐛 Bug Fixes

- fix(node): handle undefined vector fields with embedding functions by @naaa760 in https://github.com/lancedb/lancedb/pull/2655


### Release: lancedb [Python LanceDB v0.25.1-beta.3](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.1-beta.3)
## 🎉 New Features

- feat: support shallow clone by @jackye1995 in https://github.com/lancedb/lancedb/pull/2653

## 🐛 Bug Fixes

- fix(node): handle undefined vector fields with embedding functions by @naaa760 in https://github.com/lancedb/lancedb/pull/2655


### Release: lancedb [Node/Rust LanceDB v0.22.1-beta.2](https://github.com/lancedb/lancedb/releases/tag/v0.22.1-beta.2)
## 🎉 New Features

- feat: add 'target_partition_size' param by @BubbleCal in https://github.com/lancedb/lancedb/pull/2642

## 🐛 Bug Fixes

- fix: use create to resolve variables by @manhld0206 in https://github.com/lancedb/lancedb/pull/2640
- fix: add missing validations to namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2659

## Other Changes

- refactor: remove catalog implementation now that we have namespaces in database by @westonpace in https://github.com/lancedb/lancedb/pull/2662


### Release: lancedb [Python LanceDB v0.25.1-beta.2](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.1-beta.2)
## 🎉 New Features

- feat: add 'target_partition_size' param by @BubbleCal in https://github.com/lancedb/lancedb/pull/2642

## 🐛 Bug Fixes

- fix: use create to resolve variables by @manhld0206 in https://github.com/lancedb/lancedb/pull/2640
- fix: add missing validations to namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2659

## Other Changes

- refactor: remove catalog implementation now that we have namespaces in database by @westonpace in https://github.com/lancedb/lancedb/pull/2662


### Release: lancedb [Node/Rust LanceDB v0.22.1-beta.1](https://github.com/lancedb/lancedb/releases/tag/v0.22.1-beta.1)
## 🎉 New Features

- feat: support per-request header override by @jackye1995 in https://github.com/lancedb/lancedb/pull/2631


### Release: lancedb [Node/Rust LanceDB v0.22.1-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.22.1-beta.0)
## 🎉 New Features

- feat: support mTLS for remote database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2638

## 🐛 Bug Fixes

- fix: add partition statistics to MetadataEraser by @LuQQiu in https://github.com/lancedb/lancedb/pull/2637


### Release: lancedb [Python LanceDB v0.25.1-beta.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.1-beta.1)
## 🎉 New Features

- feat: support per-request header override by @jackye1995 in https://github.com/lancedb/lancedb/pull/2631


### Release: lancedb [Python LanceDB v0.25.1-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.1-beta.0)
## 🎉 New Features

- feat: support mTLS for remote database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2638

## 🐛 Bug Fixes

- fix: add partition statistics to MetadataEraser by @LuQQiu in https://github.com/lancedb/lancedb/pull/2637


### Release: lancedb [Node/Rust LanceDB v0.22.0](https://github.com/lancedb/lancedb/releases/tag/v0.22.0)
## 🛠 Breaking Changes

- feat!: support multi-level namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2603
- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622

## 🎉 New Features

- feat: allow setting `train=False` and `name` on indices by @wjones127 in https://github.com/lancedb/lancedb/pull/2586
- feat: upgrade lance to 0.33.0-beta.3 by @wjones127 in https://github.com/lancedb/lancedb/pull/2598
- feat(python): integrate with lance namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2599
- feat: add __getitems__ method impl for torch integration by @westonpace in https://github.com/lancedb/lancedb/pull/2596
- feat!: support multi-level namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2603
- feat: add `name` parameter to remaining Python create index calls by @wjones127 in https://github.com/lancedb/lancedb/pull/2617

## 🐛 Bug Fixes

- fix: make cloud features optional (#2567) by @vlovich in https://github.com/lancedb/lancedb/pull/2568
- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622
- fix: remote python sdk namespace typing by @wkalt in https://github.com/lancedb/lancedb/pull/2620


### Release: lancedb [Python LanceDB v0.25.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.0)
## 🛠 Breaking Changes

- feat!: support multi-level namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2603
- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622

## 🎉 New Features

- feat: allow setting `train=False` and `name` on indices by @wjones127 in https://github.com/lancedb/lancedb/pull/2586
- feat: upgrade lance to 0.33.0-beta.3 by @wjones127 in https://github.com/lancedb/lancedb/pull/2598
- feat(python): integrate with lance namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2599
- feat: add __getitems__ method impl for torch integration by @westonpace in https://github.com/lancedb/lancedb/pull/2596
- feat!: support multi-level namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2603
- feat: add `name` parameter to remaining Python create index calls by @wjones127 in https://github.com/lancedb/lancedb/pull/2617

## 🐛 Bug Fixes

- fix: make cloud features optional (#2567) by @vlovich in https://github.com/lancedb/lancedb/pull/2568
- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622
- fix: remote python sdk namespace typing by @wkalt in https://github.com/lancedb/lancedb/pull/2620


### Release: lancedb [Node/Rust LanceDB v0.22.0-beta.1](https://github.com/lancedb/lancedb/releases/tag/v0.22.0-beta.1)
## 🛠 Breaking Changes

- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622

## 🐛 Bug Fixes

- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622
- fix: remote python sdk namespace typing by @wkalt in https://github.com/lancedb/lancedb/pull/2620


### Release: lancedb [Python LanceDB v0.25.0-beta.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.0-beta.1)
## 🛠 Breaking Changes

- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622

## 🐛 Bug Fixes

- fix!: fix doctest in query.py by @cmccabe in https://github.com/lancedb/lancedb/pull/2622
- fix: remote python sdk namespace typing by @wkalt in https://github.com/lancedb/lancedb/pull/2620


## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers?tab=readme-ov-file#datafusion-table-providers), 2 releases: ['v0.8.1', 'v0.8.0']
### Release: datafusion-table-providers [v0.8.1](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.8.1)
## What's Changed
* Improve the read performance of Postgres' Decimals by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/438


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.8.0...v0.8.1
### Release: datafusion-table-providers [v0.8.0](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.8.0)
## What's Changed
* Bump uuid from 1.17.0 to 1.18.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/417
* Bump rand from 0.9.1 to 0.9.2 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/415
* Bump rstest from 0.25.0 to 0.26.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/414
* Bump dyn-clone from 1.0.19 to 1.0.20 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/413
* Bump prost from 0.13.5 to 0.14.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/412
* ClickHouse: Add python module  by @trueleo in https://github.com/datafusion-contrib/datafusion-table-providers/pull/418
* Upgrade datafusion to version 50 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/437


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.7.0...v0.8.0
## Project: [duckdb/duckdb](https://duckdb.org/), 1 releases: ['DuckDB 1.4.0 "Andium"']
### Release: duckdb [DuckDB 1.4.0 "Andium"](https://github.com/duckdb/duckdb/releases/tag/v1.4.0)
This release of DuckDB is named "Andium" after Anas Andium, a species of duck that lives in the Andes mountains in South America.

Please also refer to the announcement blog post: https://duckdb.org/2025/09/16/announcing-duckdb-140.html


## What's Changed
* Python package devexp improvements by @evertlammerts in https://github.com/duckdb/duckdb/pull/17483
* change exception type to not be an internal exception by @samansmink in https://github.com/duckdb/duckdb/pull/17551
* Remove redundant code path in the ConflictManager by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17562
* Add support for ToSqlString for union types by @wmTJc9IK0Q in https://github.com/duckdb/duckdb/pull/17513
* Update function descriptions and examples by @c-herrewijn in https://github.com/duckdb/duckdb/pull/17132
* Move query profiler's EndQuery after commit/rollback by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17595
* fix extension troubleshooting link by @simon0191 in https://github.com/duckdb/duckdb/pull/17616
* C API tidying by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17623
* bump DuckDB_jll to v1.3.0 by @c-herrewijn in https://github.com/duckdb/duckdb/pull/17677
* Add rowsort in generate_series test #43 by @jeewonhh in https://github.com/duckdb/duckdb/pull/17675
* [C API] Expose duckdb_scalar_function_bind_get_extra_info by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17666
* Enable profiling output for all operator types by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17665
* Output hashes in unittest and fix order by @niykko in https://github.com/duckdb/duckdb/pull/17664
* New Sorting Implementation by @lnkuiper in https://github.com/duckdb/duckdb/pull/17584
* Merge v1.3-ossivalis into main by @Mytherin in https://github.com/duckdb/duckdb/pull/17690
* Issue #17040: FILL Window Function  by @hawkfish in https://github.com/duckdb/duckdb/pull/17686
* ClientBufferManager wrapper to access the client context in the buffer manager by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17699
* Revert "set default for MAIN_BRANCH_VERSIONING to false" by @carlopi in https://github.com/duckdb/duckdb/pull/17708
* Sorting followup by @lnkuiper in https://github.com/duckdb/duckdb/pull/17717
* Correctly setting the delim offset by @Damon07 in https://github.com/duckdb/duckdb/pull/17716
* fix linux extension ci by @samansmink in https://github.com/duckdb/duckdb/pull/17720
* Aggregation performance by @lnkuiper in https://github.com/duckdb/duckdb/pull/17718
* Fix windows-2025 build errors by @adsharma in https://github.com/duckdb/duckdb/pull/17726
* [SQLLogicTester] Introduce `reset label <query label>` in the tester by @Tishj in https://github.com/duckdb/duckdb/pull/17729
* Adding additional authenticated data for encryption by @ccfelius in https://github.com/duckdb/duckdb/pull/17508
* csv_scanner: correct code comment by @Djfe in https://github.com/duckdb/duckdb/pull/17735
* Deprecate windows-2019 runners  by @hannes in https://github.com/duckdb/duckdb/pull/17745
* re-add httpfs apply_patches by @samansmink in https://github.com/duckdb/duckdb/pull/17755
* Rename decorator from test_nulls to null_test_parameters by @Mytherin in https://github.com/duckdb/duckdb/pull/17760
* [CAPI] Expose ErrorData by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17722
* Expose file_size_bytes and footer_size in parquet_file_metadata by @gijshendriksen in https://github.com/duckdb/duckdb/pull/17750
* Pass `ExtensionLoader` when loading extensions, change extension entry function by @Maxxen in https://github.com/duckdb/duckdb/pull/17772
* Support glibc 2.28 environments by @James-Gilbert- in https://github.com/duckdb/duckdb/pull/17776
* Mark Upper/LowerComparisonType as const by @JelteF in https://github.com/duckdb/duckdb/pull/17773
* [Indexes] Buffer-managed indexes part 1: segment handles by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17758
* [Julia] api docs improvements  by @tqml in https://github.com/duckdb/duckdb/pull/15645
* Ensure we use the same layout in `RadixPartitionedHashTable` and `GroupedAggregateHashTable` by @lnkuiper in https://github.com/duckdb/duckdb/pull/17790
* [Profiling] Propagate the ClientContext into file handle writes by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17754
* Fix propagatesNullValues for case expr by @suibianwanwank in https://github.com/duckdb/duckdb/pull/17796
* Add qualified parameter to Python GetTableNames API by @evertlammerts in https://github.com/duckdb/duckdb/pull/17797
* Merge v1.3 into main by @Mytherin in https://github.com/duckdb/duckdb/pull/17806
* Pushdown pivot filter by @flashmouse in https://github.com/duckdb/duckdb/pull/17801
* Replace string for const data ptr in encryption api by @ccfelius in https://github.com/duckdb/duckdb/pull/17825
* Merge130 by @carlopi in https://github.com/duckdb/duckdb/pull/17833
* fix: escape using_columns on JoinRef::ToString by @akoshchiy in https://github.com/duckdb/duckdb/pull/17839
* Fix ICE with Windows ARM64 by @staticlibs in https://github.com/duckdb/duckdb/pull/17844
* Merge v1.3 into main by @Mytherin in https://github.com/duckdb/duckdb/pull/17851
* Add `duckdb_type` column to parquet_schema by @Mytherin in https://github.com/duckdb/duckdb/pull/17852
* Internal #4991: Remove Epoch_MS(MS) by @hawkfish in https://github.com/duckdb/duckdb/pull/17816
* #17853 Enable flexible page sizes and update Android NDK to r27 in workflow. by @aprock in https://github.com/duckdb/duckdb/pull/17854
* [Indexes] Buffer-managed indexes part 2: segment handle for base nodes by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17828
* Function Serialization: adapt to removal of overloads by explicitly casting if argument types have changed by @Mytherin in https://github.com/duckdb/duckdb/pull/17864
* julia: add missing methods from C-API by @tqml in https://github.com/duckdb/duckdb/pull/17733
* Issue #17153: Window Order Columns by @hawkfish in https://github.com/duckdb/duckdb/pull/17835
* Issue #17040: FILL Secondary Sorts by @hawkfish in https://github.com/duckdb/duckdb/pull/17821
* Add STRUCT to MAP cast function by @evertlammerts in https://github.com/duckdb/duckdb/pull/17799
* Issue #17849: Test FILL Duplicates by @hawkfish in https://github.com/duckdb/duckdb/pull/17869
* Add GenAI policy by @szarnyasg in https://github.com/duckdb/duckdb/pull/17882
* Update function descriptions and examples for list, array, lambda functions by @c-herrewijn in https://github.com/duckdb/duckdb/pull/17886
* Issue #17861: FILL Argument Types by @hawkfish in https://github.com/duckdb/duckdb/pull/17888
* Reword GenAI policy by @szarnyasg in https://github.com/duckdb/duckdb/pull/17895
* Use an arena linked list for the physical operator children by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17748
* Make CTE Materialization the Default Instead of Inlining by @kryonix in https://github.com/duckdb/duckdb/pull/17459
* Merge v1.3 into main by @Mytherin in https://github.com/duckdb/duckdb/pull/17897
* Leverage `VectorType` in `ColumnDataCollection` by @lnkuiper in https://github.com/duckdb/duckdb/pull/17881
* Fix empty BP block when writing parquet by @platypii in https://github.com/duckdb/duckdb/pull/17929
* fix use after free in adbc on invalid stmt by @ruslandoga in https://github.com/duckdb/duckdb/pull/17927
* Do not dispatch JDBC/ODBC jobs in release CI runs by @staticlibs in https://github.com/duckdb/duckdb/pull/17937
* Block based encryption by @ccfelius in https://github.com/duckdb/duckdb/pull/17275
* Unittester failures summary by @hmeriann in https://github.com/duckdb/duckdb/pull/16833
* Add v1.3-ossivalis to Cross version workflow by @hmeriann in https://github.com/duckdb/duckdb/pull/17906
* [CI Nightly Fix] Skip logging test if not standard block size by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17957
* Visual Studio 17 (2022) fixes by @edouarda in https://github.com/duckdb/duckdb/pull/17948
* [Nested] Add `struct_position` and `struct_contains` functions by @maiadegraaf in https://github.com/duckdb/duckdb/pull/17819
* Enable building spatial and encodings extensions by @staticlibs in https://github.com/duckdb/duckdb/pull/17960
* [Nested] Optimize structs in `LIST_VALUE` by @maiadegraaf in https://github.com/duckdb/duckdb/pull/17169
* Unit Tester Configuration by @Mytherin in https://github.com/duckdb/duckdb/pull/17972
* [nested] Allow fixed-size arrays to be unnested by @maiadegraaf in https://github.com/duckdb/duckdb/pull/17968
* Merge v1.3-ossivalis into main by @Mytherin in https://github.com/duckdb/duckdb/pull/17973
* [CI] Skip some workflows when updating out of tree extensions SHA by @hmeriann in https://github.com/duckdb/duckdb/pull/17949
* Issue #5144: AsOf Join Threshold by @hawkfish in https://github.com/duckdb/duckdb/pull/17979
* [Fix] Reset profiling info before preparing a query by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17940
* Flag to disable database invalidation by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17938
* Issue #5123: make_timestamp_ms by @hawkfish in https://github.com/duckdb/duckdb/pull/17908
* Rework extension loading to go through thread-safe ExtensionManager by @Mytherin in https://github.com/duckdb/duckdb/pull/17994
* Implement consumption and production of Arrow Binary View by @pdet in https://github.com/duckdb/duckdb/pull/17975
* Add support to produce Polars Lazy Dataframes by @pdet in https://github.com/duckdb/duckdb/pull/17947
* c-api to copy vector with selection by @abramk in https://github.com/duckdb/duckdb/pull/17870
* Fix #18007: correctly execute expressions with pivot operator by @Mytherin in https://github.com/duckdb/duckdb/pull/18020
* [Chore] Minor conflict manager refactoring by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18015
* Remove Linux (32 Bit) job by @hmeriann in https://github.com/duckdb/duckdb/pull/18012
* [Explain] Add the YAML format for EXPLAIN statements by @qsliu2017 in https://github.com/duckdb/duckdb/pull/17572
* Unittest: Add skip_compiled option that can be used to skip built-in C++ tests by @Mytherin in https://github.com/duckdb/duckdb/pull/18034
* Add ppc64le spin-wait instruction by @mgiessing in https://github.com/duckdb/duckdb/pull/17837
* Merge ossivalis into main by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18036
* Remove match-case statements from polars_io.py by @evertlammerts in https://github.com/duckdb/duckdb/pull/18052
* Avoid adding commands read from a file to the shell history by @Mytherin in https://github.com/duckdb/duckdb/pull/18057
* Adding WAL encryption by @ccfelius in https://github.com/duckdb/duckdb/pull/17955
* Encryption: adding -key for the command line by @ccfelius in https://github.com/duckdb/duckdb/pull/17950
* fix star expr exclude error by @jayhan94 in https://github.com/duckdb/duckdb/pull/18063
* Add support for class-based expression iteration by @Mytherin in https://github.com/duckdb/duckdb/pull/18070
* Use `timestamp_t` instead of `time_t` for file last modified time by @lnkuiper in https://github.com/duckdb/duckdb/pull/18037
* Unittester: add `on_new_connection` + `on_load` + `skip_tests` options by @carlopi in https://github.com/duckdb/duckdb/pull/18042
* Fix some scaling issues by @lnkuiper in https://github.com/duckdb/duckdb/pull/17985
* Issue #18071: Temporal inf -inf by @hawkfish in https://github.com/duckdb/duckdb/pull/18083
* Switch to Optional for type hints in polars lazy dataframe function by @evertlammerts in https://github.com/duckdb/duckdb/pull/18078
* Unittest: Configure skip error messages by @carlopi in https://github.com/duckdb/duckdb/pull/18087
* Avoid running DraftPR.yml until timeout if token is missing by @carlopi in https://github.com/duckdb/duckdb/pull/18090
* Add start/end offset percentage options to Python test runner by @Flogex in https://github.com/duckdb/duckdb/pull/18091
* [CSV Reader] Prohibit options delim and sep in same read_csv call by @ackxolotl in https://github.com/duckdb/duckdb/pull/18096
* Fix  correlated subquery unnest fail by @flashmouse in https://github.com/duckdb/duckdb/pull/18092
* [CI] don't run jobs on draft PRs by @hmeriann in https://github.com/duckdb/duckdb/pull/18016
* TPC-DS: Use BIGINT fields by @szarnyasg in https://github.com/duckdb/duckdb/pull/18098
* Don't throw `InternalException` in `Sort::Sink` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18105
* ci: build duckdb against the latest emscripten by @cpcloud in https://github.com/duckdb/duckdb/pull/18110
* [chore] Merge v1.3-ossivalis on main by @carlopi in https://github.com/duckdb/duckdb/pull/18109
* Update description of 'arrow_lossless_conversion' by @szarnyasg in https://github.com/duckdb/duckdb/pull/18046
* Internal #3273: Window Task Generation by @hawkfish in https://github.com/duckdb/duckdb/pull/18113
* set ::error:: annotations for test runners by @hmeriann in https://github.com/duckdb/duckdb/pull/18072
* Improve sort key comparison performance by @lnkuiper in https://github.com/duckdb/duckdb/pull/18131
* Add support for `MERGE INTO` by @Mytherin in https://github.com/duckdb/duckdb/pull/18135
* Detect when updates have no effect, and skip performing the actual updates if we encounter these nop updates by @Mytherin in https://github.com/duckdb/duckdb/pull/18144
* Add support for AdbcConnectionGetObjects(table_type) by @kou in https://github.com/duckdb/duckdb/pull/18066
* Issue #17683: TIME_NS Compilation by @hawkfish in https://github.com/duckdb/duckdb/pull/18053
* Implement `replace_type` function by @lnkuiper in https://github.com/duckdb/duckdb/pull/18077
* Bump spatial again: include re-linking for handling global objects in Wasm by @carlopi in https://github.com/duckdb/duckdb/pull/18170
* Resolve some small build issues by @madscientist in https://github.com/duckdb/duckdb/pull/18162
* fix typo by @felixhummel in https://github.com/duckdb/duckdb/pull/18165
* Avoid `realloc` in CSV writer by @lnkuiper in https://github.com/duckdb/duckdb/pull/18174
* fix bug with allowed_paths by @samansmink in https://github.com/duckdb/duckdb/pull/18176
* Reduce lock contention for the instance cache by @NiclasHaderer in https://github.com/duckdb/duckdb/pull/18079
* Check if `GetLastSegment` is not `nullptr` in `ColumnData::RevertAppend` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18171
* [Profiling] Move the client context into more write functions by @taniabogatsch in https://github.com/duckdb/duckdb/pull/17875
* Bump Julia to v1.3.2 by @hmeriann in https://github.com/duckdb/duckdb/pull/18185
* Merge `v1.3-ossivalis` into `main` by @carlopi in https://github.com/duckdb/duckdb/pull/18188
* Parquet reader logging by @lnkuiper in https://github.com/duckdb/duckdb/pull/18172
* Add VS2019 compat flag to Python wheel build by @staticlibs in https://github.com/duckdb/duckdb/pull/18198
* [Parquet][Dev] Update the vendored `parquet.thrift` to `3ce0760` by @Tishj in https://github.com/duckdb/duckdb/pull/18195
* Two-rowID-leaf support in the conflict manager and general refactoring by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18194
* More internal-linkage by @Maxxen in https://github.com/duckdb/duckdb/pull/18177
* Temporary file encryption by @Mytherin in https://github.com/duckdb/duckdb/pull/18208
* Adding temporary file encryption by @ccfelius in https://github.com/duckdb/duckdb/pull/18013
* Skip logging test for smaller block sizes by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18201
* ci(pyodide): enable WASM exceptions on the latest pyodide build by @cpcloud in https://github.com/duckdb/duckdb/pull/18173
* Allow explicit compression for user types by @lnkuiper in https://github.com/duckdb/duckdb/pull/18219
* Get type of encoded `SortKey` from `TupleDataLayout` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18218
* Improve Parquet reader `NULL` statistics and compress all-`NULL` columns using `CompressedMaterialization` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18217
* Internal #5264: NLJ Not Distinct by @hawkfish in https://github.com/duckdb/duckdb/pull/18216
* Bug#18163 Fix STDDEV_SAMP undeterminism by @minaracic in https://github.com/duckdb/duckdb/pull/18210
* [Parquet] Add read support for the `VARIANT` LogicalType by @Tishj in https://github.com/duckdb/duckdb/pull/18187
* Track `DataChunk` memory usage in various places by @lnkuiper in https://github.com/duckdb/duckdb/pull/18191
* Better `NULL` handling in `TupleDataLayout` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18069
* Dictionary functions by @lnkuiper in https://github.com/duckdb/duckdb/pull/18127
* Add support for geoarrow encoded geometries in geoparquet files. by @cfis in https://github.com/duckdb/duckdb/pull/17942
* Improve descriptions of thresholds vars affecting join algorithm selection by @TheHillBright in https://github.com/duckdb/duckdb/pull/17377
* Connect relations that are not in a subgraph, but are still part of the new relation set by @Tmonster in https://github.com/duckdb/duckdb/pull/18182
* [Fix] Don't write empty (partial) blocks for FSST dictionary compression by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18203
* Slightly higher memory limit for test by @lnkuiper in https://github.com/duckdb/duckdb/pull/18235
* Re-add string -> hugeint compressed materialization function by @lnkuiper in https://github.com/duckdb/duckdb/pull/18234
* [Fix] Database path conflict resolution by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18247
* Remove require block size from a batch of tests by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18242
* Add nightly builds for out-of-tree python extension by @evertlammerts in https://github.com/duckdb/duckdb/pull/18239
* Backport DB invalidation flag to ossivalis by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18244
* Bump vcpkg-duckdb-ports and test extensions on Windows 10 default stdlib by @carlopi in https://github.com/duckdb/duckdb/pull/18205
* Add type safety to `FlatVector::GetData<T>`, `ConstantVector::GetData<T>` and `UnifiedVectorFormat::GetData<T>` by @Mytherin in https://github.com/duckdb/duckdb/pull/18256
* [Fix] Adjust test for smaller block sizes by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18255
* Fix integer overflow in sequence vector by @xuke-hat in https://github.com/duckdb/duckdb/pull/18245
* fixes for some minor llvm 20 complaints by @hannes in https://github.com/duckdb/duckdb/pull/18257
* update run_extension_medata_tests.sh by @hmeriann in https://github.com/duckdb/duckdb/pull/17976
* Bunch of loosely connected test/CI fixes by @carlopi in https://github.com/duckdb/duckdb/pull/18254
* disable WebAssembly duckdb-wasm builds job in NightlyTests triggered by 'workflow_dispatch' event by @hmeriann in https://github.com/duckdb/duckdb/pull/18129
* Allow for static libs from extension dependencies to be bundled by @abramk in https://github.com/duckdb/duckdb/pull/18226
* Fix dictionary-related assertions by @lnkuiper in https://github.com/duckdb/duckdb/pull/18260
* Fixes for gcc 15 by @hannes in https://github.com/duckdb/duckdb/pull/18261
* Reduce copy in Vector::Reinterpret by @xuke-hat in https://github.com/duckdb/duckdb/pull/18264
* [Parquet] Add read support for the `VARIANT` LogicalType (with shredded encoding) by @Tishj in https://github.com/duckdb/duckdb/pull/18224
* Expanded autocomplete suggestions by @Dtenwolde in https://github.com/duckdb/duckdb/pull/18243
* Support HUGEINT in printf and format by @xuke-hat in https://github.com/duckdb/duckdb/pull/13277
* Move aarch64 / arm64 to native github runner by @evertlammerts in https://github.com/duckdb/duckdb/pull/18269
* Bump vcpkg-duckdb-ports to solve OSX linking by @carlopi in https://github.com/duckdb/duckdb/pull/18268
* Add support for RETURNING to MERGE INTO by @Mytherin in https://github.com/duckdb/duckdb/pull/18271
* Use set for row ID scanning during index scans by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18274
* Use DuckDB cast infrastructure in fmt for new uhugeint/hugeint code by @Mytherin in https://github.com/duckdb/duckdb/pull/18275
* [Fix] Adjust test to run with different block sizes by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18277
* Use `FromEpochSeconds` instead of `FromTimeT` in `FileSystem::GetLastModifiedTime` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18281
* Add target for installing Python deps. by @xevix in https://github.com/duckdb/duckdb/pull/18285
* backport 'Unit Tester Configuration' pt2 by @c-herrewijn in https://github.com/duckdb/duckdb/pull/18282
* backport 'Unit Tester Configuration' by @c-herrewijn in https://github.com/duckdb/duckdb/pull/18263
* Fixup Main.yml for v1.3-ossivalis post https://github.com/duckdb/duckdb/pull/18282 by @carlopi in https://github.com/duckdb/duckdb/pull/18289
* SHOW TABLES FROM <qualified_name> by @xevix in https://github.com/duckdb/duckdb/pull/18179
* [Unittester] Add autoloading option by @carlopi in https://github.com/duckdb/duckdb/pull/18290
* Merge ossivalis into main by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18272
* resolve hidden merge conflict with duplicate db name in json configs by @c-herrewijn in https://github.com/duckdb/duckdb/pull/18292
* Bump vcpkg-duckdb-ports, now fixing also mingw by @carlopi in https://github.com/duckdb/duckdb/pull/18300
* [Fix] Missing block when renaming fields by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18293
* [Arrow] Fix unused static function warning by @Tishj in https://github.com/duckdb/duckdb/pull/18278
* feat: Parquet extension add row_group_compressed_size by @mapleFU in https://github.com/duckdb/duckdb/pull/18294
* [Parquet][Write] Fix timestamp sec writes to parquet by @Tishj in https://github.com/duckdb/duckdb/pull/18273
* bump httpfs by @Tmonster in https://github.com/duckdb/duckdb/pull/18258
* [Clang Tidy] Fix missing includes in `patas_scan.hpp` by @Tishj in https://github.com/duckdb/duckdb/pull/18276
* New Arrow C-API by @pdet in https://github.com/duckdb/duckdb/pull/18246
* Skip test/sql/copy/s3/url_encode.test due to httpfs update by @carlopi in https://github.com/duckdb/duckdb/pull/18317
* Make storage-version a test parameter by @Mytherin in https://github.com/duckdb/duckdb/pull/18324
* Backport #18254 by @carlopi in https://github.com/duckdb/duckdb/pull/18306
* feat: making Parquet write RowGroup.total_compressed_size by @mapleFU in https://github.com/duckdb/duckdb/pull/18307
* add the from-table-function as parameter to copy-from-bind by @peterboncz in https://github.com/duckdb/duckdb/pull/18004
* Python external dispatch param fixes by @evertlammerts in https://github.com/duckdb/duckdb/pull/18343
* Aarch64 backport by @evertlammerts in https://github.com/duckdb/duckdb/pull/18345
* Fix debug error in join order optimizer by @Tmonster in https://github.com/duckdb/duckdb/pull/18344
* [Fix] Block verification for add and drop field info by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18302
* download Real Nest data in quiet mode by @hmeriann in https://github.com/duckdb/duckdb/pull/18346
* Fix condition indexes in join filter pushdown by @Damon07 in https://github.com/duckdb/duckdb/pull/18341
* [unittest] - fix doubled error headers on `Unexpected failure` by @hmeriann in https://github.com/duckdb/duckdb/pull/18314
* Extend PEG parser grammar by @Dtenwolde in https://github.com/duckdb/duckdb/pull/18221
* [C API] Expose expressions and use them in scalar function binding by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18142
* Restore OSX tests, moving them to single `--autoloading available` step by @carlopi in https://github.com/duckdb/duckdb/pull/18335
* Add support for checkpointing in-memory tables by @Mytherin in https://github.com/duckdb/duckdb/pull/18348
* Revert "[unittest] - fix doubled error headers on `Unexpected failure`" by @Mytherin in https://github.com/duckdb/duckdb/pull/18355
* Python external dispatch param fixes by @evertlammerts in https://github.com/duckdb/duckdb/pull/18359
* Re-enable url-encode test by @Tmonster in https://github.com/duckdb/duckdb/pull/18360
* Enable stack traces on linux for bundled libraries by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18363
* Split up out-of-tree extensions into separate files, and allow out-of-tree extensions to be built using BUILD_EXTENSIONS={ext_name} by @Mytherin in https://github.com/duckdb/duckdb/pull/18357
* Pass `AttachOptions` to `attach` method, and turn `StorageExtensionInfo` into an `optional_ptr` by @Mytherin in https://github.com/duckdb/duckdb/pull/18368
* Merge `v1.3-ossivalis` into `main` by @carlopi in https://github.com/duckdb/duckdb/pull/18364
* More robustness around deprecated extension settings by @carlopi in https://github.com/duckdb/duckdb/pull/18353
* Add missing ninja to workflow file by @Dtenwolde in https://github.com/duckdb/duckdb/pull/18373
* bump httpfs by @Tmonster in https://github.com/duckdb/duckdb/pull/18380
* Re-enable but deprecate CORE_EXTENSIONS in CMakeLists.txt by @evertlammerts in https://github.com/duckdb/duckdb/pull/18377
* Uncomment skipped decimal REE tests by @amoeba in https://github.com/duckdb/duckdb/pull/18372
* add option 'block_size' to test configs by @c-herrewijn in https://github.com/duckdb/duckdb/pull/18347
* [chore] Fixup side-effects from 8cf9ed43b60 by @carlopi in https://github.com/duckdb/duckdb/pull/18385
* Bump httpfs by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18388
* Re-use table metadata when table is not altered during checkpoint by @Mytherin in https://github.com/duckdb/duckdb/pull/18390
* Approx database count system function by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18392
* Re-use metadata of unaltered row groups when checkpointing a table by @Mytherin in https://github.com/duckdb/duckdb/pull/18395
* Correct and consistent integer arithmetic error messages by @soerenwolfers in https://github.com/duckdb/duckdb/pull/18393
* Record whether or not cross products are implicit or not, and use this for converting queries back to SQL by @Mytherin in https://github.com/duckdb/duckdb/pull/18394
* CI: Fix Discussion mirroring by @szarnyasg in https://github.com/duckdb/duckdb/pull/18397
* Store extra metadata blocks in RowGroupPointer, and only flush dirty Metadata blocks by @Mytherin in https://github.com/duckdb/duckdb/pull/18398
* Internal #3273: Window Hashed Sort by @hawkfish in https://github.com/duckdb/duckdb/pull/18337
* Wrap runner.ExecuteFile, otherwise cleanup is not properly performed by @carlopi in https://github.com/duckdb/duckdb/pull/18400
* [BUGFIX] Update delim offset for RHS of DELIM JOIN when correlated column is in RHS of Cross product by @Tmonster in https://github.com/duckdb/duckdb/pull/18375
* CI: Add separate job for discussion mirroring by @szarnyasg in https://github.com/duckdb/duckdb/pull/18407
* [ Python SQLLogic Tester ] Add `MERGE_INTO` statement to duckdb python by @hmeriann in https://github.com/duckdb/duckdb/pull/18402
* Remove incorrect assertion by @Mytherin in https://github.com/duckdb/duckdb/pull/18404
* Internal #5294: TIME_NS C API by @hawkfish in https://github.com/duckdb/duckdb/pull/18215
* Add DuckLake back in by @Mytherin in https://github.com/duckdb/duckdb/pull/18405
* Add support for table_constraints of AdbcConnectionGetObjects() by @kou in https://github.com/duckdb/duckdb/pull/18181
* Merge `v1.3-ossivalis` in `main` by @carlopi in https://github.com/duckdb/duckdb/pull/18401
* feat: remove anything following `?` in database name by @rustyconover in https://github.com/duckdb/duckdb/pull/18417
* Correctly fetch only base column data in ColumnData::FetchUpdateData by @Mytherin in https://github.com/duckdb/duckdb/pull/18423
* Refactor extension CI to use extension-ci-tools by @samansmink in https://github.com/duckdb/duckdb/pull/18361
* Internal #5367: SortedAggregateFunction Sort Update  by @hawkfish in https://github.com/duckdb/duckdb/pull/18408
* Internal #5368: WindowNaiveAggregator Sort Update  by @hawkfish in https://github.com/duckdb/duckdb/pull/18409
* [Fix] Block size nightly by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18425
* [Chore] Tidy test configs by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18426
* Include pyodide build configuration by @rgbkrk in https://github.com/duckdb/duckdb/pull/18183
* Parquet: add row-group ordinal during writing encryption by @mapleFU in https://github.com/duckdb/duckdb/pull/18433
* [Fix] Reset segment memory when initialising new Prefix by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18441
* Update pyodide build to 0.28.0 by @rgbkrk in https://github.com/duckdb/duckdb/pull/18446
* Add support for "template" types by @Maxxen in https://github.com/duckdb/duckdb/pull/18410
* Internal #5384: WindowDistinctAggregator Sort Update  by @hawkfish in https://github.com/duckdb/duckdb/pull/18442
* [Chore] Improve skipped tests in test config and add verify_fetch_row config by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18436
* Buffer index appends during WAL replay by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18313
* Add support for generic settings, and move many settings over to generic settings by @Mytherin in https://github.com/duckdb/duckdb/pull/18447
* Internal #5385: WindowMergeSortTree Sort Update by @hawkfish in https://github.com/duckdb/duckdb/pull/18461
* Bump postgres to latest main by @Mytherin in https://github.com/duckdb/duckdb/pull/18464
* Merge ossivalis by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18456
* Internal #5366: WindowDeltaScanner  by @hawkfish in https://github.com/duckdb/duckdb/pull/18468
* SUM and + Operator for Varints by @pdet in https://github.com/duckdb/duckdb/pull/18424
* [Fix] Rework transaction logic in commit, rollback and checkpoint paths by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18474
* re-nable extensions in invokeci by @samansmink in https://github.com/duckdb/duckdb/pull/18476
* Internal #5384: Window Sorting Polish by @hawkfish in https://github.com/duckdb/duckdb/pull/18484
* Unify `ON CONFLICT` and `MERGE INTO` by @Mytherin in https://github.com/duckdb/duckdb/pull/18480
* More insights around dict_fsst compression failure by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18475
* Change ctrl-a/ctrl-e to move to start/end of line, not buffer by @tpot in https://github.com/duckdb/duckdb/pull/18490
* add delta linux back to ci by @samansmink in https://github.com/duckdb/duckdb/pull/18491
* Fix accidental internal exception in type transformation by @hannes in https://github.com/duckdb/duckdb/pull/18492
* [Profiling] Add client context into read functions by @maiadegraaf in https://github.com/duckdb/duckdb/pull/18438
* julia: config improvements by @aplavin in https://github.com/duckdb/duckdb/pull/17585
* fix: add missing space in AttachInfo::ToString() by @rustyconover in https://github.com/duckdb/duckdb/pull/18500
* Merge ossivalis by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18502
* Change UNICODE to UTF8 by @sheldonrobinson in https://github.com/duckdb/duckdb/pull/17586
* Fix: Remove overly strict assertion on empty string value by @Dtenwolde in https://github.com/duckdb/duckdb/pull/18504
* Fix several bugs/fuzzer issues by @Mytherin in https://github.com/duckdb/duckdb/pull/18503
* Allow expressions to be used in ATTACH / COPY options by @Mytherin in https://github.com/duckdb/duckdb/pull/18515
* Remove `immediate_transaction_mode` from DB config options by @jeewonhh in https://github.com/duckdb/duckdb/pull/18516
* Temporarily excluding `Build Pyodide wheel` for Python 3.11 because it fails to build `WASM` wheels  by @hmeriann in https://github.com/duckdb/duckdb/pull/18508
* ParserException for Pragma with named parameters by @Dtenwolde in https://github.com/duckdb/duckdb/pull/18506
* Add verify fetch row config to Main.yml by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18478
* Adding WITH ORDINALITY to DuckDB by @niykko in https://github.com/duckdb/duckdb/pull/16581
* When tracking evicted_data_per_tag, track actual size on disk after temp file compression by @Mytherin in https://github.com/duckdb/duckdb/pull/18521
* Fix: Write the salt together with the HT offset when determining the value for key comparison by @gropaul in https://github.com/duckdb/duckdb/pull/18374
* Fix incorrect character encoding in GetLastErrorAsString on Windows by @soutong in https://github.com/duckdb/duckdb/pull/18431
* Dynamically determine dictionary size limit in Parquet writer (if unset) by @lnkuiper in https://github.com/duckdb/duckdb/pull/18356
* Internal #16560: Numeric TRUNC Precision by @hawkfish in https://github.com/duckdb/duckdb/pull/18511
* Consistently detect JSON schema indepent of number of threads by @lnkuiper in https://github.com/duckdb/duckdb/pull/18522
* ALP test: skip TPC-DS 67 - it is not consistent with floating point numbers by @Mytherin in https://github.com/duckdb/duckdb/pull/18528
* [Varint] Negation, Subtraction and Over/under-flow checking by @pdet in https://github.com/duckdb/duckdb/pull/18477
* fix: support both field orders for variant struct by @samansmink in https://github.com/duckdb/duckdb/pull/18532
* Add CAPI to retrieve client context for table functions by @VGSML in https://github.com/duckdb/duckdb/pull/18520
* Add `StatementVerifier` for `EXPLAIN` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18529
* Use global index, not local id when creating filters in `MultiFileColumnMapper` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18537
* Add support for explicit clean-up routine in test config, and exit multi-statement execution when an error is encountered by @Mytherin in https://github.com/duckdb/duckdb/pull/18539
* fix: improve handling variant nulls and nested types by @samansmink in https://github.com/duckdb/duckdb/pull/18538
* Allow overriding openssl version for FIPS compliance by @abramk in https://github.com/duckdb/duckdb/pull/18499
* Unittester: Add the `--sort-style` parameter that allows a fallback comparison where results are sorted according to a given sort-style by @Mytherin in https://github.com/duckdb/duckdb/pull/18542
* Restore missing `test/configs/small_block_size.json` file by @hmeriann in https://github.com/duckdb/duckdb/pull/18507
* [Fix] Follow-up PR to only delete unique row IDs by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18545
* [ART] Node::Free refactoring by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18544
* Implement special-case `VARCHAR` to `JSON[]` casts and vice versa by @lnkuiper in https://github.com/duckdb/duckdb/pull/18541
* Check if `heap_block_ids` is empty before getting start/end when destroying chunks in `TupleDataCollection` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18556
* optimize/parquet: generate movable types for parquet by @mapleFU in https://github.com/duckdb/duckdb/pull/18510
* [easy] [no-op] Minor optimization on iterator lookup by @dentiny in https://github.com/duckdb/duckdb/pull/15349
* Fixing compilation with -std=cpp23 by @hannes in https://github.com/duckdb/duckdb/pull/18557
* Add compile option standalone-debug for clang by @flashmouse in https://github.com/duckdb/duckdb/pull/17433
* Rename the Varint type to Bignum by @pdet in https://github.com/duckdb/duckdb/pull/18547
* [Indexes] Buffer-managed indexes part 3: segment handle for Node48 and Node256 by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18567
* fix: add formatting to explain row counts by @rustyconover in https://github.com/duckdb/duckdb/pull/18566
* [CSV Sniffer] Fixing bug of not properly setting skipped rows from sniffer by @pdet in https://github.com/duckdb/duckdb/pull/18555
* [Fix] Tidy check ossivalis by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18583
* [Fix] Adjust shrink threshold back to original count > SHRINK_THRESHOLD by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18582
* Flip left/right delim join based on cardinalities by @lnkuiper in https://github.com/duckdb/duckdb/pull/18552
* fix: use thousands separator and decimal for row counts in`duckbox` output format by @rustyconover in https://github.com/duckdb/duckdb/pull/18564
* Force `LIST`/`ARRAY` child vectors on a Parquet single page by @lnkuiper in https://github.com/duckdb/duckdb/pull/18578
* String dictionary hash cache by @lnkuiper in https://github.com/duckdb/duckdb/pull/18580
* fix: libduckdb.so missing soversion by @strophy in https://github.com/duckdb/duckdb/pull/18305
* Pushdown filters on coalesced outer join keys compared for equality under the join condition by @matteobilardi in https://github.com/duckdb/duckdb/pull/18169
* Adds a function for updating and adding values in a struct by @teaguesterling in https://github.com/duckdb/duckdb/pull/15533
* fix hidden merge conflict by @hannes in https://github.com/duckdb/duckdb/pull/18589
* Increment storage version to enable `DICT_FSST` in benchmark file by @lnkuiper in https://github.com/duckdb/duckdb/pull/18588
* [Fix] Hidden test failure in test_struct_update.test by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18598
* correctly setting log transaction id in ThreadContext by @xuke-hat in https://github.com/duckdb/duckdb/pull/18536
* Backport renaming a config name `small_block_size.json` to `block_size_16kB` in NightlyTests by @hmeriann in https://github.com/duckdb/duckdb/pull/18581
* Update README.md by @matthew-wright07 in https://github.com/duckdb/duckdb/pull/18614
* [Test] Fix test case and a benchmark by @hmeriann in https://github.com/duckdb/duckdb/pull/18610
* [CI] Don't zip and upload Code Coverage tests results when Code Coverage got cancelled by @hmeriann in https://github.com/duckdb/duckdb/pull/18607
* [Profiling] Add client context into more read functions by @maiadegraaf in https://github.com/duckdb/duckdb/pull/18514
* bump httpfs by @Tmonster in https://github.com/duckdb/duckdb/pull/18591
* Fix serialization backwards compatability for varargs functions by @Maxxen in https://github.com/duckdb/duckdb/pull/18596
* Issue #18631: Streaming Windowed Quantile by @hawkfish in https://github.com/duckdb/duckdb/pull/18636
* parquet/parquet_multi_file_info.cpp: fix move from stack by @carlopi in https://github.com/duckdb/duckdb/pull/18634
* Adjust filter pushdown to latest polars release by @pdet in https://github.com/duckdb/duckdb/pull/18624
* Re-add `hugeint` to `__internal_compress_string` by @jeewonhh in https://github.com/duckdb/duckdb/pull/18622
* Add Field IDS to multi file reader for positional deletes by @Tmonster in https://github.com/duckdb/duckdb/pull/18617
* [CSV Sniffer] Fix type detection issue with union and empty columns by @pdet in https://github.com/duckdb/duckdb/pull/18606
* [ART] ART::Erase refactoring by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18595
* wrap httplib ::max() call in `WIN_32` check by @Tmonster in https://github.com/duckdb/duckdb/pull/18590
* Add enable verification config run by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18467
* feat: add ETA to progress bar in DuckDB CLI by @rustyconover in https://github.com/duckdb/duckdb/pull/18575
* Add "Hash Zero" verification CI run by @lnkuiper in https://github.com/duckdb/duckdb/pull/18623
* Make more configs into generic settings by @jeewonhh in https://github.com/duckdb/duckdb/pull/18592
* bump avro to v1.4 by @Tmonster in https://github.com/duckdb/duckdb/pull/18434
* bump spatial (on main) by @Maxxen in https://github.com/duckdb/duckdb/pull/18197
* Change arrow() to export record batch reader by @pdet in https://github.com/duckdb/duckdb/pull/18642
* [Fix] Prevent logger deadlock by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18637
* Remove `PRAGMA enable_verification` by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18645
* Add 1.4 release codename by @hannes in https://github.com/duckdb/duckdb/pull/18652
* Python test runner: Fix result check for `COPY ... RETURN_STATS` queries by @Flogex in https://github.com/duckdb/duckdb/pull/18625
* Merge ossivalis into main by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18644
* CLI: Make ETA more of an estimate, and support large_row_rendering for footers by @Mytherin in https://github.com/duckdb/duckdb/pull/18656
* Remove more `PRAGMA enable_verification` by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18664
* [CI] skip building encodings extension in InvokeCI by @hmeriann in https://github.com/duckdb/duckdb/pull/18655
* Python test runner: Fix hash comparison error output by @Flogex in https://github.com/duckdb/duckdb/pull/18626
* [Dev] Add script to create patch from changes in an extension repository by @Tishj in https://github.com/duckdb/duckdb/pull/18620
* Correctly set weights in reservoir sample when switch to slow sampling by @xuke-hat in https://github.com/duckdb/duckdb/pull/18563
* Internal #5366: Window Interrupt Arguments by @hawkfish in https://github.com/duckdb/duckdb/pull/18651
* Remove `PRAGMA enable_verification` in more tests by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18670
* [ Python SQLLogic Tester ] Add `MERGE_INTO` to `statement.type` enum in `result.py` by @hmeriann in https://github.com/duckdb/duckdb/pull/18675
* Load pandas in import cache before binding by @evertlammerts in https://github.com/duckdb/duckdb/pull/18658
* Internal #5662: IEJoin Test Plans by @hawkfish in https://github.com/duckdb/duckdb/pull/18680
* Correctly allocate uncompressed string data in ZSTD for many giant strings by @Mytherin in https://github.com/duckdb/duckdb/pull/18678
* Grab lock and double-check that column is not loaded in MoveToCollection by @Mytherin in https://github.com/duckdb/duckdb/pull/18677
* fix error message related to wrong memory unit by @LiranBri in https://github.com/duckdb/duckdb/pull/18671
* [CI] Temporarily skip triggering `R Package Windows (Extensions)` job by @hmeriann in https://github.com/duckdb/duckdb/pull/18628
* Fix the issue where delta_for isn't used in bitpacking when for is unavailable by @xuke-hat in https://github.com/duckdb/duckdb/pull/18616
* Add `date_trunc()` simplification rules by @rcurtin in https://github.com/duckdb/duckdb/pull/18457
* Expected errors 2053 by @hmeriann in https://github.com/duckdb/duckdb/pull/14213
* Internal #5366: Window State Arguments  by @hawkfish in https://github.com/duckdb/duckdb/pull/18676
* Add WAL test config run by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18683
* Using a different workflow to release the python package by @evertlammerts in https://github.com/duckdb/duckdb/pull/18685
* Make sure parse errors are wrapped in ErrorData by @evertlammerts in https://github.com/duckdb/duckdb/pull/18682
* [Python SQLLogicTest] Add `test/sql/pragma/profiling/test_profiling_all.test` to the SKIPPED_TESTS set by @hmeriann in https://github.com/duckdb/duckdb/pull/18689
* Issue #18457: DateTrunc Simplification Warnings by @hawkfish in https://github.com/duckdb/duckdb/pull/18687
* Expected errors 2053 by @hmeriann in https://github.com/duckdb/duckdb/pull/18695
* Hold row group lock for entire call of MoveToCollection by @Mytherin in https://github.com/duckdb/duckdb/pull/18694
* Unplug python (in ossivalis) by @evertlammerts in https://github.com/duckdb/duckdb/pull/18699
* Correctly handle collations for IN (subquery) by @Mytherin in https://github.com/duckdb/duckdb/pull/18698
* Move attached databases from a CatalogSet to a dedicated map of shared pointers by @Mytherin in https://github.com/duckdb/duckdb/pull/18693
* Make ART construction iterative via ARTBuilder by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18702
* [Fix] Correctly handle table and index chunks in WAL replay buffering by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18700
* Python-style positional/named arguments for macro's by @lnkuiper in https://github.com/duckdb/duckdb/pull/18684
* Internal #3273: Hashed Sort States by @hawkfish in https://github.com/duckdb/duckdb/pull/18690
* Add Option to Allocate Using an Arena in `string_t` by @maiadegraaf in https://github.com/duckdb/duckdb/pull/17992
* Fix issue with materialized CTE optimization in flatten_dependent_join by @kryonix in https://github.com/duckdb/duckdb/pull/18714
* [Profiling] Add Profiling to Read Function by @maiadegraaf in https://github.com/duckdb/duckdb/pull/18661
* Correctly throw an error when too few columns are supplied in MERGE INTO INSERT by @Mytherin in https://github.com/duckdb/duckdb/pull/18715
* Improved grammar generation script by @NiclasHaderer in https://github.com/duckdb/duckdb/pull/18716
* #Fix 18558: add row_group scan fast path by @flashmouse in https://github.com/duckdb/duckdb/pull/18686
* Added support for blob<->uuid conversions by @dioptre in https://github.com/duckdb/duckdb/pull/18027
* Minor fixes for other catalogs - mostly checking `IsDuckTable()` for unsupported operations by @Mytherin in https://github.com/duckdb/duckdb/pull/18720
* Fix PIVOT in multiple statements by @evertlammerts in https://github.com/duckdb/duckdb/pull/18729
* Internal #5669: Loop Join Thresholds by @hawkfish in https://github.com/duckdb/duckdb/pull/18733
* feat: enhance .tables command with schema disambiguation and filtering by @shivampr in https://github.com/duckdb/duckdb/pull/18641
* Add (CSV) file logger by @samansmink in https://github.com/duckdb/duckdb/pull/17692
* Use 1-based indexing for SQL-based JSON array extraction by @lnkuiper in https://github.com/duckdb/duckdb/pull/18735
* [unittest] SkipLoggingSameError() to make unittester report one failure per case by @hmeriann in https://github.com/duckdb/duckdb/pull/18270
* fix timetravel for default tables by @samansmink in https://github.com/duckdb/duckdb/pull/18240
* [C API] Function to set a copy callback for bind data by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18739
* Secrets: if serialization_type is not specified, assume it's a key value secret by @Mytherin in https://github.com/duckdb/duckdb/pull/18743
* Merge ossivalis into main by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18719
* Use correct type for pushing collations in subqueries by @Mytherin in https://github.com/duckdb/duckdb/pull/18744
* Add OS X notarization for DuckDB CLI and libduckdb.dylib by @hannes in https://github.com/duckdb/duckdb/pull/18747
* Add missing expected errors to the test cases by @hmeriann in https://github.com/duckdb/duckdb/pull/18746
* removed placeholder client directories for node and jdbc, its been > 1 yr by @hannes in https://github.com/duckdb/duckdb/pull/18757
* Append using a SQL query, instead of directly appending to a base table, and support user-provided queries through the QueryAppender by @Mytherin in https://github.com/duckdb/duckdb/pull/18738
* Backport #18374 to `v1.3-ossivalis` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18752
* Add leak suppressions to nightly runs by @Mytherin in https://github.com/duckdb/duckdb/pull/18748
* Remove separate WAL encryption flag by @Mytherin in https://github.com/duckdb/duckdb/pull/18750
* Fixing lazy polars execution on query result by @pdet in https://github.com/duckdb/duckdb/pull/18749
* [Profiling] Add Profiling to Write Function by @maiadegraaf in https://github.com/duckdb/duckdb/pull/18724
* Extensions.yml should also check converted_to_draft by @carlopi in https://github.com/duckdb/duckdb/pull/18754
* Minor logging fixes and more benchmarking by @samansmink in https://github.com/duckdb/duckdb/pull/18755
* Add missing expected errors to the test cases (next chunk) by @hmeriann in https://github.com/duckdb/duckdb/pull/18753
* Refactor read_blob and read_text to use MultiFileFunction. by @xevix in https://github.com/duckdb/duckdb/pull/18706
* Add support for auto-globbing within a directory: if no matches are found for a specific path, we retry with `/**/*.[ext]` appended by @Mytherin in https://github.com/duckdb/duckdb/pull/18760
* Fix radix partitioning with more than 10 bits by @ctsk in https://github.com/duckdb/duckdb/pull/18761
* Fix index resolution when querying table with index via view by @mach-kernel in https://github.com/duckdb/duckdb/pull/18319
* Fix Path Typo in Extension's CMake Warning Message by @beryllw in https://github.com/duckdb/duckdb/pull/18766
* Make `duckdb_log` return a TIMESTAMP_TZ by @Mytherin in https://github.com/duckdb/duckdb/pull/18768
* Revert "Use 1-based indexing for SQL-based JSON array extraction" by @Mytherin in https://github.com/duckdb/duckdb/pull/18758
* [CI] Adjust test configs post logger PR by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18771
* [Test Fix] Forward output to file by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18772
* Propagate `DUCKDB_*_VERSION` in extensions and tests by @Y-- in https://github.com/duckdb/duckdb/pull/18774
* Add `file_size_bytes` (de-)serialization by @lnkuiper in https://github.com/duckdb/duckdb/pull/18775
* Use microsecond resolution for printing the current timestamp by @Mytherin in https://github.com/duckdb/duckdb/pull/18776
* Improve error messages for merge / vector reference by @Mytherin in https://github.com/duckdb/duckdb/pull/18777
* Move row id logic to separate RowIdColumnData class instead of inlining it into the RowGroup by @Mytherin in https://github.com/duckdb/duckdb/pull/18780
* Treat ENABLE_EXTENSION_AUTOINSTALL as the BOOL that it is by @evertlammerts in https://github.com/duckdb/duckdb/pull/18778
* Add `memory_limit` parameter to `benchmark_runner`/`test_runner.py` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18790
* fix: improve speed of GetValue() for STRUCT type by @rustyconover in https://github.com/duckdb/duckdb/pull/18785
* Internal #3273: Parallel Window Masks by @hawkfish in https://github.com/duckdb/duckdb/pull/18731
* Task Scheduler: track exact task count, and re-signal on dequeue failure if there are tasks left by @Mytherin in https://github.com/duckdb/duckdb/pull/18792
* fix: coalesce query progress updates to reduce terminal writes by @rustyconover in https://github.com/duckdb/duckdb/pull/18672
* Support expressions as COPY file target by @Mytherin in https://github.com/duckdb/duckdb/pull/18795
* Remove everything python-package related by @evertlammerts in https://github.com/duckdb/duckdb/pull/18789
* Improve autocomplete suggestions by @Dtenwolde in https://github.com/duckdb/duckdb/pull/18773
* bump httpfs so it includes curl option by @Tmonster in https://github.com/duckdb/duckdb/pull/18691
* Issue #18767: Ignore Timestamp Offsets by @hawkfish in https://github.com/duckdb/duckdb/pull/18794
* Fixup progress_bar: avoid converting doubles into int32_t unchecked by @carlopi in https://github.com/duckdb/duckdb/pull/18800
* [chore] Fixup tidy-check on src/logging/log_manager.cpp by passing const & by @carlopi in https://github.com/duckdb/duckdb/pull/18801
* Internal #3273: Hashed Sort Callbacks by @hawkfish in https://github.com/duckdb/duckdb/pull/18796
* Typed macro parameters by @lnkuiper in https://github.com/duckdb/duckdb/pull/18786
* Fix some unindented interactions between `EMPTY_RESULT_PULLUP` and `MATERIALIZED` CTEs by @kryonix in https://github.com/duckdb/duckdb/pull/18805
* Add support for non-aggregate window functions by @Maxxen in https://github.com/duckdb/duckdb/pull/18788
* Expected errors 2053 by @hmeriann in https://github.com/duckdb/duckdb/pull/18810
* Test runner: Expand '{UUID}' into a random UUID by @carlopi in https://github.com/duckdb/duckdb/pull/18809
* Provide failing file name in Parquet reader error messages by @Mytherin in https://github.com/duckdb/duckdb/pull/18814
* [CI] install  libcurl4-openssl-dev with apt-get by @hmeriann in https://github.com/duckdb/duckdb/pull/18811
* fix: Add COLLATE NOCASE support to strpos function by @shivampr in https://github.com/duckdb/duckdb/pull/18819
* Add callback to get a list of copy options, use this to provide suggestions and to erase options from import that are only used during exporting by @Mytherin in https://github.com/duckdb/duckdb/pull/18812
* For BC reasons - keep VARINT as alias for BIGNUM by @Mytherin in https://github.com/duckdb/duckdb/pull/18821
* [Fix] Bug in fixed-size buffer when throwing out-of-memory by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18769
* Re-add accidentally removed check if copy_from is supported by @Mytherin in https://github.com/duckdb/duckdb/pull/18824
* Fix format-fix runs on Linux by @staticlibs in https://github.com/duckdb/duckdb/pull/18827
* Extensions.yml: Pass down save_cache to inner workflows by @carlopi in https://github.com/duckdb/duckdb/pull/18828
* Fix: Preserve database configuration flags for tab completion in DuckDB shell by @rustyconover in https://github.com/duckdb/duckdb/pull/18482
* Ensure a WAL file matches the DB file and checkpoint iteration by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18823
* fix: sanitize input for enable_logging by @samansmink in https://github.com/duckdb/duckdb/pull/18830
* fix: silence warnings about signed/unsigned conversions. by @rustyconover in https://github.com/duckdb/duckdb/pull/18835
* Avoid expensive checkpoints and write amplification by appending row groups, and limiting vacuum operations for the last number of row groups by @Mytherin in https://github.com/duckdb/duckdb/pull/18829
* Fix/run function in transaction by @Evannnnnnnn in https://github.com/duckdb/duckdb/pull/18741
* add appender to concurrent test by @c-herrewijn in https://github.com/duckdb/duckdb/pull/18721
* Add support for reading/writing native parquet geometry types by @Maxxen in https://github.com/duckdb/duckdb/pull/18832
* Don't notify Py pkg when override git describe is set by @evertlammerts in https://github.com/duckdb/duckdb/pull/18843
* Avoid printing '99 hours', given in most cases that means estimate is… by @carlopi in https://github.com/duckdb/duckdb/pull/18839
* Add the `VARIANT` LogicalType by @Tishj in https://github.com/duckdb/duckdb/pull/18609
* Document storage version flag in CLI + minor rendering fix by @Mytherin in https://github.com/duckdb/duckdb/pull/18841
* Ignore null verification for statistics on structs by @d-justen in https://github.com/duckdb/duckdb/pull/18813
* Add OnBeginExtensionLoad callback by @Mytherin in https://github.com/duckdb/duckdb/pull/18842
* Bump MySQL/Postgres/SQLite by @Mytherin in https://github.com/duckdb/duckdb/pull/18848
* Merge ossivalis into main by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18844
* Add test_env to unit tester by @pdet in https://github.com/duckdb/duckdb/pull/18847
* WAL <> DB File Match Fixes by @Mytherin in https://github.com/duckdb/duckdb/pull/18849
* Make ATTACH OR REPLACE atomic, keep list of used databases in MetaTransaction by @Mytherin in https://github.com/duckdb/duckdb/pull/18850
* Fix `NULL` path for `json_each`/`json_tree` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18852
* No more `wal_encryption` flag by @jeewonhh in https://github.com/duckdb/duckdb/pull/18851
* Bump Ducklake by @pdet in https://github.com/duckdb/duckdb/pull/18825
* Add more encryption modes CTR and CBC by @hannes in https://github.com/duckdb/duckdb/pull/18619
* Centralize attached database paths in a DatabaseFilePathManager which is shared across databases created through the same DBInstanceCache by @Mytherin in https://github.com/duckdb/duckdb/pull/18857
* Hold segment lock during GetColumnSegmentInfo by @Mytherin in https://github.com/duckdb/duckdb/pull/18859
* update duckdb azure extension ref for 1.4.0 by @benfleis in https://github.com/duckdb/duckdb/pull/18868
* Expected errors 2053 by @hmeriann in https://github.com/duckdb/duckdb/pull/18864
* Add a FORCE_DEBUG flag to force `-DDEBUG`, similar to FORCE_ASSERT by @Mytherin in https://github.com/duckdb/duckdb/pull/18872
* Bump & remove patches for delta, avro, excel, encodings, fts  by @samansmink in https://github.com/duckdb/duckdb/pull/18869
* [minor] Incompatible DB error message: add newline by @carlopi in https://github.com/duckdb/duckdb/pull/18861
* Bump mbedtls to v3.6.4 by @Mytherin in https://github.com/duckdb/duckdb/pull/18871
* Storage fuzzing + several fixes by @Mytherin in https://github.com/duckdb/duckdb/pull/18876
* Update ducdkb iceberg hash by @Tmonster in https://github.com/duckdb/duckdb/pull/18873
* [Test] Small fixes to concurrent attach/detach test by @taniabogatsch in https://github.com/duckdb/duckdb/pull/18862
* Internal #5796: Window Progress by @hawkfish in https://github.com/duckdb/duckdb/pull/18860
* Add `COPY (...) TO ... (FORMAT BLOB)` by @Maxxen in https://github.com/duckdb/duckdb/pull/18840
* Update spatial+vss+sqlsmith in preparation for v1.4 by @Maxxen in https://github.com/duckdb/duckdb/pull/18882
* Avoid automatically checkpointing if the database instance has been invalidated by @Mytherin in https://github.com/duckdb/duckdb/pull/18881
* Add `COPY (FORMAT BLOB)` to Andium too :^) by @Maxxen in https://github.com/duckdb/duckdb/pull/18884
* [C API] Result schema of prepared statements by @hrl20 in https://github.com/duckdb/duckdb/pull/18779
* Json: no reinterpret<size_t*> by @carlopi in https://github.com/duckdb/duckdb/pull/18886
* [Dev] Fix footgun in `string_t::SetSizeAndFinalize` by @Tishj in https://github.com/duckdb/duckdb/pull/18885
* [chore] Bump config test/configs/compressed_in_memory.json to new format by @carlopi in https://github.com/duckdb/duckdb/pull/18888
* bump aws and iceberg by @Tmonster in https://github.com/duckdb/duckdb/pull/18889
* Add rowsort to upsert_default.test by @jeewonhh in https://github.com/duckdb/duckdb/pull/18890
* fixing auto-specifying ciphers and remove double storage by @hannes in https://github.com/duckdb/duckdb/pull/18891
* Expected errors 2053 by @hmeriann in https://github.com/duckdb/duckdb/pull/18892
* Keep base data scan state alive in ColumnData::Update call by @Mytherin in https://github.com/duckdb/duckdb/pull/18893
* Add callback for when an extension fails to load, and also log this by @Mytherin in https://github.com/duckdb/duckdb/pull/18894
* Encryption now encoded as a bit, centralizing in set/getter by @carlopi in https://github.com/duckdb/duckdb/pull/18897
* Bump httpfs to v1.4-andium branch by @carlopi in https://github.com/duckdb/duckdb/pull/18898
* fix: refine query ETA display and Kalman filter stability by @rustyconover in https://github.com/duckdb/duckdb/pull/18880
* Bump inet & aws by @samansmink in https://github.com/duckdb/duckdb/pull/18899
* [chore] Fix amalgamation build in progress_bar by @carlopi in https://github.com/duckdb/duckdb/pull/18910
* Cannot create table from variant yet by @Mytherin in https://github.com/duckdb/duckdb/pull/18912
* In VerifyZeroReaders, get the header size from the buffer we are replacing instead of from the block manager by @Mytherin in https://github.com/duckdb/duckdb/pull/18909
* Fix #18152: avoid auto-detecting hive partitioning with COPY .. FROM by @Mytherin in https://github.com/duckdb/duckdb/pull/18911
* CLI: Correctly move to start of line by @Mytherin in https://github.com/duckdb/duckdb/pull/18920
* Strip question mark parameters from default temporary directory by @Mytherin in https://github.com/duckdb/duckdb/pull/18915
* Move Hash Zero CI run to nightly by @Mytherin in https://github.com/duckdb/duckdb/pull/18925
* Bump Iceberg by @Tmonster in https://github.com/duckdb/duckdb/pull/18917
* Issue template: Add the Python repository by @szarnyasg in https://github.com/duckdb/duckdb/pull/18928
* fix extension size increase by @samansmink in https://github.com/duckdb/duckdb/pull/18923
* [Dev] Fix reference of uninitialized memory in Variant conversion first pass by @Tishj in https://github.com/duckdb/duckdb/pull/18921
* Bump DuckLake to Latest Main by @pdet in https://github.com/duckdb/duckdb/pull/18926
* Make row-group metadata re-use experimental for now by @Mytherin in https://github.com/duckdb/duckdb/pull/18922
* Fix exception propagation in C API  by @mlafeldt in https://github.com/duckdb/duckdb/pull/18924
* Bump httpfs by @carlopi in https://github.com/duckdb/duckdb/pull/18930
* Bump ducklake and don't write empty bbox in geoparquet stats by @Maxxen in https://github.com/duckdb/duckdb/pull/18936
* [PROFILING] Fix EXPLAIN ANALYZE returning empty results when PRAGMA enabled_profiling = 'no_output' by @maiadegraaf in https://github.com/duckdb/duckdb/pull/18935
* Http_util can return success for all [200, 300) responses, as well as redirects by @Tmonster in https://github.com/duckdb/duckdb/pull/18940
* Fix TransformStringToLogicalType for enums arrays by @tdoehmen in https://github.com/duckdb/duckdb/pull/18941
* [unittester] Allow overriding data/ folder to custom location by @carlopi in https://github.com/duckdb/duckdb/pull/18929
* Unpin fixed-size sorting keys by @lnkuiper in https://github.com/duckdb/duckdb/pull/18945
* Add missing parameters to `COPY ... (FORMAT JSON)` by @lnkuiper in https://github.com/duckdb/duckdb/pull/18946
* Fixes for encrypted database, make cross-engine encryption work, and expand testing by @hannes in https://github.com/duckdb/duckdb/pull/18951
* fix windows linking issue ducklake by @samansmink in https://github.com/duckdb/duckdb/pull/18953
* bump iceberg by @Tmonster in https://github.com/duckdb/duckdb/pull/18957
* [SQLLogicTest] Detect errors thrown in `LoadExtension` of the `require` statement by @Tishj in https://github.com/duckdb/duckdb/pull/18950
* Don't use `VectorOperations::Copy` for string dictionary hashes by @lnkuiper in https://github.com/duckdb/duckdb/pull/18949
* Fix error reporting in SSLClient by @staticlibs in https://github.com/duckdb/duckdb/pull/18958
* bump spatial by @Maxxen in https://github.com/duckdb/duckdb/pull/18961
* Allow extensions to customize ATTACH OR REPLACE conflict behavior by @ywelsch in https://github.com/duckdb/duckdb/pull/18962
* Unify test runner keyword replacement, and don't run `LOAD [ext]` by default by @Mytherin in https://github.com/duckdb/duckdb/pull/18963
* [chore] Bump httpfs and remove patches by @carlopi in https://github.com/duckdb/duckdb/pull/18965
* Correctly update row group data pointers and root table pointer after checkpoint by @Mytherin in https://github.com/duckdb/duckdb/pull/18966
* Attach: Cleanup duplicate data path handling, and make IF NOT EXISTS no longer abort if we are adding a path with the same name by @Mytherin in https://github.com/duckdb/duckdb/pull/18974
* Bump DuckLake and HTTPFS by @pdet in https://github.com/duckdb/duckdb/pull/18975
* Issue #18971: Empty Unsorted Windows by @hawkfish in https://github.com/duckdb/duckdb/pull/18976
* Check context.interrupted flag in table scan by @Mytherin in https://github.com/duckdb/duckdb/pull/18981
* Only return cgroup memory limit if it's a sane value by @szarnyasg in https://github.com/duckdb/duckdb/pull/18668
* Macro fixes by @lnkuiper in https://github.com/duckdb/duckdb/pull/18992
* ATTACH IF NOT EXISTS - wait until database is fully attached before returning by @Mytherin in https://github.com/duckdb/duckdb/pull/18993
* WALReplay Fix: In UpdateColumn, no longer assume all updates are part of the same vector, but instead verify this and batch updates per vector by @Mytherin in https://github.com/duckdb/duckdb/pull/18999
* Bump iceberg by @Tmonster in https://github.com/duckdb/duckdb/pull/19001

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.3.2...v1.4.0
## Project: [trinodb/trino](https://trino.io/docs/current/release/release-{release}.html), 1 releases: ['Trino 477']
### Release: trino [Trino 477](https://github.com/trinodb/trino/releases/tag/477)
See https://trino.io/docs/current/release/release-477.html
## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers), 2 releases: ['v0.8.1', 'v0.8.0']
### Release: datafusion-table-providers [v0.8.1](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.8.1)
## What's Changed
* Improve the read performance of Postgres' Decimals by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/438


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.8.0...v0.8.1
### Release: datafusion-table-providers [v0.8.0](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.8.0)
## What's Changed
* Bump uuid from 1.17.0 to 1.18.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/417
* Bump rand from 0.9.1 to 0.9.2 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/415
* Bump rstest from 0.25.0 to 0.26.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/414
* Bump dyn-clone from 1.0.19 to 1.0.20 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/413
* Bump prost from 0.13.5 to 0.14.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/412
* ClickHouse: Add python module  by @trueleo in https://github.com/datafusion-contrib/datafusion-table-providers/pull/418
* Upgrade datafusion to version 50 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/437


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.7.0...v0.8.0
