# Complete List of Projects
 * Project: posit-dev/py-shiny has 1 releases
 * Project: narwhals-dev/narwhals has 1 releases
 * Project: pola-rs/polars has 3 releases
 * Project: pandas-dev/pandas has 2 releases
 * Project: holoviz/panel has 2 releases
 * Project: holoviz/hvplot has 1 releases
 * Project: holoviz/holoviews has 1 releases
 * Project: cython/cython has 1 releases
 * Project: plotly/dash has 2 releases
 * Project: dask/dask has 1 releases
 * Project: delta-io/delta-rs has 1 releases
 * Project: rapidsai/cudf has 1 releases
 * Project: lancedb/lance has 14 releases
 * Project: lancedb/lancedb has 12 releases
 * Project: datafusion-contrib/datafusion-table-providers has 4 releases
 * Project: duckdb/duckdb has 1 releases
 * Project: trinodb/trino has 1 releases
 * Project: datafusion-contrib/datafusion-table-providers has 4 releases
 * Project: unionai-oss/pandera has 1 releases
 * Project: https://spark.apache.org/news/index.html has 1 releases
 * Project: https://velox-lib.io/blog/rss.xml has 1 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 2 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 1 articles
### Release: [Spark 4.1.0 released](https://spark.apache.org/news/spark-4-1-0-released.html)

## Project: [Velox Blog](https://velox-lib.io/blog), 1 articles
### Release: [Why Sort is row-based in Velox — A Quantitative Assessment](https://velox-lib.io/blog/why-row-based-sort)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 2 articles
### Release: [Optimizing Repartitions in DataFusion: How I Went From Database Noob to Core Contribution](https://datafusion.apache.org/blog/2025/12/15/avoid-consecutive-repartitions)

### Release: [Apache DataFusion Comet 0.12.0 Release](https://datafusion.apache.org/blog/2025/12/04/datafusion-comet-0.12.0)

## Project: [posit-dev/py-shiny](https://shiny.posit.co/py/), 1 releases: ['shiny 1.5.1']
### Release: py-shiny [shiny 1.5.1](https://github.com/posit-dev/py-shiny/releases/tag/v1.5.1)
### New features

