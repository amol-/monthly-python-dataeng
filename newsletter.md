# Complete List of Projects
 * Project: apache/arrow has 3 releases
 * Project: posit-dev/great-tables has 1 releases
 * Project: ibis-project/ibis has 1 releases
 * Project: substrait-io/substrait-python has 1 releases
 * Project: narwhals-dev/narwhals has 6 releases
 * Project: pola-rs/polars has 5 releases
 * Project: holoviz/panel has 1 releases
 * Project: holoviz/holoviews has 1 releases
 * Project: pyscript/pyscript has 4 releases
 * Project: cython/cython has 7 releases
 * Project: plotly/dash has 1 releases
 * Project: dask/dask has 2 releases
 * Project: delta-io/delta-rs has 2 releases
 * Project: lancedb/lance has 13 releases
 * Project: lancedb/lancedb has 14 releases
 * Project: trinodb/trino has 1 releases
 * Project: https://spark.apache.org/news/index.html has 1 releases
 * Project: https://velox-lib.io/blog/rss.xml has 1 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 1 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 1 articles
### Release: [Preview release of Spark 4.1.0](https://spark.apache.org/news/spark-4-1-0-preview3-released.html)

## Project: [Velox Blog](https://velox-lib.io/blog), 1 articles
### Release: [Enabling Shared Library Builds in Velox](https://velox-lib.io/blog/shared-build)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 1 articles
### Release: [Apache DataFusion Comet 0.11.0 Release](https://datafusion.apache.org/blog/2025/10/21/datafusion-comet-0.11.0)

## Project: [apache/arrow](https://arrow.apache.org/docs/python/), 3 releases: ['Apache Arrow 22.0.0', 'Apache Arrow 22.0.0 RC1', 'Apache Arrow 22.0.0 RC0']
### Release: arrow [Apache Arrow 22.0.0](https://github.com/apache/arrow/releases/tag/apache-arrow-22.0.0)
Release Notes URL: https://arrow.apache.org/release/22.0.0.html
### Release: arrow [Apache Arrow 22.0.0 RC1](https://github.com/apache/arrow/releases/tag/apache-arrow-22.0.0-rc1)
Release Notes: Release Candidate: 22.0.0 RC1
### Release: arrow [Apache Arrow 22.0.0 RC0](https://github.com/apache/arrow/releases/tag/apache-arrow-22.0.0-rc0)
Release Notes: Release Candidate: 22.0.0 RC0
## Project: [posit-dev/great-tables](https://posit-dev.github.io/great-tables/get-started/), 1 releases: ['v0.20.0']
### Release: great-tables [v0.20.0](https://github.com/posit-dev/great-tables/releases/tag/v0.20.0)
## Features

* Add `grand_summary_rows()` method by @juleswg23 in https://github.com/posit-dev/great-tables/pull/765
* Support polars expressions in vals functions by @machow in https://github.com/posit-dev/great-tables/pull/793


**Full Changelog**: https://github.com/posit-dev/great-tables/compare/v0.19.0...v0.20.0
## Project: [ibis-project/ibis](https://ibis-project.org/), 1 releases: ['11.0.0']
### Release: ibis [11.0.0](https://github.com/ibis-project/ibis/releases/tag/11.0.0)
## [11.0.0](https://github.com/ibis-project/ibis/compare/10.8.0...11.0.0) (2025-10-15)

### ⚠ BREAKING CHANGES