* Added toast notification system with `ui.toast()`, `ui.toast_header()`, `ui.show_toast()`, and `ui.hide_toast()`. Toast notifications are temporary, non-intrusive messages that support multiple semantic types (success, warning, error, etc.), flexible positioning (9 positions: top/middle/bottom × left/center/right), auto-hide with configurable duration, optional headers with icons, and programmatic control. (#2111)

* Added a new `input_submit_textarea()` input element, which is similar to `input_text_area()`, but includes a submit button to only submit the text changes to the server on click. This is especially useful when the input text change triggers a long-running operation and/or the user wants to type longer-form input and review it before submitting it. (#2099)

### Bug fixes

* Fixed `ui.tooltip()`'s `options` parameter to properly pass Bootstrap tooltip options to the underlying web component. (#2101)

* Fixed an issue where `session.bookmark()` would error when non-existent `input` values are read. (#2117)

* Revised `accordion()`'s `open` logic to close all panels when an empty list is passed. (#2109)
## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 1 releases: ['Narwhals v2.14.0']
### Release: narwhals [Narwhals v2.14.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.14.0)
## Changes

## ✨ Enhancements

- feat: add list aggregate methods (#3332)
- feat: Add `{Expr,Series}.any_value` (#3315)
- enh: Add support for `slice(None)` in series getitem (#3342)

## 🐞 Bug fixes

- test: fix median tests for list.agg methods (#3354)
- fix: `ArrowSeries.fill_null(strategy=..., limit=...)` and `None` at the "edge"  (#3335)

## 📖 Documentation

- docs: API Completeness overhaul (#3285)
- docs: updated contributing with test_plugin install (#3345)

## 🛠️ Other improvements

- refactor: making _compliant selectors public (#3346)
- chore: Add project classifiers in pyproject.toml (#3306)
- fix: `is_ordered_categorical` doctest (#3348)
- make CompliantExprNameNamespace public (#3344)
- ci: Adjust based on polars 1.36 pre-release (#3343)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @dependabot[bot], @hoxbro, @raisadz, @ym-pett and [dependabot[bot]](https://github.com/apps/dependabot)

## Project: [pola-rs/polars](https://docs.pola.rs/), 3 releases: ['Python Polars 1.36.1', 'Python Polars 1.36.0', 'Python Polars 1.36.0-beta.2']
### Release: polars [Python Polars 1.36.1](https://github.com/pola-rs/polars/releases/tag/py-1.36.1)
## 🚀 Performance improvements

- Tune partitioned sink\_parquet cloud performance (#25687)

## ✨ Enhancements

- Allow creation of `Object` literal (#25690)
- Don't collect schema in SQL union processing (#25675)

## 🐞 Bug fixes

- Don't invalidate node in cluster-with-columns (#25714)
- Move `boto3` extra from s3fs in dev requirements (#25667)
- Add missing type stubs for `bin_slice`, `bin_head`, and `bin_tail` (#25697)
- Binary slice methods missing from Series and docs (#25683)
- Mix-up of variable\_name/value\_name in unpivot (#25685)
- Invalid usage of `drop_first` in `to_dummies` when nulls present (#25435)

## 📖 Documentation

- Fix typos in Excel and Pandas migration guides (#25709)
- Add "right" to `how` options in `join()` docstrings (#25678)

## 🛠️ Other improvements

- Move Object `lit` fix earlier in the function (#25713)
- Remove unused decimal file (#25701)
- Move `boto3` extra from s3fs in dev requirements (#25667)
- Upgrade to latest version of `sqlparser-rs` (#25673)
- Update slab to version without RUSTSEC (#25686)
- Fix typo (#25684)

Thank you to all our contributors for making this release possible!
@AndreaBozzo, @Kevin-Patyk, @alexander-beedie, @dsprenkels, @jamesfricker, @mcrumiller, @nameexhaustion, @orlp and @ritchie46

### Release: polars [Python Polars 1.36.0](https://github.com/pola-rs/polars/releases/tag/py-1.36.0)
🏆 Highlights
- Add Extension types (#25322)

## ✨ Enhancements

- Add SQL support for the QUALIFY clause (#25652)
- Add bin.slice(), bin.head(), and bin.tail() methods (#25647)
- Add SQL syntax support for CROSS JOIN UNNEST(col) (#25623)
- Add separate env var to log tracked metrics (#25586)
- Expose fields for generating physical plan visualization data (#25562)
- Allow pl.Object in pivot value (#25533)
- Minor improvement for as_struct repr (#25529)
- Temporal quantile in rolling context (#25479)
- Add quantile for missing temporals (#25464)
- Add strict parameter to pl.concat(how='horizontal') (#25452)
- Support decimals in search_sorted (#25450)
- Expose and document pl.Categories (#25443)
- Use reference to Graph pipes when flushing metrics (#25442)
- Extend SQL UNNEST support to handle multiple array expressions (#25418)
- Add SQL support for ROW_NUMBER, RANK, and DENSE_RANK functions (#25409)
- Allow elementwise Expr.over in aggregation context (#25402)
- Add SQL support for named WINDOW references (#25400)
- Add leftmost option to str.replace_many / str.find_many / str.extract_many (#25398)
- Automatically Parquet dictionary encode floats (#25387)
- Support unique_counts for all datatypes (#25379)
- Add maintain_order to Expr.mode (#25377)
- Allow hash for all List dtypes (#25372)
- Add empty_as_null and keep_nulls to {Lazy,Data}Frame.explode (#25369)
- Display function of streaming physical plan map node (#25368)
- Allow slice on scalar in aggregation context (#25358)
- Allow implode and aggregation in aggregation context (#25357)
- Move GraphMetrics into StreamingQuery (#25310)
- Documentation on Polars Cloud manifests (#25295)
- Add empty_as_null and keep_nulls flags to Expr.explode (#25289)
- Allow Expr.unique on List/Array with non-numeric types (#25285)
- Raise suitable error on non-integer "n" value for clear (#25266)
- Allow Expr.rolling in aggregation contexts (#25258)
- Allow bare .row() on a single-row DataFrame, equivalent to .item() on a single-element DataFrame (#25229)
- Support additional forms of SQL CREATE TABLE statements (#25191)
- Add support for Float16 dtype (#25185)
- Support column-positional SQL "UNION" operations (#25183)
- Add unstable `Schema.to_arrow()` (#25149)
- Make DSL-hash skippable (#25140)
- Improve error message on unsupported SQL subquery comparisons (#25135)
- Support arbitrary expressions in SQL `JOIN` constraints (#25132)
- Allow arbitrary expressions as the `Expr.rolling` `index_column` (#25117)
- Set polars/<version> user-agent (#25112)
- Support `ewm_var/std` in streaming engine (#25109)
- Rewrite `IR::Scan` to `IR::DataFrameScan` in `expand_datasets` when applicable (#25106)
- Add ignore_nulls to first / last (#25105)
- Allow arbitrary Expressions in "subset" parameter of `unique` frame method (#25099)
- Add `BIT_NOT` support to the SQL interface (#25094)
- Streaming `{Expr,LazyFrame}.rolling` (#25058)
- Add LazyFrame.pivot (#25016)
- Add SQL support for `LEAD` and `LAG` functions (#23956)
- Add having to group_by context (#23550)
- Add show methods for DataFrame and LazyFrame (#19634)

## 🚀 Performance improvements

- Set parallelization threshold in `take_unchecked_impl` (#25672)
- New single file IO sink pipeline enabled for sink_parquet (#25670)
- Correct overly eager local predicate insertion for unpivot (#25644)
- New partitioned IO sink pipeline enabled for sink_parquet (#25629)
- Use strong hash instead of traversal for CSPE equality (#25537)
- Reduce HuggingFace API calls (#25521)
- Fix panic in is_between support in streaming Parquet predicate push down (#25476)
- Faster kernels for rle_lengths (#25448)
- Mark output of more non-order-maintaining ops as unordered (#25419)
- Enable predicate expressions on unsigned integers (#25416)
- Allow detecting plan sortedness in more cases (#25408)
- Add parquet prefiltering for string regexes (#25381)
- Fast find start window in group_by_dynamic with large offset (#25376)
- Use fast path for agg_min/agg_max when nulls present (#25374)
- Add streaming native LazyFrame.group_by_dynamic (#25342)
- Fuse positive slice into streaming LazyFrame.rolling (#25338)
- Mark Expr.reshape((-1,)) as row separable (#25326)
- Return references from aexpr_to_leaf_names_iter (#25319)
- Use bitmap instead of Vec<bool> in first/last w. skip_nulls (#25318)
- Lazy gather for `{forward,backward}_fill` in group-by contexts (#25115)
- Add streaming sorted Group-By (#25013)

## 🐞 Bug fixes

- Rechunk on nested dtypes in take_unchecked_impl parallel path (#25662)
- Fix streaming SchemaMismatch panic on list.drop_nulls (#25661)
- Fix panic on Boolean rolling_sum calculation for list or array eval (#25660)
- Fix "dtype is unknown" panic in cross joins with literals (#25658)
- Fix panic edge-case when scanning hive partitioned data (#25656)
- Fix "unreachable code" panic in UDF dtype inference (#25655)
- Address potential "batch_size" parameter collision in scan_pyarrow_dataset (#25654)
- Fix empty format handling (#25638)
- Improve SQL GROUP BY and ORDER BY expression resolution, handling aliasing edge-cases (#25637)
- Preserve List inner dtype during chunked take operations (#25634)
- Fix lifetime for AmortSeries lazy group iterator (#25620)
- Fix spearman panicking on nulls (#25619)
- Properly resolve HAVING clause during SQL GROUP BY operations (#25615)
- Prevent false positives in is_in for large integers (#25608)
- Differentiate between empty list an no list for unpivot (#25597)
- Bug in boolean unique_counts (#25587)
- Hang in multi-chunk DataFrame .rows() (#25582)
- Correct arr_to_any_value for object arrays (#25581)
- Have PySeries::new_f16 receive pf16s instead of f32s (#25579)
- Set Float16 parquet schema type to Float16 (#25578)
- Fix incorrect .list.eval after slicing operations (#25540)
- Strict conversion AnyValue to Struct (#25536)
- Rolling mean/median for temporals (#25512)
- Add .rolling_rank() support for temporal types and pl.Boolean (#25509)
- Fix occurence of exact matches of .join_asof(strategy="nearest", allow_exact_matches=False, ...) (#25506)
- Always respect return_dtype in map_elements and map_rows (#25504)
- Fix group lengths check in sort_by with AggregatedScalar (#25503)
- Fix dictionary replacement error in write_ipc() (#25497)
- Fix expr slice pushdown causing shape error on literals (#25485)
- Allow empty list in sort_by in list.eval context (#25481)
- Raise error on out-of-range dates in temporal operations (#25471)
- Validate list.slice parameters are not lists (#25458)
- Make sum on strings error in group_by context (#25456)
- Prevent panic when joining sorted LazyFrame with itself (#25453)
- Apply CSV dict overrides by name only (#25436)
- Incorrect result in aggregated first/last with ignore_nulls (#25414)
- Fix off-by-one bug in `ColumnPredicates` generation for inequalities operating on integer columns (#25412)
- Use Cargo.template.toml to prevent git dependencies from using template (#25392)
- Fix arr.{eval,agg} in aggregation context (#25390)
- Support AggregatedList in list.{eval,agg} context (#25385)
- Nested dtypes in streaming first_non_null/last_non_null (#25375)
- Remove Expr casts in pl.lit invocations (#25373)
- Optimize projection pushdown through HConcat (#25371)
- Revert pl.format behavior with nulls (#25370)
- Correct eq_missing for struct with nulls (#25363)
- Resolve edge-case with SQL aggregates that have the same name as one of the GROUP BY keys (#25362)
- Unique on literal in aggregation context (#25359)
- Aggregation with drop_nulls on literal (#25356)
- SQL NATURAL joins should coalesce the key columns (#25353)
- Mark {forward,backward}_fill as length_preserving (#25352)
- Correct drop_items for scalar input (#25351)
- Schema mismatch with list.agg, unique and scalar (#25348)
- AnyValue::to_physical for categoricals (#25341)
- Bugs in pl.from_repr with signed exponential floats and line wrapping (#25331)
- Remove ClosableFile (#25330)
- Increase precision when constructing `float` Series (#25323)
- Fix link errors reported by markdown-link-check (#25314)
- Parquet is_in for mixed validity pages (#25313)
- Fix building polars-plan with features lazy,concat_str (but no strings) (#25306)
- Fix building polars-mem-engine with the async feature (#25300)
- Nested dtypes in streaming first/last (#25298)
- Fix length preserving check for eval expressions in streaming engine (#25294)
- Panic exception when calling Expr.rolling in .over (#25283)
- Don't quietly allow unsupported SQL SELECT clauses (#25282)
- Reverse on chunked struct (#25281)
- Correct {first,last}_non_null if there are empty chunks (#25279)
- Incorrect results for aggregated {n_,}unique on bools (#25275)
- Run async DB queries with regular asyncio if not inside a running loop (#25268)
- Fix small bug with `PyExpr` to `PyObject` conversion (#25265)
- Fix building polars-expr without timezones feature (#25254)
- Correctly prune projected columns in hints (#25250)
- Address multiple issues with SQL OVER clause behaviour for window functions (#25249)
- Allow Null dtype values in scatter (#25245)
- Make str.json_decode output deterministic with lists (#25240)
- Correct handle requested stops in streaming shift (#25239)
- Use (i64, u64) for VisualizationData (offset, length) slices (#25203)
- Fix serialization of lazyframes containing huge tables (#25190)
- Fix single-column CSV header duplication with leading empty lines (#25186)
- Enhanced column resolution/tracking through multi-way SQL joins (#25181)
- Fix `format_str` in case of multiple chunks (#25162)
- Handle some unusual `pl.col.<colname>` edge-cases (#25153)
- Fix incorrect reshape on sliced lists (#25139)
- Support "index" as column name in `group_by` iterator (#25138)
- Fix panic in `dt.truncate` for invalid duration strings (#25124)
- DSL_SCHEMA_HASH should not changed by line endings (#25123)
- Don't trigger `DeprecationWarning` from SQL "IN" constraints that use subqueries (#25111)
- Solve multiple issues relating to arena mutation in SQL subqueries (#25110)
- Return the correct string-case `Expr` reprs (#25101)
- Fix `groups` update on slices with different offsets (#25097)
- Unique key names in streaming sort/top_k (#25082)
- Fix CSV `select(len())` off by 1 with comment prefix (#25069)
- Raise error for all/any on list instead of panic (#25018)
- Ensure out-of-range integers and other edge case values don't give wrong results for index_of() (#24369)
- Improve SQL UNNEST behaviour (#22546)

## 📖 Documentation

- Document schema parameter in meta methods (#25543)
- Correct link to datetime_range instead of date_range in resampling page (#25532)
- Remove lzo from parquet write options (#25522)
- Deprecate Categorical functions for lexical ordering and local checks (#25514)
- Update LazyFrame.collect_schema() docstring (#25508)
- Update on-premise documentation (#25489)
- Add LazyFrame.pivot to reference guide (#25482)
- Fix incorrect 'bitwise' in any_horizontal/all_horizontal docstring (#25469)
- Add docstring example showing str.slice taking Expression params (#25461)
- Add Extension and BaseExtension to doc index (#25444)
- Add polars-on-premise documentation (#25431)
- Add having API references (#25428)
- Explain aggregation & sorting of lists (#25260)
- Fix LanceDB URL (#25198)
- Update user guide for QueryProgress rename to QueryProfile (#25195)
- Update `LazyFrame.remote` signature (#25175)
- Fix source path (#25170)
- Fix non-existent `replace_all` reference in `replace` docs (#25161)
- Mention Narwhals in ecosystem page (#25100)
- Clarify bitwise behaviour of `and_`, `or_`, and `not_` Expressions on integer columns (#25092)

## 🧪 Tests

- Add reliable test for `pl.format` on multiple chunks (#25164)

## 🔧 CI

- Avoid relabelling changes-dsl on every commit (#25216)
- Automatically label pull requests that change the DSL (#25177)

## 🏗️ Build system

- Fix `make fmt` and `make lint` commands (#25200)
- Make building the docs on macOS more reliable (#25095)

## 🛠️ Other improvements

- Add "panic" and "streaming" tagging to issue-labeler workflow (#25657)
- Use dtype for group_aware evaluation on ApplyExpr (#25639)
- Ensure literal-only SELECT broadcast conforms to SQL semantics (#25633)
- Ensure we hash all attributes and visit all children in traverse_and_hash_aexpr (#25627)
- Rename polars-on-premise to polars-on-premises (#25617)
- Constrain new issue-labeler workflow to the Issue title (#25614)
- Avoid rechunk requirement for Series.iter() (#25603)
- Help categorise Issues by automatically applying labels (using the same patterns used for labelling PRs) (#25599)
- Add disk-cleaning step for Ubuntu runners (#25593)
- Show on streaming engine (#25589)
- Ignore a couple of unexplained typing errors (#25580)
- Skip existing files in pypi upload (#25576)
- Fix template path in release-python workflow (#25565)
- Add asserts and tests for list.eval on multiple chunks with slicing (#25559)
- Skip rust integration tests for coverage in CI (#25558)
- Add Final type-qualifier to module-level constants (#25556)
- Print expected DSL schema hashes if mismatched (#25526)
- Update partitioned sink IR (#25524)
- Fix --uv argument for benchmark-remote (#25513)
- Add `proptest` `AnyValue` strategies (#25510)
- Fix rolling kernel dispatch with monotonic group attribute (#25494)
- Fix feature gating TZ_AWARE_RE again (#25493)
- Run maturin with --uv option (#25490)
- Add proptest DataFrame strategy (#25446)
- Add some cleanup (#25445)
- Add assert_sql_matches coverage for SQL DISTINCT and DISTINCT ON syntax (#25440)
- Test for group_by(...).having(...) (#25430)
- Remove aggregation context Context (#25424)
- Remove debug file write from test suite (#25393)
- Remove unused import (#25365)
- Enable more streaming tests (#25364)
- Dispatch Series.set to zip_with_same_dtype (#25327)
- Remove Column::Partitioned (#25324)
- Add toolchain file to runtimes for sdist (#25311)
- Fix typo in CI release workflow (#25309)
- Refactor sink IR (#25308)
- Directly take CloudScheme in parse_cloud_options() (#25304)
- Remove PyPartitioning (#25303)
- Simplify sink parameter passing from Python (#25302)
- Better coverage for group_by aggregations (#25290)
- Use dedicated runtime packages from template (#25284)
- Add test for unique with column subset (#25241)
- Fix Decimal precision annotation (#25227)
- Refactor dt_range functions (#25225)
- Add `proptest` strategies for Series nested types (#25220)
- Update markdown link checker (#25201)
- Add ElementExpr for _eval expressions (#25199)
- Upgraded `ruff` and `typos` and made the necessary lint updates (#25196)
- Make python docs build again (#25165)
- Upgrade to schemars 0.9.0 (#25158)
- Update versions (#25141)
- Silence unused mut warning (#25093)
- Add `proptest` strategies for Series logical types (#24849)

## ♻️ Refactoring

- Make polars-plan constants more consistent (#25645)
- Add support for multi-column reductions (#25640)
- Simplify _write_any_value (#25622)
- Add parquet file write pipeline for new IO sinks (#25618)
- Add streaming IO sink components (#25594)
- Add `arg_sort()` and `Writeable::as_buffered()` (#25583)
- Take task priority argument in `parallelize_first_to_local` (#25563)
- Rename `URL_ENCODE_CHARSET` to `HIVE_ENCODE_CHARSET` (#25554)
- Remove verbose prints on file opens (#25523)
- Remove some dead argminmax impl code (#25501)
- Take `sync` parameter in `Writeable::close()` (#25475)
- Fix unsoundness in ChunkedArray::{first, last} (#25449)
- Take `&dyn Any` instead of `Box<dyn Any>` in python object converters (#25421)
- Accept multiple files in `pipe_with_schema` (#25388)
- Add oneshot channel to polars-stream (#25378)
- Remove incorrect cast in reduce code (#25321)
- Clean up CSPE callsite (#25215)
- Move ewm variance code to polars-compute (#25188)
- Make `pipe_with_schema` work on Arced schema (#25155)
- Remove lower_ir conversion from Scan to InMemorySource (#25150)
- Add functions for `scan_lines` (#25136)
- Remove unused `optimization_toggle` (#25130)
- Support for named/anonymous aggregations (#25118)
- Remove old join projection pushdown logic (#25088)
- Remove unused row-count (#25080)
- Add IR for `scan_lines` (#25066)
- Add stateful `EwmCov` kernel (#25065)
- Move `EwmMeanState` to `polars-compute` (#25034)
- Move asof `tolerance` type coercion to IR conversion (#25033)
- Move supertype determination and casting to IR for `date_range` and related functions (#24084)


Thank you to all our contributors for making this release possible!
@AndreaBozzo, @DannyStoll1, @EndPositive, @JakubValtar, @Jesse-Bakker, @Kevin-Patyk, @MarcoGorelli, @TNieuwdorp, @Voultapher, @alexander-beedie, @borchero, @c-peters, @cBournhonesque, @camriddell, @carnarez, @cmdlineluser, @coastalwhite, @cr7pt0gr4ph7, @davanstrien, @davidia, @dsprenkels, @etiennebacher, @feliblo, @guilhem-dvr, @itamarst, @jannickj, @jetuk, @kdn36, @lun3x, @marinegor, @mcrumiller, @nameexhaustion, @orlp, @pomo-mondreganto, @ritchie46, @vyasr, @wtn, and more!

### Release: polars [Python Polars 1.36.0-beta.2](https://github.com/pola-rs/polars/releases/tag/py-1.36.0-beta.2)
## 🏆 Highlights

- Add Extension types (#25322)

## ✨ Enhancements

- Add SQL support for `ROW_NUMBER`, `RANK`, and `DENSE_RANK` functions (#25409)
- Add SQL support for named `WINDOW` references (#25400)
- Add `BIT_NOT` support to the SQL interface (#25094)
- Add `LazyFrame.pivot` (#25016)
- Add `allow_empty` flag to `item` (#25048)
- Add `empty_as_null` and `keep_nulls` flags to `Expr.explode` (#25289)
- Add `empty_as_null` and `keep_nulls` to `{Lazy,Data}Frame.explode` (#25369)
- Add `having` to `group_by` context (#23550)
- Add `ignore_nulls` to `first` / `last` (#25105)
- Add `maintain_order` to `Expr.mode` (#25377)
- Add `quantile` for missing temporals (#25464)
- Add leftmost option to `str.replace_many / str.find_many / str.extract_many` (#25398)
- Add strict parameter to pl.concat(how='horizontal') (#25452)
- Add support for `Float16` dtype (#25185)
- Add unstable `Schema.to_arrow` (#25149)
- Allow `Expr.rolling` in aggregation contexts (#25258)
- Allow `Expr.unique` on `List`/`Array` with non-numeric types (#25285)
- Allow `glimpse` to return a `DataFrame` (#24803)
- Allow `hash` for all `List` dtypes (#25372)
- Allow `implode` and aggregation in aggregation context (#25357)
- Allow `slice` on scalar in aggregation context (#25358)
- Allow arbitrary Expressions in "subset" parameter of `unique` frame method (#25099)
- Allow arbitrary expressions as the `Expr.rolling` `index_column` (#25117)
- Allow bare `.row` on a single-row DataFrame, equivalent to `.item` on a single-element DataFrame (#25229)
- Allow elementwise `Expr.over` in aggregation context (#25402)
- Allow pl.Object in pivot value (#25533)
- Automatically Parquet dictionary encode floats (#25387)
- Display function of streaming physical plan `map` node (#25368)
- Documentation on Polars Cloud manifests (#25295)
- Expose and document pl.Categories (#25443)
- Expose fields for generating physical plan visualization data (#25562)
- Extend SQL `UNNEST` support to handle multiple array expressions (#25418)
- Improve SQL `UNNEST` behaviour (#22546)
- Improve error message on unsupported SQL subquery comparisons (#25135)
- Make DSL-hash skippable (#25140)
- Minor improvement for `as_struct` repr (#25529)
- Move GraphMetrics into StreamingQuery (#25310)
- Raise suitable error on non-integer "n" value for `clear` (#25266)
- Rewrite `IR::Scan` to `IR::DataFrameScan` in `expand_datasets` when applicable (#25106)
- Set polars/<version> user-agent (#25112)
- Streaming `{Expr,LazyFrame}.rolling` (#25058)
- Support BYTE_ARRAY backed Decimals in Parquet (#25076)
- Support `ewm_var/std` in streaming engine (#25109)
- Support `unique_counts` for all datatypes (#25379)
- Support additional forms of SQL "CREATE TABLE" statements (#25191)
- Support arbitrary expressions in SQL `JOIN` constraints (#25132)
- Support column-positional SQL "UNION" operations (#25183)
- Support decimals in search_sorted (#25450)
- Temporal `quantile` in rolling context (#25479)
- Use reference to Graph pipes when flushing metrics (#25442)

## 🚀 Performance improvements

- Add parquet prefiltering for string regexes (#25381)
- Add streaming native `LazyFrame.group_by_dynamic` (#25342)
- Add streaming sorted Group-By (#25013)
- Allow detecting plan sortedness in more cases (#25408)
- Don't recompute full rolling moment window when NaNs/nulls leave the window (#25078)
- Enable predicate expressions on unsigned integers (#25416)
- Fast find start window in `group_by_dynamic` with large `offset` (#25376)
- Faster kernels for rle_lengths (#25448)
- Fuse positive `slice` into streaming `LazyFrame.rolling` (#25338)
- Lazy gather for `{forward,backward}_fill` in group-by contexts (#25115)
- Mark `Expr.reshape((-1,))` as row separable (#25326)
- Mark output of more non-order-maintaining ops as unordered (#25419)
- Optimize ipc stream read performance (#24671)
- Reduce HuggingFace API calls (#25521)
- Return references from `aexpr_to_leaf_names_iter` (#25319)
- Skip filtering scan IR if no paths were filtered (#25037)
- Use bitmap instead of Vec<bool> in first/last w. skip_nulls (#25318)
- Use fast path for `agg_min`/`agg_max` when nulls present (#25374)
- Use strong hash instead of traversal for CSPE equality (#25537)

## 🐞 Bug fixes

- Add `.rolling_rank` support for temporal types and `pl.Boolean` (#25509)
- Address issues with SQL `OVER` clause behaviour for window functions (#25249)
- Aggregation with `drop_nulls` on literal (#25356)
- Allow `Null` dtype values in `scatter` (#25245)
- Allow broadcast in `group_by` for `ApplyExpr` and `BinaryExpr` (#25053)
- Allow empty list in `sort_by` in `list.eval` context (#25481)
- Allow for negative time in `group_by_dynamic` iterator (#25041)
- Always respect return_dtype in map_elements and map_rows (#25504)
- AnyValue::to_physical for categoricals (#25341)
- Apply CSV dict overrides by name only (#25436)
- Block predicate pushdown when `group_by` key values are changed (#25032)
- Bugs in pl.from_repr with signed exponential floats and line wrapping (#25331)
- Correct `drop_items` for scalar input (#25351)
- Correct `eq_missing` for struct with nulls (#25363)
- Correct `{first,last}_non_null` if there are empty chunks (#25279)
- Correct handle requested stops in streaming shift (#25239)
- Correctly prune projected columns in hints (#25250)
- DSL_SCHEMA_HASH should not changed by line endings (#25123)
- Don't push down predicates passed inserted cache nodes (#25042)
- Don't quietly allow unsupported SQL `SELECT` clauses (#25282)
- Don't trigger `DeprecationWarning` from SQL "IN" constraints that use subqueries (#25111)
- Enhanced column resolution/tracking through multi-way SQL joins (#25181)
- Ensure SQL table alias resolution checks against CTE aliases on fallback (#25071)
- Ensure out-of-range integers and other edge case values don't give wrong results for index_of (#24369)
- Fix CSV `select(len)` off by 1 with comment prefix (#25069)
- Fix `arr.{eval,agg}` in aggregation context (#25390)
- Fix `format_str` in case of multiple chunks (#25162)
- Fix `groups` update on slices with different offsets (#25097)
- Fix assertion panic on `group_by` (#25179)
- Fix building polars-expr without timezones feature (#25254)
- Fix building polars-mem-engine with the async feature (#25300)
- Fix building polars-plan with features lazy,concat_str (but no strings) (#25306)
- Fix dictionary replacement error in `write_ipc` (#25497)
- Fix expr slice pushdown causing shape error on literals (#25485)
- Fix field metadata for nested categorical PyCapsule export (#25052)
- Fix group lengths check in `sort_by` with `AggregatedScalar` (#25503)
- Fix handling `Null` dtype in `ApplyExpr` on `group_by` (#25077)
- Fix incorrect `.list.eval` after slicing operations (#25540)
- Fix incorrect reshape on sliced lists (#25139)
- Fix length preserving check for `eval` expressions in streaming engine (#25294)
- Fix occurence of exact matches of `.join_asof(strategy="nearest", allow_exact_matches=False, ...)` (#25506)
- Fix off-by-one bug in `ColumnPredicates` generation for inequalities operating on integer columns (#25412)
- Fix panic if scan predicate produces 0 length mask (#25089)
- Fix panic in `dt.truncate` for invalid duration strings (#25124)
- Fix panic in is_between support in streaming Parquet predicate push down (#25476)
- Fix panic when using struct field as join key (#25059)
- Fix serialization of lazyframes containing huge tables (#25190)
- Fix single-column CSV header duplication with leading empty lines (#25186)
- Fix small bug with `PyExpr` to `PyObject` conversion (#25265)
- Group-By aggregation problems caused by `AmortSeries` (#25043)
- Handle some unusual `pl.col.<colname>` edge-cases (#25153)
- Incorrect result in aggregated `first`/`last` with `ignore_nulls` (#25414)
- Incorrect results for aggregated `{n_,}unique` on bools (#25275)
- Invert `drop_nans` filtering in group-by context (#25146)
- Make `str.json_decode` output deterministic with lists (#25240)
- Mark `{forward,backward}_fill` as `length_preserving` (#25352)
- Minor improvement to internal `is_pycapsule` utility function (#25073)
- Nested dtypes in streaming `first_non_null`/`last_non_null` (#25375)
- Nested dtypes in streaming `first`/`last` (#25298)
- Panic exception when calling `Expr.rolling` in `.over` (#25283)
- Panic in `group_by_dynamic` with `group_by` and multiple chunks (#25075)
- Parquet `is_in` for mixed validity pages (#25313)
- Prevent panic when joining sorted LazyFrame with itself (#25453)
- Raise error for all/any on list instead of panic (#25018)
- Raise error on out-of-range dates in temporal operations (#25471)
- Remove `Expr` casts in `pl.lit` invocations (#25373)
- Resolve edge-case with SQL aggregates that have the same name as one of the "GROUP BY" keys (#25362)
- Return the correct string-case `Expr` reprs (#25101)
- Reverse on chunked `struct` (#25281)
- Revert `pl.format` behavior with nulls (#25370)
- Rolling `mean`/`median` for temporals (#25512)
- Run async DB queries with regular `asyncio` if not inside a running loop (#25268)
- SQL "NATURAL" joins should coalesce the key columns (#25353)
- Schema mismatch with `list.agg`, `unique` and scalar (#25348)
- Solve multiple issues relating to arena mutation in SQL subqueries (#25110)
- Strict conversion AnyValue to Struct (#25536)
- Support "index" as column name in `group_by` iterator (#25138)
- Support `AggregatedList` in `list.{eval,agg}` context (#25385)
- The `SQL` interface should use logical, not bitwise, behaviour for unary "NOT" operator (#25091)
- Unique key names in streaming sort/top_k (#25082)
- Unique on literal in aggregation context (#25359)
- Use (i64, u64) for VisualizationData (offset, length) slices (#25203)
- Use Cargo.template.toml to prevent git dependencies from using template (#25392)
- Validate list.slice parameters are not lists (#25458)
- Wide-table join performance regression (#25222)

## 📖 Documentation

- Add Extension and BaseExtension to doc index (#25444)
- Add `LazyFrame.pivot` to reference guide (#25482)
- Add `having` API references (#25428)
- Add docstring example showing `str.slice` taking Expression params (#25461)
- Add polars-on-premise documentation (#25431)
- Clarify bitwise behaviour of `and_`, `or_`, and `not_` Expressions on integer columns (#25092)
- Correct link to `datetime_range` instead of `date_range` in resampling page (#25532)
- Deprecate `Categorical` functions for lexical ordering and local checks (#25514)
- Document schema parameter in meta methods (#25543)
- Explain aggregation & sorting of lists (#25260)
- Fix LanceDB URL (#25198)
- Fix incorrect 'bitwise' in `any_horizontal`/`all_horizontal` docstring (#25469)
- Fix link errors reported by `markdown-link-check` (#25314)
- Fix non-existent `replace_all` reference in `replace` docs (#25161)
- Fix source path (#25170)
- Fix typo in public dataset URL (#25044)
- Mention Narwhals in ecosystem page (#25100)
- Remove lzo from parquet write options (#25522)
- Update `LazyFrame.collect_schema` docstring (#25508)
- Update `LazyFrame.remote` signature (#25175)
- Update on-premise documentation (#25489)
- Update user guide for QueryProgress rename to QueryProfile (#25195)

## 🧪 Tests

- Add `assert_sql_matches` coverage for SQL "DISTINCT" and "DISTINCT ON" syntax (#25440)
- Add reliable test for `pl.format` on multiple chunks (#25164)
- Add test for unique with column subset (#25241)
- Better coverage for `group_by` aggregations (#25290)
- Test for `group_by(...).having(...)` (#25430)

## 🔧 CI

- Automatically label pull requests that change the DSL (#25177)
- Avoid relabelling changes-dsl on every commit (#25216)
- Print expected DSL schema hashes if mismatched (#25526)
- Skip existing files in pypi upload (#25576)

## 🏗️ Build system

- Fix `make fmt` and `make lint` commands (#25200)
- Make building the docs on macOS more reliable (#25095)

## 🛠️ Other improvements

- Add `Final` type-qualifier to module-level constants (#25556)
- Add `proptest` `AnyValue` strategies (#25510)
- Add `proptest` `DataFrame` strategy (#25446)
- Add `proptest` strategies for Series logical types (#24849)
- Add `proptest` strategies for Series nested types (#25220)
- Add some cleanup (#25445)
- Add toolchain file to runtimes for sdist (#25311)
- Enable more streaming tests (#25364)
- Fix --uv argument for benchmark-remote (#25513)
- Fix Decimal precision annotation (#25227)
- Fix feature gating TZ_AWARE_RE again (#25493)
- Fix template path in release-python workflow (#25565)
- Fix typo in CI release workflow (#25309)
- Make python docs build again (#25165)
- Remove `Column::Partitioned` (#25324)
- Remove debug file write from test suite (#25393)
- Remove unused import (#25365)
- Run `maturin` with `--uv` option (#25490)
- Silence unused mut warning (#25093)
- Skip rust integration tests for coverage in CI (#25558)
- Update markdown link checker (#25201)
- Update toolchain (#25007)
- Update versions (#25141)
- Upgrade to schemars 0.9.0 (#25158)
- Upgraded `ruff` and `typos` and made the necessary lint updates (#25196)

## ♻️ Refactoring

- Accept multiple files in `pipe_with_schema` (#25388)
- Add IR for `scan_lines` (#25066)
- Add `ElementExpr` for `_eval` expressions (#25199)
- Add asserts and tests for `list.eval` on multiple chunks with slicing (#25559)
- Add functions for `scan_lines` (#25136)
- Add oneshot channel to polars-stream (#25378)
- Add stateful `EwmCov` kernel (#25065)
- Change group length mismatch error to `ShapeError` (#25004)
- Clean up CSPE callsite (#25215)
- Directly take `CloudScheme` in `parse_cloud_options` (#25304)
- Disable recursive CSPE for now (#25085)
- Dispatch `Series.set` to `zip_with_same_dtype` (#25327)
- Fix unsoundness in ChunkedArray::{first, last} (#25449)
- Make `pipe_with_schema` work on Arced schema (#25155)
- Move `EwmMeanState` to `polars-compute` (#25034)
- Move asof `tolerance` type coercion to IR conversion (#25033)
- Move ewm variance code to polars-compute (#25188)
- Move supertype determination and casting to IR for `date_range` and related functions (#24084)
- Refactor `dt_range` functions (#25225)
- Refactor sink IR (#25308)
- Remove `ClosableFile` (#25330)
- Remove `PyPartitioning` (#25303)
- Remove aggregation context `Context` (#25424)
- Remove incorrect cast in reduce code (#25321)
- Remove lower_ir conversion from Scan to InMemorySource (#25150)
- Remove old join projection pushdown logic (#25088)
- Remove some dead argminmax impl code (#25501)
- Remove unused `optimization_toggle` (#25130)
- Remove unused row-count (#25080)
- Remove verbose prints on file opens (#25523)
- Rename `URL_ENCODE_CHARSET` to `HIVE_ENCODE_CHARSET` (#25554)
- Simplify sink parameter passing from Python (#25302)
- Support for named/anonymous aggregations (#25118)
- Take `&dyn Any` instead of `Box<dyn Any>` in python object converters (#25421)
- Take `sync` parameter in `Writeable::close` (#25475)
- Update partitioned sink IR (#25524)
- Use dedicated runtime packages from template (#25284)


Thank you to all our contributors for making this release possible!
@AndreaBozzo, @DannyStoll1, @EndPositive, @JakubValtar, @Jesse-Bakker, @Kevin-Patyk, @MarcoGorelli, @TNieuwdorp, @alexander-beedie, @borchero, @c-peters, @cBournhonesque, @carnarez, @cmdlineluser, @coastalwhite, @cr7pt0gr4ph7, @davanstrien, @dsprenkels, @etiennebacher, @feliblo, @itamarst, @jannickj, @jetuk, @kdn36, @lun3x, @marinegor, @mcrumiller, @nameexhaustion, @orlp, @ritchie46, @vyasr, @wtn and more!

## Project: [pandas-dev/pandas](https://pandas.pydata.org/docs/index.html), 2 releases: ['Pandas 3.0.0rc1', 'Pandas 3.0.0rc0']
### Release: pandas [Pandas 3.0.0rc1](https://github.com/pandas-dev/pandas/releases/tag/v3.0.0rc1)
ERROR: (datetime.datetime(2025, 12, 19, 21, 38, 48), 'Pandas 3.0.0rc1', '', 'https://github.com/pandas-dev/pandas/releases/tag/v3.0.0rc1')
### Release: pandas [Pandas 3.0.0rc0](https://github.com/pandas-dev/pandas/releases/tag/v3.0.0rc0)
We are pleased to announce a first release candidate for pandas 3.0.0. If all goes well, we'll release pandas 3.0.0 in a few weeks.

See the [whatsnew][0] for a list of all the changes.

The release is available on conda-forge and PyPI.

The release can be installed from PyPI

    python -m pip install --upgrade --pre pandas==3.0.0rc0

Or from conda-forge

    conda install -c conda-forge/label/pandas_rc pandas==3.0.0rc0

Please report any issues with the release candidate on the pandas issue tracker.

[0]: https://pandas.pydata.org/docs/dev/whatsnew/v3.0.0.html
## Project: [holoviz/panel](https://panel.holoviz.org/), 2 releases: ['Version 1.8.5', 'Version 1.8.4']
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

### Release: panel [Version 1.8.4](https://github.com/holoviz/panel/releases/tag/v1.8.4)
Panel 1.8.4 includes key bug fixes and behavior improvements around event ordering, Tabulator interop, and Jupyter/Notebook usage. It also improves support for async usage, validation, and app routing—plus quality-of-life enhancements for both developers and users. Thanks to @philippjfr, @hoxbro, @maximlt, @ahuang11, @MarcSkovMadsen, @TheoMathurin, @ruoyu0088, and @dieterweber for your contributions to this release!

### ✨ Enhancements

- Add config toggle to disable Bokeh validation ([#8294](https://github.com/holoviz/panel/pull/8294))
- Allow `Tabulator.row_content` to be an async function ([#8309](https://github.com/holoviz/panel/pull/8309))
- Improve documentation and validation of `patch_value` ([#8312](https://github.com/holoviz/panel/pull/8312))
- Propagate layout-related parameters to `NestedSelect` ([#8317](https://github.com/holoviz/panel/pull/8317))

### 🐛 Bug Fixes

- Fix crash when emptying a `DataFrame` ([#8256](https://github.com/holoviz/panel/pull/8256))
- Ensure new Panel instance is always loaded ([#8293](https://github.com/holoviz/panel/pull/8293))
- Improve robustness of Bokeh/Panel notebook integration ([#8289](https://github.com/holoviz/panel/pull/8289))
- Fix notebook reading errors by explicitly using UTF-8 encoding ([#8304](https://github.com/holoviz/panel/pull/8304))
- Ensure `param.Action` only triggers one event ([#8305](https://github.com/holoviz/panel/pull/8305))
- Fix conflict when using both `ipywidgets` and `Tabulator` extensions ([#8308](https://github.com/holoviz/panel/pull/8308))
- Ensure discrete events (e.g. button clicks) are scheduled after change events ([#8311](https://github.com/holoviz/panel/pull/8311), [#8319](https://github.com/holoviz/panel/pull/8319))
- Reinstate application name as default index page title ([#8313](https://github.com/holoviz/panel/pull/8313))
- Redirect requests to the prefixed root when `--prefix` is set ([#8321](https://github.com/holoviz/panel/pull/8321))
- Ensure non-active `Tabs` are not clickable ([#8324](https://github.com/holoviz/panel/pull/8324))

### 🧪 Maintenance & Infrastructure

- Update Python/JS dependencies ([#8318](https://github.com/holoviz/panel/pull/8318))
- Fix type checking errors ([#8314](https://github.com/holoviz/panel/pull/8314))
- Pin `jupyterlite-core` temporarily ([#8315](https://github.com/holoviz/panel/pull/8315))
- Clean up `pixi.toml` project config ([#8303](https://github.com/holoviz/panel/pull/8303))

## Project: [holoviz/hvplot](https://hvplot.holoviz.org/), 1 releases: ['Version 0.12.2']
### Release: hvplot [Version 0.12.2](https://github.com/holoviz/hvplot/releases/tag/v0.12.2)

The 0.12.2 release is a patch release that brings a few bugfixes and enhancements. Many thanks to @ahuang11, @Azaya89, @hoxbro, @MarcSkovMadsen, @maximlt, and @MridulS for their contributions!

Enhancements:

- Automatically convert `xlim/ylim` to Web Mercator when `tiles=True` ([#1685](https://github.com/holoviz/hvplot/pull/1685))
- Automatically use `y` as default `text` kwarg if only two columns ([#1681](https://github.com/holoviz/hvplot/pull/1681))

Bug Fixes:

- Fix handling of `hv.dim` expressions in `size` and `color` parameters ([#1691](https://github.com/holoviz/hvplot/pull/1691))
- Exclude internal style columns (`_color` and `_size`) from tooltips ([#1690](https://github.com/holoviz/hvplot/pull/1690))

Documentation:

- Document `attr_labels` ([#1677](https://github.com/holoviz/hvplot/pull/1677))
- Fix typo in the NetworkX user guide ([#1686](https://github.com/holoviz/hvplot/pull/1686))
- Scale networkx layout and fix graphviz init in doc build ([#1672](https://github.com/holoviz/hvplot/pull/1672))
- Roadmap updates ([#1694](https://github.com/holoviz/hvplot/pull/1694))

Compatibility:

- Ensure Python 3.14 support ([#1688](https://github.com/holoviz/hvplot/pull/1688), [#1703](https://github.com/holoviz/hvplot/pull/1703))
- Compatibility with the latest versions of DuckDB ([#1682](https://github.com/holoviz/hvplot/pull/1682))
- Compatibility with the upcoming Pandas 3.0 ([#1704](https://github.com/holoviz/hvplot/pull/1704))

Infrastructure / Tests:

- Address warnings emitted by the unit tests suite ([#1700](https://github.com/holoviz/hvplot/pull/1700))
- Miscellaneous changes ([#1697](https://github.com/holoviz/hvplot/pull/1697), [#1698](https://github.com/holoviz/hvplot/pull/1698), [#1699](https://github.com/holoviz/hvplot/pull/1699), [#1701](https://github.com/holoviz/hvplot/pull/1701), [#1702](https://github.com/holoviz/hvplot/pull/1702), [#1706](https://github.com/holoviz/hvplot/pull/1706), [#1707](https://github.com/holoviz/hvplot/pull/1707))

[Full Changelog](https://github.com/holoviz/hvplot/compare/v0.12.1...v0.12.2)
## Project: [holoviz/holoviews](https://holoviews.org/), 1 releases: ['Version 1.22.1']
### Release: holoviews [Version 1.22.1](https://github.com/holoviz/holoviews/releases/tag/v1.22.1)
This patch release includes a number of bug fixes and enhancements, and adds compatibility with Pandas 3.
Many thanks to [@chrisbotica](https://github.com/chrisbotica) (first contribution), [@JelmerBot](https://github.com/JelmerBot) (first contribution), [@Azaya89](https://github.com/Azaya89), and [@hoxbro](https://github.com/hoxbro) for their contributions.

Enhancements:

- Add `text_outline_color` and `text_outline_width` style to Labels (Bokeh) ([#6738](https://github.com/holoviz/holoviews/pull/6738), [#6746](https://github.com/holoviz/holoviews/pull/6746))
- Add support for timedelta axis and Narwhals duration (Bokeh) ([#6734](https://github.com/holoviz/holoviews/pull/6734))
- Add numpy masked array to `masked_types` ([#6732](https://github.com/holoviz/holoviews/pull/6732))

Bug Fixes:

- Have hover tool work across different DynamicMaps elements (Bokeh) ([#6748](https://github.com/holoviz/holoviews/pull/6748))
- Suppress Runtime warnings for negative size values (Matplotlib) ([#6744](https://github.com/holoviz/holoviews/pull/6744))
- Don't error if `Heatmap` is optimized and color style is used ([#6730](https://github.com/holoviz/holoviews/pull/6730))
- Narwhals Series not being seen as arraylike and not computing `dim` expression ([#6729](https://github.com/holoviz/holoviews/pull/6729))
- Check categorical legend dtypes for `categories` before accessing it ([#6053](https://github.com/holoviz/holoviews/pull/6053))
- Element interface mask to allow for `np.nan` ([#5790](https://github.com/holoviz/holoviews/pull/5790))

Documentation:

- Add documentation for `legend_opts` (Bokeh) ([#6751](https://github.com/holoviz/holoviews/pull/6751))

Compatibility:

- Pandas 3.0.0 ([#6749](https://github.com/holoviz/holoviews/pull/6749))

## Project: [cython/cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html), 1 releases: ['3.2.3-1']
### Release: cython [3.2.3-1](https://github.com/cython/cython/releases/tag/3.2.3-1)
ERROR: (datetime.datetime(2025, 12, 14, 7, 47, 36), '3.2.3-1', None, 'https://github.com/cython/cython/releases/tag/3.2.3-1')
## Project: [plotly/dash](https://plotly.com/dash/), 2 releases: ['v4.0.0rc5', 'v4.0.0rc4']
### Release: dash [v4.0.0rc5](https://github.com/plotly/dash/releases/tag/v4.0.0rc5)
## Added
- New prop in `dcc.Upload` allows users to recursively upload entire folders at once

## Changed
- Bugfixes for feedback received in `rc4`
### Release: dash [v4.0.0rc4](https://github.com/plotly/dash/releases/tag/v4.0.0rc4)
- New `dcc.Button` component that mirrors `html.Button` but with default styles applied
- Fix various bugs found in `rc3`
## Project: [dask/dask](https://www.dask.org/), 1 releases: ['2025.12.0']
### Release: dask [2025.12.0](https://github.com/dask/dask/releases/tag/2025.12.0)
## Changes

- Stable sort in Series.value\_counts for pandas 3.x @TomAugspurger (#12191)
- Add new "optimization.tune.active" configuration option to disable partition fusion @rjzamora (#12194)
- Build llms.txt files in Sphinx documentation @jacobtomlinson (#12192)
- Support zarr sharding through create\_array @melonora (#12153)
- Support min/max of datetime @jsignell (#12183)
- pandas 3.x compatibility @TomAugspurger (#12180)
- Minimal version of setuptools-scm @DimitriPapadopoulos (#12184)
- Bump actions/checkout from 5 to 6 @[dependabot[bot]](https://github.com/apps/dependabot) (#12171)
- Update `test_ufunc_meta` for upstream-dev failure @TomAugspurger (#12170)
- Upstream compat @TomAugspurger (#12165)
- Enforce a few more ruff rules @DimitriPapadopoulos (#12157)
- Enforce ruff/refurb rules (FURB) @DimitriPapadopoulos (#12144)
- DEP: bump minimal requirement on toolz (0.10.0 -> 0.12.0) @neutrinoceros (#12163)
- Fix execution stop in da.to\_zarr due to (misleading) PerformanceWarning raised as exception @m-albert (#12161)
- Use f-string interpolation where possible @DimitriPapadopoulos (#12140)
- pre-commit black hook: use implicit defaults @DimitriPapadopoulos (#12156)
- Enforce ruff/pygrep-hooks rules (PGH) @DimitriPapadopoulos (#12143)
- Apply Repo-Review rules @DimitriPapadopoulos (#12148)
- Document groupby: split\_every, split\_out @jayeshmanani (#12135)
- isort → ruff @DimitriPapadopoulos (#12149)
- Enforce ruff/pyupgrade rule UP031 @DimitriPapadopoulos (#12137)
- Bump JamesIves/github-pages-deploy-action from 4.7.3 to 4.7.4 @[dependabot[bot]](https://github.com/apps/dependabot) (#12150)
- Replace pre-commit hook with ruff rule @DimitriPapadopoulos (#12142)
- Fix reify to handle sparse arrays and other objects without \_\_len\_\_ @batcity (#12103)
- Ruff supersedes absolufy-imports @DimitriPapadopoulos (#12141)
-  Enforce ruff/pyupgrade rule UP032 @DimitriPapadopoulos (#12136)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

## Project: [delta-io/delta-rs](https://delta-io.github.io/delta-rs/usage/installation/), 1 releases: ['rust-v0.30.0']
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
## Project: [rapidsai/cudf](https://docs.rapids.ai/api/cudf/stable/user_guide/10min/), 1 releases: ['v25.12.00']
### Release: cudf [v25.12.00](https://github.com/rapidsai/cudf/releases/tag/v25.12.00)
<!-- Release notes generated using configuration in .github/release.yml at v25.12.00 -->

## What's Changed
### 🚨 Breaking Changes
* Rewrite JNI functions to use `JNI_TRY`/`JNI_CATCH` by @ttnghia in https://github.com/rapidsai/cudf/pull/19053
* Remove compatibility with nvCOMP versions before 5.0 by @vuule in https://github.com/rapidsai/cudf/pull/20140
* Remove DataFrame.apply_chunks, Groupby.apply_grouped by @mroeschke in https://github.com/rapidsai/cudf/pull/20194
* Change .str.starts/endswith with tuple argument to match any pattern instead of pairwise matching by @mroeschke in https://github.com/rapidsai/cudf/pull/20249
* [cudf-polars] CUDA stream by @madsbk in https://github.com/rapidsai/cudf/pull/20154
* Chunked read parquet, prepend index column, and apply deletion vector by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20201
* Zero-copy `hostdevice_vector` on integrated systems by @vuule in https://github.com/rapidsai/cudf/pull/20225
* Use int64_t for the num_rows slot in parquet_reader_options by @wence- in https://github.com/rapidsai/cudf/pull/20256
* Require CUDA 12.2+ by @jakirkham in https://github.com/rapidsai/cudf/pull/20416
* Remove compatibility for CCCL < 3.1 by @bdice in https://github.com/rapidsai/cudf/pull/20468
* Remove deprecated types and APIs by @vuule in https://github.com/rapidsai/cudf/pull/20422
* Support signed integers and decimals in `SUM_WITH_OVERFLOW` groupby by @PointKernel in https://github.com/rapidsai/cudf/pull/19598
* Change groupby-scan COUNT to 1-based results by @davidwendt in https://github.com/rapidsai/cudf/pull/20168
* Change strings::like() pattern parameter from string_scalar to string_view by @davidwendt in https://github.com/rapidsai/cudf/pull/20428
* No-op performance tracking wrappers by @galipremsagar in https://github.com/rapidsai/cudf/pull/20595
### 🐛 Bug Fixes
* Copy `attrs` at correct place in `DataFrame` constructor by @galipremsagar in https://github.com/rapidsai/cudf/pull/20074
* Handle missing nightly runs in pandas tests job by @galipremsagar in https://github.com/rapidsai/cudf/pull/20081
* Fix numpy ufunc for `DataFrame` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20070
* Unproxy few unnecessary testing utilities in pandas by @galipremsagar in https://github.com/rapidsai/cudf/pull/20088
* Fix libcudf groupby benchmarks to not include internal cache by @davidwendt in https://github.com/rapidsai/cudf/pull/20038
* Fix cudf.date_range with non-iso start and end date strings by @mroeschke in https://github.com/rapidsai/cudf/pull/20116
* Fix create_distinct_rows_column to create non-nullable columns by @davidwendt in https://github.com/rapidsai/cudf/pull/20082
* Fix arrow timestamp frequency cases in `cudf.pandas` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20128
* Cast inputs to true division from decimal to float by @Matt711 in https://github.com/rapidsai/cudf/pull/20077
* Handle NVMLError_NotSupported in cudf-polars by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20179
* Fix RMM JNI pinned_fallback_host_memory_resource for CCCL 3.1.0 by @bdice in https://github.com/rapidsai/cudf/pull/20160
* Require passing memory resources to from_libcudf methods by @vyasr in https://github.com/rapidsai/cudf/pull/20171
* Enable hash-groupby for decimal32/64 type and MEAN aggregation by @davidwendt in https://github.com/rapidsai/cudf/pull/20040
* Align decimal dtypes in predicate before conditional join by @Matt711 in https://github.com/rapidsai/cudf/pull/20060
* Change stream_checking_resource_adaptor::do_deallocate to noexcept by @vyasr in https://github.com/rapidsai/cudf/pull/20218
* Deallocation should be noexcept by @bdice in https://github.com/rapidsai/cudf/pull/20219
* Fix a race condition in the decode of delta encoded Parquet columns by @vuule in https://github.com/rapidsai/cudf/pull/20216
* Fix the host-device tdigest offsets by using cuda::std::span by @PointKernel in https://github.com/rapidsai/cudf/pull/20220
* Add `stream` and `mr` arguments to `Column.from_arrow` type stub by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20244
* Pin `deltalake` in cudf-polars-polars-tests CI job by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20255
* Pin ibis-framework<11.0.0 by @Matt711 in https://github.com/rapidsai/cudf/pull/20267
* Add private attributes for `cudf.pandas` proxy objects by @galipremsagar in https://github.com/rapidsai/cudf/pull/20276
* Add Proxy for `SparseAccessor` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20278
* We need this to pacify mypy by @wence- in https://github.com/rapidsai/cudf/pull/20285
* Purge non-empty nulls for the generated lists columns in data generation utility by @ttnghia in https://github.com/rapidsai/cudf/pull/20283
* Fix missing table compatibility check in two_table_comparator constructor by @PointKernel in https://github.com/rapidsai/cudf/pull/20305
* Fix the check for equal `num_cols` across empty parquet sources by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20320
* Add `nans_to_nulls` to `Frame` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20314
* Add support for list type in `get` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20332
* Fix decimal dtype serialization in cudf-polars by @Matt711 in https://github.com/rapidsai/cudf/pull/20300
* Make the `GroupedRollingWindow`expression node reconstructable in cudf-polars by @Matt711 in https://github.com/rapidsai/cudf/pull/20288
* Ensure pylibcudf.Scalar.from_py uses CUDA streams by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20340
* Skip failing cudf-polars test due to hash groupby bug by @Matt711 in https://github.com/rapidsai/cudf/pull/20356
* Support order by keys for order-sensitive scalar aggregations in grouped windows by @Matt711 in https://github.com/rapidsai/cudf/pull/20350
* Honor user-passed stream in slice_strings for scalar inputs by @mroeschke in https://github.com/rapidsai/cudf/pull/20349
* Thread missing streams in column/table view creation to char size calculation by @vyasr in https://github.com/rapidsai/cudf/pull/20351
* Fix missed-sync for `mapping_indices_kernel` in hash-based groupby aggregation by @ttnghia in https://github.com/rapidsai/cudf/pull/20370
* Fix a few SPDX-related issues by @KyleFromNVIDIA in https://github.com/rapidsai/cudf/pull/20364
* Fix a `dtype` bug in column constructor by @galipremsagar in https://github.com/rapidsai/cudf/pull/20384
* Refactor `as_column` dtype parameter calls by @galipremsagar in https://github.com/rapidsai/cudf/pull/20379
* Add CUDA stream to `cudf_polars.Column.deserialize` by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20396
* Add missing CUDA stream to cudf-polars left-semi join by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20398
* Fix various string APIs to work with extension types by @galipremsagar in https://github.com/rapidsai/cudf/pull/20368
* Add parameter validation for `merge` and `MultiIndex.from_frame` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20382
* Fix nvtext::normalize_characters special token case by @davidwendt in https://github.com/rapidsai/cudf/pull/20242
* Fix pinned memory resource `shared_pointer` lifetime in tests. by @bdice in https://github.com/rapidsai/cudf/pull/20407
* Support new `nvcompStatus_t` enum value by @vuule in https://github.com/rapidsai/cudf/pull/20376
* Don't skip blank CSV lines rows after the header in cudf-polars scan_csv by @mroeschke in https://github.com/rapidsai/cudf/pull/20341
* Fix OOB accesses in JSON_CornerCase_Empty test and get_row_array_parent_col_id function by @bdice in https://github.com/rapidsai/cudf/pull/20421
* Change calls to cudaMemcpyToSymbol to cudaMemcpyToSymbolAsync by @davidwendt in https://github.com/rapidsai/cudf/pull/20374
* Do not accelerate `pandas._config.config` by @Matt711 in https://github.com/rapidsai/cudf/pull/20413
* Return timedelta instead of datetime type with std with datetime type with missing values by @mroeschke in https://github.com/rapidsai/cudf/pull/20439
* Disallow non-bool skipna arguments to reduction methods by @mroeschke in https://github.com/rapidsai/cudf/pull/20436
* Fix parquet scans for duckDB PDS-DS by @Matt711 in https://github.com/rapidsai/cudf/pull/20388
* Support `__array_function__` on the proxy array type by @Matt711 in https://github.com/rapidsai/cudf/pull/20419
* Make `memory_usage` and `__sizeof__` proxy attributes and always skip all memory usage tests by @Matt711 in https://github.com/rapidsai/cudf/pull/20425
* Add input validation for `from_records` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20412
* Use computed reduction result type for empty sum and product aggregations by @mroeschke in https://github.com/rapidsai/cudf/pull/20438
* Correct level arg validation for Index.isin, unique by @mroeschke in https://github.com/rapidsai/cudf/pull/20449
* Add private `_grouper` attribute to `DataFrameGroupBy` proxy type by @Matt711 in https://github.com/rapidsai/cudf/pull/20448
* Raise ValueError when indexing with zero step slice by @mroeschke in https://github.com/rapidsai/cudf/pull/20453
* Raise IndexError for float-like indexers in RangeIndex/MultiIndex.__getitem__ by @mroeschke in https://github.com/rapidsai/cudf/pull/20454
* Disallow slice(bool, ...) in DataFrame.loc with MultiIndex by @mroeschke in https://github.com/rapidsai/cudf/pull/20457
* Fix core dump in MemoryCleaner by @res-life in https://github.com/rapidsai/cudf/pull/19872
* Disallow multiple ellipse values in loc/iloc indexing by @mroeschke in https://github.com/rapidsai/cudf/pull/20456
* Fix `scan` operations for `string` columns by @galipremsagar in https://github.com/rapidsai/cudf/pull/20460
* Fix UTF8 data generator in libcudf benchmarks utility by @davidwendt in https://github.com/rapidsai/cudf/pull/20465
* Handle dealloc in stream-ordered cudf-polars ops by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20467
* Raise on unsupported unstack cases by @Matt711 in https://github.com/rapidsai/cudf/pull/20463
* Allow early exit for left semi-/anti- joins with empty build/probe tables by @shrshi in https://github.com/rapidsai/cudf/pull/20452
* Fix OOB memory access in JSON reader ingest_raw utility by @davidwendt in https://github.com/rapidsai/cudf/pull/20451
* Round up small-type groupby outputs to 4-byte boundary by @PointKernel in https://github.com/rapidsai/cudf/pull/20455
* Fix GPU acceleration bug in decimal type-cast by @galipremsagar in https://github.com/rapidsai/cudf/pull/20471
* Add missing CUDA stream in cudf_polars Distinct by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20477
* Support `__arrow_array__` on proxy extension array by @Matt711 in https://github.com/rapidsai/cudf/pull/20478
* Enable scan operation for `datetime64` and `timedelta64` types by @galipremsagar in https://github.com/rapidsai/cudf/pull/20464
* Remove unneeded type check in cudf::strings::slice_strings by @davidwendt in https://github.com/rapidsai/cudf/pull/20437
* Fix join match context tests by @PointKernel in https://github.com/rapidsai/cudf/pull/20472
* Fix the statistics_mr in benchmark fixture by @PointKernel in https://github.com/rapidsai/cudf/pull/20496
* Guard `__sizeof__` in pandas compatability mode by @Matt711 in https://github.com/rapidsai/cudf/pull/20495
* Fix OOB memory access in Orc and Parquet stacks from fixed-width unaligned loads by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20458
* Fix cudf.pandas Timestamp/Timedelta not subclassing stdlib datetime objects by @mroeschke in https://github.com/rapidsai/cudf/pull/20433
* Revert benchmark input generation logic for list type by @davidwendt in https://github.com/rapidsai/cudf/pull/20498
* Avoid using pylibcudf directly in rapidsmpf runtime by @rjzamora in https://github.com/rapidsai/cudf/pull/20501
* Suppress NVRTC arch warnings by @brandon-b-miller in https://github.com/rapidsai/cudf/pull/20517
* Fix ``ChannelManager`` and ``Lineariser`` by @rjzamora in https://github.com/rapidsai/cudf/pull/20516
* Synchronize streams in ``LocalShuffle`` by @rjzamora in https://github.com/rapidsai/cudf/pull/20515
* Make `argsort` have return type `np.intp` to match pandas by @Matt711 in https://github.com/rapidsai/cudf/pull/20487
* Fix `polars.concat_str` with one column in cudf_polars by @mroeschke in https://github.com/rapidsai/cudf/pull/20535
* Override `__sizeof__` for `cudf.Index` by @Matt711 in https://github.com/rapidsai/cudf/pull/20530
* Fix `pl.scan_csv(...).slice(...).collect(engine="gpu")` with None endpoint by @mroeschke in https://github.com/rapidsai/cudf/pull/20519
* Fix DataChunkSourceTest by syncing default stream by @davidwendt in https://github.com/rapidsai/cudf/pull/20492
* Fix data size errors in some libcudf benchmarks by @davidwendt in https://github.com/rapidsai/cudf/pull/20512
* Pin cython and pytest dependencies by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20571
* Pin Cython pre-3.2.0 and PyTest pre-9 by @jakirkham in https://github.com/rapidsai/cudf/pull/20573
* Handle `Empty` child IRs in `_decompose` by @Matt711 in https://github.com/rapidsai/cudf/pull/20409
* Skip flaky pandas datetime test by @Matt711 in https://github.com/rapidsai/cudf/pull/20585
* Fix max-pool-size-exceeded error in DATA_CHUNK_SOURCE_TEST by @davidwendt in https://github.com/rapidsai/cudf/pull/20534
* Fix racecheck in nvtext wordpiece tokenizer kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20588
* Fix the check to determine if all column chunk pages are dict encoded by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20524
* Add stream synchronize to QUANTILES_TEST PercentileApprox gtests by @davidwendt in https://github.com/rapidsai/cudf/pull/20558
* updated update-version.sh to handle release branch version changes by @rockhowse in https://github.com/rapidsai/cudf/pull/20598
* Fix nvtext tokenizers handling invalid UTF8 data by @davidwendt in https://github.com/rapidsai/cudf/pull/20514
* Fix overflow errors in distinct and filtered joins when hash table size exceeds int32 limits by @shrshi in https://github.com/rapidsai/cudf/pull/20594
* [FEA] Optimize JIT Filter for Low-Selectivity by @lamarrr in https://github.com/rapidsai/cudf/pull/20222
* Compute boolean function(NOT) on integers as a bitwise invert by @Matt711 in https://github.com/rapidsai/cudf/pull/20599
* Cast output dtype of rolling aggregations to match pandas by @Matt711 in https://github.com/rapidsai/cudf/pull/20526
* Add noop path for `Frame.astype` by @Matt711 in https://github.com/rapidsai/cudf/pull/20581
* Fix `copy` semantics bugs thus reduce copies and memory usage by @galipremsagar in https://github.com/rapidsai/cudf/pull/20121
* Ensure the sum after expression decomposition for mean has float output dtype by @Matt711 in https://github.com/rapidsai/cudf/pull/20596
* Use `Decimal(0)` literal for all-null decimal groups in groupby-sum by @Matt711 in https://github.com/rapidsai/cudf/pull/20591
* Do not drop `freq` when constructing `DatetimeIndex` from pandas by @brandon-b-miller in https://github.com/rapidsai/cudf/pull/18778
* Fix --validation flag for cudf.pandas PDSH benchmarks by @mroeschke in https://github.com/rapidsai/cudf/pull/20540
* Enable GPU acceleration for more binops by @galipremsagar in https://github.com/rapidsai/cudf/pull/20507
* Fix `rmm` function calls due to removed deprecated APIs and macro by @ttnghia in https://github.com/rapidsai/cudf/pull/20661
* Fix orc reader bool bug due to not being able to resume rle decode by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20666
* Fix categorical comparisons in `cudf` to match `pandas` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20674
* Fix `any` and `all` to match pandas by @galipremsagar in https://github.com/rapidsai/cudf/pull/20679
* Fix return types of string APIs in `cudf.pandas` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20683
* Resolve pandas test failures  by @galipremsagar in https://github.com/rapidsai/cudf/pull/20704
* Fix DatetimeIndex pickling by @vyasr in https://github.com/rapidsai/cudf/pull/20709
* `DatetimeIndex.serialize()` headers are msgpack serializable by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20714
### 📖 Documentation
* Add note that --rmm-async only affects distributed scheduler. by @bdice in https://github.com/rapidsai/cudf/pull/20129
* Add profiling guide by @bdice in https://github.com/rapidsai/cudf/pull/20292
* Find RMM before CCCL by @wence- in https://github.com/rapidsai/cudf/pull/20336
* Use current system architecture in conda environment creation command by @bdice in https://github.com/rapidsai/cudf/pull/20500
* Use uname -m instead of arch command by @bdice in https://github.com/rapidsai/cudf/pull/20502
* Use RAPIDS_BRANCH file for documentation links by @bdice in https://github.com/rapidsai/cudf/pull/20494
### 🚀 New Features
* Add memory resources to unary, transform, and filling modules by @vyasr in https://github.com/rapidsai/cudf/pull/20054
* Add memory resources to binaryop, copying, and stream_compaction by @vyasr in https://github.com/rapidsai/cudf/pull/20059
* Add memory resources to groupby, datetime, and lists modules by @vyasr in https://github.com/rapidsai/cudf/pull/20102
* Add memory resources to search, reshape, and partitioning module by @vyasr in https://github.com/rapidsai/cudf/pull/20101
* Add memory resources to rolling, sorting, and quantiles modules by @vyasr in https://github.com/rapidsai/cudf/pull/20099
* [FEA] Implement JIT Filter for read_parquet by @lamarrr in https://github.com/rapidsai/cudf/pull/19831
* Add memory resources to all nvtext APIs by @vyasr in https://github.com/rapidsai/cudf/pull/20119
* Add memory resource to all strings modules by @vyasr in https://github.com/rapidsai/cudf/pull/20123
* Add memory resources to reduce, column, column_factories, and contiguous_split by @vyasr in https://github.com/rapidsai/cudf/pull/20135
* Add memory resources to I/O modules by @vyasr in https://github.com/rapidsai/cudf/pull/20136
* Remove rounding from cudf java by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20110
* Add memory resources to replace, json, and hashing by @vyasr in https://github.com/rapidsai/cudf/pull/20150
* Add support for maintain_order param in joins by @Matt711 in https://github.com/rapidsai/cudf/pull/17698
* Add an example to inspect parquet files and dump row group and page level metadata information by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20117
* Support forward/backward filling null values in a grouped window context by @Matt711 in https://github.com/rapidsai/cudf/pull/19907
* Allow multiple calls to `cudf::initialize` and `cudf::deinitialize` by @vuule in https://github.com/rapidsai/cudf/pull/20111
* Add remaining memory resources by @vyasr in https://github.com/rapidsai/cudf/pull/20197
* Add memory resources to scalars by @vyasr in https://github.com/rapidsai/cudf/pull/20196
* Add pylibcudf is_valid_reduce_aggregation API by @davidwendt in https://github.com/rapidsai/cudf/pull/20145
* Support decimal literals in cudf-polars by @Matt711 in https://github.com/rapidsai/cudf/pull/20147
* Support `cum_sum(...).over(...)` expressions in cudf-polars by @Matt711 in https://github.com/rapidsai/cudf/pull/19908
* Passthrough unary ops through Parquet predicate pushdown by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20127
* Implement `ARGMIN` and `ARGMAX` aggregations for reduction by @ttnghia in https://github.com/rapidsai/cudf/pull/20207
* Skip decompression of pruned parquet pages by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20192
* Add an example to demonstrate the use of next-gen parquet reader to read a parquet file with highly selective filters by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/19469
* Evaluate `IS_NULL` at row group and page level in Parquet filtering by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20144
* [Java] Add optional native deps loader by @zpuller in https://github.com/rapidsai/cudf/pull/20414
* Add cudf-polars + rapidsmpf CI check by @rjzamora in https://github.com/rapidsai/cudf/pull/20355
* Add Python bindings for the hybrid scan reader by @vyasr in https://github.com/rapidsai/cudf/pull/20381
* RapidsMPF streaming-engine translation by @rjzamora in https://github.com/rapidsai/cudf/pull/20161
* [JNI] Use a read/write lock pattern in Rmm.class by @abellina in https://github.com/rapidsai/cudf/pull/20521
* [Java] Supports output projection indices for `contiguousSplitGroupsAndGenUniqKeys` by @res-life in https://github.com/rapidsai/cudf/pull/20391
* Support `Series.at` and `Series.iat` for pandas compatability by @Matt711 in https://github.com/rapidsai/cudf/pull/20529
* Add COUNT_VALID aggregation support to groupby-scan by @davidwendt in https://github.com/rapidsai/cudf/pull/20531
* Use RapidsMPF `read_parquet` in "rapidsmpf" runtime by @rjzamora in https://github.com/rapidsai/cudf/pull/20497
* Support decimal128 SUM aggregation in hash-based groupby by @PointKernel in https://github.com/rapidsai/cudf/pull/20509
* Add stream testing in pylibcudf by @vyasr in https://github.com/rapidsai/cudf/pull/20625
### 🛠️ Improvements
* Deprecate .from_pandas constructor by @mroeschke in https://github.com/rapidsai/cudf/pull/19996
* Prune entries in Sphinx nitpick_ignore by @mroeschke in https://github.com/rapidsai/cudf/pull/20045
* Avoid direct CategoricalColumn calls in dask_cudf by @mroeschke in https://github.com/rapidsai/cudf/pull/20080
* Fix typing issues in pylibcudf by @vyasr in https://github.com/rapidsai/cudf/pull/20069
* Avoid shadowing module names by @vyasr in https://github.com/rapidsai/cudf/pull/20071
* Remove calling to `purge_nonempty_nulls` in `make_lists_column` by @ttnghia in https://github.com/rapidsai/cudf/pull/12873
* Reduce verbosity of running the pandas test suite by @vyasr in https://github.com/rapidsai/cudf/pull/20107
* Clean up detail device atomic logic using atomic_ref by @PointKernel in https://github.com/rapidsai/cudf/pull/19924
* Use 8 processes for pandas tests, show top 10 test times by @bdice in https://github.com/rapidsai/cudf/pull/20109
* Update nvbench by @bdice in https://github.com/rapidsai/cudf/pull/19619
* Cleanup of some libcudf aggregation code by @davidwendt in https://github.com/rapidsai/cudf/pull/20053
* Run cudf-polars conda unit tests with more than 1 process by @mroeschke in https://github.com/rapidsai/cudf/pull/19980
* Avoid running pandas unit tests for private functionality with cudf.pandas by @mroeschke in https://github.com/rapidsai/cudf/pull/20115
* Remove MultiIndex.from_pandas pytest benchmark by @mroeschke in https://github.com/rapidsai/cudf/pull/20112
* Switch host_vector and host_span dependency by @davidwendt in https://github.com/rapidsai/cudf/pull/20106
* Have ListColumn.from_sequence go through pylibcudf by @mroeschke in https://github.com/rapidsai/cudf/pull/20098
* Fix `RAPIDS_BRANCH` version and update script by @galipremsagar in https://github.com/rapidsai/cudf/pull/20091
* Add pyarrow stubs to mypy environment and fix associated errors by @vyasr in https://github.com/rapidsai/cudf/pull/20118
* Fix slowdown in cudf-polars distributed tests by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20137
* Improve performance of string column size computation during parquet reads. by @nvdbaranec in https://github.com/rapidsai/cudf/pull/19986
* Disable async MR priming in cudf.pandas by @bdice in https://github.com/rapidsai/cudf/pull/20133
* Rework reduction case statement as dispatch_type_and_aggregation by @davidwendt in https://github.com/rapidsai/cudf/pull/20078
* Fix type annotations in cudf-polars by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20131
* Add tests for AUTO and HYBRID (de)compression modes by @vuule in https://github.com/rapidsai/cudf/pull/20126
* Branch 25.12 merge branch 25.10 by @vyasr in https://github.com/rapidsai/cudf/pull/20152
* Manual forward merger for Branch 25.12 - branch 25.10 by @galipremsagar in https://github.com/rapidsai/cudf/pull/20157
* Temporarily disable conda-java-tests by @bdice in https://github.com/rapidsai/cudf/pull/20162
* Remove unused ColumnBase.view by @mroeschke in https://github.com/rapidsai/cudf/pull/20141
* Avoid NumericalColumn call from CategoricalColumn.children by @mroeschke in https://github.com/rapidsai/cudf/pull/20153
* Deprecate legacy public row operators by @PointKernel in https://github.com/rapidsai/cudf/pull/20097
* Avoid more explicit calls to IntervalColumn and StructColumn by @mroeschke in https://github.com/rapidsai/cudf/pull/20064
* Run cudf-polars wheels unit tests with more than 1 process by @mroeschke in https://github.com/rapidsai/cudf/pull/20124
* Trace node execution in cudf-polars by @TomAugspurger in https://github.com/rapidsai/cudf/pull/19895
* Make ColumnBase.as_*_column convert via pylibcudf by @mroeschke in https://github.com/rapidsai/cudf/pull/20149
* Reduce execution times for parquet dictionary tests by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20176
* Update to rapids-logger 0.2 by @bdice in https://github.com/rapidsai/cudf/pull/20172
* Adjust rmm pool handling in PDSH benchmarks by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20138
* Don't assume cudf_polars benchmarking scale factor is always an integer by @mroeschke in https://github.com/rapidsai/cudf/pull/20182
* Skip filtering Parquet row groups with dictionaries if there are non-dict encoded pages by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20175
* Remove unnecessary work from `read_parquet_metadata` by @vuule in https://github.com/rapidsai/cudf/pull/20180
* Improve performance of groupby tdigests gtests by @davidwendt in https://github.com/rapidsai/cudf/pull/20173
* Revert "Temporarily disable conda-java-tests" by @bdice in https://github.com/rapidsai/cudf/pull/20184
* Add PDSH benchmark runner for cudf.pandas by @mroeschke in https://github.com/rapidsai/cudf/pull/20164
* Make Column.set_mask go through pylibcudf by @mroeschke in https://github.com/rapidsai/cudf/pull/20103
* Pin pydantic<2.12 in ci/test_cudf_polars_polars_tests.sh by @mroeschke in https://github.com/rapidsai/cudf/pull/20200
* Add an overhead field to cudf-polars tracing by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20198
* Support binops between float scalar to decimal column by @mroeschke in https://github.com/rapidsai/cudf/pull/20199
* Reduce output buffer sizes for pruned pages of columns with a `list` parent by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20086
* Make ListColumn._transform_leaves convert via pylibcudf by @mroeschke in https://github.com/rapidsai/cudf/pull/20151
* Rename `comparison_binop_generator` to `arg_minmax_binop_generator` and corresponding file to `nested_types_extrema_utils.cuh` by @Copilot in https://github.com/rapidsai/cudf/pull/20212
* Pin polars version <1.34 and >=1.29 by @Matt711 in https://github.com/rapidsai/cudf/pull/19912
* Stop using libcudf default parameters in pylibcudf by @vyasr in https://github.com/rapidsai/cudf/pull/20204
* Fix various typing errors by @vyasr in https://github.com/rapidsai/cudf/pull/20205
* Cleanup parquet for simple columns by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/19869
* Configuration for which metrics are enabled during tracing by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20223
* [pre-commit.ci] pre-commit autoupdate by @pre-commit-ci[bot] in https://github.com/rapidsai/cudf/pull/20189
* Fix parquet row number check for page bounds by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20217
* More mypy and docs fixes by @vyasr in https://github.com/rapidsai/cudf/pull/20224
* Prevent accidental copies of expensive-to-copy object types by @vuule in https://github.com/rapidsai/cudf/pull/20226
* Split row operator header by @PointKernel in https://github.com/rapidsai/cudf/pull/20166
* Standardize setting StructDtype field names post libcudf conversion by @mroeschke in https://github.com/rapidsai/cudf/pull/20235
* Add arm testing of cudf.pandas unit tests by @vyasr in https://github.com/rapidsai/cudf/pull/20251
* Enable `sccache-dist` connection pool by @trxcllnt in https://github.com/rapidsai/cudf/pull/20264
* Run polars tests with the streaming and in-memory executors by @Matt711 in https://github.com/rapidsai/cudf/pull/19354
* Move and rename ``ScanPartitionPlan`` by @rjzamora in https://github.com/rapidsai/cudf/pull/20248
* Unpin DuckDB and Ibis in cudf.pandas thirdparty tests by @mroeschke in https://github.com/rapidsai/cudf/pull/20269
* Add pylibcudf to pre-commit linting and fix outstanding errors by @vyasr in https://github.com/rapidsai/cudf/pull/20250
* Update ``ConfigOptions`` for rapidsmpf-streaming integration by @rjzamora in https://github.com/rapidsai/cudf/pull/20252
* Handle unordered grouped windows properly for null filling and cum sums by @Matt711 in https://github.com/rapidsai/cudf/pull/20275
* Add more type annotations to cudf/core/column subclasses by @mroeschke in https://github.com/rapidsai/cudf/pull/20277
* Remove extraneous host_memory_resource include by @bdice in https://github.com/rapidsai/cudf/pull/20284
* Add `MultiIndex.dtypes` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20279
* Skip mypy in pre-commit.ci by @bdice in https://github.com/rapidsai/cudf/pull/20286
* Make ColumnBase.deserialize construct via pylibcudf by @mroeschke in https://github.com/rapidsai/cudf/pull/20142
* Add numpy to the mypy pre-commit environment by @vyasr in https://github.com/rapidsai/cudf/pull/20282
* Add ability to set the source_info of parquet_reader_options by @wence- in https://github.com/rapidsai/cudf/pull/20253
* Add more Python type annotations to `cudf/core` by @mroeschke in https://github.com/rapidsai/cudf/pull/20287
* Use main in RAPIDS_BRANCH by @bdice in https://github.com/rapidsai/cudf/pull/20312
* Move "All rights reserved" statements to copyright line by @KyleFromNVIDIA in https://github.com/rapidsai/cudf/pull/20313
* Add `inferred_type` and missing `IntervalIndex` properties by @galipremsagar in https://github.com/rapidsai/cudf/pull/20294
* Avoid unseeded, random data generation in cuDF classic tests by @mroeschke in https://github.com/rapidsai/cudf/pull/20319
* Improve hash-based groupby aggregation: direct write to the dense output columns whenever possible by @ttnghia in https://github.com/rapidsai/cudf/pull/19764
* Avoid accessing range values in cudf::strings::contains_re logic by @davidwendt in https://github.com/rapidsai/cudf/pull/20122
* Migrate mixed join to use the multiset data structure  by @PointKernel in https://github.com/rapidsai/cudf/pull/19989
* Add benchmark for strings cast to/from integer APIs by @davidwendt in https://github.com/rapidsai/cudf/pull/20247
* Use main shared-workflows branch by @bdice in https://github.com/rapidsai/cudf/pull/20324
* Use the thread pool for Parquet metadata processing by @vuule in https://github.com/rapidsai/cudf/pull/20263
* Add `.dt.day_of_week` and `.dt.daysinmonth` by @galipremsagar in https://github.com/rapidsai/cudf/pull/20298
* Avoid Column materialization in RangeIndex.nans_to_nulls by @mroeschke in https://github.com/rapidsai/cudf/pull/20331
* Update the code to be compatible with the new cuco stream-ordered allocator by @PointKernel in https://github.com/rapidsai/cudf/pull/20258
* Deprecate Series.data by @mroeschke in https://github.com/rapidsai/cudf/pull/20281
* Align cudf Python's Column constructors by @mroeschke in https://github.com/rapidsai/cudf/pull/20233
* Make type annotations of ColumnBase.set_mask stricter by @mroeschke in https://github.com/rapidsai/cudf/pull/20261
* Make type annotations of ColumnBase.find_and_replace stricter by @mroeschke in https://github.com/rapidsai/cudf/pull/20259
* Make type annotations of ColumnBase.apply_boolean_mask stricter by @mroeschke in https://github.com/rapidsai/cudf/pull/20262
* Skip Python LZ4 tests when nvCOMP is disabled by @vuule in https://github.com/rapidsai/cudf/pull/20293
* Move cudf/io/nvcomp_adapter.hpp to cudf/io/detail by @davidwendt in https://github.com/rapidsai/cudf/pull/20327
* Add context to IR.do_evaluate by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20322
* Update mypy `# type: ignore` comments according to stricter mypy configs by @mroeschke in https://github.com/rapidsai/cudf/pull/20272
* Remove duplicated enforce null consistency code by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20342
* Use SPDX for all copyright headers by @KyleFromNVIDIA in https://github.com/rapidsai/cudf/pull/20321
* Add more type annotations to `cudf/core/series.py` by @mroeschke in https://github.com/rapidsai/cudf/pull/20304
* Remove/Replace uses of numba.cuda arrays in pytest benchmarks and tests by @mroeschke in https://github.com/rapidsai/cudf/pull/20359
* Add duckdb pdsh query queries by @Matt711 in https://github.com/rapidsai/cudf/pull/20257
* Use stream in cudf_polars.DataFrame.to_polars by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20323
* Add `join_streams` to pylibcudf API by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20316
* Use CUDA streams in all pylibcudf calls made by cudf-polars by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20291
* Add cudf/io/config_utils.hpp to doxygen by @davidwendt in https://github.com/rapidsai/cudf/pull/20329
* Test coverage for parallel metadata parsing by @vuule in https://github.com/rapidsai/cudf/pull/20334
* Support serializing more polars types by @Matt711 in https://github.com/rapidsai/cudf/pull/20347
* Add CUDAStreamPolicy to cudf-polars configuration by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20366
* Unskip cudf-polars groupby test by @Matt711 in https://github.com/rapidsai/cudf/pull/20406
* Deprecate pylibcudf interop arrow APIs by @Matt711 in https://github.com/rapidsai/cudf/pull/20405
* Get rid of the hashing helper header by @PointKernel in https://github.com/rapidsai/cudf/pull/20360
* Minor cleanup and fixes for libcudf generate_input.cu by @davidwendt in https://github.com/rapidsai/cudf/pull/20363
* Ignore assert_produces_warning and shares_memory pandas unit tests for cudf.pandas by @mroeschke in https://github.com/rapidsai/cudf/pull/20434
* Short circut RangeIndex.append for length 0 input, proxy private attribute by @mroeschke in https://github.com/rapidsai/cudf/pull/20442
* Mark DataFrame.insert as _external_only_api by @Copilot in https://github.com/rapidsai/cudf/pull/20403
* Deprecate `get_current_device_resource` in favor of `get_current_device_resource_ref` by @PointKernel in https://github.com/rapidsai/cudf/pull/20386
* Promote `JoinNoneValue` to public as `JoinNoMatch` for clear non-match Join semantics by @PointKernel in https://github.com/rapidsai/cudf/pull/20440
* Remove duplicate entries in NODEIDS_THAT_FAIL_WITH_CUDF_PANDAS by @mroeschke in https://github.com/rapidsai/cudf/pull/20447
* Use the thread pool in the compact protocol reader by @vuule in https://github.com/rapidsai/cudf/pull/20417
* Update README.md generalizing all cuDF components by @mroeschke in https://github.com/rapidsai/cudf/pull/20357
* Skip TestDatetimelikeCoercion pandas tests that assert ._value identity by @mroeschke in https://github.com/rapidsai/cudf/pull/20459
* Add PSDH Q2-9 for cudf.pandas by @mroeschke in https://github.com/rapidsai/cudf/pull/20418
* Add s3fs to `test_cudf_python` common dependencies by @trxcllnt in https://github.com/rapidsai/cudf/pull/20473
* Use public pandas APIs in StringColumn.to_pandas by @mroeschke in https://github.com/rapidsai/cudf/pull/20474
* Expose java GatherMap internals and add toString to AST by @revans2 in https://github.com/rapidsai/cudf/pull/20483
* Add create_ascii_string_column to the libcudf benchmark data generator by @davidwendt in https://github.com/rapidsai/cudf/pull/20354
* Skip more pandas unit tests that tests BlockManager, private sparse types by @mroeschke in https://github.com/rapidsai/cudf/pull/20489
* Add boto3/botocore/aiobotocore to common test dependencies by @trxcllnt in https://github.com/rapidsai/cudf/pull/20490
* Use a lower bound when estimating the partial file-size by @rjzamora in https://github.com/rapidsai/cudf/pull/20193
* Performance improvement for nvtext::edit_distance for long strings by @davidwendt in https://github.com/rapidsai/cudf/pull/20268
* Add MemoryResourceConfig to cudf-polars config by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20042
* Improve project automation by @vyasr in https://github.com/rapidsai/cudf/pull/20523
* Fuse simple streaming reductions in cudf-polars by @rjzamora in https://github.com/rapidsai/cudf/pull/18757
* Migrate to new CCCL memory resource interface by @bdice in https://github.com/rapidsai/cudf/pull/20513
* Add empty input gtest for cudf::transform by @davidwendt in https://github.com/rapidsai/cudf/pull/20505
* Rework internal json headers to allow converting gtests files from .cu to .cpp by @davidwendt in https://github.com/rapidsai/cudf/pull/20491
* Set continue on error in the cudf-polars-rapidsmpf nightly CI job by @Matt711 in https://github.com/rapidsai/cudf/pull/20550
* Permanently back cuDF column by a pylibcudf.Column by @mroeschke in https://github.com/rapidsai/cudf/pull/20306
* Skip flaky upstream polars rolling test by @Matt711 in https://github.com/rapidsai/cudf/pull/20552
* Accelerate data page mask computation on device by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20280
* Change default rapidsmpf stream policy to 'pool' by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20527
* Increase gtests coverage for cudf::strings::like patterns by @davidwendt in https://github.com/rapidsai/cudf/pull/20348
* Add cuda::std::span operator to cudf::column_view by @davidwendt in https://github.com/rapidsai/cudf/pull/20541
* Update ArrowStringView compare benchmark for gather by @davidwendt in https://github.com/rapidsai/cudf/pull/19935
* Add pytest stubs and remove ujson usage by @vyasr in https://github.com/rapidsai/cudf/pull/20560
* Skip arrow array constructor tests by @Matt711 in https://github.com/rapidsai/cudf/pull/20579
* Add Polars to mypy environment and fix errors by @vyasr in https://github.com/rapidsai/cudf/pull/20563
* Ensure table chunks are unspilled and available by @madsbk in https://github.com/rapidsai/cudf/pull/20583
* Skip tests that assert behavior when copy-on-write is False by @Matt711 in https://github.com/rapidsai/cudf/pull/20506
* Pass streams through `Column.from_array`/`from_iterable_of_py` by @Matt711 in https://github.com/rapidsai/cudf/pull/20569
* Stop using Dtype annotation by @vyasr in https://github.com/rapidsai/cudf/pull/20590
* Workaround to enable running PDS-H via WebHDFS by @kingcrimsontianyu in https://github.com/rapidsai/cudf/pull/20132
* Update RMM includes from `<rmm/mr/device/*>` to `<rmm/mr/*>` by @bdice in https://github.com/rapidsai/cudf/pull/20607
* Stricter typing import for cudf-polars by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20614
* Avoid the unnecessary H2H copy in the `std::vector` sink by @vuule in https://github.com/rapidsai/cudf/pull/20602
* Preprocessing offsets for Parquet non-dictionary string columns by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20430
* Move more pandas unit tests that test private APIs by @mroeschke in https://github.com/rapidsai/cudf/pull/20511
* Use `.plc_column` instead of `.to_pylibcudf` in rolling, string utilties by @mroeschke in https://github.com/rapidsai/cudf/pull/20562
* Skip TestSetitemNADatetimeLikeDtype pandas unit tests due to private assertion by @mroeschke in https://github.com/rapidsai/cudf/pull/20578
* Pin Polars version <1.35 by @Matt711 in https://github.com/rapidsai/cudf/pull/20266
* Skip pandas unit tests in `test_old_base.py` that test private APIs by @mroeschke in https://github.com/rapidsai/cudf/pull/20572
* Use `.plc_column` attribute instead of `to_pylibcudf` more internally by @mroeschke in https://github.com/rapidsai/cudf/pull/20559
* Skip arrow-backed arithmetic tests and categorize the remaining failing tests by @Matt711 in https://github.com/rapidsai/cudf/pull/20577
* Fix a pytest execution that is spawned in a subprocess by @galipremsagar in https://github.com/rapidsai/cudf/pull/20660
* Accelerated parquet page header decoding when page index is available by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20369
* feat: add error handling for non-existent columns in parquet reader by @gforsyth in https://github.com/rapidsai/cudf/pull/20659
* Optimize row mask computation for single filter column by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20335
* Skip MultiIndex pandas unit tests testing private functionalty, `test_chaining_and_caching.py` by @mroeschke in https://github.com/rapidsai/cudf/pull/20575
* Address minor comments from recent hybrid scan PRs by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20672
* Add a timeout for the rapidsmpf test run by @vyasr in https://github.com/rapidsai/cudf/pull/20681
* Use `sccache-dist` build cluster for conda and wheel builds by @trxcllnt in https://github.com/rapidsai/cudf/pull/20488

## New Contributors
* @Copilot made their first contribution in https://github.com/rapidsai/cudf/pull/20212
* @rockhowse made their first contribution in https://github.com/rapidsai/cudf/pull/20598

**Full Changelog**: https://github.com/rapidsai/cudf/compare/v25.12.00a...v25.12.00
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 14 releases: ['v1.0.1', 'v2.0.0-beta.5', 'v2.0.0-beta.4', 'v1.0.1-rc.1', 'v1.0.1-beta.1', 'v2.0.0-beta.3', 'v2.0.0-beta.2', 'v1.0.0', 'v2.0.0-beta.1', 'v1.0.0-rc.3', 'v1.1.0-beta.2', 'v1.1.0-beta.1', 'v1.0.0-rc.2', 'v1.0.0-rc.1']
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
### Release: lance [v2.0.0-beta.4](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.4)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.4 -->

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
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
* perf: offload IVF partition build to CPU pool by @BubbleCal in https://github.com/lance-format/lance/pull/5551
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449
* refactor: expose take_blobs_by_addresses to python by @Xuanwo in https://github.com/lance-format/lance/pull/5474
* refactor: add store_prefix to lance-io's ObjectStore by @cmccabe in https://github.com/lance-format/lance/pull/5468
* refactor: rename RowIdMask to RowAddrMask by @yanghua in https://github.com/lance-format/lance/pull/5281

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

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.4
### Release: lance [v1.0.1-rc.1](https://github.com/lance-format/lance/releases/tag/v1.0.1-rc.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.1-rc.1 -->

## What's Changed
### Bug Fixes 🐛
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5495
* fix: panic unwrap on None in decoder.rs by @jackye1995 in https://github.com/lance-format/lance/pull/5498
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5500


**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.0...v1.0.1-rc.1
### Release: lance [v1.0.1-beta.1](https://github.com/lance-format/lance/releases/tag/v1.0.1-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.1-beta.1 -->

## What's Changed
### Bug Fixes 🐛
* fix: dir namespace cloud storage path removes one subdir level by @jackye1995 in https://github.com/lance-format/lance/pull/5495
* fix: panic unwrap on None in decoder.rs by @jackye1995 in https://github.com/lance-format/lance/pull/5498
* fix: ensure trailing slash is normalized in rest adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5500


**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.0...v1.0.1-beta.1
### Release: lance [v2.0.0-beta.3](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.3)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.3 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
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
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
* perf: reuse session context by @wjones127 in https://github.com/lance-format/lance/pull/5462
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449

## New Contributors
* @mackrorysd made their first contribution in https://github.com/lance-format/lance/pull/5315
* @valkum made their first contribution in https://github.com/lance-format/lance/pull/5372
* @rongou made their first contribution in https://github.com/lance-format/lance/pull/5439
* @camilesing made their first contribution in https://github.com/lance-format/lance/pull/5424

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.3
### Release: lance [v2.0.0-beta.2](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.2 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
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
### Bug Fixes 🐛
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449

## New Contributors
* @mackrorysd made their first contribution in https://github.com/lance-format/lance/pull/5315
* @valkum made their first contribution in https://github.com/lance-format/lance/pull/5372
* @rongou made their first contribution in https://github.com/lance-format/lance/pull/5439

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.2
### Release: lance [v1.0.0](https://github.com/lance-format/lance/releases/tag/v1.0.0)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.0 -->

## What's Changed
### Breaking Changes 🛠
* perf!: dynamic pruning for vector search by @BubbleCal in https://github.com/lance-format/lance/pull/4773
* feat!: remove unnecessary mut of dataset::sql by @ddupg in https://github.com/lance-format/lance/pull/5207
* refactor!: move all previous code into `previous` mod by @Xuanwo in https://github.com/lance-format/lance/pull/5217
* refactor!: deprecate TFRecord support by @jackye1995 in https://github.com/lance-format/lance/pull/4593
* refactor!: use org.lance namespace for java package by @jackye1995 in https://github.com/lance-format/lance/pull/5339
* refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lance-format/lance/pull/5391
### Critical Fixes ‼️
* fix: convert some panics into errors by @wjones127 in https://github.com/lance-format/lance/pull/5258
### New Features 🎉
* feat: provide inline_transaction model for IO optimizing by @majin1102 in https://github.com/lance-format/lance/pull/4774
* feat(python): add support for HuggingFace IterableDataset by @changhiskhan in https://github.com/lance-format/lance/pull/2599
* feat: add public accessors for count plan construction by @wkalt in https://github.com/lance-format/lance/pull/5103
* feat: add adapter for REST namespace with manifest namespace backend by @jackye1995 in https://github.com/lance-format/lance/pull/4984
* feat: add blob compaction support by @Xuanwo in https://github.com/lance-format/lance/pull/5189
* feat: add inline optimization for dir namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5244
* feat: conflict resolution for DataReplacement by @wjones127 in https://github.com/lance-format/lance/pull/3631
* feat: support namespace vended credentials for write by @jackye1995 in https://github.com/lance-format/lance/pull/5161
* docs: correct the comment in util.py by @shiyajuan123 in https://github.com/lance-format/lance/pull/5252
* feat: introduce community governance by @jackye1995 in https://github.com/lance-format/lance/pull/5262
* feat: add describe_indices function by @westonpace in https://github.com/lance-format/lance/pull/5221
* feat: add target_bases extension to python write_fragments API by @jaystarshot in https://github.com/lance-format/lance/pull/5234
* feat: support credentials vending for file reader and session by @jackye1995 in https://github.com/lance-format/lance/pull/5256
* feat: introduce blob arrow extension type by @Xuanwo in https://github.com/lance-format/lance/pull/5239
* feat(java): add binding for rest and dir namespaces by @jackye1995 in https://github.com/lance-format/lance/pull/5292
* feat: expose file upload and download in Lance file session by @jackye1995 in https://github.com/lance-format/lance/pull/5336
* feat(java): support credential vending at write time by @jackye1995 in https://github.com/lance-format/lance/pull/5309
* feat(ds-sql-api): support JSON bulit in functions in ds.sql API by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5350
* feat: support GEO types by @ddupg in https://github.com/lance-format/lance/pull/4678
* feat(python): expose DatasetDeltaBuilder and relevant apis by @yanghua in https://github.com/lance-format/lance/pull/5091
* feat: return Unprocessable error while expected error happened by @Xuanwo in https://github.com/lance-format/lance/pull/5347
* feat: add huggingface native support by @Xuanwo in https://github.com/lance-format/lance/pull/5353
* feat: dynamically choose distance type by @BubbleCal in https://github.com/lance-format/lance/pull/5370
* feat(java): support writing schema metadata through java LanceFileWriter API by @steFaiz in https://github.com/lance-format/lance/pull/5310
### Bug Fixes 🐛
* fix: ensure recheck for IsNotNull in bloom filter by @Xuanwo in https://github.com/lance-format/lance/pull/5192
* fix: contributing URL gives 404 by @prrao87 in https://github.com/lance-format/lance/pull/5196
* fix: merge struct array use wrong child values by @wojiaodoubao in https://github.com/lance-format/lance/pull/5106
* fix: avoid unnecessary get_fragments calling during plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5179
* fix: split partition may be assigned to itself by @BubbleCal in https://github.com/lance-format/lance/pull/5190
* fix: improve schema validation for nullability and subschemas by @fenfeng9 in https://github.com/lance-format/lance/pull/4994
* fix: compile error in test_inline_transaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5206
* docs: fix batch udf with checkpoint document error by @fangyinc in https://github.com/lance-format/lance/pull/5185
* fix: memory-limited string BTREE index building by @wjones127 in https://github.com/lance-format/lance/pull/5175
* fix: home page code snippets cuasing various problems by @jackye1995 in https://github.com/lance-format/lance/pull/5245
* fix: panic if only one partition and split is triggered by @BubbleCal in https://github.com/lance-format/lance/pull/5241
* fix: clearer error in dataset take by @wkalt in https://github.com/lance-format/lance/pull/5243
* fix: docs and comment have broken links by @prrao87 in https://github.com/lance-format/lance/pull/5261
* fix: handle logical rows deletion properly for zonemap and bloomfilter by @HaochengLIU in https://github.com/lance-format/lance/pull/5140
* fix: blob version should be passed in Projection by @Xuanwo in https://github.com/lance-format/lance/pull/5295
* docs: fix broken links and 404s by @prrao87 in https://github.com/lance-format/lance/pull/5284
* fix: index overestimates the posting list size by @BubbleCal in https://github.com/lance-format/lance/pull/5327
* fix: update CachedFileMetadata version API to V2.0 by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5330
* fix: correctly handle OSS commit protocol to prevent data loss by @Pmathsun in https://github.com/lance-format/lance/pull/5332
* fix: update btree index with its own zone size instead of DEFAULT_BTR… by @ztorchan in https://github.com/lance-format/lance/pull/5301
* fix: join job may cause inconsistent delta indices by @BubbleCal in https://github.com/lance-format/lance/pull/5328
* fix: panicException when calling compaction by @yanghua in https://github.com/lance-format/lance/pull/5282
* fix: parallelize bitmap partition loading in IsIn expressions by @wkalt in https://github.com/lance-format/lance/pull/5355
* fix: avx512 related symbol not found in mac x86 by @jackye1995 in https://github.com/lance-format/lance/pull/5379
* fix: add graceful shutdown and start for rest namespace adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5325
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5397
* fix: critical fixes for 1.0.0-rc3 by @jackye1995 in https://github.com/lance-format/lance/pull/5421
### Documentation 📚
* docs: introduce lance as a lakehouse format by @jackye1995 in https://github.com/lance-format/lance/pull/5209
* docs: update readme with latest lakehouse format info by @jackye1995 in https://github.com/lance-format/lance/pull/5216
* docs: capitalization change by @timsaucer in https://github.com/lance-format/lance/pull/5269
* docs: build project specific guidelines into web doc by @jackye1995 in https://github.com/lance-format/lance/pull/5324
### Performance Improvements 🚀
* perf: speed up filtered scan by up to 18.9× by moving the heavy CPU task out by @Xuanwo in https://github.com/lance-format/lance/pull/5165
* perf: parallelize split job assigning by @BubbleCal in https://github.com/lance-format/lance/pull/5265
* perf: use CPU pool to run WAND algo by @BubbleCal in https://github.com/lance-format/lance/pull/5363
* perf: avoid allocating filtered nodes on HNSW search path by @BubbleCal in https://github.com/lance-format/lance/pull/5377
### Other Changes
* refactor: move blob version as a table level config by @Xuanwo in https://github.com/lance-format/lance/pull/5220
* refactor: add helper functions to delta.rs tests by @yanghua in https://github.com/lance-format/lance/pull/5298
* refactor: move LanceNamespace interface to pylance and java lance-core by @jackye1995 in https://github.com/lance-format/lance/pull/5345
* refactor: allow datafiles to contain columns without field id by @Xuanwo in https://github.com/lance-format/lance/pull/5348
* refactor: rename RowIdSelection to RowAddrSelection by @yanghua in https://github.com/lance-format/lance/pull/5263
* refactor: separate out python and java LanceNamespace interface by @jackye1995 in https://github.com/lance-format/lance/pull/5364
* refactor: align with blob v2 logical types change by @Xuanwo in https://github.com/lance-format/lance/pull/5375

## New Contributors
* @prrao87 made their first contribution in https://github.com/lance-format/lance/pull/5196
* @fangyinc made their first contribution in https://github.com/lance-format/lance/pull/5185
* @shiyajuan123 made their first contribution in https://github.com/lance-format/lance/pull/5252
* @Pmathsun made their first contribution in https://github.com/lance-format/lance/pull/5332
* @ztorchan made their first contribution in https://github.com/lance-format/lance/pull/5301
* @fMeow made their first contribution in https://github.com/lance-format/lance/pull/5371

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/1.0.0-beta.N...v1.0.0
### Release: lance [v2.0.0-beta.1](https://github.com/lance-format/lance/releases/tag/v2.0.0-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-beta.1 -->

## What's Changed
### Breaking Changes 🛠
* fix!: null handling when using `NOT` with scalar indices by @wjones127 in https://github.com/lance-format/lance/pull/5270
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
### Bug Fixes 🐛
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
* fix: remove expensive clone in bitmap search by @westonpace in https://github.com/lance-format/lance/pull/5409
* fix: stop documenting FTS index type, standardize on INVERTED by @mackrorysd in https://github.com/lance-format/lance/pull/5315
* fix: remove logging for project_batch by @westonpace in https://github.com/lance-format/lance/pull/5267
### Documentation 📚
* docs: fix Append call in distributed write guide by @rongou in https://github.com/lance-format/lance/pull/5439
### Performance Improvements 🚀
* perf: do not instrument self in multipart upload by @westonpace in https://github.com/lance-format/lance/pull/5416
* perf: various btree performance improvements by @westonpace in https://github.com/lance-format/lance/pull/5446
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387
* refactor: write bitmap index statistics in file instead by @Xuanwo in https://github.com/lance-format/lance/pull/5251
* refactor: consolidate logic between zonemap and bloomfilter indexes by @fenfeng9 in https://github.com/lance-format/lance/pull/5374
* refactor: use the same path for dedicated and packed blob by @Xuanwo in https://github.com/lance-format/lance/pull/5449

## New Contributors
* @mackrorysd made their first contribution in https://github.com/lance-format/lance/pull/5315
* @valkum made their first contribution in https://github.com/lance-format/lance/pull/5372
* @rongou made their first contribution in https://github.com/lance-format/lance/pull/5439

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-beta.1
### Release: lance [v1.0.0-rc.3](https://github.com/lance-format/lance/releases/tag/v1.0.0-rc.3)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.0-rc.3 -->

## What's Changed
### Breaking Changes 🛠
* perf!: dynamic pruning for vector search by @BubbleCal in https://github.com/lance-format/lance/pull/4773
* feat!: remove unnecessary mut of dataset::sql by @ddupg in https://github.com/lance-format/lance/pull/5207
* refactor!: move all previous code into `previous` mod by @Xuanwo in https://github.com/lance-format/lance/pull/5217
* refactor!: deprecate TFRecord support by @jackye1995 in https://github.com/lance-format/lance/pull/4593
* refactor!: use org.lance namespace for java package by @jackye1995 in https://github.com/lance-format/lance/pull/5339
* refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lance-format/lance/pull/5391
### Critical Fixes ‼️
* fix: convert some panics into errors by @wjones127 in https://github.com/lance-format/lance/pull/5258
### New Features 🎉
* feat: provide inline_transaction model for IO optimizing by @majin1102 in https://github.com/lance-format/lance/pull/4774
* feat(python): add support for HuggingFace IterableDataset by @changhiskhan in https://github.com/lance-format/lance/pull/2599
* feat: add public accessors for count plan construction by @wkalt in https://github.com/lance-format/lance/pull/5103
* feat: add adapter for REST namespace with manifest namespace backend by @jackye1995 in https://github.com/lance-format/lance/pull/4984
* feat: add blob compaction support by @Xuanwo in https://github.com/lance-format/lance/pull/5189
* feat: add inline optimization for dir namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5244
* feat: conflict resolution for DataReplacement by @wjones127 in https://github.com/lance-format/lance/pull/3631
* feat: support namespace vended credentials for write by @jackye1995 in https://github.com/lance-format/lance/pull/5161
* docs: correct the comment in util.py by @shiyajuan123 in https://github.com/lance-format/lance/pull/5252
* feat: introduce community governance by @jackye1995 in https://github.com/lance-format/lance/pull/5262
* feat: add describe_indices function by @westonpace in https://github.com/lance-format/lance/pull/5221
* feat: add target_bases extension to python write_fragments API by @jaystarshot in https://github.com/lance-format/lance/pull/5234
* feat: support credentials vending for file reader and session by @jackye1995 in https://github.com/lance-format/lance/pull/5256
* feat: introduce blob arrow extension type by @Xuanwo in https://github.com/lance-format/lance/pull/5239
* feat(java): add binding for rest and dir namespaces by @jackye1995 in https://github.com/lance-format/lance/pull/5292
* feat: expose file upload and download in Lance file session by @jackye1995 in https://github.com/lance-format/lance/pull/5336
* feat(java): support credential vending at write time by @jackye1995 in https://github.com/lance-format/lance/pull/5309
* feat(ds-sql-api): support JSON bulit in functions in ds.sql API by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5350
* feat: support GEO types by @ddupg in https://github.com/lance-format/lance/pull/4678
* feat(python): expose DatasetDeltaBuilder and relevant apis by @yanghua in https://github.com/lance-format/lance/pull/5091
* feat: return Unprocessable error while expected error happened by @Xuanwo in https://github.com/lance-format/lance/pull/5347
* feat: add huggingface native support by @Xuanwo in https://github.com/lance-format/lance/pull/5353
* feat: dynamically choose distance type by @BubbleCal in https://github.com/lance-format/lance/pull/5370
* feat(java): support writing schema metadata through java LanceFileWriter API by @steFaiz in https://github.com/lance-format/lance/pull/5310
### Bug Fixes 🐛
* fix: ensure recheck for IsNotNull in bloom filter by @Xuanwo in https://github.com/lance-format/lance/pull/5192
* fix: contributing URL gives 404 by @prrao87 in https://github.com/lance-format/lance/pull/5196
* fix: merge struct array use wrong child values by @wojiaodoubao in https://github.com/lance-format/lance/pull/5106
* fix: avoid unnecessary get_fragments calling during plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5179
* fix: split partition may be assigned to itself by @BubbleCal in https://github.com/lance-format/lance/pull/5190
* fix: improve schema validation for nullability and subschemas by @fenfeng9 in https://github.com/lance-format/lance/pull/4994
* fix: compile error in test_inline_transaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5206
* docs: fix batch udf with checkpoint document error by @fangyinc in https://github.com/lance-format/lance/pull/5185
* fix: memory-limited string BTREE index building by @wjones127 in https://github.com/lance-format/lance/pull/5175
* fix: home page code snippets cuasing various problems by @jackye1995 in https://github.com/lance-format/lance/pull/5245
* fix: panic if only one partition and split is triggered by @BubbleCal in https://github.com/lance-format/lance/pull/5241
* fix: clearer error in dataset take by @wkalt in https://github.com/lance-format/lance/pull/5243
* fix: docs and comment have broken links by @prrao87 in https://github.com/lance-format/lance/pull/5261
* fix: handle logical rows deletion properly for zonemap and bloomfilter by @HaochengLIU in https://github.com/lance-format/lance/pull/5140
* fix: blob version should be passed in Projection by @Xuanwo in https://github.com/lance-format/lance/pull/5295
* docs: fix broken links and 404s by @prrao87 in https://github.com/lance-format/lance/pull/5284
* fix: index overestimates the posting list size by @BubbleCal in https://github.com/lance-format/lance/pull/5327
* fix: update CachedFileMetadata version API to V2.0 by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5330
* fix: correctly handle OSS commit protocol to prevent data loss by @Pmathsun in https://github.com/lance-format/lance/pull/5332
* fix: update btree index with its own zone size instead of DEFAULT_BTR… by @ztorchan in https://github.com/lance-format/lance/pull/5301
* fix: join job may cause inconsistent delta indices by @BubbleCal in https://github.com/lance-format/lance/pull/5328
* fix: panicException when calling compaction by @yanghua in https://github.com/lance-format/lance/pull/5282
* fix: parallelize bitmap partition loading in IsIn expressions by @wkalt in https://github.com/lance-format/lance/pull/5355
* fix: avx512 related symbol not found in mac x86 by @jackye1995 in https://github.com/lance-format/lance/pull/5379
* fix: add graceful shutdown and start for rest namespace adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5325
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5397
* fix: critical fixes for 1.0.0-rc3 by @jackye1995 in https://github.com/lance-format/lance/pull/5421
### Documentation 📚
* docs: introduce lance as a lakehouse format by @jackye1995 in https://github.com/lance-format/lance/pull/5209
* docs: update readme with latest lakehouse format info by @jackye1995 in https://github.com/lance-format/lance/pull/5216
* docs: capitalization change by @timsaucer in https://github.com/lance-format/lance/pull/5269
* docs: build project specific guidelines into web doc by @jackye1995 in https://github.com/lance-format/lance/pull/5324
### Performance Improvements 🚀
* perf: speed up filtered scan by up to 18.9× by moving the heavy CPU task out by @Xuanwo in https://github.com/lance-format/lance/pull/5165
* perf: parallelize split job assigning by @BubbleCal in https://github.com/lance-format/lance/pull/5265
* perf: use CPU pool to run WAND algo by @BubbleCal in https://github.com/lance-format/lance/pull/5363
* perf: avoid allocating filtered nodes on HNSW search path by @BubbleCal in https://github.com/lance-format/lance/pull/5377
### Other Changes
* refactor: move blob version as a table level config by @Xuanwo in https://github.com/lance-format/lance/pull/5220
* refactor: add helper functions to delta.rs tests by @yanghua in https://github.com/lance-format/lance/pull/5298
* refactor: move LanceNamespace interface to pylance and java lance-core by @jackye1995 in https://github.com/lance-format/lance/pull/5345
* refactor: allow datafiles to contain columns without field id by @Xuanwo in https://github.com/lance-format/lance/pull/5348
* refactor: rename RowIdSelection to RowAddrSelection by @yanghua in https://github.com/lance-format/lance/pull/5263
* refactor: separate out python and java LanceNamespace interface by @jackye1995 in https://github.com/lance-format/lance/pull/5364
* refactor: align with blob v2 logical types change by @Xuanwo in https://github.com/lance-format/lance/pull/5375

## New Contributors
* @prrao87 made their first contribution in https://github.com/lance-format/lance/pull/5196
* @fenfeng9 made their first contribution in https://github.com/lance-format/lance/pull/4994
* @fangyinc made their first contribution in https://github.com/lance-format/lance/pull/5185
* @shiyajuan123 made their first contribution in https://github.com/lance-format/lance/pull/5252
* @Pmathsun made their first contribution in https://github.com/lance-format/lance/pull/5332
* @ztorchan made their first contribution in https://github.com/lance-format/lance/pull/5301
* @fMeow made their first contribution in https://github.com/lance-format/lance/pull/5371

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/1.0.0-beta.N...v1.0.0-rc.3
### Release: lance [v1.1.0-beta.2](https://github.com/lance-format/lance/releases/tag/v1.1.0-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v1.1.0-beta.2 -->

## What's Changed
### New Features 🎉
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
### Bug Fixes 🐛
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
* fix: take_blobs_by_indices fails with stable row IDs on fragment 1+ by @jmhsieh in https://github.com/lance-format/lance/pull/5392
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387


**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/1.1.0-beta.N...v1.1.0-beta.2
### Release: lance [v1.1.0-beta.1](https://github.com/lance-format/lance/releases/tag/v1.1.0-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.1.0-beta.1 -->

## What's Changed
### New Features 🎉
* feat(blob_v2): add external blob support by @Xuanwo in https://github.com/lance-format/lance/pull/5385
### Bug Fixes 🐛
* fix: don't allow change blob version during update by @Xuanwo in https://github.com/lance-format/lance/pull/5386
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5395
### Other Changes
* refactor: rename RowIdTreeMap to RowAddrTreeMap by @yanghua in https://github.com/lance-format/lance/pull/5266
* refactor: split dataset tests in a tests mod by @Xuanwo in https://github.com/lance-format/lance/pull/5387


**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/1.1.0-beta.N...v1.1.0-beta.1
### Release: lance [v1.0.0-rc.2](https://github.com/lance-format/lance/releases/tag/v1.0.0-rc.2)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.0-rc.2 -->

## What's Changed
### Breaking Changes 🛠
* perf!: dynamic pruning for vector search by @BubbleCal in https://github.com/lance-format/lance/pull/4773
* feat!: remove unnecessary mut of dataset::sql by @ddupg in https://github.com/lance-format/lance/pull/5207
* refactor!: move all previous code into `previous` mod by @Xuanwo in https://github.com/lance-format/lance/pull/5217
* refactor!: deprecate TFRecord support by @jackye1995 in https://github.com/lance-format/lance/pull/4593
* refactor!: use org.lance namespace for java package by @jackye1995 in https://github.com/lance-format/lance/pull/5339
* refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lance-format/lance/pull/5391
### Critical Fixes ‼️
* fix: convert some panics into errors by @wjones127 in https://github.com/lance-format/lance/pull/5258
### New Features 🎉
* feat: provide inline_transaction model for IO optimizing by @majin1102 in https://github.com/lance-format/lance/pull/4774
* feat(python): add support for HuggingFace IterableDataset by @changhiskhan in https://github.com/lance-format/lance/pull/2599
* feat: add public accessors for count plan construction by @wkalt in https://github.com/lance-format/lance/pull/5103
* feat: add adapter for REST namespace with manifest namespace backend by @jackye1995 in https://github.com/lance-format/lance/pull/4984
* feat: add blob compaction support by @Xuanwo in https://github.com/lance-format/lance/pull/5189
* feat: add inline optimization for dir namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5244
* feat: conflict resolution for DataReplacement by @wjones127 in https://github.com/lance-format/lance/pull/3631
* feat: support namespace vended credentials for write by @jackye1995 in https://github.com/lance-format/lance/pull/5161
* docs: correct the comment in util.py by @shiyajuan123 in https://github.com/lance-format/lance/pull/5252
* feat: introduce community governance by @jackye1995 in https://github.com/lance-format/lance/pull/5262
* feat: add describe_indices function by @westonpace in https://github.com/lance-format/lance/pull/5221
* feat: add target_bases extension to python write_fragments API by @jaystarshot in https://github.com/lance-format/lance/pull/5234
* feat: support credentials vending for file reader and session by @jackye1995 in https://github.com/lance-format/lance/pull/5256
* feat: introduce blob arrow extension type by @Xuanwo in https://github.com/lance-format/lance/pull/5239
* feat(java): add binding for rest and dir namespaces by @jackye1995 in https://github.com/lance-format/lance/pull/5292
* feat: expose file upload and download in Lance file session by @jackye1995 in https://github.com/lance-format/lance/pull/5336
* feat(java): support credential vending at write time by @jackye1995 in https://github.com/lance-format/lance/pull/5309
* feat(ds-sql-api): support JSON bulit in functions in ds.sql API by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5350
* feat: support GEO types by @ddupg in https://github.com/lance-format/lance/pull/4678
* feat(python): expose DatasetDeltaBuilder and relevant apis by @yanghua in https://github.com/lance-format/lance/pull/5091
* feat: return Unprocessable error while expected error happened by @Xuanwo in https://github.com/lance-format/lance/pull/5347
* feat: add huggingface native support by @Xuanwo in https://github.com/lance-format/lance/pull/5353
* feat: dynamically choose distance type by @BubbleCal in https://github.com/lance-format/lance/pull/5370
* feat(java): support writing schema metadata through java LanceFileWriter API by @steFaiz in https://github.com/lance-format/lance/pull/5310
### Bug Fixes 🐛
* fix: ensure recheck for IsNotNull in bloom filter by @Xuanwo in https://github.com/lance-format/lance/pull/5192
* fix: contributing URL gives 404 by @prrao87 in https://github.com/lance-format/lance/pull/5196
* fix: merge struct array use wrong child values by @wojiaodoubao in https://github.com/lance-format/lance/pull/5106
* fix: avoid unnecessary get_fragments calling during plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5179
* fix: split partition may be assigned to itself by @BubbleCal in https://github.com/lance-format/lance/pull/5190
* fix: improve schema validation for nullability and subschemas by @fenfeng9 in https://github.com/lance-format/lance/pull/4994
* fix: compile error in test_inline_transaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5206
* docs: fix batch udf with checkpoint document error by @fangyinc in https://github.com/lance-format/lance/pull/5185
* fix: memory-limited string BTREE index building by @wjones127 in https://github.com/lance-format/lance/pull/5175
* fix: home page code snippets cuasing various problems by @jackye1995 in https://github.com/lance-format/lance/pull/5245
* fix: panic if only one partition and split is triggered by @BubbleCal in https://github.com/lance-format/lance/pull/5241
* fix: clearer error in dataset take by @wkalt in https://github.com/lance-format/lance/pull/5243
* fix: docs and comment have broken links by @prrao87 in https://github.com/lance-format/lance/pull/5261
* fix: handle logical rows deletion properly for zonemap and bloomfilter by @HaochengLIU in https://github.com/lance-format/lance/pull/5140
* fix: blob version should be passed in Projection by @Xuanwo in https://github.com/lance-format/lance/pull/5295
* docs: fix broken links and 404s by @prrao87 in https://github.com/lance-format/lance/pull/5284
* fix: index overestimates the posting list size by @BubbleCal in https://github.com/lance-format/lance/pull/5327
* fix: update CachedFileMetadata version API to V2.0 by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5330
* fix: correctly handle OSS commit protocol to prevent data loss by @Pmathsun in https://github.com/lance-format/lance/pull/5332
* fix: update btree index with its own zone size instead of DEFAULT_BTR… by @ztorchan in https://github.com/lance-format/lance/pull/5301
* fix: join job may cause inconsistent delta indices by @BubbleCal in https://github.com/lance-format/lance/pull/5328
* fix: panicException when calling compaction by @yanghua in https://github.com/lance-format/lance/pull/5282
* fix: parallelize bitmap partition loading in IsIn expressions by @wkalt in https://github.com/lance-format/lance/pull/5355
* fix: avx512 related symbol not found in mac x86 by @jackye1995 in https://github.com/lance-format/lance/pull/5379
* fix: add graceful shutdown and start for rest namespace adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5325
* fix: respect index metric when user overrides by @BubbleCal in https://github.com/lance-format/lance/pull/5397
### Documentation 📚
* docs: introduce lance as a lakehouse format by @jackye1995 in https://github.com/lance-format/lance/pull/5209
* docs: update readme with latest lakehouse format info by @jackye1995 in https://github.com/lance-format/lance/pull/5216
* docs: capitalization change by @timsaucer in https://github.com/lance-format/lance/pull/5269
* docs: build project specific guidelines into web doc by @jackye1995 in https://github.com/lance-format/lance/pull/5324
### Performance Improvements 🚀
* perf: speed up filtered scan by up to 18.9× by moving the heavy CPU task out by @Xuanwo in https://github.com/lance-format/lance/pull/5165
* perf: parallelize split job assigning by @BubbleCal in https://github.com/lance-format/lance/pull/5265
* perf: use CPU pool to run WAND algo by @BubbleCal in https://github.com/lance-format/lance/pull/5363
* perf: avoid allocating filtered nodes on HNSW search path by @BubbleCal in https://github.com/lance-format/lance/pull/5377
### Other Changes
* refactor: move blob version as a table level config by @Xuanwo in https://github.com/lance-format/lance/pull/5220
* refactor: add helper functions to delta.rs tests by @yanghua in https://github.com/lance-format/lance/pull/5298
* refactor: move LanceNamespace interface to pylance and java lance-core by @jackye1995 in https://github.com/lance-format/lance/pull/5345
* refactor: allow datafiles to contain columns without field id by @Xuanwo in https://github.com/lance-format/lance/pull/5348
* refactor: rename RowIdSelection to RowAddrSelection by @yanghua in https://github.com/lance-format/lance/pull/5263
* refactor: separate out python and java LanceNamespace interface by @jackye1995 in https://github.com/lance-format/lance/pull/5364
* refactor: align with blob v2 logical types change by @Xuanwo in https://github.com/lance-format/lance/pull/5375

## New Contributors
* @prrao87 made their first contribution in https://github.com/lance-format/lance/pull/5196
* @fenfeng9 made their first contribution in https://github.com/lance-format/lance/pull/4994
* @fangyinc made their first contribution in https://github.com/lance-format/lance/pull/5185
* @shiyajuan123 made their first contribution in https://github.com/lance-format/lance/pull/5252
* @Pmathsun made their first contribution in https://github.com/lance-format/lance/pull/5332
* @ztorchan made their first contribution in https://github.com/lance-format/lance/pull/5301
* @fMeow made their first contribution in https://github.com/lance-format/lance/pull/5371

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/1.0.0-beta.N...v1.0.0-rc.2
### Release: lance [v1.0.0-rc.1](https://github.com/lance-format/lance/releases/tag/v1.0.0-rc.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.0-rc.1 -->

## What's Changed
### Breaking Changes 🛠
* perf!: dynamic pruning for vector search by @BubbleCal in https://github.com/lance-format/lance/pull/4773
* feat!: remove unnecessary mut of dataset::sql by @ddupg in https://github.com/lance-format/lance/pull/5207
* refactor!: move all previous code into `previous` mod by @Xuanwo in https://github.com/lance-format/lance/pull/5217
* refactor!: deprecate TFRecord support by @jackye1995 in https://github.com/lance-format/lance/pull/4593
* refactor!: use org.lance namespace for java package by @jackye1995 in https://github.com/lance-format/lance/pull/5339
* refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lance-format/lance/pull/5391
### Critical Fixes ‼️
* fix: convert some panics into errors by @wjones127 in https://github.com/lance-format/lance/pull/5258
### New Features 🎉
* feat: provide inline_transaction model for IO optimizing by @majin1102 in https://github.com/lance-format/lance/pull/4774
* feat(python): add support for HuggingFace IterableDataset by @changhiskhan in https://github.com/lance-format/lance/pull/2599
* feat: add public accessors for count plan construction by @wkalt in https://github.com/lance-format/lance/pull/5103
* feat: add adapter for REST namespace with manifest namespace backend by @jackye1995 in https://github.com/lance-format/lance/pull/4984
* feat: add blob compaction support by @Xuanwo in https://github.com/lance-format/lance/pull/5189
* feat: add inline optimization for dir namespace by @jackye1995 in https://github.com/lance-format/lance/pull/5244
* feat: conflict resolution for DataReplacement by @wjones127 in https://github.com/lance-format/lance/pull/3631
* feat: support namespace vended credentials for write by @jackye1995 in https://github.com/lance-format/lance/pull/5161
* docs: correct the comment in util.py by @shiyajuan123 in https://github.com/lance-format/lance/pull/5252
* feat: introduce community governance by @jackye1995 in https://github.com/lance-format/lance/pull/5262
* feat: add describe_indices function by @westonpace in https://github.com/lance-format/lance/pull/5221
* feat: add target_bases extension to python write_fragments API by @jaystarshot in https://github.com/lance-format/lance/pull/5234
* feat: support credentials vending for file reader and session by @jackye1995 in https://github.com/lance-format/lance/pull/5256
* feat: introduce blob arrow extension type by @Xuanwo in https://github.com/lance-format/lance/pull/5239
* feat(java): add binding for rest and dir namespaces by @jackye1995 in https://github.com/lance-format/lance/pull/5292
* feat: expose file upload and download in Lance file session by @jackye1995 in https://github.com/lance-format/lance/pull/5336
* feat(java): support credential vending at write time by @jackye1995 in https://github.com/lance-format/lance/pull/5309
* feat(ds-sql-api): support JSON bulit in functions in ds.sql API by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5350
* feat: support GEO types by @ddupg in https://github.com/lance-format/lance/pull/4678
* feat(python): expose DatasetDeltaBuilder and relevant apis by @yanghua in https://github.com/lance-format/lance/pull/5091
* feat: return Unprocessable error while expected error happened by @Xuanwo in https://github.com/lance-format/lance/pull/5347
* feat: add huggingface native support by @Xuanwo in https://github.com/lance-format/lance/pull/5353
* feat: dynamically choose distance type by @BubbleCal in https://github.com/lance-format/lance/pull/5370
* feat(java): support writing schema metadata through java LanceFileWriter API by @steFaiz in https://github.com/lance-format/lance/pull/5310
### Bug Fixes 🐛
* fix: ensure recheck for IsNotNull in bloom filter by @Xuanwo in https://github.com/lance-format/lance/pull/5192
* fix: contributing URL gives 404 by @prrao87 in https://github.com/lance-format/lance/pull/5196
* fix: merge struct array use wrong child values by @wojiaodoubao in https://github.com/lance-format/lance/pull/5106
* fix: avoid unnecessary get_fragments calling during plan compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5179
* fix: split partition may be assigned to itself by @BubbleCal in https://github.com/lance-format/lance/pull/5190
* fix: improve schema validation for nullability and subschemas by @fenfeng9 in https://github.com/lance-format/lance/pull/4994
* fix: compile error in test_inline_transaction by @wojiaodoubao in https://github.com/lance-format/lance/pull/5206
* docs: fix batch udf with checkpoint document error by @fangyinc in https://github.com/lance-format/lance/pull/5185
* fix: memory-limited string BTREE index building by @wjones127 in https://github.com/lance-format/lance/pull/5175
* fix: home page code snippets cuasing various problems by @jackye1995 in https://github.com/lance-format/lance/pull/5245
* fix: panic if only one partition and split is triggered by @BubbleCal in https://github.com/lance-format/lance/pull/5241
* fix: clearer error in dataset take by @wkalt in https://github.com/lance-format/lance/pull/5243
* fix: docs and comment have broken links by @prrao87 in https://github.com/lance-format/lance/pull/5261
* fix: handle logical rows deletion properly for zonemap and bloomfilter by @HaochengLIU in https://github.com/lance-format/lance/pull/5140
* fix: blob version should be passed in Projection by @Xuanwo in https://github.com/lance-format/lance/pull/5295
* docs: fix broken links and 404s by @prrao87 in https://github.com/lance-format/lance/pull/5284
* fix: index overestimates the posting list size by @BubbleCal in https://github.com/lance-format/lance/pull/5327
* fix: update CachedFileMetadata version API to V2.0 by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5330
* fix: correctly handle OSS commit protocol to prevent data loss by @Pmathsun in https://github.com/lance-format/lance/pull/5332
* fix: update btree index with its own zone size instead of DEFAULT_BTR… by @ztorchan in https://github.com/lance-format/lance/pull/5301
* fix: join job may cause inconsistent delta indices by @BubbleCal in https://github.com/lance-format/lance/pull/5328
* fix: panicException when calling compaction by @yanghua in https://github.com/lance-format/lance/pull/5282
* fix: parallelize bitmap partition loading in IsIn expressions by @wkalt in https://github.com/lance-format/lance/pull/5355
* fix: avx512 related symbol not found in mac x86 by @jackye1995 in https://github.com/lance-format/lance/pull/5379
* fix: add graceful shutdown and start for rest namespace adapter by @jackye1995 in https://github.com/lance-format/lance/pull/5325
### Documentation 📚
* docs: introduce lance as a lakehouse format by @jackye1995 in https://github.com/lance-format/lance/pull/5209
* docs: update readme with latest lakehouse format info by @jackye1995 in https://github.com/lance-format/lance/pull/5216
* docs: capitalization change by @timsaucer in https://github.com/lance-format/lance/pull/5269
* docs: build project specific guidelines into web doc by @jackye1995 in https://github.com/lance-format/lance/pull/5324
### Performance Improvements 🚀
* perf: speed up filtered scan by up to 18.9× by moving the heavy CPU task out by @Xuanwo in https://github.com/lance-format/lance/pull/5165
* perf: parallelize split job assigning by @BubbleCal in https://github.com/lance-format/lance/pull/5265
* perf: use CPU pool to run WAND algo by @BubbleCal in https://github.com/lance-format/lance/pull/5363
* perf: avoid allocating filtered nodes on HNSW search path by @BubbleCal in https://github.com/lance-format/lance/pull/5377
### Other Changes
* refactor: move blob version as a table level config by @Xuanwo in https://github.com/lance-format/lance/pull/5220
* refactor: add helper functions to delta.rs tests by @yanghua in https://github.com/lance-format/lance/pull/5298
* refactor: move LanceNamespace interface to pylance and java lance-core by @jackye1995 in https://github.com/lance-format/lance/pull/5345
* refactor: allow datafiles to contain columns without field id by @Xuanwo in https://github.com/lance-format/lance/pull/5348
* refactor: rename RowIdSelection to RowAddrSelection by @yanghua in https://github.com/lance-format/lance/pull/5263
* refactor: separate out python and java LanceNamespace interface by @jackye1995 in https://github.com/lance-format/lance/pull/5364
* refactor: align with blob v2 logical types change by @Xuanwo in https://github.com/lance-format/lance/pull/5375

## New Contributors
* @prrao87 made their first contribution in https://github.com/lance-format/lance/pull/5196
* @fenfeng9 made their first contribution in https://github.com/lance-format/lance/pull/4994
* @fangyinc made their first contribution in https://github.com/lance-format/lance/pull/5185
* @shiyajuan123 made their first contribution in https://github.com/lance-format/lance/pull/5252
* @Pmathsun made their first contribution in https://github.com/lance-format/lance/pull/5332
* @ztorchan made their first contribution in https://github.com/lance-format/lance/pull/5301
* @fMeow made their first contribution in https://github.com/lance-format/lance/pull/5371

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/1.0.0-beta.N...v1.0.0-rc.1
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 12 releases: ['Node/Rust LanceDB v0.23.1-beta.1', 'Node/Rust LanceDB v0.23.1-beta.0', 'Python LanceDB v0.26.1-beta.1', 'Python LanceDB v0.26.1-beta.0', 'Node/Rust LanceDB v0.23.0', 'Python LanceDB v0.26.0', 'Node/Rust LanceDB v0.23.0-beta.1', 'Python LanceDB v0.26.0-beta.1', 'Node/Rust LanceDB v0.23.0-beta.0', 'Python LanceDB v0.26.0-beta.0', 'Node/Rust LanceDB v0.22.4-beta.3', 'Python LanceDB v0.25.4-beta.3']
### Release: lancedb [Node/Rust LanceDB v0.23.1-beta.1](https://github.com/lancedb/lancedb/releases/tag/v0.23.1-beta.1)
## 🐛 Bug Fixes

- fix: pass namespace storage options provider into native table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2873


### Release: lancedb [Node/Rust LanceDB v0.23.1-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.23.1-beta.0)
## 🐛 Bug Fixes

- fix: use post for describe_namespace and allow access to underlying client by @jackye1995 in https://github.com/lancedb/lancedb/pull/2871


### Release: lancedb [Python LanceDB v0.26.1-beta.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.26.1-beta.1)
## 🐛 Bug Fixes

- fix: pass namespace storage options provider into native table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2873


### Release: lancedb [Python LanceDB v0.26.1-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.26.1-beta.0)
## 🐛 Bug Fixes

- fix: use post for describe_namespace and allow access to underlying client by @jackye1995 in https://github.com/lancedb/lancedb/pull/2871


### Release: lancedb [Node/Rust LanceDB v0.23.0](https://github.com/lancedb/lancedb/releases/tag/v0.23.0)
## 🛠 Breaking Changes

- refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lancedb/lancedb/pull/2836
- refactor!: use namespace models directly for namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2806

## 🎉 New Features

- feat: pare down docs to only show API refs by @prrao87 in https://github.com/lancedb/lancedb/pull/2770
- feat: bump lance version to 0.40-0-beta.2 by @cmccabe in https://github.com/lancedb/lancedb/pull/2772
- feat: let lance determine the default num_partitions param by @BubbleCal in https://github.com/lancedb/lancedb/pull/2775
- feat: support namespace credentials vending by @jackye1995 in https://github.com/lancedb/lancedb/pull/2778
- feat: add num_attempts to merge insert result by @wkalt in https://github.com/lancedb/lancedb/pull/2795
- feat(python): support `to_pydantic` in async by @mykolaskrynnyk in https://github.com/lancedb/lancedb/pull/2438
- feat: support async namespace connection by @jackye1995 in https://github.com/lancedb/lancedb/pull/2788
- feat: implement head() for remote tables by @cmccabe in https://github.com/lancedb/lancedb/pull/2793
- feat: update codex url key by @wkalt in https://github.com/lancedb/lancedb/pull/2812
- feat: remove remote default features on lance-namespace-impls by @valkum in https://github.com/lancedb/lancedb/pull/2828
- feat: support stable row IDs via storage_options by @jmhsieh in https://github.com/lancedb/lancedb/pull/2831
- feat: support namespace server side query by @jackye1995 in https://github.com/lancedb/lancedb/pull/2811
- feat: add IVF SQ index support and HNSW aliases by @BubbleCal in https://github.com/lancedb/lancedb/pull/2832
- feat: use rest namespace for lancedb java sdk by @jackye1995 in https://github.com/lancedb/lancedb/pull/2845
- feat: make java client builder generic by @jackye1995 in https://github.com/lancedb/lancedb/pull/2851
- feat: infer vector type to float32 if integers are out of uint8 range by @BubbleCal in https://github.com/lancedb/lancedb/pull/2856
- feat: upgrade lance-namespace python to 0.3.2 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2868

## 🐛 Bug Fixes

- docs: update readme quickstart link (under how to install) by @erik-wang-lancedb in https://github.com/lancedb/lancedb/pull/2780
- feat: support namespace credentials vending by @jackye1995 in https://github.com/lancedb/lancedb/pull/2778
- fix: convert schema metadata to strings for JsonArrowSchema by @rpgreen in https://github.com/lancedb/lancedb/pull/2786
- fix: use None default for namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2797
- fix: .phrase_query() not working by @jachewz in https://github.com/lancedb/lancedb/pull/2781
- fix: table_names error at root namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2842

## 📚 Documentation

- docs: update readme quickstart link (under how to install) by @erik-wang-lancedb in https://github.com/lancedb/lancedb/pull/2780
- docs: add some missing classes by @wjones127 in https://github.com/lancedb/lancedb/pull/2450
- docs: 404 and outdated URLs should now work by @prrao87 in https://github.com/lancedb/lancedb/pull/2800
- docs: nodejs failing CI is fixed by @prrao87 in https://github.com/lancedb/lancedb/pull/2802
- docs: improve docstring for RabitQ in Python by @prrao87 in https://github.com/lancedb/lancedb/pull/2808

## 🔧 Build and CI

- ci: migrate codex to API key based by @Xuanwo in https://github.com/lancedb/lancedb/pull/2783
- ci: make rust ci faster, get ci green by @wjones127 in https://github.com/lancedb/lancedb/pull/2782
- ci: add timely lance release check by @Xuanwo in https://github.com/lancedb/lancedb/pull/2790
- ci: use larger runner for doctest and fix failing tests by @jackye1995 in https://github.com/lancedb/lancedb/pull/2801
- ci: add support for lance-format fury index for downloading pylance by @jackye1995 in https://github.com/lancedb/lancedb/pull/2804
- ci: trigger downstream verification after version bump by @jackye1995 in https://github.com/lancedb/lancedb/pull/2809
- ci: migrate macos ci runners by @Xuanwo in https://github.com/lancedb/lancedb/pull/2818


### Release: lancedb [Python LanceDB v0.26.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.26.0)
## 🛠 Breaking Changes

- refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lancedb/lancedb/pull/2836
- refactor!: use namespace models directly for namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2806

## 🎉 New Features

- feat: pare down docs to only show API refs by @prrao87 in https://github.com/lancedb/lancedb/pull/2770
- feat: bump lance version to 0.40-0-beta.2 by @cmccabe in https://github.com/lancedb/lancedb/pull/2772
- feat: let lance determine the default num_partitions param by @BubbleCal in https://github.com/lancedb/lancedb/pull/2775
- feat: support namespace credentials vending by @jackye1995 in https://github.com/lancedb/lancedb/pull/2778
- feat: add num_attempts to merge insert result by @wkalt in https://github.com/lancedb/lancedb/pull/2795
- feat(python): support `to_pydantic` in async by @mykolaskrynnyk in https://github.com/lancedb/lancedb/pull/2438
- feat: support async namespace connection by @jackye1995 in https://github.com/lancedb/lancedb/pull/2788
- feat: implement head() for remote tables by @cmccabe in https://github.com/lancedb/lancedb/pull/2793
- feat: update codex url key by @wkalt in https://github.com/lancedb/lancedb/pull/2812
- feat: remove remote default features on lance-namespace-impls by @valkum in https://github.com/lancedb/lancedb/pull/2828
- feat: support stable row IDs via storage_options by @jmhsieh in https://github.com/lancedb/lancedb/pull/2831
- feat: support namespace server side query by @jackye1995 in https://github.com/lancedb/lancedb/pull/2811
- feat: add IVF SQ index support and HNSW aliases by @BubbleCal in https://github.com/lancedb/lancedb/pull/2832
- feat: use rest namespace for lancedb java sdk by @jackye1995 in https://github.com/lancedb/lancedb/pull/2845
- feat: make java client builder generic by @jackye1995 in https://github.com/lancedb/lancedb/pull/2851
- feat: infer vector type to float32 if integers are out of uint8 range by @BubbleCal in https://github.com/lancedb/lancedb/pull/2856
- feat: upgrade lance-namespace python to 0.3.2 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2868

## 🐛 Bug Fixes

- docs: update readme quickstart link (under how to install) by @erik-wang-lancedb in https://github.com/lancedb/lancedb/pull/2780
- feat: support namespace credentials vending by @jackye1995 in https://github.com/lancedb/lancedb/pull/2778
- fix: convert schema metadata to strings for JsonArrowSchema by @rpgreen in https://github.com/lancedb/lancedb/pull/2786
- fix: use None default for namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2797
- fix: .phrase_query() not working by @jachewz in https://github.com/lancedb/lancedb/pull/2781
- fix: table_names error at root namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2842

## 📚 Documentation

- docs: update readme quickstart link (under how to install) by @erik-wang-lancedb in https://github.com/lancedb/lancedb/pull/2780
- docs: add some missing classes by @wjones127 in https://github.com/lancedb/lancedb/pull/2450
- docs: 404 and outdated URLs should now work by @prrao87 in https://github.com/lancedb/lancedb/pull/2800
- docs: nodejs failing CI is fixed by @prrao87 in https://github.com/lancedb/lancedb/pull/2802
- docs: improve docstring for RabitQ in Python by @prrao87 in https://github.com/lancedb/lancedb/pull/2808

## 🔧 Build and CI

- ci: migrate codex to API key based by @Xuanwo in https://github.com/lancedb/lancedb/pull/2783
- ci: make rust ci faster, get ci green by @wjones127 in https://github.com/lancedb/lancedb/pull/2782
- ci: add timely lance release check by @Xuanwo in https://github.com/lancedb/lancedb/pull/2790
- ci: use larger runner for doctest and fix failing tests by @jackye1995 in https://github.com/lancedb/lancedb/pull/2801
- ci: add support for lance-format fury index for downloading pylance by @jackye1995 in https://github.com/lancedb/lancedb/pull/2804
- ci: trigger downstream verification after version bump by @jackye1995 in https://github.com/lancedb/lancedb/pull/2809
- ci: migrate macos ci runners by @Xuanwo in https://github.com/lancedb/lancedb/pull/2818


### Release: lancedb [Node/Rust LanceDB v0.23.0-beta.1](https://github.com/lancedb/lancedb/releases/tag/v0.23.0-beta.1)
## 🎉 New Features

- feat: use rest namespace for lancedb java sdk by @jackye1995 in https://github.com/lancedb/lancedb/pull/2845
- feat: make java client builder generic by @jackye1995 in https://github.com/lancedb/lancedb/pull/2851


### Release: lancedb [Python LanceDB v0.26.0-beta.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.26.0-beta.1)
## 🎉 New Features

- feat: use rest namespace for lancedb java sdk by @jackye1995 in https://github.com/lancedb/lancedb/pull/2845
- feat: make java client builder generic by @jackye1995 in https://github.com/lancedb/lancedb/pull/2851


### Release: lancedb [Node/Rust LanceDB v0.23.0-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.23.0-beta.0)
## 🛠 Breaking Changes

- refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lancedb/lancedb/pull/2836
- refactor!: use namespace models directly for namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2806

## 🎉 New Features

- feat: support namespace server side query by @jackye1995 in https://github.com/lancedb/lancedb/pull/2811
- feat: add IVF SQ index support and HNSW aliases by @BubbleCal in https://github.com/lancedb/lancedb/pull/2832

## 🐛 Bug Fixes

- fix: table_names error at root namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2842


### Release: lancedb [Python LanceDB v0.26.0-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.26.0-beta.0)
## 🛠 Breaking Changes

- refactor!: deprecate mac x86 support by @jackye1995 in https://github.com/lancedb/lancedb/pull/2836
- refactor!: use namespace models directly for namespace operations by @jackye1995 in https://github.com/lancedb/lancedb/pull/2806

## 🎉 New Features

- feat: support namespace server side query by @jackye1995 in https://github.com/lancedb/lancedb/pull/2811
- feat: add IVF SQ index support and HNSW aliases by @BubbleCal in https://github.com/lancedb/lancedb/pull/2832

## 🐛 Bug Fixes

- fix: table_names error at root namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2842


### Release: lancedb [Node/Rust LanceDB v0.22.4-beta.3](https://github.com/lancedb/lancedb/releases/tag/v0.22.4-beta.3)
## 🎉 New Features

- feat: implement head() for remote tables by @cmccabe in https://github.com/lancedb/lancedb/pull/2793
- feat: update codex url key by @wkalt in https://github.com/lancedb/lancedb/pull/2812
- feat: remove remote default features on lance-namespace-impls by @valkum in https://github.com/lancedb/lancedb/pull/2828
- feat: support stable row IDs via storage_options by @jmhsieh in https://github.com/lancedb/lancedb/pull/2831

## 🐛 Bug Fixes

- fix: use None default for namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2797
- fix: .phrase_query() not working by @jachewz in https://github.com/lancedb/lancedb/pull/2781

## 📚 Documentation

- docs: add some missing classes by @wjones127 in https://github.com/lancedb/lancedb/pull/2450
- docs: 404 and outdated URLs should now work by @prrao87 in https://github.com/lancedb/lancedb/pull/2800
- docs: nodejs failing CI is fixed by @prrao87 in https://github.com/lancedb/lancedb/pull/2802
- docs: improve docstring for RabitQ in Python by @prrao87 in https://github.com/lancedb/lancedb/pull/2808

## 🔧 Build and CI

- ci: use larger runner for doctest and fix failing tests by @jackye1995 in https://github.com/lancedb/lancedb/pull/2801
- ci: add support for lance-format fury index for downloading pylance by @jackye1995 in https://github.com/lancedb/lancedb/pull/2804
- ci: trigger downstream verification after version bump by @jackye1995 in https://github.com/lancedb/lancedb/pull/2809
- ci: migrate macos ci runners by @Xuanwo in https://github.com/lancedb/lancedb/pull/2818


### Release: lancedb [Python LanceDB v0.25.4-beta.3](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.4-beta.3)
## 🎉 New Features

- feat: implement head() for remote tables by @cmccabe in https://github.com/lancedb/lancedb/pull/2793
- feat: update codex url key by @wkalt in https://github.com/lancedb/lancedb/pull/2812
- feat: remove remote default features on lance-namespace-impls by @valkum in https://github.com/lancedb/lancedb/pull/2828
- feat: support stable row IDs via storage_options by @jmhsieh in https://github.com/lancedb/lancedb/pull/2831

## 🐛 Bug Fixes

- fix: use None default for namespace by @jackye1995 in https://github.com/lancedb/lancedb/pull/2797
- fix: .phrase_query() not working by @jachewz in https://github.com/lancedb/lancedb/pull/2781

## 📚 Documentation

- docs: add some missing classes by @wjones127 in https://github.com/lancedb/lancedb/pull/2450
- docs: 404 and outdated URLs should now work by @prrao87 in https://github.com/lancedb/lancedb/pull/2800
- docs: nodejs failing CI is fixed by @prrao87 in https://github.com/lancedb/lancedb/pull/2802
- docs: improve docstring for RabitQ in Python by @prrao87 in https://github.com/lancedb/lancedb/pull/2808

## 🔧 Build and CI

- ci: use larger runner for doctest and fix failing tests by @jackye1995 in https://github.com/lancedb/lancedb/pull/2801
- ci: add support for lance-format fury index for downloading pylance by @jackye1995 in https://github.com/lancedb/lancedb/pull/2804
- ci: trigger downstream verification after version bump by @jackye1995 in https://github.com/lancedb/lancedb/pull/2809
- ci: migrate macos ci runners by @Xuanwo in https://github.com/lancedb/lancedb/pull/2818


## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers?tab=readme-ov-file#datafusion-table-providers), 4 releases: ['v0.9.2', 'v0.9.1', 'v0.9.0', 'v0.8.2']
### Release: datafusion-table-providers [v0.9.2](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.2)
## What's Changed
* Add write support for Decimal32 and Decimal64 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/519


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.1...v0.9.2
### Release: datafusion-table-providers [v0.9.1](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.1)
## What's Changed
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/505
* Prevent `InsertBuilder` from taking ownership of record batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/518


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.0...v0.9.1
### Release: datafusion-table-providers [v0.9.0](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.0)
## What's Changed
* deps: point r2d2-adbc at deployed crates.io version by @zeroshade in https://github.com/datafusion-contrib/datafusion-table-providers/pull/486
* Upgrade rusqlite to v0.37 & tokio-rusqlite to v0.7 by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/495
* Upgrade to `datafusion` 51, `arrow` 57 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/497


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.8.2...v0.9.0
### Release: datafusion-table-providers [v0.8.2](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.8.2)
## What's Changed
* feat: [sqlite] Delegate supports_filters_pushdown to read provider by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/454
* Bump insta from 1.43.1 to 1.43.2 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/445
* Bump serde_json from 1.0.140 to 1.0.145 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/447
* Bump bollard from 0.19.1 to 0.19.3 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/449
* Bump serde from 1.0.225 to 1.0.228 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/448
* feat: [sqlite] Batch insert using prepared statements by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/453
* Upgrade Rust toolchain from 1.86 to 1.89 by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/456
* Use a Actions feature matrix to improve build times by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/458
* Add Rust caching to PR workflow to improve performance by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/460
* Bump snafu from 0.8.6 to 0.8.9 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/462
* Bump astral-sh/setup-uv from 5 to 7 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/461
* Bump anyhow from 1.0.98 to 1.0.100 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/463
* Bump tracing-subscriber from 0.3.19 to 0.3.20 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/465
* Bump sea-query from 0.32.6 to 0.32.7 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/464
* Bump tracing-subscriber from 0.3.19 to 0.3.20 in the cargo group across 1 directory by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/459
* Add table provider for ADBC drivers by @zeroshade in https://github.com/datafusion-contrib/datafusion-table-providers/pull/481


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.8.1...v0.8.2
## Project: [duckdb/duckdb](https://duckdb.org/), 1 releases: ['v1.4.3 Bugfix Release']
### Release: duckdb [v1.4.3 Bugfix Release](https://github.com/duckdb/duckdb/releases/tag/v1.4.3)
This is a bug fix release for various issues discovered after we released 1.4.2.

## What's Changed
* implement proper equals for table functions by @Maxxen in https://github.com/duckdb/duckdb/pull/19722
* Fix behavior for HAVING clause without a GROUP BY by @Tishj in https://github.com/duckdb/duckdb/pull/19739
* Remove httpfs patches and bump by @carlopi in https://github.com/duckdb/duckdb/pull/19763
* Correctly use a lock when accessing the EncryptionKeyManager by @Mytherin in https://github.com/duckdb/duckdb/pull/19772
* Bump iceberg to now default available extension by @carlopi in https://github.com/duckdb/duckdb/pull/19764
* Extract all column bindings of json each function by @Tmonster in https://github.com/duckdb/duckdb/pull/19766
* constraint violation bug fix by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/19776
* Avoid binding macro arguments for untyped macros by @lnkuiper in https://github.com/duckdb/duckdb/pull/19779
* It should probably be `${EXTENSION_CONFIG_BUILD}` instead of `EXTENSION_CONFIG_BUILD` by @hannes in https://github.com/duckdb/duckdb/pull/19694
* Fix #19575: Fix illegal utf8 character by @flashmouse in https://github.com/duckdb/duckdb/pull/19699
* chore: bump vortex to 0.56.0 by @0ax1 in https://github.com/duckdb/duckdb/pull/19815
* PositionalScan: handle also HAVE_MORE_OUTPUT + empty chunk via iteration by @carlopi in https://github.com/duckdb/duckdb/pull/19824
* AttachDatabase: first set whether file is remote, then do the rest by @carlopi in https://github.com/duckdb/duckdb/pull/19826
* Add CacheBehavior::AUTOMATIC to DBInstanceCache that automatically does the right thing™ by @Mytherin in https://github.com/duckdb/duckdb/pull/19841
* Reuse metadata even in the presence of deletes by @ywelsch in https://github.com/duckdb/duckdb/pull/19823
* DuckIndexScanState::TableScanFunc, split into 2 explicit phases by @carlopi in https://github.com/duckdb/duckdb/pull/19838
* Bump httpfs and iceberg by @carlopi in https://github.com/duckdb/duckdb/pull/19859
* Keep cte_root alive while binding materialized CTEs in MERGE INTO children by @Mytherin in https://github.com/duckdb/duckdb/pull/19863
* CI Cleanup (#19840) by @yan-alex in https://github.com/duckdb/duckdb/pull/19857
* Fix #19517: preserve relation name for table-qualified star LIKE expression by @henry8128 in https://github.com/duckdb/duckdb/pull/19887
* avoid underflow/"inf" loop while reporting unittest summary (backport… by @benfleis in https://github.com/duckdb/duckdb/pull/19900
* Fixes incorrect handing of APPROX_QUANTILE TIME by @Damon07 in https://github.com/duckdb/duckdb/pull/19891
* Add v1.4.3 to Storage Version by @maiadegraaf in https://github.com/duckdb/duckdb/pull/19907
* clean up tmp files while building extensions by @c-herrewijn in https://github.com/duckdb/duckdb/pull/19908
* Bump: ducklake, mysql_scanner by @maiadegraaf in https://github.com/duckdb/duckdb/pull/19910
* remove large limit optimization whenever there is a filter by @guillesd in https://github.com/duckdb/duckdb/pull/19911
* free disk space in Upload Extensions job by @c-herrewijn in https://github.com/duckdb/duckdb/pull/19912
* [Compression] Prevent overriding `COMPRESSION_EMPTY` with `COMPRESSION_CONSTANT` by @Tishj in https://github.com/duckdb/duckdb/pull/19913
* Make `make tidy-check-diff` compare against base branch, instead of always comparing against `origin/main` by @Mytherin in https://github.com/duckdb/duckdb/pull/19917
* More testing for appender and attach-detach by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19708
* Script to release a extension manually by @samansmink in https://github.com/duckdb/duckdb/pull/19881
* Assert that result types match with column data collection when fetching data by @pdet in https://github.com/duckdb/duckdb/pull/19750
* No longer auto-enable profiling on DEBUG mode by @maiadegraaf in https://github.com/duckdb/duckdb/pull/19931
* Fix optimizer incorrectly remove ORDER BY clause from aggregates by @tianjq16 in https://github.com/duckdb/duckdb/pull/19925
* Backport revert append fixes by @Mytherin in https://github.com/duckdb/duckdb/pull/19941
* Bump: spatial by @Maxxen in https://github.com/duckdb/duckdb/pull/19943
* Issue #19916: WASM Time Zones by @hawkfish in https://github.com/duckdb/duckdb/pull/19918
* Fix correlated column binding in ConstantBinder by @d-justen in https://github.com/duckdb/duckdb/pull/19945
* [chore] Increase slow threshold by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19965
* [Parquet] Fix prepared copy option parameter by @Tishj in https://github.com/duckdb/duckdb/pull/19966
* [TestConfig] Fix `verify_fetch_row` config, reduce duplication in `skip_tests` by @Tishj in https://github.com/duckdb/duckdb/pull/19967
* remove sha from artifacts by @c-herrewijn in https://github.com/duckdb/duckdb/pull/19957
* Unbound index binding with context by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/19953
* [Fix] Bug in `FetchRow` after update on indexed table with `dict_fsst` compression by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19970
* Null assertion on denormalized_table argument by @Dtenwolde in https://github.com/duckdb/duckdb/pull/19947
* [Art][Wal]Unbound index allocations by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/19901
* No sampling over 281TB by @Tmonster in https://github.com/duckdb/duckdb/pull/19978
* Take in consideration if the sniffer used unstrictness while selecting candidates by @pdet in https://github.com/duckdb/duckdb/pull/20005
* [CSV] Avoid throwing unnecessary errors on strict mode by @pdet in https://github.com/duckdb/duckdb/pull/20007
* [Compression] Fix an issue with NULL updates to a column compressed with DICT_FSST by @Tishj in https://github.com/duckdb/duckdb/pull/20009
* Bump: delta, ducklake, iceberg by @maiadegraaf in https://github.com/duckdb/duckdb/pull/20012
* add unity_catalog, update delta by @samansmink in https://github.com/duckdb/duckdb/pull/20019
* Bump spatial by @staticlibs in https://github.com/duckdb/duckdb/pull/20020
* Retag #19821 to v1.4 - Use PLAIN_DICTIONARY for Parquet version 1 by @pdet in https://github.com/duckdb/duckdb/pull/20024
* Fix INSERT OR REPLACE BY NAME with partial columns(#19845) by @henry8128 in https://github.com/duckdb/duckdb/pull/19989
* Bump MySQL scanner by @staticlibs in https://github.com/duckdb/duckdb/pull/20025
* Windows must sample less by @Tmonster in https://github.com/duckdb/duckdb/pull/20018
* Issue #20015: Streaming Window Sequence by @hawkfish in https://github.com/duckdb/duckdb/pull/20027
* bump iceberg by @Tmonster in https://github.com/duckdb/duckdb/pull/20032
* Fix #20014: correctly use numeric_limits<T>::min for NumericLimits::Min so that stats are initialized to -infinity for floating points by @Mytherin in https://github.com/duckdb/duckdb/pull/20039
* Enable windows_arm64 arch for main extensions by @staticlibs in https://github.com/duckdb/duckdb/pull/20004
* Fix mark join decorrelation by @kryonix in https://github.com/duckdb/duckdb/pull/20033
* propagate gate status in Node4::DeleteChild by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/20044
* Bump: httpfs by @samansmink in https://github.com/duckdb/duckdb/pull/20036
* Bump ducklake by @pdet in https://github.com/duckdb/duckdb/pull/20054
* bump azure to v1.4.3 by @benfleis in https://github.com/duckdb/duckdb/pull/20057
* Bump extensions by @samansmink in https://github.com/duckdb/duckdb/pull/20055
* Fix unnecessary dependent join rewrite by @kryonix in https://github.com/duckdb/duckdb/pull/20048
* Version tag for local files for robust external file cache validation by @lnkuiper in https://github.com/duckdb/duckdb/pull/20058
* backport runner cleanup action by @hannes in https://github.com/duckdb/duckdb/pull/20085

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.4.2...v1.4.3
## Project: [trinodb/trino](https://trino.io/docs/current/release/release-{release}.html), 1 releases: ['Trino 479']
### Release: trino [Trino 479](https://github.com/trinodb/trino/releases/tag/479)
See the [release notes](https://trino.io/docs/current/release/release-479.html) or [download Trino](https://trino.io/download)
## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers), 4 releases: ['v0.9.2', 'v0.9.1', 'v0.9.0', 'v0.8.2']
### Release: datafusion-table-providers [v0.9.2](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.2)
## What's Changed
* Add write support for Decimal32 and Decimal64 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/519


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.1...v0.9.2
### Release: datafusion-table-providers [v0.9.1](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.1)
## What's Changed
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/505
* Prevent `InsertBuilder` from taking ownership of record batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/518


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.0...v0.9.1
### Release: datafusion-table-providers [v0.9.0](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.0)
## What's Changed
* deps: point r2d2-adbc at deployed crates.io version by @zeroshade in https://github.com/datafusion-contrib/datafusion-table-providers/pull/486
* Upgrade rusqlite to v0.37 & tokio-rusqlite to v0.7 by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/495
* Upgrade to `datafusion` 51, `arrow` 57 by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/497


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.8.2...v0.9.0
### Release: datafusion-table-providers [v0.8.2](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.8.2)
## What's Changed
* feat: [sqlite] Delegate supports_filters_pushdown to read provider by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/454
* Bump insta from 1.43.1 to 1.43.2 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/445
* Bump serde_json from 1.0.140 to 1.0.145 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/447
* Bump bollard from 0.19.1 to 0.19.3 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/449
* Bump serde from 1.0.225 to 1.0.228 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/448
* feat: [sqlite] Batch insert using prepared statements by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/453
* Upgrade Rust toolchain from 1.86 to 1.89 by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/456
* Use a Actions feature matrix to improve build times by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/458
* Add Rust caching to PR workflow to improve performance by @lukekim in https://github.com/datafusion-contrib/datafusion-table-providers/pull/460
* Bump snafu from 0.8.6 to 0.8.9 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/462
* Bump astral-sh/setup-uv from 5 to 7 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/461
* Bump anyhow from 1.0.98 to 1.0.100 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/463
* Bump tracing-subscriber from 0.3.19 to 0.3.20 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/465
* Bump sea-query from 0.32.6 to 0.32.7 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/464
* Bump tracing-subscriber from 0.3.19 to 0.3.20 in the cargo group across 1 directory by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/459
* Add table provider for ADBC drivers by @zeroshade in https://github.com/datafusion-contrib/datafusion-table-providers/pull/481


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.8.1...v0.8.2
## Project: [unionai-oss/pandera](https://pandera.readthedocs.io/en/stable/index.html), 1 releases: ['Release v0.27.1: bugfix related to numpy==2.4.0']
### Release: pandera [Release v0.27.1: bugfix related to numpy==2.4.0](https://github.com/unionai-oss/pandera/releases/tag/v0.27.1)
## What's Changed
* enhancement #2122 by @Jarek-Rolski in https://github.com/unionai-oss/pandera/pull/2177
* Fix failure_cases index value for MultiIndex schema errors by @amerberg in https://github.com/unionai-oss/pandera/pull/2186
* handle new numpy 2.4.0 ValueError when type is not recognized by @cosmicBboy in https://github.com/unionai-oss/pandera/pull/2191


**Full Changelog**: https://github.com/unionai-oss/pandera/compare/v0.27.0...v0.27.1