* **clickhouse:** adjust array indexing code for later versions of clickhouse
* **trino:** remove deprecated password parameter (#11538)
* **datatypes:** `DataType.name` is removed. Use `DataType.__class__.__name__` instead.
* **memtables:** `memtable`s can no longer be named explicitly, please use `create_table` or `create_view` to create a named object instead.
* **api:** `Struct.destructure` is removed in favor of `Table.unpack`.
* **api:** `String.to_date` is removed in favor of `String.as_date`.
* **api:** `String.to_timestamp` method is removed in favor of `String.as_timestamp`.
* **api:** `IntegerValue.to_interval` is removed. Use `IntegerValue.as_interval` instead.
* **api:** `IntegerValue.to_timestamp` is removed. Use `IntegerValue.as_timestamp` instead.
* **api:** `ibis.case()` is removed. Use `ibis.cases()` instead.
* **pyspark:** Type annotations using pd.Series/pd.DataFrame are now required per the non-deprecated PySpark Pandas UDF API.

### Features

* **databricks:** allow reads of streaming tables ([#11565](https://github.com/ibis-project/ibis/issues/11565)) ([75a944b](https://github.com/ibis-project/ibis/commit/75a944ba641ee88e21d000ad9ce53e50160f5a3c))
* **databricks:** use temporary view for memtables to avoid polluting the catalog ([#11562](https://github.com/ibis-project/ibis/issues/11562)) ([346504f](https://github.com/ibis-project/ibis/commit/346504f1a5b8586016a7fc10761e6b8ff45b44c1))
* **deps:** support duckdb 1.4.0 ([#11622](https://github.com/ibis-project/ibis/issues/11622)) ([aacf072](https://github.com/ibis-project/ibis/commit/aacf0724331b937160f848eb5c75e79ddea8b769))

### Bug Fixes

* **backends:** ensure that memtable finalizers do not hold onto references to self ([096efa3](https://github.com/ibis-project/ibis/commit/096efa3745396040a8c51e58a820b441e51ada92))
* **clickhouse:** adjust array indexing code for later versions of clickhouse ([a16f13f](https://github.com/ibis-project/ibis/commit/a16f13f3694f53eb8bebbd00c914098932e4cdce))
* **clickhouse:** ensure that sqlglot does not capitalize the `translate` function ([6fcabf5](https://github.com/ibis-project/ibis/commit/6fcabf51f73fa540c19f2b5ff152cec111431152))
* **clickhouse:** reraise non-unknown-table exceptions when running `get_schema` queries ([#11520](https://github.com/ibis-project/ibis/issues/11520)) ([c95436d](https://github.com/ibis-project/ibis/commit/c95436d6b0802947eb41fa219e11cd560582f0d1))
* **duckdb:** allow creating tables with columns containing sql keywords ([#11532](https://github.com/ibis-project/ibis/issues/11532)) ([db1a727](https://github.com/ibis-project/ibis/commit/db1a727b3c4c75e8e4af0f7ef3d0101d26d4450b))
* **duckdb:** support duckdb 1.4.1 ([f9f2363](https://github.com/ibis-project/ibis/commit/f9f23635fb2eea6bc7bc8e2b3b667033c1b20aed))
* **exasol:** ensure back compat for exasol ([93e847c](https://github.com/ibis-project/ibis/commit/93e847c676c4e043ff54ed6bbece6198c8714167))
* **flink:** update key_hack SQL for array handling ([71b50a2](https://github.com/ibis-project/ibis/commit/71b50a2bafce51cc71fb8c252e35bae7f2eca080))
* **impala:** compile to NOW instead of hive-default current_timestamp ([563cb8e](https://github.com/ibis-project/ibis/commit/563cb8ea346091733842dcc749a1f9afbb85bb4b))
* lazily import packaging so we don't depend on it in a base install ([bad3ca3](https://github.com/ibis-project/ibis/commit/bad3ca3dcd54383c1435bf327e009c9058dd9850))
* **packaging:** remove unnecessary base install requirement for `packaging` and cleanup packaging requirement for other backends ([05397d7](https://github.com/ibis-project/ibis/commit/05397d739bc9f12acc8742042eab45e3514628f8))
* **pyspark:** only register json unwraps if they are being used ([#11503](https://github.com/ibis-project/ibis/issues/11503)) ([2fc3303](https://github.com/ibis-project/ibis/commit/2fc33034412cb6d65a09303fadcee8971f27f61a))
* **snowflake:** allow expressions in window bounds ([a82631b](https://github.com/ibis-project/ibis/commit/a82631bdd4128b6eab71acf11ac31a492ac753ec))
* **typing:** harmonize Table.join and Table.*_join type hints ([c60431e](https://github.com/ibis-project/ibis/commit/c60431e74d5f0292989c3ac639861021caa3032e))

### Documentation

* **contribute:** add missing "Install just" in uv set-up guide ([68e8c55](https://github.com/ibis-project/ibis/commit/68e8c55ea45dddda3ca35ec5846f3e8394cdc21d))
* disable duckdb credential chain creation ([393da16](https://github.com/ibis-project/ibis/commit/393da1605bbdd21fc40da1553349dddaec76d07e))
* improve Value.identical_to() docstring and example ([7c8fcf7](https://github.com/ibis-project/ibis/commit/7c8fcf7da493d008e5e87c8b21951b953cd1bcd5))

### Refactors

* **api:** remove deprecated `IntegerValue.to_interval` method ([378f7ee](https://github.com/ibis-project/ibis/commit/378f7ee2553ef46abae12753d24692d8ee4eab12))
* **api:** remove deprecated `IntegerValue.to_timestamp` method ([12b92a5](https://github.com/ibis-project/ibis/commit/12b92a57f9c37dacdb36e5d45dfbcc8571843dcc))
* **api:** remove deprecated `String.to_date` method ([0d22310](https://github.com/ibis-project/ibis/commit/0d223108e6730b8aaff740af54a5e19616cd3bc4))
* **api:** remove deprecated `String.to_timestamp` method ([db4c83b](https://github.com/ibis-project/ibis/commit/db4c83be6dc89779849804767fb560b9007d0542))
* **api:** remove deprecated `Struct.destructure` method ([95caf6e](https://github.com/ibis-project/ibis/commit/95caf6ed4a0f943a3807aacbae54b8838215b162))
* **api:** remove deprecated top-level `case` function ([ce927d7](https://github.com/ibis-project/ibis/commit/ce927d7b008bc81739e55c6c2cc8bd2ecf06a033))
* **binding:** make DerefMap computation lazy and support multiple value inputs ([#11540](https://github.com/ibis-project/ibis/issues/11540)) ([5757caa](https://github.com/ibis-project/ibis/commit/5757caa4a2cefd1b64aee9ea502bab615fb67eb9))
* **datatypes:** fully remove unused DataType.name ([#11102](https://github.com/ibis-project/ibis/issues/11102)) ([8a7534c](https://github.com/ibis-project/ibis/commit/8a7534c8ef3c675229edd17f2f4467f314d0c143))
* **memtables:** remove support for problematic memtable properties ([5d35ad5](https://github.com/ibis-project/ibis/commit/5d35ad50bae9ac18140544030ebbef2b78f4905a))
* split temp table support along finalizer lines ([4e4a165](https://github.com/ibis-project/ibis/commit/4e4a165a9ab204f15c6c4dbc468f62d725563b3c))
* **trino:** remove deprecated password parameter ([#11538](https://github.com/ibis-project/ibis/issues/11538)) ([a178459](https://github.com/ibis-project/ibis/commit/a178459ad4e30cb3305ad261e62e826352b4b38a))

### Performance

* **athena:** replace `list_table_metadata` with `get_table_metadata` in `_get_schema_with_query`  ([#11573](https://github.com/ibis-project/ibis/issues/11573)) ([40b73e7](https://github.com/ibis-project/ibis/commit/40b73e751ec4834eb5191a7f6c21852c8e9a49ff))
* **athena:** use `get_table_metadata` in `get_schema` ([#11574](https://github.com/ibis-project/ibis/issues/11574)) ([e4e582a](https://github.com/ibis-project/ibis/commit/e4e582a920a7255078cb96c2769d859827b66db1))
* **binding:** only create a dereference map in `Table.bind` when needed ([#11531](https://github.com/ibis-project/ibis/issues/11531)) ([90e790c](https://github.com/ibis-project/ibis/commit/90e790c680ad12513446d6f2e459b0c731935015))

## Project: [substrait-io/substrait-python](https://substrait.io/), 1 releases: ['v0.25.0']
### Release: substrait-python [v0.25.0](https://github.com/substrait-io/substrait-python/releases/tag/v0.25.0)
## What's Changed
* fix: issue-96 function name incorrect by @mbwhite in https://github.com/substrait-io/substrait-python/pull/97
* feat: drop JSON functions and dependency on substrait-cpp by @benbellick in https://github.com/substrait-io/substrait-python/pull/100
* chore(deps): bump astral-sh/setup-uv from 6 to 7 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/103
* fix: add nullability check for NamedStruct in builder by @mbwhite in https://github.com/substrait-io/substrait-python/pull/104
* feat: advanced_extensions by @mbwhite in https://github.com/substrait-io/substrait-python/pull/105
* chore: fix and update devcontainer by @nielspardon in https://github.com/substrait-io/substrait-python/pull/108
* chore: run tests with uv by @tokoko in https://github.com/substrait-io/substrait-python/pull/106
* fix: update protobuf dependency to v5.29.5 by @nielspardon in https://github.com/substrait-io/substrait-python/pull/111
* chore(deps): bump actions/setup-node from 5 to 6 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/109
* fix: remove SHELL from devcontainer by @tokoko in https://github.com/substrait-io/substrait-python/pull/116
* chore(deps): bump actions/download-artifact from 5 to 6 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/117
* chore(deps): bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in https://github.com/substrait-io/substrait-python/pull/118
* feat: configurable registry for sql conversion by @tokoko in https://github.com/substrait-io/substrait-python/pull/115
* feat: graceful URI -> URN migration by @benbellick in https://github.com/substrait-io/substrait-python/pull/114

## New Contributors
* @mbwhite made their first contribution in https://github.com/substrait-io/substrait-python/pull/97
* @benbellick made their first contribution in https://github.com/substrait-io/substrait-python/pull/100
* @nielspardon made their first contribution in https://github.com/substrait-io/substrait-python/pull/108

**Full Changelog**: https://github.com/substrait-io/substrait-python/compare/v0.24.2...v0.25.0
## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 6 releases: ['Narwhals v2.11.0', 'Narwhals v2.10.2', 'Narwhals v2.10.1', 'Narwhals v2.10.0', 'Narwhals v2.9.0', 'Narwhals v2.8.0']
### Release: narwhals [Narwhals v2.11.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.11.0)
## Changes

## ✨ Enhancements

- feat: Add `Expr.replace_strict` support for lazy backends if `default` is provided (#3282)
- enh: Show more informative `not_implemented` and "could not translate" errors for plugins (#3297)
- feat: Add `default` in `{Expr,Series}.replace_strict` (#3276)

## 🐞 Bug fixes

- fix: `with_row_index` was returning incorrect results when used with `order_by` for pandas, pyarrow, and polars (#3292)
- fix: Make `is_finite` consistent for Polars < 1.18 (#3288)
- feat: Add `default` in `{Expr,Series}.replace_strict` (#3276)
- fix: Pass/Retrieve empty categories from nw.Enum (#3284)

## 📖 Documentation

- docs: document Daft support (#3299)

## 🛠️ Other improvements

- chore: simplify dask implementation for direct translations (#3287)
- chore: document closed interval options (#3291)
- test: xfail polars `cat.get_categories` (flaky) (#3283)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @camriddell and @liamholmes31

### Release: narwhals [Narwhals v2.10.2](https://github.com/narwhals-dev/narwhals/releases/tag/v2.10.2)
## Changes

- test: un-xfail `is_finite` for `sqlframe` (#3268)

## ✨ Enhancements

- enh: rewrite duckdb groupby so it avoids group-by-all (#3267)

## 🐞 Bug fixes

- fix when/then/otherwise for empty frame (#3280)
- fix: `coalesce` was raising with multi-output expression (#3278)

Thank you to all our contributors for making this release possible!
@MarcoGorelli, @dangotbanned, @dependabot[bot] and [dependabot[bot]](https://github.com/apps/dependabot)

### Release: narwhals [Narwhals v2.10.1](https://github.com/narwhals-dev/narwhals/releases/tag/v2.10.1)
## Changes

## ✨ Enhancements

- fix: allow for `None` dtype in `from_dict` (#3252)
- [Enh] added modifications to make tests accessible to plugins (#3248)

## 🐞 Bug fixes

- fix: Ibis failing with IntegerColumn and `.is_finite` (#3258)
- fix: allow for `None` dtype in `from_dict` (#3252)
- fix: Address `pandas.Series.to_frame` for unnamed series in internal usage (#3251)

## 🛠️ Other improvements

- chore: Duckdb pre-release compat (#3263)
- chore: Add `DTypeClass` to improve `DType.__repr__` and simplify `__slots__` (#3213)
- ci: Add `typos-cli` in pre-commit (#3260)
- tests: Allow to run polars without extra deps (#3256)
- fix(test): TPCH `find_spec('dask') and find_spec('dask.dataframe')` (#3253)
- test: Refactor TPCH testing to run without all dependencies installed (#3244)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @hoxbro and @ym-pett

### Release: narwhals [Narwhals v2.10.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.10.0)
## Changes

## 🚀 Performance improvements

- perf: Rewrite `with_row_index` so it's faster for pandas/pyarrow and doesn't use `rank` (#3239)

## ✨ Enhancements

- feat: introduce (experimental) plugin system (#2978)
- feat: Support `over` expressions more freely, make expressions printable, rewrite internals (travelling pr 🌴 ) (#3152)

## 🐞 Bug fixes

- fix: align `nw.nth` expansion with `nw.col` during `group_by` (#3243)
- fix: Align `str.to_titlecase` with polars v1.35.0 behavior (#3238)

## 🛠️ Other improvements

- ci: Add Fairlearn to downstream tests and ecosystem page (#3228)
- chore: fix ci (cuDF fixes, coverage) (#3245)
- feat: Support `over` expressions more freely, make expressions printable, rewrite internals (travelling pr 🌴 ) (#3152)
- chore: Simplify spark-like and ibis `concat_str` (#3240)
- ci: Make it a bit greener (#3241)
- chore: Share std and var implementations for sql backends (#3229)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli and @ym-pett

### Release: narwhals [Narwhals v2.9.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.9.0)
## Changes

## ✨ Enhancements

- feat: Add support for `{Expr,Series}.{ceil,floor}` (#3198)
- feat: Add `assert_series_equal` (#2983)

## 🐞 Bug fixes

- fix: Allow pyarrow extension dtypes (mapped to `nw.Unknown`) (#3223)
- fix(dependencies): update import check for modin.pandas module (#3219)

## 📖 Documentation

- refactor(typing): Add `_native.py` (#3086)

## 🛠️ Other improvements

- refactor(typing): Add `_native.py` (#3086)
- ci: test pi-thon (#3218)
- chore: fixup ci (#3217)
- chore: add flake8-typing-imports (#3203)
- ci: Unpin DuckDB version (#3211)
- test: Add serde tests for `DType`s (#3205)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @dangotbanned, @m-richards and @sfc-gh-eferguson

### Release: narwhals [Narwhals v2.8.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.8.0)
## Changes

## 🚀 Performance improvements

- perf: Add `__slots__` to all `DType`s (#3194)
- perf: avoid full broadcast in horizontal functions (#3199)
- fix: correctly preserve arrow dtypes for pandas-like, improve `concat_str` performance (#3193)
- perf: Prefer `Iterator > tuple > list`, use native `pyarrow.repeat`, simplify `nw.concat_str` for DuckDB backend (#3190)

## ✨ Enhancements

- feat: Add support for `{Expr,Series}.str.to_titlecase` (#3116)

## 🐞 Bug fixes

- fix: correctly preserve arrow dtypes for pandas-like, improve `concat_str` performance (#3193)
- fix: `BaseFrame.filter` with `list[bool]` in predicates (#3183)

## 🛠️ Other improvements

- chore: Add script to automatically sort members in api-reference  (#3200)
- ci: Unpin (some) dependencies (#3186)
- chore: pandas-nightly and duckdb-nightly fixes (#3158)
- [pre-commit.ci] pre-commit autoupdate (#3181)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @dangotbanned, @pre-commit-ci[bot] and [pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci)

## Project: [pola-rs/polars](https://docs.pola.rs/), 5 releases: ['Python Polars 1.35.2', 'Rust Polars 0.52.0', 'Python Polars 1.35.1', 'Python Polars 1.35.0', 'Python Polars 1.35.0-beta.1']
### Release: polars [Python Polars 1.35.2](https://github.com/pola-rs/polars/releases/tag/py-1.35.2)
* Fix incorrect `drop_nans()` result when used in `group_by()` / `over()` (https://github.com/pola-rs/polars/pull/25146)
* Fix handling `Null` dtype in `ApplyExpr` on `group_by`(https://github.com/pola-rs/polars/pull/25077)
* Fix assertion panic on `group_by` (https://github.com/pola-rs/polars/pull/25179)
* Fix Wide-table join performance regression (https://github.com/pola-rs/polars/pull/25222)

Thank you to all our contributors for making this release possible!
@coastalwhite, @kdn36, @nameexhaustion and @ritchie46

### Release: polars [Rust Polars 0.52.0](https://github.com/pola-rs/polars/releases/tag/rs-0.52.0)
## 🏆 Highlights

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)

## 🚀 Performance improvements

- Lazy gather for `{forward,backward}_fill` in group-by contexts (#25115)
- Don't recompute full rolling moment window when NaNs/nulls leave the window (#25078)
- Skip filtering scan IR if no paths were filtered (#25037)
- Optimize ipc stream read performance (#24671)
- Bump foldhash to 0.2.0 and hashbrown to 0.16.0 (#25014)
- Lower `unique` to native group-by and speed up `n_unique` in group-by context (#24976)
- Better parallelize `take{_slice,}_unchecked` (#24980)
- Implement native `skew` and `kurtosis` in group-by context (#24961)
- Use native group-by aggregations for `bitwise_*` operations (#24935)
- Address `group_by_dynamic` slowness in sparse data (#24916)
- Native `filter/drop_nulls/drop_nans` in group-by context (#24897)
- Implement `cumulative_eval` using the group-by engine (#24889)
- Prevent generation of copies of `Dataframe`s in `DslPlan` serialization (#24852)
- Implement native `null_count`, `any` and `all` group-by aggregations (#24859)
- Speed up `reverse` in group-by context (#24855)
- Prune unused categorical values when exporting to arrow/parquet/IPC/pickle (#24829)
- Don't check duplicates on streaming simple projection in release mode (#24830)
- Lower approx\_n\_unique to the streaming engine (#24821)
- Duration/interval string parsing optimisation (2-5x faster) (#24771)
- Use native reducer for `first/last` on Decimals, Categoricals and Enums (#24786)
- Implement indexed method for `BitMapIter::nth` (#24766)
- Pushdown slices on plans within unions (#24735)
- Optimize gather\_every(n=1) to slice (#24704)
- Lower null count to streaming engine (#24703)
- Native streaming `gather_every` (#24700)
- Pushdown filter with `strptime` if input is literal (#24694)
- Avoid copying expanded paths (#24669)
- Relax filter expr ordering (#24662)
- Remove unnecessary `groups` call in `aggregated` (#24651)
- Skip files in `scan_iceberg` with filter based on metadata statistics (#24547)
- Push row\_index predicate for all scan types (#24537)
- Perform integer in-filtering for Parquet inequality predicates (#24525)
- Stop caching Parquet metadata after 8 files (#24513)

## ✨ Enhancements

- Improve error message on unsupported SQL subquery comparisons (#25135)
- Rewrite `IR::Scan` to `IR::DataFrameScan` in `expand_datasets` when applicable (#25106)
- Support `ewm_var/std` in streaming engine (#25109)
- Make DSL-hash skippable (#25140)
- Streaming `{Expr,LazyFrame}.rolling` (#25058)
- Set polars/\<version> user-agent (#25112)
- Add `BIT_NOT` support to the SQL interface (#25094)
- Support BYTE\_ARRAY backed Decimals in Parquet (#25076)
- Add `allow_empty` flag to `item` (#25048)
- Support `ewm_mean()` in streaming engine (#25003)
- Improve row-count estimates (#24996)
- Remove filtered scan paths in IR when possible (#24974)
- Introduce remote Polars MCP server (#24977)
- Allow local scans on polars cloud (configurable) (#24962)
- Add `Expr.item` to strictly extract a single value from an expression (#24888)
- Add environment variable to roundtrip empty struct in Parquet (#24914)
- Add `glob` parameter to `scan_ipc` (#24898)
- Prevent generation of copies of `Dataframe`s in `DslPlan` serialization (#24852)
- Add `list.agg` and `arr.agg` (#24790)
- Implement `{Expr,Series}.rolling_rank()` (#24776)
- Support MergeSorted in CSPE (#24805)
- Duration/interval string parsing optimisation (2-5x faster) (#24771)
- Recursively apply CSPE (#24798)
- Add streaming engine per-node metrics (#24788)
- Add `arr.eval` (#24472)
- Improve rolling\_(sum|mean) accuracy (#24743)
- Add `nth_set_bit_u64()` with unit test (#24035)
- Add `separator` to `{Data,Lazy}Frame.unnest` (#24716)
- Add `union()` function for unordered concatenation (#24298)
- Add `name.replace` to the set of column rename options (#17942)
- Allow duration strings with leading "+" (#24737)
- Drop now-unnecessary post-init "schema\_overrides" cast on `DataFrame` load from list of dicts (#24739)
- Add support for UInt128 to pyo3-polars (#24731)
- Implement maintain\_order for cross join (#24665)
- Add support to output `dt.total_{}()` duration values as fractionals (#24598)
- Support scanning from `file:/path` URIs (#24603)
- Log which file the schema was sourced from, and which file caused an extra column error (#24621)
- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)
- Add support to display lazy query plan in marimo notebooks without needing to install matplotlib or mermaid (#24540)
- Add unstable `hidden_file_prefix` parameter to `scan_parquet` (#24507)
- Use fixed-scale Decimals (#24542)
- Add support for unsigned 128-bit integers (#24346)

## 🐞 Bug fixes

- Fix CSV `select(len())` off by 1 with comment prefix (#25069)
- Fix incorrect reshape on sliced lists (#25139)
- Support "index" as column name in `group_by` iterator (#25138)
- DSL\_SCHEMA\_HASH should not changed by line endings (#25123)
- Solve multiple issues relating to arena mutation in SQL subqueries (#25110)
- Fix panic in `dt.truncate` for invalid duration strings (#25124)
- Don't trigger `DeprecationWarning` from SQL "IN" constraints that use subqueries (#25111)
- Return the correct string-case `Expr` reprs (#25101)
- Fix `groups` update on slices with different offsets (#25097)
- Fix handling `Null` dtype in `ApplyExpr` on `group_by` (#25077)
- Raise error for all/any on list instead of panic (#25018)
- Unique key names in streaming sort/top\_k (#25082)
- The `SQL` interface should use logical, not bitwise, behaviour for unary "NOT" operator (#25091)
- Fix panic if scan predicate produces 0 length mask (#25089)
- Ensure SQL table alias resolution checks against CTE aliases on fallback (#25071)
- Panic in `group_by_dynamic` with `group_by` and multiple chunks (#25075)
- Fix panic when using struct field as join key (#25059)
- Allow broadcast in `group_by` for `ApplyExpr` and `BinaryExpr` (#25053)
- Fix field metadata for nested categorical PyCapsule export (#25052)
- Block predicate pushdown when `group_by` key values are changed (#25032)
- Group-By aggregation problems caused by `AmortSeries` (#25043)
- Don't push down predicates passed inserted cache nodes (#25042)
- Allow for negative time in `group_by_dynamic` iterator (#25041)
- Re-enable CPU feature check before import (#25010)
- Correctness `any(ignore_nulls)` and OOB in `all` (#25005)
- Streaming any/all with ignore\_nulls=False (#25008)
- Fix incorrect `join_asof` on a casted expression (#25006)
- Optimize memory on rolling groups in `ApplyExpr` (#24709)
- Fallback `Pyarrow` scan to in-memory engine (#24991)
- Make `Operator::swap_operands` return correct operators for `Plus`, `Minus`, `Multiply` and `Divide` (#24997)
- Capitalize letters after numbers in to\_titlecase (#24993)
- Preserve null values in `pct_change` (#24952)
- Raise length mismatch on `over` with sliced groups (#24887)
- Check duplicate name in transpose (#24956)
- Follow Kleene logic in `any` / `all` for group-by (#24940)
- Do not optimize cross join to iejoin if order maintaining (#24950)
- Broadcast `partition_by` columns in `over` expression (#24874)
- Clear index cache on stacked `df.filter` expressions (#24870)
- Fix 'explode' mapping strategy on scalar value (#24861)
- Fix repeated `with_row_index()` after `scan()` silently ignored (#24866)
- Correctly return min and max for enums in groupby aggregation (#24808)
- Refactor `BinaryExpr` in `group_by` dispatch logic (#24548)
- Fix aggstate for `gather` (#24857)
- Keep scalars for length preserving functions in `group_by` (#24819)
- Have `range` feature depend on `dtype-array` feature (#24853)
- Fix duplicate select panic (#24836)
- Inconsistency of list.sum() result type with None values (#24476)
- Division by zero in Expr.dt.truncate (#24832)
- Potential deadlock in \_\_arrow\_c\_stream\_\_ (#24831)
- Allow double aggregations in group-by contexts (#24823)
- Series.shrink\_dtype for i128/u128 (#24833)
- Fix dtype in `EvalExpr` (#24650)
- Allow aggregations on `AggState::LiteralScalar` (#24820)
- Dispatch to `group_aware` for fallible expressions with masked out elements (#24815)
- Fix error for `arr.sum()` on small integer Array dtypes containing nulls (#24478)
- Fix XOR did not follow kleene when one side is unit-length (#24810)
- Incorrect precision in Series.str.to\_decimal (#24804)
- Use `overlapping` instead of `rolling` (#24787)
- Fix iterable on `dynamic_group_by` and `rolling` object (#24740)
- Use Kahan summation for in-memory groupby sum/mean (#24774)
- Release GIL in PythonScan predicate evaluation (#24779)
- Type error in `bitmask::nth_set_bit_u64` (#24775)
- Add `Expr.sign` for `Decimal` datatype (#24717)
- Correct `str.replace` with missing pattern (#24768)
- Support `decimal_comma` on `Decimal` type in `write_csv` (#24718)
- Parse `Decimal` with comma as decimal separator in CSV (#24685)
- Make `Categories` pickleable (#24691)
- Shift on array within list (#24678)
- Fix handling of `AggregatedScalar` in `ApplyExpr` single input (#24634)
- Support reading of mixed compressed/uncompressed IPC buffers (#24674)
- Overflow in slice-slice optimization (#24658)
- Package discovery for `setuptools` (#24656)
- Add type assertion to prevent out-of-bounds in `GenericFirstLastGroupedReduction` (#24590)
- Remove inclusion of polars dir in runtime sdist/wheel (#24654)
- Method `dt.month_end` was unnecessarily raising when the month-start timestamp was ambiguous (#24647)
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
- Have `log()` prioritize the leftmost dtype for its output dtype (#24581)
- CSV pl.len() was incorrect (#24587)
- Add support for float inputs for duration types (#24529)
- Roundtrip empty string through hive partitioning (#24546)
- Fix potential OOB writes in unaligned IPC read (#24550)
- Fix regression error when scanning AWS presigned URL (#24530)
- Make `PlPath::join` for cloud paths replace on absolute paths (#24514)
- Correct dtype for cum\_agg in streaming engine (#24510)
- Escape backslashes in EscapeLabel to produce valid DOT labels (#24532)

## 📖 Documentation

- Mention Narwhals in ecosystem page (#25100)
- Fix typo in public dataset URL (#25044)
- Introduce remote Polars MCP server (#24977)
- Update Cloud docs with correct fn argument order (#24939)
- Add i128 and u128 features to user guide (#24938)
- Relax fsspec wording (#24881)
- Fix duplicated article in SECURITY.md (#24762)
- Specify that precision=None becomes 38 for Decimal (#24742)
- Mention polars[rt64] and polars[rtcompat] instead of u64-idx and lts-cpu (#24749)
- Fix source mapping (#24736)
- Fix syntax error in data-types-and-structures.md (#24606)

## 📦 Build system

- Make building the docs on macOS more reliable (#25095)
- Ensure `build_feature_flags.py` is included in artifact (#25024)
- Python pre-release 1.34.0b5 (#24699)
- Use cargo-run to call dsl-schema script (#24607)

## 🛠️ Other improvements

- Support for named/anonymous aggregations (#25118)
- Silence unused mut warning (#25093)
- Remove old join projection pushdown logic (#25088)
- Disable recursive CSPE for now (#25085)
- Remove unused row-count (#25080)
- Add `proptest` strategies for Series logical types (#24849)
- Add stateful `EwmCov` kernel (#25065)
- Add IR for `scan_lines` (#25066)
- Change group length mismatch error to `ShapeError` (#25004)
- Move asof `tolerance` type coercion to IR conversion (#25033)
- Move `EwmMeanState` to `polars-compute` (#25034)
- Update toolchain (#25007)
- Fix benchmark ci (#25019)
- Fix non-deterministic test (#25009)
- Fix makefile arch detection (#25011)
- Make `LazyFrame.set_sorted` into a `FunctionIR::Hint` (#24981)
- Update row estimation and reader schema in `filter_scan_ir` (#24995)
- Insert casts for `ewm_mean` inputs in type coercion (#24992)
- Remove unused `expr_eval` (#24988)
- Remove symbolic links (#24982)
- Add stateful `EwmMean` kernel (#24972)
- Dispatch to no-op rayon thread-pool from streaming (#24957)
- Add function to filter `IR::Scan` based on indices (#24979)
- Organize code for opaque functions in a module (#24978)
- Move scan filter code to `polars-mem-engine` (#24959)
- Unpin pydantic (#24955)
- Ensure safety of scan fast-count IR lowering in streaming (#24953)
- Expose `polars_compute` from polars (#24556)
- Re-use iterators in `set_` operations (#24850)
- Move order code to instance function (#24895)
- Visualization data generator for streaming physical plan (#24896)
- Remove `GroupByPartitioned` and dispatch to streaming engine (#24903)
- Improve IR visualization for IEJoin (#24902)
- Turn `element()` into `{A,}Expr::Element` (#24885)
- Pass `ScanOptions` to `new_from_ipc` (#24893)
- Update tests to be index type agnostic (#24891)
- Remove legacy `order_sensitive` code (#24894)
- Rename `text_plan_graph` to `visualization_data` (#24878)
- Use `UnifiedScanArgs` in `new_from_ipc` and remove `LazyIpcReader` (#24883)
- Document safety of `CategoricalToArrowConverter` (#24876)
- Unset `Context` in `Window` expression (#24875)
- Unify expression order resolution (#24723)
- Move `FunctionExpr` dispatch from `plan` to `expr` (#24839)
- Fix SQL test giving wrong error message (#24835)
- Consolidate dtype paths in `ApplyExpr` (#24825)
- Add `days_in_month` to documentation (#24822)
- Enable ruff D417 lint (#24814)
- Turn `pl.format` into proper elementwise expression (#24811)
- Fix remote benchmark by no-longer saving builds (#24812)
- Expose function on IPC writer to write dictionary batches (#24802)
- Refactor `ApplyExpr` in `group_by` context on multiple inputs (#24520)
- IR text plan graph generator (#24733)
- Move Series `to_arrow()` logic to struct function (#24794)
- Temporarily pin pydantic to fix CI (#24797)
- Extend and rename `rolling` groups to `overlapping` (#24577)
- Refactor `DataType` `proptest` strategies (#24763)
- Add `union` to documentation (#24769)
- Cleaner whitespace skipping in CSV field parser (#24705)
- Remove duplicate maintain\_order from CrossJoinOptions (#24725)
- Change function order flags to be less error prone (#24604)
- Remove `{Upper,Lower}Bound` expressions in IR (#24701)
- Fix Makefile `uv pip` option syntax (#24711)
- Add egg-info to gitignore (#24712)
- Restructure python project directories again (#24676)
- Use IR for `polars-expr` output field resolution (#24661)
- Add `proptest` strategies for Series physical types (#24549)
- Expose `CloudScheme` via `polars::prelude` (#24643)
- Remove dist/ from release python workflow (#24639)
- Escape `sed` ampersand in release script (#24631)
- Remove PyOdide from release for now (#24630)
- Fix sed in-place in release script (#24628)
- Release script pyodide wheel (#24627)
- Release script pyodide wheel (#24626)
- Update release script for runtimes (#24610)
- Remove tokio-util dependency (#24617)
- Remove unused `UnknownKind::Ufunc` (#24614)
- Use cargo-run to call dsl-schema script (#24607)
- Genericize UnitVec for any T (#24597)
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
- Add `CloudScheme::FileNoHostname` variant (#24535)
- Add a couple of missing type definitions in python (#24561)
- Fix quickstart example in Polars Cloud user guide (#24554)
- Add implementations for loading min/max statistics for Iceberg (#24496)
- Move collapse\_joins optimizer logic into predicate pushdown optimizer (#24495)

Thank you to all our contributors for making this release possible!
@DeflateAwning, @EndPositive, @EnricoMi, @FBruzzesi, @JakubValtar, @Kevin-Patyk, @Liyixin95, @MarcoGorelli, @Object905, @alexander-beedie, @alonsosilvaallende, @andreseje, @borchero, @carnarez, @cmdlineluser, @coastalwhite, @craigalodon, @dangotbanned, @deanm0000, @dsprenkels, @eitsupi, @etrotta, @henryharbeck, @itamarst, @jan-krueger, @jordanosborn, @kdn36, @lzcmian, @math-hiyoko, @mcrumiller, @mjanssen, @moizescbf, @nameexhaustion, @orlp, @pavelzw, @r-brink, @ritchie46, @stijnherfst, @thomasjpfan and @williambdean

### Release: polars [Python Polars 1.35.1](https://github.com/pola-rs/polars/releases/tag/py-1.35.1)
## 🚀 Performance improvements

- Don't recompute full rolling moment window when NaNs/nulls leave the window (#25078)
- Skip filtering scan IR if no paths were filtered (#25037)
- Optimize ipc stream read performance (#24671)

## ✨ Enhancements

- Support BYTE\_ARRAY backed Decimals in Parquet (#25076)
- Allow `glimpse` to return a `DataFrame` (#24803)
- Add `allow_empty` flag to `item` (#25048)

## 🐞 Bug fixes

- The `SQL` interface should use logical, not bitwise, behaviour for unary "NOT" operator (#25091)
- Fix panic if scan predicate produces 0 length mask (#25089)
- Ensure SQL table alias resolution checks against CTE aliases on fallback (#25071)
- Panic in `group_by_dynamic` with `group_by` and multiple chunks (#25075)
- Minor improvement to internal `is_pycapsule` utility function (#25073)
- Fix panic when using struct field as join key (#25059)
- Allow broadcast in `group_by` for `ApplyExpr` and `BinaryExpr` (#25053)
- Fix field metadata for nested categorical PyCapsule export (#25052)
- Block predicate pushdown when `group_by` key values are changed (#25032)
- Group-By aggregation problems caused by `AmortSeries` (#25043)
- Don't push down predicates passed inserted cache nodes (#25042)
- Allow for negative time in `group_by_dynamic` iterator (#25041)

## 📖 Documentation

- Fix typo in public dataset URL (#25044)

## 🛠️ Other improvements

- Disable recursive CSPE for now (#25085)
- Change group length mismatch error to `ShapeError` (#25004)
- Update toolchain (#25007)

Thank you to all our contributors for making this release possible!
@Kevin-Patyk, @Liyixin95, @alexander-beedie, @coastalwhite, @kdn36, @nameexhaustion, @orlp, @r-brink, @ritchie46 and @stijnherfst

### Release: polars [Python Polars 1.35.0](https://github.com/pola-rs/polars/releases/tag/py-1.35.0)
## 🏆 Highlights

- Stabilize decimal (#25020)

## 🚀 Performance improvements

- Bump foldhash to 0.2.0 and hashbrown to 0.16.0 (#25014)
- Lower `unique` to native group-by and speed up `n_unique` in group-by context (#24976)
- Better parallelize `take{_slice,}_unchecked` (#24980)
- Implement native `skew` and `kurtosis` in group-by context (#24961)
- Use native group-by aggregations for `bitwise_*` operations (#24935)
- Address `group_by_dynamic` slowness in sparse data (#24916)
- Push filters to PyIceberg (#24910)
- Native `filter/drop_nulls/drop_nans` in group-by context (#24897)
- Implement `cumulative_eval` using the group-by engine (#24889)
- Prevent generation of copies of `Dataframe`s in `DslPlan` serialization (#24852)
- Implement native `null_count`, `any` and `all` group-by aggregations (#24859)
- Speed up `reverse` in group-by context (#24855)
- Prune unused categorical values when exporting to arrow/parquet/IPC/pickle (#24829)
- Don't check duplicates on streaming simple projection in release mode (#24830)
- Lower approx\_n\_unique to the streaming engine (#24821)
- Duration/interval string parsing optimisation (2-5x faster) (#24771)
- Use native reducer for `first/last` on Decimals, Categoricals and Enums (#24786)
- Implement indexed method for `BitMapIter::nth` (#24766)
- Pushdown slices on plans within unions (#24735)

## ✨ Enhancements

- Stabilize decimal (#25020)
- Support `ewm_mean()` in streaming engine (#25003)
- Improve row-count estimates (#24996)
- Remove filtered scan paths in IR when possible (#24974)
- Introduce remote Polars MCP server (#24977)
- Allow local scans on polars cloud (configurable) (#24962)
- Add `Expr.item` to strictly extract a single value from an expression (#24888)
- Add environment variable to roundtrip empty struct in Parquet (#24914)
- Fast-count for `scan_iceberg().select(len())` (#24602)
- Add `glob` parameter to `scan_ipc` (#24898)
- Prevent generation of copies of `Dataframe`s in `DslPlan` serialization (#24852)
- Add `list.agg` and `arr.agg` (#24790)
- Implement `{Expr,Series}.rolling_rank()` (#24776)
- Don't require PyArrow for `read_database_uri` if ADBC engine version supports PyCapsule interface (#24029)
- Make `Series` init consistent with `DataFrame` init for string values declared with temporal dtype (#24785)
- Support MergeSorted in CSPE (#24805)
- Duration/interval string parsing optimisation (2-5x faster) (#24771)
- Recursively apply CSPE (#24798)
- Add streaming engine per-node metrics (#24788)
- Add `arr.eval` (#24472)
- Drop PyArrow requirement for non-batched usage of `read_database` with the ADBC engine and support `iter_batches` with the ADBC engine (#24180)
- Improve rolling\_(sum|mean) accuracy (#24743)
- Add `separator` to `{Data,Lazy}Frame.unnest` (#24716)
- Add `union()` function for unordered concatenation (#24298)
- Add `name.replace` to the set of column rename options (#17942)
- Support `np.ndarray -> AnyValue` conversion (#24748)
- Allow duration strings with leading "+" (#24737)
- Drop now-unnecessary post-init "schema\_overrides" cast on `DataFrame` load from list of dicts (#24739)
- Add support for UInt128 to pyo3-polars (#24731)

## 🐞 Bug fixes

- Re-enable CPU feature check before import (#25010)
- Implement `read_excel` workaround for fastexcel/calamine issue loading a column subset from a named table (#25012)
- Correctness `any(ignore_nulls)` and OOB in `all` (#25005)
- Streaming any/all with ignore\_nulls=False (#25008)
- Fix incorrect `join_asof` on a casted expression (#25006)
- Optimize memory on rolling groups in `ApplyExpr` (#24709)
- Fallback `Pyarrow` scan to in-memory engine (#24991)
- Make `Operator::swap_operands` return correct operators for `Plus`, `Minus`, `Multiply` and `Divide` (#24997)
- Capitalize letters after numbers in to\_titlecase (#24993)
- Preserve null values in `pct_change` (#24952)
- Raise length mismatch on `over` with sliced groups (#24887)
- Check duplicate name in transpose (#24956)
- Follow Kleene logic in `any` / `all` for group-by (#24940)
- Do not optimize cross join to iejoin if order maintaining (#24950)
- Fix typing of `scan_parquet` partially unknown (#24928)
- Properly release the GIL for `read_parquet_metadata` (#24922)
- Broadcast `partition_by` columns in `over` expression (#24874)
- Clear index cache on stacked `df.filter` expressions (#24870)
- Fix 'explode' mapping strategy on scalar value (#24861)
- Fix repeated `with_row_index()` after `scan()` silently ignored (#24866)
- Correctly return min and max for enums in groupby aggregation (#24808)
- Refactor `BinaryExpr` in `group_by` dispatch logic (#24548)
- Fix aggstate for `gather` (#24857)
- Keep scalars for length preserving functions in `group_by` (#24819)
- Have `range` feature depend on `dtype-array` feature (#24853)
- Fix duplicate select panic (#24836)
- Inconsistency of list.sum() result type with None values (#24476)
- Division by zero in Expr.dt.truncate (#24832)
- Potential deadlock in \_\_arrow\_c\_stream\_\_ (#24831)
- Allow double aggregations in group-by contexts (#24823)
- Series.shrink\_dtype for i128/u128 (#24833)
- Fix dtype in `EvalExpr` (#24650)
- Allow aggregations on `AggState::LiteralScalar` (#24820)
- Dispatch to `group_aware` for fallible expressions with masked out elements (#24815)
- Fix error for `arr.sum()` on small integer Array dtypes containing nulls (#24478)
- Fix regression on `write_database()` to Snowflake due to unsupported string view type (#24622)
- Fix XOR did not follow kleene when one side is unit-length (#24810)
- Make `Series` init consistent with `DataFrame` init for string values declared with temporal dtype (#24785)
- Incorrect precision in Series.str.to\_decimal (#24804)
- Use `overlapping` instead of `rolling` (#24787)
- Fix iterable on `dynamic_group_by` and `rolling` object (#24740)
- Use Kahan summation for in-memory groupby sum/mean (#24774)
- Release GIL in PythonScan predicate evaluation (#24779)
- Type error in `bitmask::nth_set_bit_u64` (#24775)
- Add `Expr.sign` for `Decimal` datatype (#24717)
- Correct `str.replace` with missing pattern (#24768)
- Ensure `schema_overrides` is respected when loading iterable row data (#24721)
- Support `decimal_comma` on `Decimal` type in `write_csv` (#24718)

## 📖 Documentation

- Introduce remote Polars MCP server (#24977)
- Add `{arr,list}.agg` API references (#24970)
- Support LLM in docs (#24958)
- Update Cloud docs with correct fn argument order (#24939)
- Update `name.replace` examples (#24941)
- Add i128 and u128 features to user guide (#24938)
- Add partitioning examples for `sink_*` methods (#24918)
- Add more `{unique,value}_counts` examples (#24927)
- Indent the versionchanged (#24783)
- Relax fsspec wording (#24881)
- Add `pl.field` into the api docs (#24846)
- Fix duplicated article in SECURITY.md (#24762)
- Document output name determination in when/then/otherwise (#24746)
- Specify that precision=None becomes 38 for Decimal (#24742)
- Mention polars[rt64] and polars[rtcompat] instead of u64-idx and lts-cpu (#24749)
- Fix source mapping (#24736)

## 📦 Build system

- Ensure `build_feature_flags.py` is included in artifact (#25024)
- Update pyo3 and numpy crates to version 0.26 (#24760)

## 🛠️ Other improvements

- Fix benchmark ci (#25019)
- Fix non-deterministic test (#25009)
- Fix makefile arch detection (#25011)
- Make `LazyFrame.set_sorted` into a `FunctionIR::Hint` (#24981)
- Remove symbolic links (#24982)
- Deprecate `Expr.agg_groups()` and `pl.groups()` (#24919)
- Dispatch to no-op rayon thread-pool from streaming (#24957)
- Unpin pydantic (#24955)
- Ensure safety of scan fast-count IR lowering in streaming (#24953)
- Re-use iterators in `set_` operations (#24850)
- Remove `GroupByPartitioned` and dispatch to streaming engine (#24903)
- Turn `element()` into `{A,}Expr::Element` (#24885)
- Pass `ScanOptions` to `new_from_ipc` (#24893)
- Update tests to be index type agnostic (#24891)
- Unset `Context` in `Window` expression (#24875)
- Fix failing delta test (#24867)
- Move `FunctionExpr` dispatch from `plan` to `expr` (#24839)
- Fix SQL test giving wrong error message (#24835)
- Consolidate dtype paths in `ApplyExpr` (#24825)
- Add `days_in_month` to documentation (#24822)
- Enable ruff D417 lint (#24814)
- Turn `pl.format` into proper elementwise expression (#24811)
- Fix remote benchmark by no-longer saving builds (#24812)
- Refactor `ApplyExpr` in `group_by` context on multiple inputs (#24520)
- IR text plan graph generator (#24733)
- Temporarily pin pydantic to fix CI (#24797)
- Extend and rename `rolling` groups to `overlapping` (#24577)
- Refactor `DataType` `proptest` strategies (#24763)
- Add `union` to documentation (#24769)

Thank you to all our contributors for making this release possible!
@EndPositive, @EnricoMi, @JakubValtar, @Kevin-Patyk, @MarcoGorelli, @Object905, @alexander-beedie, @borchero, @carnarez, @cmdlineluser, @coastalwhite, @craigalodon, @dsprenkels, @eitsupi, @etrotta, @henryharbeck, @jordanosborn, @kdn36, @math-hiyoko, @mjanssen, @nameexhaustion, @orlp, @pavelzw, @r-brink, @ritchie46, @thomasjpfan and @williambdean

### Release: polars [Python Polars 1.35.0-beta.1](https://github.com/pola-rs/polars/releases/tag/py-1.35.0-beta.1)
## 🚀 Performance improvements

- Address `group_by_dynamic` slowness in sparse data (#24916)
- Push filters to PyIceberg (#24910)
- Native `filter/drop_nulls/drop_nans` in group-by context (#24897)
- Implement `cumulative_eval` using the group-by engine (#24889)
- Prevent generation of copies of `Dataframe`s in `DslPlan` serialization (#24852)
- Implement native `null_count`, `any` and `all` group-by aggregations (#24859)
- Speed up `reverse` in group-by context (#24855)
- Prune unused categorical values when exporting to arrow/parquet/IPC/pickle (#24829)
- Don't check duplicates on streaming simple projection in release mode (#24830)
- Lower approx\_n\_unique to the streaming engine (#24821)
- Duration/interval string parsing optimisation (2-5x faster) (#24771)
- Use native reducer for `first/last` on Decimals, Categoricals and Enums (#24786)
- Implement indexed method for `BitMapIter::nth` (#24766)
- Pushdown slices on plans within unions (#24735)

## ✨ Enhancements

- Add environment variable to roundtrip empty struct in Parquet (#24914)
- Fast-count for `scan_iceberg().select(len())` (#24602)
- Add `glob` parameter to `scan_ipc` (#24898)
- Prevent generation of copies of `Dataframe`s in `DslPlan` serialization (#24852)
- Add `list.agg` and `arr.agg` (#24790)
- Implement `{Expr,Series}.rolling_rank()` (#24776)
- Don't require PyArrow for `read_database_uri` if ADBC engine version supports PyCapsule interface (#24029)
- Make `Series` init consistent with `DataFrame` init for string values declared with temporal dtype (#24785)
- Support MergeSorted in CSPE (#24805)
- Duration/interval string parsing optimisation (2-5x faster) (#24771)
- Recursively apply CSPE (#24798)
- Add streaming engine per-node metrics (#24788)
- Add `arr.eval` (#24472)
- Drop PyArrow requirement for non-batched usage of `read_database` with the ADBC engine and support `iter_batches` with the ADBC engine (#24180)
- Improve rolling\_(sum|mean) accuracy (#24743)
- Add `separator` to `{Data,Lazy}Frame.unnest` (#24716)
- Add `union()` function for unordered concatenation (#24298)
- Add `name.replace` to the set of column rename options (#17942)
- Support `np.ndarray -> AnyValue` conversion (#24748)
- Allow duration strings with leading "+" (#24737)
- Drop now-unnecessary post-init "schema\_overrides" cast on `DataFrame` load from list of dicts (#24739)
- Add support for UInt128 to pyo3-polars (#24731)

## 🐞 Bug fixes

- Properly release the GIL for `read_parquet_metadata` (#24922)
- Broadcast `partition_by` columns in `over` expression (#24874)
- Clear index cache on stacked `df.filter` expressions (#24870)
- Fix 'explode' mapping strategy on scalar value (#24861)
- Fix repeated `with_row_index()` after `scan()` silently ignored (#24866)
- Correctly return min and max for enums in groupby aggregation (#24808)
- Refactor `BinaryExpr` in `group_by` dispatch logic (#24548)
- Fix aggstate for `gather` (#24857)
- Keep scalars for length preserving functions in `group_by` (#24819)
- Have `range` feature depend on `dtype-array` feature (#24853)
- Fix duplicate select panic (#24836)
- Inconsistency of list.sum() result type with None values (#24476)
- Division by zero in Expr.dt.truncate (#24832)
- Potential deadlock in \_\_arrow\_c\_stream\_\_ (#24831)
- Allow double aggregations in group-by contexts (#24823)
- Series.shrink\_dtype for i128/u128 (#24833)
- Fix dtype in `EvalExpr` (#24650)
- Allow aggregations on `AggState::LiteralScalar` (#24820)
- Dispatch to `group_aware` for fallible expressions with masked out elements (#24815)
- Fix error for `arr.sum()` on small integer Array dtypes containing nulls (#24478)
- Fix regression on `write_database()` to Snowflake due to unsupported string view type (#24622)
- Fix XOR did not follow kleene when one side is unit-length (#24810)
- Make `Series` init consistent with `DataFrame` init for string values declared with temporal dtype (#24785)
- Incorrect precision in Series.str.to\_decimal (#24804)
- Use `overlapping` instead of `rolling` (#24787)
- Fix iterable on `dynamic_group_by` and `rolling` object (#24740)
- Use Kahan summation for in-memory groupby sum/mean (#24774)
- Release GIL in PythonScan predicate evaluation (#24779)
- Type error in `bitmask::nth_set_bit_u64` (#24775)
- Add `Expr.sign` for `Decimal` datatype (#24717)
- Correct `str.replace` with missing pattern (#24768)
- Ensure `schema_overrides` is respected when loading iterable row data (#24721)
- Support `decimal_comma` on `Decimal` type in `write_csv` (#24718)

## 📖 Documentation

- Add partitioning examples for `sink_*` methods (#24918)
- Add more `{unique,value}_counts` examples (#24927)
- Indent the versionchanged (#24783)
- Relax fsspec wording (#24881)
- Add `pl.field` into the api docs (#24846)
- Fix duplicated article in SECURITY.md (#24762)
- Document output name determination in when/then/otherwise (#24746)
- Specify that precision=None becomes 38 for Decimal (#24742)
- Mention polars[rt64] and polars[rtcompat] instead of u64-idx and lts-cpu (#24749)
- Fix source mapping (#24736)

## 📦 Build system

- Update pyo3 and numpy crates to version 0.26 (#24760)

## 🛠️ Other improvements

- Re-use iterators in `set_` operations (#24850)
- Remove `GroupByPartitioned` and dispatch to streaming engine (#24903)
- Turn `element()` into `{A,}Expr::Element` (#24885)
- Pass `ScanOptions` to `new_from_ipc` (#24893)
- Update tests to be index type agnostic (#24891)
- Unset `Context` in `Window` expression (#24875)
- Fix failing delta test (#24867)
- Move `FunctionExpr` dispatch from `plan` to `expr` (#24839)
- Fix SQL test giving wrong error message (#24835)
- Consolidate dtype paths in `ApplyExpr` (#24825)
- Add `days_in_month` to documentation (#24822)
- Enable ruff D417 lint (#24814)
- Turn `pl.format` into proper elementwise expression (#24811)
- Fix remote benchmark by no-longer saving builds (#24812)
- Refactor `ApplyExpr` in `group_by` context on multiple inputs (#24520)
- IR text plan graph generator (#24733)
- Temporarily pin pydantic to fix CI (#24797)
- Extend and rename `rolling` groups to `overlapping` (#24577)
- Refactor `DataType` `proptest` strategies (#24763)
- Add `union` to documentation (#24769)

Thank you to all our contributors for making this release possible!
@JakubValtar, @Kevin-Patyk, @MarcoGorelli, @Object905, @alexander-beedie, @borchero, @cmdlineluser, @coastalwhite, @craigalodon, @dsprenkels, @eitsupi, @etrotta, @henryharbeck, @jordanosborn, @kdn36, @math-hiyoko, @nameexhaustion, @orlp, @pavelzw, @ritchie46, @thomasjpfan and @williambdean

## Project: [holoviz/panel](https://panel.holoviz.org/), 1 releases: ['Version 1.8.3']
### Release: panel [Version 1.8.3](https://github.com/holoviz/panel/releases/tag/v1.8.3)
This patch release brings targeted UI fixes, improves Python and Django compatibility, and enhances the developer and contributor experience. It also includes fixes for Tabulator, Pyodide, templates, and app interactivity, along with several documentation and robustness improvements. Many thanks to @ahuang11, @hoxbro, @maximlt, @MarcSkovMadsen, @Coderambling and  @philippjfr for their contributions to this release.

### ✨ Enhancements

- Align CSS variables between default and dark themes ([#8248](https://github.com/holoviz/panel/pull/8248))
- Ensure behavior of dynamically served apps is aligned with file based apps ([#8249](https://github.com/holoviz/panel/pull/8249))
- Add `export()` method to `Vega` pane ([#8266](https://github.com/holoviz/panel/pull/8266))
- Add official support for **Python 3.14** ([#8241](https://github.com/holoviz/panel/pull/8241))
- Add `render_policy="manual"` option for `JSComponent` ([#8285](https://github.com/holoviz/panel/pull/8285))
- Disable text selection when editing in `EditableTemplate` ([#8286](https://github.com/holoviz/panel/pull/8286))
- Prevent full text selection when replacing input values on `CodeEditor` ([#8262](https://github.com/holoviz/panel/pull/8262))

### 🐛 Bug Fixes

- Fix FastAPI bug where `pn.state.location` wasn’t retained ([#8283](https://github.com/holoviz/panel/pull/8283))
- Fix Tabulator popup container rendering issues ([#8247](https://github.com/holoviz/panel/pull/8247))
- Resolve issues with pipeline `next/previous` buttons ([#8273](https://github.com/holoviz/panel/pull/8273))
- Ensure ESM compilation uses `_esm` path ([#8245](https://github.com/holoviz/panel/pull/8245))
- Fix CORS issue with `turbine` data URL in Pyodide ([#8272](https://github.com/holoviz/panel/pull/8272))
- Ensure `ParamRef`, `ParamFunction`, and `ParamMethod` do not override styling ([#8264](https://github.com/holoviz/panel/pull/8264))
- Fix toggle behavior in `BootstrapTemplate` sidebar ([#8268](https://github.com/holoviz/panel/pull/8268))
- Minor robustness improvements for Bokeh model interop ([#8270](https://github.com/holoviz/panel/pull/8270))

### 📚 Documentation

- Minor enhancements to the [Panel Gallery](https://panel.holoviz.org/gallery/) deployment ([#8240](https://github.com/holoviz/panel/pull/8240))
- Update Django integration docs ([#8252](https://github.com/holoviz/panel/pull/8252))
- Clarify setup instructions ([#8255](https://github.com/holoviz/panel/pull/8255))
- Fix typo and layout issue in `README.md` ([#8287](https://github.com/holoviz/panel/pull/8287))
- Fix unclosed code block in `convert.md` ([#8280](https://github.com/holoviz/panel/pull/8280))

### 🧪 Infrastructure & Developer Experience

- Remove Bokeh metadata workaround related to Tornado ([#8243](https://github.com/holoviz/panel/pull/8243))
- Bump Django versions in example apps:

  - `4.2.22` → `4.2.25` ([#8226](https://github.com/holoviz/panel/pull/8226))
  - `4.2.22` → `4.2.26` in multi-apps example ([#8282](https://github.com/holoviz/panel/pull/8282))
- Add `setup-dev` command for easier local development ([#8277](https://github.com/holoviz/panel/pull/8277))
- Improve internal `_descendents` resolution for parameterized classes ([#8284](https://github.com/holoviz/panel/pull/8284))
- Add `__panel__` stub method to `PyComponent` ([#8271](https://github.com/holoviz/panel/pull/8271))

## Project: [holoviz/holoviews](https://holoviews.org/), 1 releases: ['Version 1.22.0']
### Release: holoviews [Version 1.22.0](https://github.com/holoviz/holoviews/releases/tag/v1.22.0)
This release adds [Narwhals](https://narwhals-dev.github.io/narwhals/) support for broader dataframe compatibility. By doing so, we now also support Polars and DuckDB data backends.
Another new feature is the addition of sizebar support for `Points` elements, allowing for better visualization of point sizes in plots.
Along with these new features, this release includes numerous enhancements, bug fixes, compatibility updates, and improved documentation.
Many thanks to [@epaaso](https://github.com/epaaso) (first contribution), [@thuydotm](https://github.com/thuydotm) (first contribution), [@ahuang11](https://github.com/ahuang11), [@Azaya89](https://github.com/Azaya89), [@maximlt](https://github.com/maximlt), [@philippjfr](https://github.com/philippjfr), [@stanwest](https://github.com/stanwest), and [@hoxbro](https://github.com/hoxbro) for their contributions.

New Features:

- Support Narwhals ([#6567](https://github.com/holoviz/holoviews/pull/6567), [#6725](https://github.com/holoviz/holoviews/pull/6725))
- Add `sizebar` support to `Point` ([#6663](https://github.com/holoviz/holoviews/pull/6663))

Enhancements:

- Add `gridstyle` to matplotlib ([#6700](https://github.com/holoviz/holoviews/pull/6700))
- Add `from_sparse` classmethod for `Graph` ([#6673](https://github.com/holoviz/holoviews/pull/6673))
- Add support for synthetic legends on `ImageStackPlot` ([#6662](https://github.com/holoviz/holoviews/pull/6662))
- Sync tools with Bokeh and use `auto_box_zoom` as default ([#6650](https://github.com/holoviz/holoviews/pull/6650))
- Add hover filter ([#6646](https://github.com/holoviz/holoviews/pull/6646))
- Improve error message for non-matching types when aspect is set to equal ([#6103](https://github.com/holoviz/holoviews/pull/6103))
- Use `ImageStack` as an `element_type` in `rasterize` ([#6631](https://github.com/holoviz/holoviews/pull/6631))
- Improve `core.util` to work better without pandas installed ([#6702](https://github.com/holoviz/holoviews/pull/6702))
- Implement `link_selections.unlink` ([#6685](https://github.com/holoviz/holoviews/pull/6685))

Deprecations:

- Deprecate `IbisInterface` for `NarwhalsInterface` ([#6718](https://github.com/holoviz/holoviews/pull/6718))

Performance:

- Optimize `HeatMap` rendering path if gridded and contiguous ([#6680](https://github.com/holoviz/holoviews/pull/6680))
- Add debounce support to `PlotSize` and `RangeXY` Bokeh callbacks ([#6672](https://github.com/holoviz/holoviews/pull/6672))
- Don't import IPython in `find_stack_level` ([#6724](https://github.com/holoviz/holoviews/pull/6724))

Bug Fixes:

- Interpolation for `Image` with `datashade` ([#6707](https://github.com/holoviz/holoviews/pull/6707))
- `subcoordinate_y` for `DynamicMap` if labels mismatched between plots ([#6694](https://github.com/holoviz/holoviews/pull/6694))
- Setting `selection_expr` programmatically ([#6689](https://github.com/holoviz/holoviews/pull/6689))
- Handle `node_color` in element transformations for Bokeh and MPL ([#6678](https://github.com/holoviz/holoviews/pull/6678))
- `hv.dim` and `hv.Dimension` as color opts for Matplotlib Path plots ([#6721](https://github.com/holoviz/holoviews/pull/6721), [#6665](https://github.com/holoviz/holoviews/pull/6665))
- Use native bokeh `x` marker in plots and legends ([#6676](https://github.com/holoviz/holoviews/pull/6676))
- Silence Bokeh `FIXED_SIZING_MODE` warning on hv.save ([#6674](https://github.com/holoviz/holoviews/pull/6674))
- Comparison for non-numeric dtypes ([#6671](https://github.com/holoviz/holoviews/pull/6671))
- Allow discovering `.apply` operation on pipeline ([#6670](https://github.com/holoviz/holoviews/pull/6670))
- `dendrogram` edgecases ([#6669](https://github.com/holoviz/holoviews/pull/6669))
- Don't select in `decimate` if start and end are the same ([#6661](https://github.com/holoviz/holoviews/pull/6661))

Compatibility:

- Ibis 11.0.0 ([#6706](https://github.com/holoviz/holoviews/pull/6706))
- Python 3.14 ([#6704](https://github.com/holoviz/holoviews/pull/6704))
- xarray 2025.08 ([#6664](https://github.com/holoviz/holoviews/pull/6664))
- cuDF 25.10 ([#6659](https://github.com/holoviz/holoviews/pull/6659))
- Pillow 11.3.0 ([#6651](https://github.com/holoviz/holoviews/pull/6651))



## Project: [pyscript/pyscript](https://pyscript.com/), 4 releases: ['2025.11.1', '2025.10.3', '2025.10.2', '2025.10.1']
### Release: pyscript [2025.11.1](https://github.com/pyscript/pyscript/releases/tag/2025.11.1)
* PyScript does not throw errors anymore if a package is not available in the official Pyodide packages "graph". See [this PR](https://github.com/pyscript/polyscript/pull/162) for more details.
* PyScript allows passing File and Blob instances to any worker from the main thread, through worker related Python code. See [this change](https://github.com/WebReflection/reflected-ffi/commit/5ead591d9b3b185ee845e3344556414792a65acc) for the underlying technical details.

<!-- Release notes generated using configuration in .github/release.yml at 2025.11.1 -->



**Full Changelog**: https://github.com/pyscript/pyscript/compare/2025.10.3...2025.11.1
### Release: pyscript [2025.10.3](https://github.com/pyscript/pyscript/releases/tag/2025.10.3)
After a Chromium update we have noticed our `pyscript.fs` broke so that:

  * a bug has been filed to inform Chromium about the regression or breaking change: https://issues.chromium.org/issues/454531070
  * investigation occurred and code has been updated to use the pattern that doesn't throw cryptic errors anymore
  * extensive tests both on Pyodide and MicroPython, main thread and workers, has been manually done to be sure all expectations are met

From users' perspective, the modal about granting access might happen twice now:

  * the first time lasts the whole session or until you close your browser
  * the next time you get a chance to allow that access *always*, as opposite of *once*
  * if you accept *always* that dialog will never bother you again unless you clear the whole browser cache

More details in #2395.
### Release: pyscript [2025.10.2](https://github.com/pyscript/pyscript/releases/tag/2025.10.2)
* Fixed remote packages issue found after real-world use case example. See: #2393 
### Release: pyscript [2025.10.1](https://github.com/pyscript/pyscript/releases/tag/2025.10.1)
* Added a *transform* ability from main to worker, not just worker to main: https://github.com/pyscript/polyscript/issues/148
* Added `experimental_remote_packages` config flag for remote packages: https://github.com/pyscript/polyscript/commit/f0861291247bd8282b6765391862ddfc3f69e216
* Augmented Pyodide bootstrap with pre-fetched packages details to improve feedback on incompatible packages when bootstrapping PyScript: https://github.com/pyscript/polyscript/commit/c879c6edf09e359435bf70383c05b65e824ee457
* Simplified the `@pyscript/bridge` to bring in automatically PyScript if not already on the page: https://github.com/pyscript/pyscript/pull/2379
* Fixed PyEditor issue on Ctrl+Enter (now working): https://github.com/pyscript/pyscript/pull/2385
* Improved `pyscript.web` after MicroPython updates: https://github.com/pyscript/pyscript/pull/2387
* We now allow you to define a custom TOML parser for more complex configs: https://github.com/pyscript/pyscript/pull/2390
* First steps (of a work in progress) to validate Pyodide package availability and metadata: https://github.com/pyscript/pyscript/pull/2392
* Updated MicroPython to version 1.27.0-preview-283:
    * Fixed proxies references
    * Improved interoperability with JS
    * Added `inspect.signature` for callables / generators / others
* Update Pyodide to version 0.29.0:
    * `py-game-ce` is back!
    * Default conversion of `to_js` as JS object literal, not map
    * Fixed a Wasm GC reference leak on invokes
    * New features / enhancements here: https://pyodide.org/en/stable/project/changelog.html#version-0-29-0
## Project: [cython/cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html), 7 releases: ['3.2.0', '3.2.0b3', '3.2.0b2', '3.1.6', '3.2.0b1-3', '3.2.0b1', '3.1.5']
### Release: cython [3.2.0](https://github.com/cython/cython/releases/tag/3.2.0)

### Release: cython [3.2.0b3](https://github.com/cython/cython/releases/tag/3.2.0b3)

### Release: cython [3.2.0b2](https://github.com/cython/cython/releases/tag/3.2.0b2)

### Release: cython [3.1.6](https://github.com/cython/cython/releases/tag/3.1.6)

### Release: cython [3.2.0b1-3](https://github.com/cython/cython/releases/tag/3.2.0b1-3)

### Release: cython [3.2.0b1](https://github.com/cython/cython/releases/tag/3.2.0b1)
Not released due to package metadata problems.
### Release: cython [3.1.5](https://github.com/cython/cython/releases/tag/3.1.5)
3.1.5 (2025-10-19)
==================

Bugs fixed
----------

* Conversion from C++ strings longer than `PY_SSIZE_T_MAX` did not validate the length.

* Some non-Limited API code was incorrectly used in generated header files.
  (Github issue :issue:`7157`)

* Optimised unpacking of Python integers in expressions uses a slightly safer scheme.
  (Github issue :issue:`7134`)

* Empty return statements were not always reported when tracing.
  (Github issue :issue:`7022`)

* Value conversion errors when tracing C return statements no longer fail the trace
  but fall back to reporting ``None`` returns instead.
  (Github issue :issue:`6503`)
## Project: [plotly/dash](https://plotly.com/dash/), 1 releases: ['Dash Version 3.3.0rc2']
### Release: dash [Dash Version 3.3.0rc2](https://github.com/plotly/dash/releases/tag/v3.3.0rc2)
- Remove placeholde publish button when on workspace
## Project: [dask/dask](https://www.dask.org/), 2 releases: ['2025.11.0', '2025.10.0']
### Release: dask [2025.11.0](https://github.com/dask/dask/releases/tag/2025.11.0)
## Changes

- Replace versioneer with setuptools-scm @jacobtomlinson (#12133)
- Apply ruff/Pylint Refactor rules (PLR) @DimitriPapadopoulos (#12010)
- Remove files from `MANIFEST.in` @DimitriPapadopoulos (#12041)
- FIX: Stabilize test\_filter\_nonpartition\_columns @dongwonmoon (#12131)
- Enforce ruff/pyupgrade rules UP007 and UP033 @DimitriPapadopoulos (#12125)
- Update ``np.accumulate`` workaround comment @jacobtomlinson (#12129)
- flake8, bugbear, pyupgrade → ruff @DimitriPapadopoulos (#12002)
- Adjust pyarrow version skip in test\_parquet @TomAugspurger (#12124)
- Fix ufunc in dask.array.cumreduction @tonyyuyiding (#12119)
- Fix docs footer @jacobtomlinson (#12120)
- use integer multiple of shard shape when rechunking in to\_zarr @d-v-b (#12106)
- ensure that the shard shape is used as the default chunk shape for sharded Zarr arrays @d-v-b (#12104)
- Skip ``test\_parquet`` for ``pyarrow==22.0`` @TomAugspurger (#12116)
- Bump actions/upload-artifact from 4 to 5 @[dependabot[bot]](https://github.com/apps/dependabot) (#12114)
- Clean up setuptools-specific configuration @DimitriPapadopoulos (#12040)
- PEP 639 compliance @DimitriPapadopoulos (#12024)
- Fix deprecated quantile 'interpolation' being passed to numpy @djhoese (#12108)
- Add uv.lock to gitignore @jacobtomlinson (#12110)
- use shard shape when available in to\_zarr @d-v-b (#12105)
- Add more optional dependencies to Python 3.13 CI builds @jrbourbeau (#12100)
- Remove ``pip`` pin for docs @jrbourbeau (#12102)
- Address collection-based ``meta`` arguments in ``GroupByApply`` @rjzamora (#12099)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

### Release: dask [2025.10.0](https://github.com/dask/dask/releases/tag/2025.10.0)
## Changes

- Use updated docs theme @jacobtomlinson (#12093)
- Fix: `dask.array.cumprod` does not deal with `dtype` @tonyyuyiding (#12097)
- cupy compatibility for percentile @TomAugspurger (#12098)
- Fix: avoid using methods.concat on empty lists @tonyyuyiding (#12096)
- Add distribution check for optional dependencies @jrbourbeau (#12087)
- Fix percentile inconsistencies @Oisin-M (#12088)
- Fix warning in test\_ufunc\_where\_no\_out @TomAugspurger (#12094)
- Fix/choose trivial case @Oisin-M (#12090)
- Add input validation on `dask.dataframe.read_sql_query()` @jacobtomlinson (#12091)
- Numpy 2.2 updates for cov function with tests @mmccarty (#12079)
- Fix/nanvar @Oisin-M (#12089)
- Document manually triggering the conda-forge bots @jacobtomlinson (#12083)
- Fix mixed HLG/Expr handling in ``\_ExprSequence.\_simplify\_down`` @rjzamora (#12081)
- DOC: Add dask.tokenize to API docs @Username46786 (#12080)
- CreateOverlappingPartitions: Add before and after to prepend name @faulaire (#11965)
- fix: csc scalar declaration in `_array_like_safe` @ilan-gold (#12078)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

## Project: [delta-io/delta-rs](https://delta-io.github.io/delta-rs/usage/installation/), 2 releases: ['python-v1.2.1: lazy writes', 'python-v1.2.0']
### Release: delta-rs [python-v1.2.1: lazy writes](https://github.com/delta-io/delta-rs/releases/tag/python-v1.2.1)
## Performance improvements
* feat: in-flight, streaming `PartitionWriter` by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/3857
* fix: use single writer for all partition streams by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3870

## What's Changed
* feat: datafusion based kernel engine by @roeap in https://github.com/delta-io/delta-rs/pull/3831
* fix: update pyproject.toml by @wagenrace in https://github.com/delta-io/delta-rs/pull/3854
* chore: upgrade datafusion, arrow and parquet by @dentiny in https://github.com/delta-io/delta-rs/pull/3856
* feat: allow RecordBatchWriter to pass through pass-through-commit-properties by @rtyler in https://github.com/delta-io/delta-rs/pull/3858
* perf: support pushing physical filters down through DeltaScan by @alexwilcoxson-rel in https://github.com/delta-io/delta-rs/pull/3859
* chore: remove some deprecated methods by @roeap in https://github.com/delta-io/delta-rs/pull/3861
* fix: resolve some warnings by @roeap in https://github.com/delta-io/delta-rs/pull/3862
* chore: deprecate file_actions on state by @roeap in https://github.com/delta-io/delta-rs/pull/3863
* refactor: consolidate datafusion session setup by @roeap in https://github.com/delta-io/delta-rs/pull/3860
* fix(core): handle Result type after get_actions sync conversion by @yousefsaad12 in https://github.com/delta-io/delta-rs/pull/3846
* chore: change the core and meta crate versions for release by @rtyler in https://github.com/delta-io/delta-rs/pull/3864
* chore: use form based issue templates by @roeap in https://github.com/delta-io/delta-rs/pull/3865
* chore: add python deprecation warnings by @roeap in https://github.com/delta-io/delta-rs/pull/3869
* feat(bench): add TPC-DS benchmarks by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/3845
* fix: add regression test for working with dotted-named columns in Python by @rtyler in https://github.com/delta-io/delta-rs/pull/3873
* fix: add a regression test while I'm tooting around by @rtyler in https://github.com/delta-io/delta-rs/pull/3874
* feat: allow for lazy loading files in operations by @roeap in https://github.com/delta-io/delta-rs/pull/3872

## New Contributors
* @wagenrace made their first contribution in https://github.com/delta-io/delta-rs/pull/3854
* @dentiny made their first contribution in https://github.com/delta-io/delta-rs/pull/3856
* @yousefsaad12 made their first contribution in https://github.com/delta-io/delta-rs/pull/3846

**Full Changelog**: https://github.com/delta-io/delta-rs/compare/python-v1.2.0...python-v1.2.1
### Release: delta-rs [python-v1.2.0](https://github.com/delta-io/delta-rs/releases/tag/python-v1.2.0)
## What's Changed
* feat!: kernel log replay by @roeap in https://github.com/delta-io/delta-rs/pull/3660
* chore: update hdfs object store to 0.15 by @Kimahriman in https://github.com/delta-io/delta-rs/pull/3681
* fix(pandas): implement-automatic-conversion-for-pandas-null-types by @fvaleye in https://github.com/delta-io/delta-rs/pull/3695
* fix(format): fix formatting in Python for conversion file by @fvaleye in https://github.com/delta-io/delta-rs/pull/3705
* chore: remove unused dependencies by @rtyler in https://github.com/delta-io/delta-rs/pull/3698
* fix: enabling correctly pulling partition values out of column mapped tables by @rtyler in https://github.com/delta-io/delta-rs/pull/3706
* feat!: use kernel predicates on file streams by @roeap in https://github.com/delta-io/delta-rs/pull/3669
* fix: reintroduce the 100 commit checkpoint interval by @rtyler in https://github.com/delta-io/delta-rs/pull/3708
* chore: follow up changes on rust-v0.28.0 by @rtyler in https://github.com/delta-io/delta-rs/pull/3712
* chore(cargo): add cargo-machete to detect and remove unused dependencies by @fvaleye in https://github.com/delta-io/delta-rs/pull/3713
* chore: update kernel to 0.15.1 by @roeap in https://github.com/delta-io/delta-rs/pull/3714
* feat(storage): expand user with tilde in local path by @fvaleye in https://github.com/delta-io/delta-rs/pull/3717
* chore: bump to a minor version for a small core release with the new kernel by @rtyler in https://github.com/delta-io/delta-rs/pull/3718
* feat: domain metadata read support by @roeap in https://github.com/delta-io/delta-rs/pull/3678
* chore!: remove deprecated methods by @roeap in https://github.com/delta-io/delta-rs/pull/3715
* refactor: move table provider to dedicated mod by @roeap in https://github.com/delta-io/delta-rs/pull/3726
* feat(url): use Url in Rust for accessing to DeltaTable, use only string-based api in Python by @fvaleye in https://github.com/delta-io/delta-rs/pull/3707
* chore(ci): cache rust dependencies in the CI by @fvaleye in https://github.com/delta-io/delta-rs/pull/3728
* refactor: avoid explicit mutex in MergeBarrier by @roeap in https://github.com/delta-io/delta-rs/pull/3734
* fix: re-export the DecimalType for consumers by @rtyler in https://github.com/delta-io/delta-rs/pull/3738
* fix: `write_deltalake` with `mode="overwrite"` mode and `schema_mode=None` does not overwrite schema metadata by @FrankPortman in https://github.com/delta-io/delta-rs/pull/3747
* feat: add per column Parquet Encoding support for Delta Table column by @niltecedu in https://github.com/delta-io/delta-rs/pull/3737
* fix: better error handles in unity client by @hntd187 in https://github.com/delta-io/delta-rs/pull/3752
* feat(datafusion): add insert_into operation with DataFusion by @fvaleye in https://github.com/delta-io/delta-rs/pull/3762
* fix: ensure that invalid URLs are bubbled up as errors when parsed by @rtyler in https://github.com/delta-io/delta-rs/pull/3766
* feat: change history() to return an Iterator by @rtyler in https://github.com/delta-io/delta-rs/pull/3764
* chore: update docs by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3761
* feat: update to DataFusion 50, pyo3 24, pyo3-arrow 0.11 by @alamb in https://github.com/delta-io/delta-rs/pull/3749
* feat: allow OptimizeBuilder to accept  SessionConfig for finer-grained control of execution by @rtyler in https://github.com/delta-io/delta-rs/pull/3763
* feat(unity-catalog): support credentials via storage options by @fvaleye in https://github.com/delta-io/delta-rs/pull/3769
* fix: check if eligible to read by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3771
* chore: upgrade the aws dependencies in deltalake-aws by @rtyler in https://github.com/delta-io/delta-rs/pull/3772
* chore: pin cargo-machete action to the sha right before a regression by @rtyler in https://github.com/delta-io/delta-rs/pull/3779
* chore: fix some typos in comment by @juejinyuxitu in https://github.com/delta-io/delta-rs/pull/3781
* chore: upgrade to delta-kernel-rs 0.16.0 and remove more dependencies by @rtyler in https://github.com/delta-io/delta-rs/pull/3773
* feat: get the delta table row count based on the table history by @ohadmata in https://github.com/delta-io/delta-rs/pull/3732
* fix: somehow the right test value didn't make it into the pr by @rtyler in https://github.com/delta-io/delta-rs/pull/3788
* fix: correct RecordBatchWriter interior schema mutation outside of evolution by @rtyler in https://github.com/delta-io/delta-rs/pull/3783
* fix: use a safe checkpoint when cleaning up metadata by @corwinjoy in https://github.com/delta-io/delta-rs/pull/3748
* chore(deps): update sqlparser requirement from 0.56.0 to 0.59.0 by @dependabot[bot] in https://github.com/delta-io/delta-rs/pull/3792
* chore(ci): add automatic cache cleanup for closed main branch PRs by @fvaleye in https://github.com/delta-io/delta-rs/pull/3793
* chore(deps): update foyer requirement from 0.17.2 to 0.20.0 by @dependabot[bot] in https://github.com/delta-io/delta-rs/pull/3791
* refactor: use EagerSnapshot in datafusion module by @roeap in https://github.com/delta-io/delta-rs/pull/3796
* feat: allow passing a `SessionState` into a `OptimizeBuilder` by @abhi-airspace-intelligence in https://github.com/delta-io/delta-rs/pull/3802
* refactor: remove table_url from Snapshot by @roeap in https://github.com/delta-io/delta-rs/pull/3803
* fix: maintaining load config from state by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3805
* refactor: consolidate extension planners by @roeap in https://github.com/delta-io/delta-rs/pull/3804
* ci: split out integration tests by @roeap in https://github.com/delta-io/delta-rs/pull/3806
* feat: access tombstones via TombstoneView by @roeap in https://github.com/delta-io/delta-rs/pull/3809
* refactor: use EagerSnapshot in vacuum operation by @roeap in https://github.com/delta-io/delta-rs/pull/3812
* fix: avoid overflow for large table state by @roeap in https://github.com/delta-io/delta-rs/pull/3801
* refactor: avoid downcasting to SessionState by @roeap in https://github.com/delta-io/delta-rs/pull/3813
* feat: add deletion_vector_descriptor method by @zeevm in https://github.com/delta-io/delta-rs/pull/3721
* refactor: move find_files into dedicated mod by @roeap in https://github.com/delta-io/delta-rs/pull/3815
* chore: remove unreferenced file by @roeap in https://github.com/delta-io/delta-rs/pull/3819
* feat: shim kernel Scan and ScanBuilder by @roeap in https://github.com/delta-io/delta-rs/pull/3818
* chore(deps): update datatest-stable requirement from 0.2 to 0.3 by @dependabot[bot] in https://github.com/delta-io/delta-rs/pull/3817
* feat: expose arrow schema on snapshots by @roeap in https://github.com/delta-io/delta-rs/pull/3822
* fix: update deprecation versions to next release by @roeap in https://github.com/delta-io/delta-rs/pull/3828
* chore: unify inconsistent `SessionState` in datafusion operations by @abhi-airspace-intelligence in https://github.com/delta-io/delta-rs/pull/3816
* fix(rust): protect recent uncommitted files in vacuum full mode by @vsmanish1772 in https://github.com/delta-io/delta-rs/pull/3835
* feat: enable ability to do writes through Unity Catalog by @hntd187 in https://github.com/delta-io/delta-rs/pull/3834
* chore(performance): optimize JSON parsing in get_actions and snapshot reading by @fvaleye in https://github.com/delta-io/delta-rs/pull/3830
* refactor(bench): remove baseline while keeping the json_parsing benchmark by @fvaleye in https://github.com/delta-io/delta-rs/pull/3838
* perf(path): only clone string for the path by @fvaleye in https://github.com/delta-io/delta-rs/pull/3841
* feat(tracing): add tracing spans to all I/O sections by @fvaleye in https://github.com/delta-io/delta-rs/pull/3795
* feat(bench): add new benchmarking script, harness, and profiling guide by @abhiaagarwal in https://github.com/delta-io/delta-rs/pull/3840
* chore: bump version from 1.1.4 to 1.2.0 by @ion-elgreco in https://github.com/delta-io/delta-rs/pull/3842

## New Contributors
* @FrankPortman made their first contribution in https://github.com/delta-io/delta-rs/pull/3747
* @niltecedu made their first contribution in https://github.com/delta-io/delta-rs/pull/3737
* @juejinyuxitu made their first contribution in https://github.com/delta-io/delta-rs/pull/3781
* @ohadmata made their first contribution in https://github.com/delta-io/delta-rs/pull/3732
* @abhi-airspace-intelligence made their first contribution in https://github.com/delta-io/delta-rs/pull/3802
* @vsmanish1772 made their first contribution in https://github.com/delta-io/delta-rs/pull/3835

**Full Changelog**: https://github.com/delta-io/delta-rs/compare/python-v1.1.4...python-v1.2.0
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 13 releases: ['v0.40.0-beta.2', 'v0.40.0-beta.1', 'v0.39.0', 'v0.38.3', 'v0.38.3-beta.11', 'v0.38.3-beta.10', 'v0.38.3-beta.9', 'v0.38.3-beta.8', 'v0.38.3-beta.7', 'v0.38.3-beta.6', 'v0.38.3-beta.5', 'v0.38.3-beta.4', 'v0.38.3-beta.3']
### Release: lance [v0.40.0-beta.2](https://github.com/lancedb/lance/releases/tag/v0.40.0-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v0.40.0-beta.2 -->



**Full Changelog**: https://github.com/lancedb/lance/compare/release-root/0.40.0-beta.N...v0.40.0-beta.2
### Release: lance [v0.40.0-beta.1](https://github.com/lancedb/lance/releases/tag/v0.40.0-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v0.40.0-beta.1 -->

## What's Changed
### Breaking Changes 🛠
* refactor: remove not used storage class and blob dataset by @Xuanwo in https://github.com/lancedb/lance/pull/5131
### New Features 🎉
* feat: add fuzziness to json inverted match query by @wojiaodoubao in https://github.com/lancedb/lance/pull/5048
* feat(java): expose cleanup_with_policy api by @fangbo in https://github.com/lancedb/lance/pull/5136
* feat(java): supports building scalar indices distributedly in java module by @steFaiz in https://github.com/lancedb/lance/pull/4961
### Bug Fixes 🐛
* fix: always return correct json schema to users by @Xuanwo in https://github.com/lancedb/lance/pull/5109
* fix: ensure I/O cancels correctly when scan is dropped by @westonpace in https://github.com/lancedb/lance/pull/5129
* fix: remove unnecessary object store initialization by @zhangyue19921010 in https://github.com/lancedb/lance/pull/5145
* fix: use typed LanceNamespace for python storage options provider by @jackye1995 in https://github.com/lancedb/lance/pull/5151
### Performance Improvements 🚀
* perf: add a chunk cache to avoid decoding duplicated miniblock chunks by @niyue in https://github.com/lancedb/lance/pull/4846


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.39.0...v0.40.0-beta.1
### Release: lance [v0.39.0](https://github.com/lancedb/lance/releases/tag/v0.39.0)
<!-- Release notes generated using configuration in .github/release.yml at v0.39.0 -->

## What's Changed
### Breaking Changes 🛠
* feat!: incremental indexing via SPFresh by @BubbleCal in https://github.com/lancedb/lance/pull/4837
### New Features 🎉
* feat(java): expose ManifestSummary to java api by @steFaiz in https://github.com/lancedb/lance/pull/5092
* feat: support dynamic storage options provider with AWS credentials vending by @jackye1995 in https://github.com/lancedb/lance/pull/4905
### Bug Fixes 🐛
* fix: infinite kmeans if the largest cluster produces only 1 cluster by @BubbleCal in https://github.com/lancedb/lance/pull/5078
* fix: remove remainder explain_plan method in Python by @ddupg in https://github.com/lancedb/lance/pull/5085
* fix(rust): add explicit dependency on chrono serde feature by @wjones127 in https://github.com/lancedb/lance/pull/5110
* fix: no panic on unknown version by @wjones127 in https://github.com/lancedb/lance/pull/5111
* fix: skip compression in create_per_value if compression metadata is set to none by @wojiaodoubao in https://github.com/lancedb/lance/pull/5086
* fix: forward incompatibility of prerelease in writer version by @jackye1995 in https://github.com/lancedb/lance/pull/5116
### Documentation 📚
* docs: minor doc fix for docs/src/format/file/encoding.md by @zhangyue19921010 in https://github.com/lancedb/lance/pull/5108
* docs: add fragment level update columns docs by @xloya in https://github.com/lancedb/lance/pull/5123
### Other Changes
* refactor: introduce SchemaAdapter to perform logical/physical transform by @Xuanwo in https://github.com/lancedb/lance/pull/5096


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3...v0.39.0
### Release: lance [v0.38.3](https://github.com/lancedb/lance/releases/tag/v0.38.3)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3 -->

## What's Changed
### Breaking Changes 🛠
* refactor!: cleanup public API, remove lance_arrow re-exports by @westonpace in https://github.com/lancedb/lance/pull/4991
### New Features 🎉
* feat: handle forking better by @cmccabe in https://github.com/lancedb/lance/pull/4903
* feat: add multi-path support for lance data paths by @jaystarshot in https://github.com/lancedb/lance/pull/4765
* feat: support general compression zstd/lz4 in blocks by @lyang24 in https://github.com/lancedb/lance/pull/4900
* feat: fts supports custom stop words by @wojiaodoubao in https://github.com/lancedb/lance/pull/4866
* feat: implement add_bases api to add bases to lance dataset by @jaystarshot in https://github.com/lancedb/lance/pull/4945
* feat: allow a commit message to be specified in the python dataset commit method by @westonpace in https://github.com/lancedb/lance/pull/4952
* feat: support tracking newly inserted and updated rows between versions by @yanghua in https://github.com/lancedb/lance/pull/4741
* feat: support fetching _rowid and _rowaddr in take operation by @chunshao90 in https://github.com/lancedb/lance/pull/4794
* feat: support mTLS in REST namespace by @jackye1995 in https://github.com/lancedb/lance/pull/4981
* fix: populate all fields from ExecutionSummaryCounts to  ScannerStats by @jaystarshot in https://github.com/lancedb/lance/pull/4980
* feat: support WhenMatched::Fail for MergeInsert by @ddupg in https://github.com/lancedb/lance/pull/4956
* feat(java): support shallow_clone by @majin1102 in https://github.com/lancedb/lance/pull/4962
* feat: add VariablePackedStruct defination by @Xuanwo in https://github.com/lancedb/lance/pull/4950
* feat: log version on dataset load event by @wjones127 in https://github.com/lancedb/lance/pull/4988
* feat(java): support blob api by @majin1102 in https://github.com/lancedb/lance/pull/4769
* feat(python): support shallow_clone by @majin1102 in https://github.com/lancedb/lance/pull/4949
* feat: expose storage options in dataset by @jackye1995 in https://github.com/lancedb/lance/pull/5016
* feat: should dictionary encode based on size by @yingjianwu98 in https://github.com/lancedb/lance/pull/4972
* feat: add variable packed struct support by @Xuanwo in https://github.com/lancedb/lance/pull/5003
* feat(python): support index for nested field by @jackye1995 in https://github.com/lancedb/lance/pull/5027
* feat(java): support branch operations by @majin1102 in https://github.com/lancedb/lance/pull/5012
* feat(python): support branch operations by @majin1102 in https://github.com/lancedb/lance/pull/5010
* feat: add json fts in python by @wojiaodoubao in https://github.com/lancedb/lance/pull/5020
* feat: add file audit events for deleting staging manifest paths in external commit handler by @wjones127 in https://github.com/lancedb/lance/pull/4989
* feat: implement create index and data replacement conflict rules by @westonpace in https://github.com/lancedb/lance/pull/5077
* feat: support fragment level update columns operation in Python by @xloya in https://github.com/lancedb/lance/pull/5001
### Bug Fixes 🐛
* fix: let Java module use LanceFileVersion::Stable (#4558) by @ColdL in https://github.com/lancedb/lance/pull/4559
* fix: fts match query on column without inverted index by @wojiaodoubao in https://github.com/lancedb/lance/pull/4859
* fix: fix broken FTS example by replacing ROW_ID with DOC_ID by @niebayes in https://github.com/lancedb/lance/pull/4917
* fix: correctly record output_rows in filtered read with hard range_after by @westonpace in https://github.com/lancedb/lance/pull/4919
* fix: rewrap LanceFilterExec with_new_children by @wkalt in https://github.com/lancedb/lance/pull/4920
* fix: optimize_indices may unexpectly delete delta indices by @BubbleCal in https://github.com/lancedb/lance/pull/4931
* fix: rebuild HNSW graph while remapping it by @BubbleCal in https://github.com/lancedb/lance/pull/4941
* fix: be compatible to old `pack` metadata in 2.0 by @Xuanwo in https://github.com/lancedb/lance/pull/4964
* fix: filter with < current_date() should expand with correct time by @Xuanwo in https://github.com/lancedb/lance/pull/4963
* fix: use correct logic to detect old/new scheme in binary block decoder by @westonpace in https://github.com/lancedb/lance/pull/4966
* fix: support preview relase in writer version by @jackye1995 in https://github.com/lancedb/lance/pull/4974
* fix: index cache assumed_entry_size is inconsistent by @ddupg in https://github.com/lancedb/lance/pull/4975
* fix: clarify column names in missing column errors by @wkalt in https://github.com/lancedb/lance/pull/4942
* fix: the KMeans may result in all zeros centroids by @BubbleCal in https://github.com/lancedb/lance/pull/4977
* fix: full text search may miss some results by @BubbleCal in https://github.com/lancedb/lance/pull/4986
* fix: do not modify Lance schema when projecting system columns by @jackye1995 in https://github.com/lancedb/lance/pull/4997
* fix: handle empty batches in dictionary decode helper by @yingjianwu98 in https://github.com/lancedb/lance/pull/4995
* fix: coerce nested regexp_match to boolean in filters by @BubbleCal in https://github.com/lancedb/lance/pull/5019
* fix: update to respect file version from write params when writing fragments in java by @morales-t-netflix in https://github.com/lancedb/lance/pull/5014
* fix: general block decompression mismatch for Lance 2.2 dictionaries by @Xuanwo in https://github.com/lancedb/lance/pull/5025
* fix: handle List types in Substrait field counting by @LuQQiu in https://github.com/lancedb/lance/pull/5015
* fix: ensure limit cancels scan by @westonpace in https://github.com/lancedb/lance/pull/5032
* fix: don't panic in 2.1 if one page has nulls and the other doesn't by @westonpace in https://github.com/lancedb/lance/pull/5074
* fix: correct read column ordering in Fragment::update_columns by @wayneli-vt in https://github.com/lancedb/lance/pull/4983
* fix(java): the CompactionOptions is not serializable by @steFaiz in https://github.com/lancedb/lance/pull/4819
* fix: fix the deduplicated prefix in the opendal s3 store root setting by @xloya in https://github.com/lancedb/lance/pull/5082
### Documentation 📚
* docs: add RabitQ in vector index spec by @BubbleCal in https://github.com/lancedb/lance/pull/4913
* docs: document the metadata cache by @westonpace in https://github.com/lancedb/lance/pull/4953
* docs: add docs for newly added options by @Xuanwo in https://github.com/lancedb/lance/pull/4976
* docs: minor fix for docs/src/format/table/index.md#Deletion by @zhangyue19921010 in https://github.com/lancedb/lance/pull/5033
* docs: minor doc fix for stable row id description by @zhangyue19921010 in https://github.com/lancedb/lance/pull/5047
* docs: add initial migration guide and document some steps for 0.39 by @westonpace in https://github.com/lancedb/lance/pull/5052
* docs: add migration guide for diff_meta and namespace by @jackye1995 in https://github.com/lancedb/lance/pull/5054
* docs: add json to full text search document by @wojiaodoubao in https://github.com/lancedb/lance/pull/4865
### Other Changes
* refactor: move lance-namespace into lance repo by @jackye1995 in https://github.com/lancedb/lance/pull/4978
* refactor: use lance-io object store for dir namespace and improve builder by @jackye1995 in https://github.com/lancedb/lance/pull/5045
* refactor: don't add new with_... columns to scanner by @westonpace in https://github.com/lancedb/lance/pull/5007

## New Contributors
* @yingjianwu98 made their first contribution in https://github.com/lancedb/lance/pull/4901
* @niebayes made their first contribution in https://github.com/lancedb/lance/pull/4917
* @zhangyue19921010 made their first contribution in https://github.com/lancedb/lance/pull/4915
* @dependabot[bot] made their first contribution in https://github.com/lancedb/lance/pull/4954
* @chunshao90 made their first contribution in https://github.com/lancedb/lance/pull/4794

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.2...v0.38.3
### Release: lance [v0.38.3-beta.11](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.11)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.11 -->

## What's Changed
### New Features 🎉
* feat(java): support branch operations by @majin1102 in https://github.com/lancedb/lance/pull/5012
* feat(python): support branch operations by @majin1102 in https://github.com/lancedb/lance/pull/5010
* feat: add json fts in python by @wojiaodoubao in https://github.com/lancedb/lance/pull/5020
### Bug Fixes 🐛
* fix: ensure limit cancels scan by @westonpace in https://github.com/lancedb/lance/pull/5032
* fix: don't panic in 2.1 if one page has nulls and the other doesn't by @westonpace in https://github.com/lancedb/lance/pull/5074
### Documentation 📚
* docs: minor doc fix for stable row id description by @zhangyue19921010 in https://github.com/lancedb/lance/pull/5047
* docs: add initial migration guide and document some steps for 0.39 by @westonpace in https://github.com/lancedb/lance/pull/5052
* docs: add migration guide for diff_meta and namespace by @jackye1995 in https://github.com/lancedb/lance/pull/5054
* docs: add json to full text search document by @wojiaodoubao in https://github.com/lancedb/lance/pull/4865
### Other Changes
* refactor: use lance-io object store for dir namespace and improve builder by @jackye1995 in https://github.com/lancedb/lance/pull/5045
* refactor: don't add new with_... columns to scanner by @westonpace in https://github.com/lancedb/lance/pull/5007


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.10...v0.38.3-beta.11
### Release: lance [v0.38.3-beta.10](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.10)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.10 -->

## What's Changed
### New Features 🎉
* feat: should dictionary encode based on size by @yingjianwu98 in https://github.com/lancedb/lance/pull/4972
* feat: add variable packed struct support by @Xuanwo in https://github.com/lancedb/lance/pull/5003
* feat(python): support index for nested field by @jackye1995 in https://github.com/lancedb/lance/pull/5027
### Bug Fixes 🐛
* fix: update to respect file version from write params when writing fragments in java by @morales-t-netflix in https://github.com/lancedb/lance/pull/5014
* fix: general block decompression mismatch for Lance 2.2 dictionaries by @Xuanwo in https://github.com/lancedb/lance/pull/5025
* fix: handle List types in Substrait field counting by @LuQQiu in https://github.com/lancedb/lance/pull/5015
### Documentation 📚
* docs: minor fix for docs/src/format/table/index.md#Deletion by @zhangyue19921010 in https://github.com/lancedb/lance/pull/5033


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.9...v0.38.3-beta.10
### Release: lance [v0.38.3-beta.9](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.9)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.9 -->

## What's Changed
### Breaking Changes 🛠
* refactor!: cleanup public API, remove lance_arrow re-exports by @westonpace in https://github.com/lancedb/lance/pull/4991
### New Features 🎉
* feat: expose storage options in dataset by @jackye1995 in https://github.com/lancedb/lance/pull/5016


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.8...v0.38.3-beta.9
### Release: lance [v0.38.3-beta.8](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.8)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.8 -->

## What's Changed
### New Features 🎉
* feat: log version on dataset load event by @wjones127 in https://github.com/lancedb/lance/pull/4988
* feat(java): support blob api by @majin1102 in https://github.com/lancedb/lance/pull/4769
* feat(python): support shallow_clone by @majin1102 in https://github.com/lancedb/lance/pull/4949
### Bug Fixes 🐛
* fix: coerce nested regexp_match to boolean in filters by @BubbleCal in https://github.com/lancedb/lance/pull/5019


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.7...v0.38.3-beta.8
### Release: lance [v0.38.3-beta.7](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.7)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.7 -->



**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.6...v0.38.3-beta.7
### Release: lance [v0.38.3-beta.6](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.6)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.6 -->

## What's Changed
### New Features 🎉
* feat: support WhenMatched::Fail for MergeInsert by @ddupg in https://github.com/lancedb/lance/pull/4956
* feat(java): support shallow_clone by @majin1102 in https://github.com/lancedb/lance/pull/4962
* feat: add VariablePackedStruct defination by @Xuanwo in https://github.com/lancedb/lance/pull/4950
### Bug Fixes 🐛
* fix: do not modify Lance schema when projecting system columns by @jackye1995 in https://github.com/lancedb/lance/pull/4997
* fix: handle empty batches in dictionary decode helper by @yingjianwu98 in https://github.com/lancedb/lance/pull/4995


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.5...v0.38.3-beta.6
### Release: lance [v0.38.3-beta.5](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.5)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.5 -->

## What's Changed
### New Features 🎉
* feat: support fetching _rowid and _rowaddr in take operation by @chunshao90 in https://github.com/lancedb/lance/pull/4794
* feat: support mTLS in REST namespace by @jackye1995 in https://github.com/lancedb/lance/pull/4981
* fix: populate all fields from ExecutionSummaryCounts to  ScannerStats by @jaystarshot in https://github.com/lancedb/lance/pull/4980
### Bug Fixes 🐛
* fix: index cache assumed_entry_size is inconsistent by @ddupg in https://github.com/lancedb/lance/pull/4975
* fix: clarify column names in missing column errors by @wkalt in https://github.com/lancedb/lance/pull/4942
* fix: the KMeans may result in all zeros centroids by @BubbleCal in https://github.com/lancedb/lance/pull/4977
* fix: full text search may miss some results by @BubbleCal in https://github.com/lancedb/lance/pull/4986
### Documentation 📚
* docs: add docs for newly added options by @Xuanwo in https://github.com/lancedb/lance/pull/4976
### Other Changes
* refactor: move lance-namespace into lance repo by @jackye1995 in https://github.com/lancedb/lance/pull/4978

## New Contributors
* @chunshao90 made their first contribution in https://github.com/lancedb/lance/pull/4794

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.4...v0.38.3-beta.5
### Release: lance [v0.38.3-beta.4](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.4)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.4 -->

## What's Changed
### Bug Fixes 🐛
* fix: support preview relase in writer version by @jackye1995 in https://github.com/lancedb/lance/pull/4974


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.3...v0.38.3-beta.4
### Release: lance [v0.38.3-beta.3](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.3)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.3 -->

## What's Changed
### New Features 🎉
* feat: support general compression zstd/lz4 in blocks by @lyang24 in https://github.com/lancedb/lance/pull/4900
* feat: fts supports custom stop words by @wojiaodoubao in https://github.com/lancedb/lance/pull/4866
* feat: implement add_bases api to add bases to lance dataset by @jaystarshot in https://github.com/lancedb/lance/pull/4945
* feat: allow a commit message to be specified in the python dataset commit method by @westonpace in https://github.com/lancedb/lance/pull/4952
* feat: support tracking newly inserted and updated rows between versions by @yanghua in https://github.com/lancedb/lance/pull/4741
### Bug Fixes 🐛
* fix: optimize_indices may unexpectly delete delta indices by @BubbleCal in https://github.com/lancedb/lance/pull/4931
* fix: rebuild HNSW graph while remapping it by @BubbleCal in https://github.com/lancedb/lance/pull/4941
* fix: be compatible to old `pack` metadata in 2.0 by @Xuanwo in https://github.com/lancedb/lance/pull/4964
* fix: filter with < current_date() should expand with correct time by @Xuanwo in https://github.com/lancedb/lance/pull/4963
* fix: use correct logic to detect old/new scheme in binary block decoder by @westonpace in https://github.com/lancedb/lance/pull/4966
### Documentation 📚
* docs: document the metadata cache by @westonpace in https://github.com/lancedb/lance/pull/4953

## New Contributors
* @zhangyue19921010 made their first contribution in https://github.com/lancedb/lance/pull/4915
* @dependabot[bot] made their first contribution in https://github.com/lancedb/lance/pull/4954

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.2...v0.38.3-beta.3
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 14 releases: ['Node/Rust LanceDB v0.22.3', 'Python LanceDB v0.25.3', 'Node/Rust LanceDB v0.22.3-beta.5', 'Node/Rust LanceDB v0.22.3-beta.4', 'Python LanceDB v0.25.3-beta.5', 'Python LanceDB v0.25.3-beta.4', 'Node/Rust LanceDB v0.22.3-beta.3', 'Python LanceDB v0.25.3-beta.3', 'Node/Rust LanceDB v0.22.3-beta.2', 'Python LanceDB v0.25.3-beta.2', 'Node/Rust LanceDB v0.22.3-beta.1', 'Python LanceDB v0.25.3-beta.1', 'Node/Rust LanceDB v0.22.3-beta.0', 'Python LanceDB v0.25.3-beta.0']
### Release: lancedb [Node/Rust LanceDB v0.22.3](https://github.com/lancedb/lancedb/releases/tag/v0.22.3)
## 🎉 New Features

- feat(index): add IVF_RQ index type by @BubbleCal in https://github.com/lancedb/lancedb/pull/2687
- feat: a utility for creating "permutation views" by @westonpace in https://github.com/lancedb/lancedb/pull/2552
- feat: bump lance to 0.38.3-beta.2 and rust to 1.90.0 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2714
- feat: add output_schema method to queries by @westonpace in https://github.com/lancedb/lancedb/pull/2717
- feat: remove dynamodb default dependency by @valkum in https://github.com/lancedb/lancedb/pull/2720
- feat: expand support for multivector colpali models and enchancements by @AyushExel in https://github.com/lancedb/lancedb/pull/2719
- feat: using codex to auto upgrade lance by @Xuanwo in https://github.com/lancedb/lancedb/pull/2723
- feat: add a permutation reader that can read a permutation view by @westonpace in https://github.com/lancedb/lancedb/pull/2712
- feat: expose storage options in table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2736
- feat(voyageai): update voyage integration by @fzowl in https://github.com/lancedb/lancedb/pull/2713
- feat: add fts udtf in sql by @LuQQiu in https://github.com/lancedb/lancedb/pull/2755
- feat: add `source` to TableNotFound errors by @wjones127 in https://github.com/lancedb/lancedb/pull/2765
- feat: add python Permutation class to mimic hugging face dataset and provide pytorch dataloader by @westonpace in https://github.com/lancedb/lancedb/pull/2725

## 🐛 Bug Fixes

- fix: relax bytemuck and crunchy version pins by @rm-dr in https://github.com/lancedb/lancedb/pull/2768

## 📚 Documentation

- docs: remove DynamoDB commit store section by @ozkatz in https://github.com/lancedb/lancedb/pull/2715

## Other Changes

- chore: update lance dependency to v0.38.3-beta.7 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2735
- chore: update lance dependency to v0.38.3-beta.8 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2737

## 🔧 Build and CI

- ci: polish prompt to make codex happy work by @Xuanwo in https://github.com/lancedb/lancedb/pull/2724
- ci: use robot token instead of github's own token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2732
- ci: add instruct for codex to use gh with token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2734
- ci: make sure GH_TOKEN included in codex env by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2738
- ci: polish codex prompt for better behavior by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2739
- ci: add agents and add reviewing instructions by @wjones127 in https://github.com/lancedb/lancedb/pull/2754


### Release: lancedb [Python LanceDB v0.25.3](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3)
## 🎉 New Features

- feat(index): add IVF_RQ index type by @BubbleCal in https://github.com/lancedb/lancedb/pull/2687
- feat: a utility for creating "permutation views" by @westonpace in https://github.com/lancedb/lancedb/pull/2552
- feat: bump lance to 0.38.3-beta.2 and rust to 1.90.0 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2714
- feat: add output_schema method to queries by @westonpace in https://github.com/lancedb/lancedb/pull/2717
- feat: remove dynamodb default dependency by @valkum in https://github.com/lancedb/lancedb/pull/2720
- feat: expand support for multivector colpali models and enchancements by @AyushExel in https://github.com/lancedb/lancedb/pull/2719
- feat: using codex to auto upgrade lance by @Xuanwo in https://github.com/lancedb/lancedb/pull/2723
- feat: add a permutation reader that can read a permutation view by @westonpace in https://github.com/lancedb/lancedb/pull/2712
- feat: expose storage options in table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2736
- feat(voyageai): update voyage integration by @fzowl in https://github.com/lancedb/lancedb/pull/2713
- feat: add fts udtf in sql by @LuQQiu in https://github.com/lancedb/lancedb/pull/2755
- feat: add `source` to TableNotFound errors by @wjones127 in https://github.com/lancedb/lancedb/pull/2765
- feat: add python Permutation class to mimic hugging face dataset and provide pytorch dataloader by @westonpace in https://github.com/lancedb/lancedb/pull/2725

## 🐛 Bug Fixes

- fix: relax bytemuck and crunchy version pins by @rm-dr in https://github.com/lancedb/lancedb/pull/2768

## 📚 Documentation

- docs: remove DynamoDB commit store section by @ozkatz in https://github.com/lancedb/lancedb/pull/2715

## Other Changes

- chore: update lance dependency to v0.38.3-beta.7 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2735
- chore: update lance dependency to v0.38.3-beta.8 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2737

## 🔧 Build and CI

- ci: polish prompt to make codex happy work by @Xuanwo in https://github.com/lancedb/lancedb/pull/2724
- ci: use robot token instead of github's own token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2732
- ci: add instruct for codex to use gh with token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2734
- ci: make sure GH_TOKEN included in codex env by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2738
- ci: polish codex prompt for better behavior by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2739
- ci: add agents and add reviewing instructions by @wjones127 in https://github.com/lancedb/lancedb/pull/2754


### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.5](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.5)
## 🎉 New Features

- feat: add fts udtf in sql by @LuQQiu in https://github.com/lancedb/lancedb/pull/2755


### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.4](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.4)
## 🎉 New Features

- feat(voyageai): update voyage integration by @fzowl in https://github.com/lancedb/lancedb/pull/2713

## 📚 Documentation

- docs: remove DynamoDB commit store section by @ozkatz in https://github.com/lancedb/lancedb/pull/2715

## 🔧 Build and CI

- ci: add agents and add reviewing instructions by @wjones127 in https://github.com/lancedb/lancedb/pull/2754


### Release: lancedb [Python LanceDB v0.25.3-beta.5](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3-beta.5)
## 🎉 New Features

- feat: add fts udtf in sql by @LuQQiu in https://github.com/lancedb/lancedb/pull/2755


### Release: lancedb [Python LanceDB v0.25.3-beta.4](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3-beta.4)
## 🎉 New Features

- feat(voyageai): update voyage integration by @fzowl in https://github.com/lancedb/lancedb/pull/2713

## 📚 Documentation

- docs: remove DynamoDB commit store section by @ozkatz in https://github.com/lancedb/lancedb/pull/2715

## 🔧 Build and CI

- ci: add agents and add reviewing instructions by @wjones127 in https://github.com/lancedb/lancedb/pull/2754


### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.3](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.3)

### Release: lancedb [Python LanceDB v0.25.3-beta.3](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3-beta.3)

### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.2](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.2)
## 🎉 New Features

- feat: expose storage options in table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2736

## Other Changes

- chore: update lance dependency to v0.38.3-beta.7 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2735
- chore: update lance dependency to v0.38.3-beta.8 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2737

## 🔧 Build and CI

- ci: use robot token instead of github's own token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2732
- ci: add instruct for codex to use gh with token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2734
- ci: make sure GH_TOKEN included in codex env by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2738
- ci: polish codex prompt for better behavior by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2739


### Release: lancedb [Python LanceDB v0.25.3-beta.2](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3-beta.2)
## 🎉 New Features

- feat: expose storage options in table by @jackye1995 in https://github.com/lancedb/lancedb/pull/2736

## Other Changes

- chore: update lance dependency to v0.38.3-beta.7 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2735
- chore: update lance dependency to v0.38.3-beta.8 by @github-actions[bot] in https://github.com/lancedb/lancedb/pull/2737

## 🔧 Build and CI

- ci: use robot token instead of github's own token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2732
- ci: add instruct for codex to use gh with token by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2734
- ci: make sure GH_TOKEN included in codex env by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2738
- ci: polish codex prompt for better behavior by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2739


### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.1](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.1)
## 🎉 New Features

- feat: add output_schema method to queries by @westonpace in https://github.com/lancedb/lancedb/pull/2717
- feat: remove dynamodb default dependency by @valkum in https://github.com/lancedb/lancedb/pull/2720
- feat: expand support for multivector colpali models and enchancements by @AyushExel in https://github.com/lancedb/lancedb/pull/2719
- feat: using codex to auto upgrade lance by @Xuanwo in https://github.com/lancedb/lancedb/pull/2723
- feat: add a permutation reader that can read a permutation view by @westonpace in https://github.com/lancedb/lancedb/pull/2712

## 🔧 Build and CI

- ci: polish prompt to make codex happy work by @Xuanwo in https://github.com/lancedb/lancedb/pull/2724


### Release: lancedb [Python LanceDB v0.25.3-beta.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3-beta.1)
## 🎉 New Features

- feat: add output_schema method to queries by @westonpace in https://github.com/lancedb/lancedb/pull/2717
- feat: remove dynamodb default dependency by @valkum in https://github.com/lancedb/lancedb/pull/2720
- feat: expand support for multivector colpali models and enchancements by @AyushExel in https://github.com/lancedb/lancedb/pull/2719
- feat: using codex to auto upgrade lance by @Xuanwo in https://github.com/lancedb/lancedb/pull/2723
- feat: add a permutation reader that can read a permutation view by @westonpace in https://github.com/lancedb/lancedb/pull/2712

## 🔧 Build and CI

- ci: polish prompt to make codex happy work by @Xuanwo in https://github.com/lancedb/lancedb/pull/2724


### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.0)
## 🎉 New Features

- feat(index): add IVF_RQ index type by @BubbleCal in https://github.com/lancedb/lancedb/pull/2687
- feat: a utility for creating "permutation views" by @westonpace in https://github.com/lancedb/lancedb/pull/2552
- feat: bump lance to 0.38.3-beta.2 and rust to 1.90.0 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2714


### Release: lancedb [Python LanceDB v0.25.3-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.3-beta.0)
## 🎉 New Features

- feat(index): add IVF_RQ index type by @BubbleCal in https://github.com/lancedb/lancedb/pull/2687
- feat: a utility for creating "permutation views" by @westonpace in https://github.com/lancedb/lancedb/pull/2552
- feat: bump lance to 0.38.3-beta.2 and rust to 1.90.0 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2714


## Project: [trinodb/trino](https://trino.io/docs/current/release/release-{release}.html), 1 releases: ['Trino 478']
### Release: trino [Trino 478](https://github.com/trinodb/trino/releases/tag/478)
See the [release notes](https://trino.io/docs/current/release/release-478.html) or [download Trino](https://trino.io/download)
