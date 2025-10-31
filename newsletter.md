# Complete List of Projects
 * Project: apache/arrow has 3 releases
 * Project: posit-dev/great-tables has 1 releases
 * Project: ibis-project/ibis has 1 releases
 * Project: narwhals-dev/narwhals has 4 releases
 * Project: pola-rs/polars has 5 releases
 * Project: holoviz/panel has 1 releases
 * Project: pyscript/pyscript has 3 releases
 * Project: cython/cython has 6 releases
 * Project: plotly/dash has 3 releases
 * Project: dask/dask has 1 releases
 * Project: delta-io/delta-rs has 2 releases
 * Project: rapidsai/cudf has 1 releases
 * Project: lancedb/lance has 15 releases
 * Project: lancedb/lancedb has 17 releases
 * Project: duckdb/duckdb has 1 releases
 * Project: trinodb/trino has 1 releases
 * Project: https://spark.apache.org/news/index.html has 1 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 1 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 1 articles
### Release: [Preview release of Spark 4.1.0](https://spark.apache.org/news/spark-4-1-0-preview3-released.html)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 1 articles
### Release: [Apache DataFusion Comet 0.11.0 Release](https://datafusion.apache.org/blog/2025/10/21/datafusion-comet-0.11.0)

## Project: [apache/arrow](https://arrow.apache.org/docs/python/), 3 releases: ['Apache Arrow 22.0.0', 'Apache Arrow 22.0.0 RC1', 'Apache Arrow 22.0.0 RC0']
### Release: arrow [Apache Arrow 22.0.0](https://github.com/apache/arrow/releases/tag/apache-arrow-22.0.0)
Release Notes URL: https://arrow.apache.org/release/22.0.0.html
### Release: arrow [Apache Arrow 22.0.0 RC1](https://github.com/apache/arrow/releases/tag/apache-arrow-22.0.0-rc1)
Release Notes: Release Candidate: 22.0.0 RC1
### Release: arrow [Apache Arrow 22.0.0 RC0](https://github.com/apache/arrow/releases/tag/apache-arrow-22.0.0-rc0)
Release Notes: Release Candidate: 22.0.0 RC0
## Project: [posit-dev/great-tables](https://posit-dev.github.io/great-tables/get-started/), 1 releases: ['v0.19.0']
### Release: great-tables [v0.19.0](https://github.com/posit-dev/great-tables/releases/tag/v0.19.0)
## Fixes

* Code using the NumPy library was replaced with standard Python to enable the removal of NumPy from the dependencies list, by @tylerriccio33 in https://github.com/posit-dev/great-tables/pull/749
* An error when setting `groupname_col=` without `rowname_col=` in the `GT` constructor has been fixed by @juleswg23 in https://github.com/posit-dev/great-tables/pull/756
* Using `row_group_as_column = True` now structures row groups as a column in the stub (previously, this was a no-op), by @juleswg23 in https://github.com/posit-dev/great-tables/pull/754
* The `data_color()` method now takes the alpha value for the cell background color into account when choosing the foreground text color (fixes the internal `_ideal_fgnd_color()` util function), by @juleswg23 in https://github.com/posit-dev/great-tables/pull/747
* When enabling row striping, there is now better color contrast between the text and the underlying cell background, by @juleswg23 in https://github.com/posit-dev/great-tables/pull/745
* We now internally access column names consistently through `get_column_names()` instead of `.columns`, by @FBruzzesi in https://github.com/posit-dev/great-tables/pull/736
* Column values with the `pyarrow` `float64` type are now right-aligned to match the default behavior when using Pandas and Polars DFs, by @FBruzzesi in https://github.com/posit-dev/great-tables/pull/734
* We now avoid the double use of `clear` internally with Polars DFs, by @FBruzzesi in https://github.com/posit-dev/great-tables/pull/729

## Docs

* Various typos were corrected by @FBruzzesi in https://github.com/posit-dev/great-tables/pull/730
* We now include a Posit badge in the header of the project website, by @rich-iannone in https://github.com/posit-dev/great-tables/pull/777

## Chores

* Refactoring was done to better adhere to best practices and to improve code performance, by @FBruzzesi in https://github.com/posit-dev/great-tables/pull/731

## New Contributors
* @FBruzzesi made their first contribution in https://github.com/posit-dev/great-tables/pull/731

**Full Changelog**: https://github.com/posit-dev/great-tables/compare/v0.18.0...v0.19.0
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

## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 4 releases: ['Narwhals v2.10.0', 'Narwhals v2.9.0', 'Narwhals v2.8.0', 'Narwhals v2.7.0']
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

### Release: narwhals [Narwhals v2.7.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.7.0)
## Changes

## ✨ Enhancements

- enh: Add `nw.format` (#3169)
- feat: Adds `{Expr,Series}.{first,last}` (#2528)
- feat: Support `polars.UInt128` (#3138)
- feat: Add `prefix` argument to `generate_temporary_column_name` (#3147)
- feat: Add `{nw,DataFrame}.from_dicts` (#3148)

## 🐞 Bug fixes

- fix: raise for rank followed by over with order_by for sql-like backends (#3178)
- chore: Make `Implementation.UNKNOWN._backend_version()` safe (#3133)

## 📖 Documentation

- docs(python) remove now unnecessary returns statements (#3170)

## 🛠️ Other improvements

- chore: Add `CompliantNamespace.is_native` (#3130)
- chore: Make `Implementation.UNKNOWN._backend_version()` safe (#3133)
- chore(typing): Ignore another `EagerDataFrame` intermittent [False Negative] (#3142)
- ci: fix darts job (#3172)
- fix: add `--upgrade` flag to `uv sync --dev` (#3175)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @akmalsoliev, @dangotbanned, @dependabot[bot], @felixgwilliams and [dependabot[bot]](https://github.com/apps/dependabot)

## Project: [pola-rs/polars](https://docs.pola.rs/), 5 releases: ['Python Polars 1.35.1', 'Python Polars 1.35.0', 'Python Polars 1.35.0-beta.1', 'Python Polars 1.34.0', 'Python Polars 1.34.0-beta.5']
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

### Release: polars [Python Polars 1.34.0](https://github.com/pola-rs/polars/releases/tag/py-1.34.0)
## 🏆 Highlights

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)

## 🚀 Performance improvements

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
- Native streaming `.mode()` expression (#24459)

## ✨ Enhancements

- Implement maintain\_order for cross join (#24665)
- Add support to output `dt.total_{}()` duration values as fractionals (#24598)
- Avoid forcing a `pyarrow` dependency in `read_excel` when using the default "calamine" engine (#24655)
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

- Removing dots after noqa comments (#24722)
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

- Add default parquet compression levels (#24686)
- Fix syntax error in data-types-and-structures.md (#24606)
- Rename `avg_birthday` -> `avg_age` in examples aggregation (#23726)
- Update Polars Cloud user guide (#24366)
- Fix typo in `set_expr_depth_warning` docstring (#24427)

## 📦 Build system

- Python pre-release 1.34.0b5 (#24699)
- Use cargo-run to call dsl-schema script (#24607)

## 🛠️ Other improvements

- Removing dots after noqa comments (#24722)
- Make `test_multiple_sorting_columns` test runnable (#24719)
- Remove `{Upper,Lower}Bound` expressions in IR (#24701)
- Fix Makefile `uv pip` option syntax (#24711)
- Add egg-info to gitignore (#24712)
- Restructure python project directories again (#24676)
- Use IR for `polars-expr` output field resolution (#24661)
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
@DeflateAwning, @Gusabary, @JakubValtar, @Kevin-Patyk, @MarcoGorelli, @Matt711, @alexander-beedie, @alonsosilvaallende, @andreseje, @borchero, @c-peters, @camriddell, @coastalwhite, @dangotbanned, @deanm0000, @dongchao-1, @dsprenkels, @eitsupi, @itamarst, @jan-krueger, @joshuamarkovic, @juansolm, @kdn36, @moizescbf, @nameexhaustion, @orlp, @r-brink, @ritchie46 and @stijnherfst

### Release: polars [Python Polars 1.34.0-beta.5](https://github.com/pola-rs/polars/releases/tag/py-1.34.0-beta.5)
## 🏆 Highlights

- Add `LazyFrame.{sink,collect}_batches` (#23980)
- Deterministic import order for Python Polars package variants (#24531)

## 🚀 Performance improvements

- Pushdown filter with `strptime` if input is literal (#24694)
- Avoid copying expanded paths (#24669)
- Relax filter expr ordering (#24662)
- Remove unnecessary `groups` call in `aggregated` (#24651)
- Skip files in `scan_iceberg` with filter based on metadata statistics (#24547)
- Push row\_index predicate for all scan types (#24537)
- Perform integer in-filtering for Parquet inequality predicates (#24525)
- Stop caching Parquet metadata after 8 files (#24513)
- Native streaming `.mode()` expression (#24459)

## ✨ Enhancements

- Implement maintain\_order for cross join (#24665)
- Add support to output `dt.total_{}()` duration values as fractionals (#24598)
- Avoid forcing a `pyarrow` dependency in `read_excel` when using the default "calamine" engine (#24655)
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

- Make `Categories` pickleable (#24691)
- Shift on array within list (#24678)
- Fix handling of `AggregatedScalar` in `ApplyExpr` single input (#24634)
- Support reading of mixed compressed/uncompressed IPC buffers (#24674)
- Overflow in slice-slice optimization (#24658)
- Package discovery for `setuptools` (#24656)
- Add type assertion to prevent out-of-bounds in `GenericFirstLastGroupedReduction` (#24590)
- Remove inclusion of polars dir in runtime sdist/wheel (#24654)
- Method `dt.month_end` was unnecessarily raising when the month-start timestamp was ambiguous (#24647)
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

- Add default parquet compression levels (#24686)
- Fix syntax error in data-types-and-structures.md (#24606)
- Rename `avg_birthday` -> `avg_age` in examples aggregation (#23726)
- Update Polars Cloud user guide (#24366)
- Fix typo in `set_expr_depth_warning` docstring (#24427)

## 📦 Build system

- Python pre-release 1.34.0b5 (#24699)
- Use cargo-run to call dsl-schema script (#24607)

## 🛠️ Other improvements

- Restructure python project directories again (#24676)
- Use IR for `polars-expr` output field resolution (#24661)
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
@DeflateAwning, @Gusabary, @JakubValtar, @Kevin-Patyk, @MarcoGorelli, @Matt711, @alexander-beedie, @alonsosilvaallende, @borchero, @c-peters, @camriddell, @coastalwhite, @dangotbanned, @deanm0000, @dongchao-1, @dsprenkels, @eitsupi, @itamarst, @jan-krueger, @joshuamarkovic, @juansolm, @kdn36, @moizescbf, @nameexhaustion, @orlp, @r-brink, @ritchie46 and @stijnherfst

## Project: [holoviz/panel](https://panel.holoviz.org/), 1 releases: ['Version 1.8.2']
### Release: panel [Version 1.8.2](https://github.com/holoviz/panel/releases/tag/v1.8.2)
This patch release focuses on polishing the user experience, fixing regressions, and improving documentation, particularly around app deployment and Tabulator interactivity. It includes several frontend and CSS tweaks, pyodide compatibility fixes, and two new deployment guides for **Anaconda Notebooks** and **PythonAnywhere**. Thanks to @philippjfr, @maximlt, @etihwo, @MarcSkovMadsen, and @Coderambling for their contributions to this release.

### ✨ Enhancements

- Allow custom control over Tabulator editable rows using `JSCode` ([#8204](https://github.com/holoviz/panel/pull/8204))
- Improve UI discoverability on `EditableTemplate` ([#8206](https://github.com/holoviz/panel/pull/8206))
- Set pointer cursor on "Connection Lost" toast notification ([#8209](https://github.com/holoviz/panel/pull/8209))
- Serve `index.html` automatically when serving a static directory ([#8222](https://github.com/holoviz/panel/pull/8222))

### 🐛 Bug Fixes

- Ensure Tabulator does not break if other components don't correctly initialize ([#8212](https://github.com/holoviz/panel/pull/8212))
- Fix Pyodide `jsnull` value conversion in Bokeh JSON patches ([#8217](https://github.com/holoviz/panel/pull/8217))
- Fix regression causing column headers not to stretch properly across layout ([#8219](https://github.com/holoviz/panel/pull/8219))
- Ensure `config.npm_cdn` is respected ([#8233](https://github.com/holoviz/panel/issues/8233))
- Ensure bundled pyodide resources use correct path separator ([#8230](https://github.com/holoviz/panel/pull/8230))
- Ensure pyodide resource bundle is only generated if necessary ([#8234](https://github.com/holoviz/panel/pull/8234))
- Ensure pyodide session is registered as loaded ([#8235](https://github.com/holoviz/panel/pull/8234))

### 📚 Documentation

- Add how-to guide on deploying Panel apps on [**Anaconda Notebooks**](https://notebooks.anaconda.cloud) ([#8207](https://github.com/holoviz/panel/pull/8207))
- Add how-to guide on deploying Panel apps on [**PythonAnywhere**](https://www.pythonanywhere.com/) ([#8216](https://github.com/holoviz/panel/pull/8216))
-  Update `Plotly.ipynb` to reflect current Plotly version and correct doc URLs ([#8214](https://github.com/holoviz/panel/pull/8214), [#8203](https://github.com/holoviz/panel/pull/8203))
- Add missing Anaconda logo to documentation ([#8208](https://github.com/holoviz/panel/pull/8208))
- Add how-to guide on using `uv` to distribute Panel apps and dependencies ([#8205](https://github.com/holoviz/panel/pull/8205))

## Project: [pyscript/pyscript](https://pyscript.com/), 3 releases: ['2025.10.3', '2025.10.2', '2025.10.1']
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
## Project: [cython/cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html), 6 releases: ['3.2.0b3', '3.2.0b2', '3.1.6', '3.2.0b1-3', '3.2.0b1', '3.1.5']
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
## Project: [plotly/dash](https://plotly.com/dash/), 3 releases: ['Dash Version 3.3.0rc2', 'v4.0.0rc2', 'Dash Version 3.3.0rc1']
### Release: dash [Dash Version 3.3.0rc2](https://github.com/plotly/dash/releases/tag/v3.3.0rc2)
- Remove placeholde publish button when on workspace
### Release: dash [v4.0.0rc2](https://github.com/plotly/dash/releases/tag/v4.0.0rc2)
## Added
- [3468](https://github.com/plotly/dash/pull/3468) Modernize dcc.TextArea & dcc.Tooltip
- [3467](https://github.com/plotly/dash/pull/3467) Modernize dcc.Loading
- [3453](https://github.com/plotly/dash/pull/3453) Modernize dcc.Checklist & dcc.RadioItems

## Changed

- Various tweaks and bugfixes to issues reported in `4.0.0rc1`

- Dropdown API changes
    * default value of optionHeight is now 'auto' which supports text wrapping of lengthy text on small screens; you can still specify a numeric pixel height if desired
    * new `labels` prop to customize strings used within the component
    * default value for closeOnSelect is now `True` for single-select dropdowns and `False` for multi-select

- Slider API changes
    * default value of `step` is now only set to `1` if the `min` and `max` props are both integers. Otherwise, it will be dynamically computed according to the available space for the slider

### Release: dash [Dash Version 3.3.0rc1](https://github.com/plotly/dash/releases/tag/v3.3.0rc1)
- Add placeholder plotly CLI
- Add dash[cloud] optional dependency.
- Add placeholder plotly cloud publish button in the devtools.
## Project: [dask/dask](https://www.dask.org/), 1 releases: ['2025.10.0']
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
## Project: [rapidsai/cudf](https://docs.rapids.ai/api/cudf/stable/user_guide/10min/), 1 releases: ['v25.10.00']
### Release: cudf [v25.10.00](https://github.com/rapidsai/cudf/releases/tag/v25.10.00)
## 🚨 Breaking Changes

- Remove UCX-Py (#19979) @pentschev
- Revert &quot;Migrate mixed join to use multiset #19660&quot; (#19933) @PointKernel
- Fill missing values in `Series/Index.values` for numeric types with np.nan by default (#19923) @mroeschke
- Remove deprecated `DataFrame.apply_rows`, deprecate `DataFrame.apply_chunks` and `Groupby.apply_grouped` (#19896) @mroeschke
- Move prefetching out of experimental and simplify the API (#19875) @vyasr
- Add join `*_match_context` APIs to hash join (#19835) @PointKernel
- Vendor libnvcomp in libcudf (#19743) @bdice
- Migrate mixed join to use multiset (#19660) @PointKernel
- Separate row mask and page mask computation and usage (#19537) @mhaseeb123
- [FEA] Implement null-aware transforms and filters (#19502) @lamarrr
- Support output-type for MEDIAN/QUANTILE aggregation in cudf::reduce (#19267) @davidwendt

## 🐛 Bug Fixes

- Fix edge cases in statistics collection (#20094) @rjzamora
- Fix multi-partition `Filter` bug (#20075) @rjzamora
- Fix `reindex` to fill only the reindexed values with `fill_value` (#20063) @galipremsagar
- Fix arrow arrays + numpy ufunc interaction (#20047) @galipremsagar
- Fix race conditions in ORC reader decimal decoding (#20044) @vuule
- Keep mr alive along with arrow tables and columns (#20028) @vyasr
- Fix `value_counts` missing `nan` bug (#20026) @galipremsagar
- Compatibility for rapidsmpf&#39;s unspill_partitions (#20020) @TomAugspurger
- Fix type metadata preservation in `shift` (#20017) @galipremsagar
- Fix incorrect type propagation in dataframe assignment (#20010) @galipremsagar
- Fix OOB memory read in decode_page_data_generic kernel (#19995) @davidwendt
- Fix data_type creation in ast::operation::instantiate (#19994) @davidwendt
- Skip Narwhals pandas get_dtype_backend[pyarrow] tests after ArrowDtype proxy changes (#19992) @Matt711
- Make cudf.pandas callables usable with inspect.getfullargspec (#19988) @mroeschke
- Align decimal dtypes to schema after parquet IO scan (#19974) @Matt711
- Avoid undefined numpy protocols on cudf.pandas proxy objects (#19968) @mroeschke
- Skip failing polars iceberg test (#19955) @Matt711
- Revert &quot;Migrate mixed join to use multiset #19660&quot; (#19933) @PointKernel
- Define FrozenList proxy independently in cudf.pandas (#19931) @mroeschke
- Ignore scalars when broadcasting for horizontal string concatenation in cudf-polars (#19893) @Matt711
- Fix is_valid_rolling_aggregation for STD aggregation (#19888) @davidwendt
- Fix a decompression parameter in the chunked ORC reader (#19882) @vuule
- Skip flaky stats tests pending follow up (#19881) @brandon-b-miller
- Require list type for is_valid_aggregation and MERGE_LISTS/SETS (#19876) @davidwendt
- Temporary solution to ensure data-source/sink stream ordering (#19874) @kingcrimsontianyu
- Check for integer overflow in cudf::strings::find_multiple (#19867) @davidwendt
- Fix missing stream from cudf::top_k_order (#19866) @davidwendt
- Disallow loc.__setitem__ with list-like indexer when list elements not in index (#19851) @mroeschke
- Fix .str.replace ignoring n for single character replacements (#19848) @mroeschke
- Fix strings::find_instance warp parallel logic (#19845) @davidwendt
- Add changed-files to the needs of every job that requires it (#19830) @Matt711
- xfail polars `decimal(precision=None)` test (#19821) @Matt711
- Fix empty column returned by cudf::from_arrow_stream_column (#19812) @davidwendt
- Filter pandas warning in dask_cudf test (#19808) @TomAugspurger
- Update identify_stream_usage CUDA runtime hooks to CUDA 13 (#19807) @robertmaynard
- When bundling `libnvcomp.so.X` only append the major version value (#19786) @robertmaynard
- Improvements to `pylibcudf.from_iterable_of_py` (#19781) @Matt711
- Avoid using multiple `Cache` nodes with the same hash (#19769) @rjzamora
- Fix window var() test failures from float rounding (#19761) @Matt711
- Use `is_compressed` field from Parquet V2 data page headers to determine if they are compressed (#19755) @mhaseeb123
- Fix bug in `eval` function with `nvtx-0.2.11` (#19754) @galipremsagar
- Fix ndsh benchmarks nvtx range usage (#19753) @davidwendt
- Support `nan` in non-floating point column in cudf-polars (#19742) @Matt711
- Fix filter call in benchmark (#19732) @vyasr
- Suppress NVRTC warning from stdint.h (#19712) @davidwendt
- Correctly decode boolean lists in chunked parquet reader (#19707) @mhaseeb123
- Add new xfails for xarray release (#19705) @vyasr
- Fix &quot;--executor&quot; pytest parameter for cudf-polars (#19703) @rjzamora
- Match polars semantics for rolling-sum with all-null windows (non-empty) (#19680) @Matt711
- [BUG] Set `query_set` arg when validating/running cudf-polars PDS-DS benchmarks (#19674) @Matt711
- Fix `group_by().agg()` on non-aggregatable dtypes (#19669) @Matt711
- Fix broken links in 10min notebook (#19665) @Matt711
- Skip managed memory test if managed memory not supported in cudf-polars (#19653) @Matt711
- Fix integer overflow in warp-per-row grid calculation (#19638) @davidwendt
- Propagate exceptions thrown in async IO operations (#19628) @vuule
- Make `DataFrame.dtypes` not fallback to CPU always (#19627) @galipremsagar
- Set scalar to valid in range_window_bounds unbounded/current_row (#19622) @davidwendt
- Enable data page mask computation for nullable `list` and `struct` columns (#19617) @mhaseeb123
- Fix cudf::sequence() to throw exception for invalid scalar inputs (#19612) @davidwendt
- Fix uninitialized variable and misaligned write in parquet generic decoder (#19601) @mhaseeb123
- Compatibility with rapidsmpf 25.10.0 (#19591) @TomAugspurger
- Avoid querying device memory on systems without it in dask-cudf (#19577) @Matt711
- Avoid querying device memory on systems without it in cudf-polars benchmarks (#19575) @Matt711
- Increase alignment requirement for parquet bloom filter to 256 (#19573) @mhaseeb123
- Fix strftime with non-exact %a, %A, %b, %B (#19570) @mroeschke
- Fix OOB memcheck error in group_rank_to_percentage utility (#19567) @davidwendt
- Fix logic for number of unique values generated by data profile in benchmarks (#19540) @shrshi
- Fix contiguous-split nvbench cmake build (#19534) @davidwendt
- Fix value counts expression when the column has nulls (#19524) @Matt711
- Prefer `Column.astype` over `plc.unary.cast` in the fill null unary function expression (#19479) @Matt711
- Fix missing return in StringFunction.Strptime strict=True path (#19464) @Matt711
- Make dividing a boolean column return f64 dtype in cudf-polars (#19443) @Matt711
- branch-25.10-merge-branch-25.08 (#19429) @davidwendt
- Replace sprintf with std::format in libcudf parquet tests (#19364) @davidwendt

## 📖 Documentation

- Update missing docs (#19925) @vyasr
- Add examples of null handling to doxygen for cudf::rank (#19774) @davidwendt
- Fix cudf-polars dependency list docs (#19750) @pentschev
- Update cuDF classic testing documention regarding testing organization (#19745) @mroeschke
- Improve documentation around why we need no_gc_clear on pylibcudf Scalars (#19661) @vyasr

## 🚀 New Features

- Add memory resource parameters to interop, merge, and transpose (#20007) @vyasr
- Add mixed join benchmark with complex AST operators (#20004) @PointKernel
- Add memory resource arguments to join, round, and labeling (#20001) @vyasr
- `cudf-polars` `strptime` format inference (#19997) @brandon-b-miller
- Filter parquet row groups using byte offset bounds (#19991) @mhaseeb123
- Add memory resource arguments to concatenate (#19943) @vyasr
- Use column statistics to generate the physical plan in cuDF-Polars (#19940) @rjzamora
- Add all missing stream parameters (#19922) @vyasr
- Remote IO support in cudf-polars (#19921) @Matt711
- Add streams to io/timezone and io/text modules (#19913) @vyasr
- Add stream support to all nvtext modules (#19911) @vyasr
- Add streams to all top-level strings modules (#19910) @vyasr
- Update strings split APIs with stream parameters (#19909) @vyasr
- Support ordered grouped windows in cudf-polars (#19891) @Matt711
- Add local row-count and unique-count estimates to `explain(... logical=True)` (#19864) @rjzamora
- Add join `*_match_context` APIs to hash join (#19835) @PointKernel
- Support `rank(...).over(...)` expressions in cudf-polars (#19803) @Matt711
- Add strings to/from encoded integer APIs (#19789) @davidwendt
- Add to_arrow method to pylibcudf core types (#19787) @Matt711
- Add streams to strings convert APIs (#19780) @vyasr
- Add an option to support reading ORC timestamp column as UTC time. (#19773) @res-life
- Support null_count in groupby/rolling context (#19739) @Matt711
- Collect join-key information in cudf-polars (#19736) @rjzamora
- Add count aggregation support to cudf::reduce (#19734) @davidwendt
- [FEA] Implement AST Expression - JIT codegen (#19733) @lamarrr
- Add streams to all scalar factories (#19729) @vyasr
- Add streams to reshape (#19728) @vyasr
- Add streams to null mask APIs (#19727) @vyasr
- Add streams to column APIs (#19726) @vyasr
- Construct next-gen parquet reader with pre-populated footer (#19724) @mhaseeb123
- Require `numba-cuda&gt;=0.19.0,&lt;0.20.0a0` (#19711) @brandon-b-miller
- Support `over` expression (window mapping) in cudf-polars (#19684) @Matt711
- Add streams support to all list APIs (#19683) @vyasr
- [FEA] Add Filter Benchmark (#19678) @lamarrr
- Add streams to pylibcudf join APIs (#19672) @vyasr
- Add streams to sorting APIs (#19671) @vyasr
- [FEA] Remove excessive copies of JITIFY&#39;s ProgramData during JIT kernel launch (#19667) @lamarrr
- Add streams to hashing APIs (#19663) @vyasr
- Use a more robust metric for sorting (de)compression tasks (#19656) @vuule
- Add streams support to datetime APIs (#19654) @vyasr
- Add streams to stream_compaction (#19651) @vyasr
- Enable casting `pl.Datetime` to integer types in `cudf-polars` (#19647) @brandon-b-miller
- Add Java JNI interface to get Gpu UUID (#19646) @res-life
- Add reduction with overflow detection (#19641) @PointKernel
- Upgrade to nvCOMP 5.0.0.6 (#19636) @vuule
- Use the nvCOMP 5.0 API to better estimate decompression memory requirements (#19616) @vuule
- Add streams to transform and unary (#19613) @vyasr
- Add streams to all modules with 4-5 functions (#19609) @vyasr
- Enable casting integer dtypes to `pl.Datetime` via `cudf-polars` (#19607) @brandon-b-miller
- Add fast path for Parquet reading with predicate pushdown via AST filters (#19605) @Matt711
- Add streams to all modules with three or fewer functions (#19600) @vyasr
- Add libcudf top_k_segmented APIs (#19597) @davidwendt
- Update Arrow bounds to &gt;=15,&lt;22 (#19592) @bdice
- Update cudf to handle CUDA 13 changes (#19585) @robertmaynard
- Support hash-based workflow for `M2` groupby aggregation (#19569) @ttnghia
- Expose `filter` and `columns` parquet reader builder options to python (#19566) @Matt711
- [FEA] Switch to NVIDIA&#39;s JITIFY2 (#19561) @lamarrr
- Add streams to all single-function modules (#19559) @vyasr
- Add support for streams to all copying APIs. (#19553) @vyasr
- Benchmarks comparing Arrow string formats (#19552) @davidwendt
- Compile `libcudf_kafka` and `cudf_kafka` with C++20 (#19543) @vuule
- RapidsMPF &quot;single&quot; shuffle integration (#19530) @rjzamora
- Make nvCOMP ZLIB (de)compression available by default (#19528) @vuule
- Implement chunking in the next-gen parquet reader (#19526) @mhaseeb123
- Add primitive row dispatch support for semi/anti join and cudf::contains (#19518) @PointKernel
- Derive and use page mask at subpass level for chunked reads (#19515) @mhaseeb123
- [FEA] Implement null-aware transforms and filters (#19502) @lamarrr
- Add PDS-DS queries 2 through 10 to cudf-polars benchmarks (#19488) @Matt711
- Add API to &quot;initialize&quot; column statistics (#19447) @rjzamora
- Implement top k expression in cudf-polars using `cudf::top_k` (#19431) @Matt711
- Add hash-based SUM_WITH_OVERFLOW aggregation for INT64 values (#19403) @PointKernel
- Support rank expression in cudf-polars (#19340) @Matt711
- Support fill_null with fill strategy in cudf-polars (#19318) @Matt711
- Support output-type for MEDIAN/QUANTILE aggregation in cudf::reduce (#19267) @davidwendt
- Support ternary expression inside groupby/rolling context (#19242) @Matt711
- Experimental API to read a parquet table, build a custom index column, and apply roaring bitmap deletion vector (#19237) @mhaseeb123
- Support `cudf-polars` `str.zfill` (#19081) @brandon-b-miller
- [FEA] Add chunked Parquet sink support using the libcudf writer (#19015) @Matt711
- Add multi-column support for primitive row operator dispatch (#18940) @tgujar

## 🛠️ Improvements

- Fix CI failures for `pandas-2.3.3` (#20146) @galipremsagar
- Skip passing failures for latest `numexpr` version (#20092) @galipremsagar
- Empty commit to trigger a build (#20084) @msarahan
- Update the reason to skip for parquet bloom filter test (#20043) @mhaseeb123
- Remove test_scan_hf_url_raises (#20035) @mroeschke
- xfail(strict=False) test_scan_hf_url_raises due to rate limiting (#20027) @mroeschke
- Deprecate left semi- and anti- join functional APIs (#20014) @shrshi
- Use to_arrow methods throughout pylibcudf and cudf (#20013) @Matt711
- Fix chunked reads of list of bools. (#20000) @pmattione-nvidia
- Raise more exceptions for invalid or unsupported cuDF arguments (#19990) @mroeschke
- Configure repo for automatic release notes generation (#19984) @AyodeAwe
- Pin duckdb&lt;1.4 in test_python_narwhals (#19982) @mroeschke
- Default to False if `CUDA_ENABLE_NRT` isn&#39;t set in config (#19981) @brandon-b-miller
- Remove UCX-Py (#19979) @pentschev
- Add support for `attrs` (#19978) @galipremsagar
- Run pytest-benchmarks in CI with --benchmark-disable (#19969) @mroeschke
- Change target type so we can test on workflows (#19963) @vyasr
- Update to actions/labeler v5 (#19962) @vyasr
- Revert &quot;ci(labeler): update labeler action to @v5&quot; (#19961) @vyasr
- Add `ArrowDtype` proxy class (#19960) @galipremsagar
- Add missing type stub (#19958) @vyasr
- Add missing `Styler` attributes (#19956) @galipremsagar
- Allow newer CMake in Java tests (#19949) @bdice
- Make stream a required parameter for from_libcudf methods (#19945) @vyasr
- Return False instead of NA for comparison ops against NA in cudf.pandas (#19942) @mroeschke
- Don&#39;t fall back in Series.describe in cudf.pandas for numeric types (#19941) @mroeschke
- Move groupby benchmarks to nvbench (#19930) @davidwendt
- Perform more input validation in cuDF classic APIs (#19929) @mroeschke
- update nvidia-ml-py (&gt;=12), use cuda-toolkit wheels (#19927) @jameslamb
- Fill missing values in `Series/Index.values` for numeric types with np.nan by default (#19923) @mroeschke
- Add `rmm-release-threshold` to pdsh benchmarks CLI (#19918) @TomAugspurger
- Also use the CUDA 12 container for nightlies (#19917) @vyasr
- Move test_binops.py to new cuDF classic directory structure (#19914) @mroeschke
- Eagerly load nvCOMP library in `cudf::initialize()` (#19906) @vuule
- Pin to CUDA 12 image for integration tests (#19903) @vyasr
- Use branch-25.10 again (#19902) @jameslamb
- Disable test on non-default stream (#19901) @vyasr
- Use cupy array instead of numba device array as inputs to jit routines (#19897) @mroeschke
- Remove deprecated `DataFrame.apply_rows`, deprecate `DataFrame.apply_chunks` and `Groupby.apply_grouped` (#19896) @mroeschke
- Move test_dataframe.py to new cuDF classic directory structure (#19890) @mroeschke
- Make sure conftest fixture data is valid on exit (#19889) @vyasr
- Move test_index/multiindex/indexing.py to new cuDF classic directory structure (#19887) @mroeschke
- [FEA] Build CUDF with CCCL 3.1.0 (#19886) @lamarrr
- Coalesce IO of chunks with different compression when reading Parquet files (#19884) @vuule
- Update boost version to 1.79 for JNI dockerfile (#19883) @pxLi
- Move test_categorical/dask/serialize.py to new cuDF classic test directory structure (#19877) @mroeschke
- Move prefetching out of experimental and simplify the API (#19875) @vyasr
- Remove `diff.sh` and merge diff generation into `run.sh` (#19871) @galipremsagar
- Remove pyarrow upper bound (#19870) @vyasr
- Prevent installation of pytest-rerunfailures 16.0.0 (#19863) @pentschev
- use &#39;nvidia-ml-py&#39; package for &#39;pynvml&#39; module (#19862) @jameslamb
- Avoid more direct construction of cuDF classic columns (#19858) @mroeschke
- Bump pandas supported version to `2.3.2` (#19856) @galipremsagar
- Use cupy arrays instead of numba device arrays for cuDF classic intermediates (#19855) @mroeschke
- Move row operators to detail and deprecate legacy (#19849) @PointKernel
- Fix flaky DataFrame `to_string` test (#19847) @brandon-b-miller
- Pin pytest-rerunfailures&lt;16 (#19846) @mroeschke
- revert numba CUDA 13 workaround (#19842) @jameslamb
- Avoid CategoricalColumn constructors in cuDF classic (#19837) @mroeschke
- Construct cuDF classic Decimal32/64Columns from RMM buffers (#19834) @mroeschke
- Avoid direct construction of cuDF classic columns (#19829) @mroeschke
- Support input filename in ndsh q01 benchmark (#19820) @davidwendt
- Run cudf-polars-polars-tests on changes in test_python file group (#19819) @mroeschke
- Remove test_mvc.py (#19816) @mroeschke
- pin oldest numpy in dask-cudf tests, update dependency floors (cuda-python 12.9.2, cupy 13.6.0, numba 0.60.0) (#19806) @jameslamb
- Remove iterative `nan` &amp; `nat` inefficient checks in `as_column` constructor (#19804) @galipremsagar
- Simplify/consolidate from_arrow logic (#19801) @mroeschke
- Refactor column_empty to use only pylibcudf APIs (#19800) @mroeschke
- Use more cached_property where possible for Index and subclasses (#19799) @mroeschke
- Update rapids-dependency-file-generator (#19796) @KyleFromNVIDIA
- rearrange dependencies.yaml, other small changes (#19794) @jameslamb
- Update exception handling in pdsh benchmarks (#19793) @TomAugspurger
- Fix how nvcomp major version is extracted (#19791) @KyleFromNVIDIA
- Use KvikIO&#39;s unified interface to create remote I/O endpoints (#19788) @kingcrimsontianyu
- Add object-oriented APIs for left semi- and anti- join (Part I) (#19778) @shrshi
- Add nvbench benchmark for cudf::encode API (#19777) @davidwendt
- Some clarifications, improvements to GroupedRollingWindows in cudf-polars (#19776) @Matt711
- Remove validation on import (#19775) @vyasr
- Move more test_dataframe.py tests to new cudf classic testing directory (#19770) @mroeschke
- Build and test with CUDA 13.0.0 (#19768) @jameslamb
- Skip polars CPU perf test for with_columns (#19763) @Matt711
- Optionally capture Shuffle Stats in cudf-polars pdsh benchmarks (#19762) @TomAugspurger
- Expand compression codec coverage in ORC and Parquet benchmarks (#19760) @vuule
- Add ``ColumnSourceInfo`` convenience layer (#19752) @rjzamora
- Support decimal columns in cudf_polars (#19749) @mroeschke
- Skip third-party tests when possible (#19747) @vyasr
- Revert &quot;Support decimal columns in cudf_polars&quot; (#19746) @mroeschke
- Vendor libnvcomp in libcudf (#19743) @bdice
- Remove outdated numba workarounds (#19738) @bdice
- Move test_buffer/column/column_accesor/cuda_apply.py to new cudf classic testing directory (#19737) @mroeschke
- Move more test_dataframe.py tests to new cudf classic testing directory (#19731) @mroeschke
- Move test_udf_masked_ops/test_dropna to new cudf classic testing directory (#19730) @mroeschke
- Move test_numerical/{numpy|pandas}_interop/setitem.py to new cudf classic testing directory (#19725) @mroeschke
- Move test_timedelta/string/sorting/list/datetime.py to new cudf classic directory structure (#19723) @mroeschke
- Warn on fallback in the streaming tests in cudf-polars (#19721) @Matt711
- Optionally print shuffle stats in pdsh benchmarks (#19719) @TomAugspurger
- Move test_{io}.py files to new cudf classic test directory (#19709) @mroeschke
- Move to pyarrow and numpy to run_constrained (#19706) @vyasr
- Remove unreachable code in rapidsmpf shuffle (#19704) @TomAugspurger
- Moves test_options to cudf testing directory, clean up old, stubbed testing files in directory (#19698) @mroeschke
- Move (most of) test_index.py to new cudf classic directory structure (#19696) @mroeschke
- Improve `M2`, `VARIANCE` and `STD` hash-based groupby aggregations (#19694) @ttnghia
- Move quantiles libcudf benchmark to nvbench (#19692) @davidwendt
- Handle `TIMESTAMP_DAYS` in rolling window offsets (#19689) @Matt711
- Move test_groupby to new cudf classic directory structure (#19688) @mroeschke
- Move some of test_dataframe.py to new cudf classic directory structure (#19687) @mroeschke
- Change nvtext::character_tokenize to return a list column (#19685) @davidwendt
- Split up rolling.cuh into separate headers (#19682) @davidwendt
- Move test_factorize/drop_duplicates.py to new cudf classic test directory (#19681) @mroeschke
- Move test_offset/repr.py to new cudf classic testing directory (#19677) @mroeschke
- Move test_stats/reductions/quantile and misc to new cudf classic testing directory (#19675) @mroeschke
- Cache hash values to improve hash-based groupby performance with wide/complex table keys (#19670) @ttnghia
- Move test_interval/test_dtypes/test_rank.py to new cudf directory structure (#19668) @mroeschke
- Clean and move test_join_order/interpolate/onehot.py to new cudf classic test directory structure (#19662) @mroeschke
- Migrate mixed join to use multiset (#19660) @PointKernel
- Run pylibcudf tests without its optional dependencies (#19657) @vyasr
- Use build cluster in devcontainers (#19652) @trxcllnt
- Use rapids_cuda_enable_fatbin_compression (#19650) @robertmaynard
- Re-enable Disabled Join Tests (#19649) @PointKernel
- Use public Arrow functions for TDigest in PercentileApproxInputTypesTests (#19648) @davidwendt
- Use cudaDeviceGetAttribute to get ComputeMode for CUDA13 (#19645) @GaryShen2008
- remove initial memset of values in parquet reader (#19643) @pmattione-nvidia
- Move ~half of test_groupby.py to new cudf classic test directory structure (#19640) @mroeschke
- Move test_csv/feather/json.py to new cudf classic test directory structure (#19639) @mroeschke
- Move test_array_function/ufunc to new cudf classic test directory structure (#19637) @mroeschke
- Fix anchor naming conventions in dependencies.yaml (#19635) @KyleFromNVIDIA
- Require `--scale` for PDS-DS benchmarks (due to nonlinear scaling) (#19631) @Matt711
- Move test_replace.py to new cudf classic directory structure (#19629) @mroeschke
- Move test_concat/test_reductions.py to new cudf classic directory structure (#19626) @mroeschke
- Update rapids_config to handle user defined branch name (#19623) @robertmaynard
- Add nvtx ranges to public APIs of the experimental parquet reader (#19618) @mhaseeb123
- Move test_resampling/query/pickling to new cudf classic directory structure (#19615) @mroeschke
- Move test_reshape.py to new cudf classic directory strucutre, remove reshape._merge_sorted (#19614) @mroeschke
- Move test_rolling/ewm.py to new cudf classic directory structure (#19611) @mroeschke
- Simplify cudf::scalar usage in reduce utility (#19608) @davidwendt
- Update to numba-cuda&gt;=0.18.0,&lt;0.19.0 (#19604) @bdice
- Update spark-rapdis-jni action to use PR&#39;s base.ref and fix issue of ccache version in dockerfile (#19603) @pxLi
- Multithreaded CPU algorithm for data page mask computation (#19602) @mhaseeb123
- Move test_cuda_array_interface/cut/dataframe_copy.py to new cudf classic test directories (#19599) @mroeschke
- Support decimal columns in cudf_polars (#19589) @mroeschke
- Preserve decimal precision in `cudf::interop::column_metadata` (#19587) @mroeschke
- Always use strict zipping (#19584) @vyasr
- Pin polars version to &lt;1.33 (#19582) @Matt711
- ci(labeler): update labeler action to @v5 (#19581) @gforsyth
- Update rapids-build-backend to 0.4.0 (#19580) @KyleFromNVIDIA
- Move (most of) test_list.py to new cudf classic test directories (#19574) @mroeschke
- Move test_monotonic.py to new cudf classic test directory structure (#19572) @mroeschke
- Additional gtests error checks for string/timestamp convert libcudf APIs (#19562) @davidwendt
- Avoid cudf.pandas fallback for `pandas.array.NumpyExtensionArray` of strings (#19558) @mroeschke
- Move str accessor tests in test_string.py to new cudf classic test directory structure (#19557) @mroeschke
- Rework fill/repeat benchmark to use nvbench (#19556) @davidwendt
- Use no_validity() instead of null_probability(0) in benchmarks profile (#19554) @davidwendt
- Move (most of) test_timedelta.py and test_struct.py to new cudf classic test directory structure (#19551) @mroeschke
- Capture commit hashes in pdsh benchmarks (#19548) @TomAugspurger
- Simplify clang dependency spec (#19546) @vyasr
- Move timeout in cudf.pandas pandas unit tests script to ci script (#19542) @mroeschke
- [FEA] Refactor AST `operator_functor`s for use in JIT-compiled CUDA (#19541) @lamarrr
- Construct cuDF classic columns with __array_interface__ through pylibcudf (#19538) @mroeschke
- Separate row mask and page mask computation and usage (#19537) @mhaseeb123
- Get rid of CG logic in the mixed semi-join kernel (#19536) @PointKernel
- Construct more cuDF classic Columns with pylibcudf instead of using Buffers (#19535) @mroeschke
- Fix clang-tools version pinning (#19529) @wence-
- Add cudf_polars unit test for `is_in([])` expr (#19525) @mroeschke
- Expose `nvtext::letter_type` to python (#19520) @Matt711
- Remove c++ stringview interop example (#19516) @davidwendt
- Remove cudf/_fuzz_testing directory (#19510) @mroeschke
- Add missing import of pyarrow.parquet when reading specified row_groups. (#19509) @bdice
- Don&#39;t run serial cudf_pandas tests when testing multiple pandas versions (#19507) @mroeschke
- Clean testing/_utils.py (#19506) @mroeschke
- Move some test_datetime.py tests to new cudf classic test directory structure (#19505) @mroeschke
- Move test_joining to new cudf classic test directory structure (#19501) @mroeschke
- Upgrade `gcc-toolset` for Java/JNI build to version 14 (#19500) @ttnghia
- Remove deprecated subword-tokenizer APIs (#19498) @davidwendt
- Move some test_multiindex.py to new cudf classic test directory structure (#19496) @mroeschke
- Add nvtx ranges and minor fix for `lists` types in the next-gen parquet reader (#19493) @mhaseeb123
- Move test_search/test_scan/test_seriesmap.py to new cudf classic test directory structure (#19492) @mroeschke
- Improve support for sliced input on from_arrow_host APIs (#19491) @davidwendt
- Move test_avro/test_api_types.py and some DataFrame tests to new cudf classic test directory structure (#19490) @mroeschke
- Move test_series.py to new cudf classic test directory structure (#19485) @mroeschke
- Move test_testing.py to new cudf classic test directory structure (#19481) @mroeschke
- Allow latest OS in devcontainers (#19480) @bdice
- Move test_unaops/test_unique/test_transform.py to new cudf classic test directory structure (#19477) @mroeschke
- Branch 25.10 merge branch 25.08 (#19475) @davidwendt
- Use more pytest fixtures and clean data files cuDF classic tests subdirectories (#19474) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in test_binops/column/column_accessor/contains.py and more (#19473) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in test_csv/cuda_*/cut.py and more (#19463) @mroeschke
- Improve readability when printing pylibcudf enums (#19451) @Matt711
- Use more pytest fixtures and avoid GPU parameterization in cuDF classic tests (#19450) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in test_dropna/factorize.py and more (#19449) @mroeschke
- Update build infra to support new branching strategy (#19445) @robertmaynard
- Updated libcudf-example conda package to preserve directories structure (#19440) @Avinash-Raj
- Use more pytest fixtures and avoid GPU parameterization in test_groupby/index.py (#19438) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in test_indexing/joining/monotonic/multiindex.py (#19437) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in cuDF classic tests (#19436) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in test_query/rank/reduction/repr.py (#19434) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in test_replace/reshape/rolling.py (#19426) @mroeschke
- Update s3 Bucket fixture creation in test_s3 (#19424) @mroeschke
- Use more pytest fixtures and avoid GPU parameterization in cuDF classic tests (#19419) @mroeschke
- Fix various pandas test failures in `cudf.pandas` (#19372) @galipremsagar
- Pin Narwhals to 1.47 (#19358) @Matt711
- Run cudf-polars tests with all supported polars versions (#19353) @Matt711
- Update `pandas-tests-diff` to only display GPU/CPU usage metrics (#19210) @galipremsagar
- Use GCC 14 in conda builds. (#19192) @vyasr
- Use KvikIO&#39;s implementation of file-backed memory mapping (#19164) @kingcrimsontianyu
- Replace `rmm::device_scalar` with `cudf::detail::device_scalar` due to unnecessary synchronization (Part 3 of miss-sync) (#19119) @JigaoLuo
- Implement distributed sorted for ``cudf_polars`` (#18912) @seberg
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 15 releases: ['v0.38.3', 'v0.38.3-beta.11', 'v0.38.3-beta.10', 'v0.38.3-beta.9', 'v0.38.3-beta.8', 'v0.38.3-beta.7', 'v0.38.3-beta.6', 'v0.38.3-beta.5', 'v0.38.3-beta.4', 'v0.38.3-beta.3', 'v0.38.3-beta.2', 'v0.38.3-beta.1', 'v0.38.2', 'v0.38.1', 'v0.38.0']
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
### Release: lance [v0.38.3-beta.2](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.2 -->

## What's Changed
### New Features 🎉
* feat: add multi-path support for lance data paths by @jaystarshot in https://github.com/lancedb/lance/pull/4765
### Bug Fixes 🐛
* fix: let Java module use LanceFileVersion::Stable (#4558) by @ColdL in https://github.com/lancedb/lance/pull/4559
* fix: fts match query on column without inverted index by @wojiaodoubao in https://github.com/lancedb/lance/pull/4859
* fix: fix broken FTS example by replacing ROW_ID with DOC_ID by @niebayes in https://github.com/lancedb/lance/pull/4917
* fix: correctly record output_rows in filtered read with hard range_after by @westonpace in https://github.com/lancedb/lance/pull/4919
* fix: rewrap LanceFilterExec with_new_children by @wkalt in https://github.com/lancedb/lance/pull/4920
### Documentation 📚
* docs: add RabitQ in vector index spec by @BubbleCal in https://github.com/lancedb/lance/pull/4913

## New Contributors
* @yingjianwu98 made their first contribution in https://github.com/lancedb/lance/pull/4901
* @niebayes made their first contribution in https://github.com/lancedb/lance/pull/4917

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.3-beta.1...v0.38.3-beta.2
### Release: lance [v0.38.3-beta.1](https://github.com/lancedb/lance/releases/tag/v0.38.3-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.3-beta.1 -->

## What's Changed
### New Features 🎉
* feat: handle forking better by @cmccabe in https://github.com/lancedb/lance/pull/4903


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.2...v0.38.3-beta.1
### Release: lance [v0.38.2](https://github.com/lancedb/lance/releases/tag/v0.38.2)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.2 -->

## What's Changed
### Bug Fixes 🐛
* fix: short circuit SQL parsing by @timsaucer in https://github.com/lancedb/lance/pull/4825
* fix: forward compatibility of FTS index by @jackye1995 in https://github.com/lancedb/lance/pull/4906


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.1...v0.38.2
### Release: lance [v0.38.1](https://github.com/lancedb/lance/releases/tag/v0.38.1)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.1 -->

## What's Changed
### New Features 🎉
* feat: upgrade url crate, rework temporary directory utils by @westonpace in https://github.com/lancedb/lance/pull/4860
* feat: support fragment-level update columns by @wayneli-vt in https://github.com/lancedb/lance/pull/4715
* feat: change one-pass GPU ivf-pq indexing as default by @eddyxu in https://github.com/lancedb/lance/pull/4879
* feat: add scan_range_after_filter pushdown optimization for filtered reads by @LuQQiu in https://github.com/lancedb/lance/pull/4795
### Bug Fixes 🐛
* fix: typo in ut test_fragment_update by @wojiaodoubao in https://github.com/lancedb/lance/pull/4878
* fix: filter out vectors that could produce infinite l2 distances by @wjones127 in https://github.com/lancedb/lance/pull/4890
* fix: don't log the 'experimental' warning if users are using 2.1 by @westonpace in https://github.com/lancedb/lance/pull/4880
* fix: don't retain indices that have no rows by @wjones127 in https://github.com/lancedb/lance/pull/4875
### Documentation 📚
* docs: rework file specification docs by @westonpace in https://github.com/lancedb/lance/pull/4619
### Other Changes
* refactor: remove unecessary parens by @cmccabe in https://github.com/lancedb/lance/pull/4876


**Full Changelog**: https://github.com/lancedb/lance/compare/v0.38.0...v0.38.1
### Release: lance [v0.38.0](https://github.com/lancedb/lance/releases/tag/v0.38.0)
<!-- Release notes generated using configuration in .github/release.yml at v0.38.0 -->

## What's Changed
:tada: :tada: :exclamation:  As of this release, the 2.1 version of the file format is considered _stable_.  There will be no more breaking changes and the format should be readable by future versions of lance.  In an upcoming release (possibly the next release) the 2.1 version will become the default.
### Breaking Changes 🛠
* feat(rust)!: support branch based on shallow_clone by @majin1102 in https://github.com/lancedb/lance/pull/4710
### New Features 🎉
* feat: support manifeset summary and get it from Version by @majin1102 in https://github.com/lancedb/lance/pull/4754
* feat: implement blob encoding for 2.1 by @westonpace in https://github.com/lancedb/lance/pull/4802
* feat(java): expose additional Operation::Update fields to bindings by @wayneli-vt in https://github.com/lancedb/lance/pull/4788
* feat(index/fts): build fst at write time instead of read time by @Xuanwo in https://github.com/lancedb/lance/pull/4811
* feat: support RabitQ quantization by @BubbleCal in https://github.com/lancedb/lance/pull/4344
* feat: add scalar and system index spec by @jackye1995 in https://github.com/lancedb/lance/pull/4736
* feat: add support for already-dictionary to 2.1 by @westonpace in https://github.com/lancedb/lance/pull/4813
* feat: allow reading blob descs in 2.1, fix bugs in FSL decoder when items are nullable by @westonpace in https://github.com/lancedb/lance/pull/4840
* feat: add full text json index by @wojiaodoubao in https://github.com/lancedb/lance/pull/4752
### Bug Fixes 🐛
* fix: propagate span in filtered read by @wjones127 in https://github.com/lancedb/lance/pull/4790
* fix: add incremental metrics in FilteredRead by @wjones127 in https://github.com/lancedb/lance/pull/4798
* fix: fix handling of all-preamble chunks in mini-block scheduling by @westonpace in https://github.com/lancedb/lance/pull/4823
* fix: don't interpret 64-bit offsets as 32 bits when decompressing per-value data in 2.1 by @westonpace in https://github.com/lancedb/lance/pull/4824
* fix: aggregate gauge metrics in bytes_read for zonemap scans by @chenghao-guo in https://github.com/lancedb/lance/pull/4830
* fix: remove blocking call in async function by @wjones127 in https://github.com/lancedb/lance/pull/4841
* fix: index stats reports incorrect partition size by @BubbleCal in https://github.com/lancedb/lance/pull/4847
* fix: fix typo "blfoat16" -> "bfloat16" in datatypes.rs by @huyuanfeng2018 in https://github.com/lancedb/lance/pull/4852
* fix: blocking_take may hang on V2.0 by @ColdL in https://github.com/lancedb/lance/pull/4539
* fix: schema mismatch when filtering nullable List<Struct> columns by @Xuanwo in https://github.com/lancedb/lance/pull/4838
* fix: ensure fragment IDs are sorted in load_training_data by @jtuglu1 in https://github.com/lancedb/lance/pull/4871
### Documentation 📚
* docs: vector index specs by @BubbleCal in https://github.com/lancedb/lance/pull/4810
### Performance Improvements 🚀
* perf: move cpu heavy fst building into blocking threads by @Xuanwo in https://github.com/lancedb/lance/pull/4803
* perf: optmize doc set loading by @Xuanwo in https://github.com/lancedb/lance/pull/4821
### Other Changes
* refactor: cowardly refuse to use scalar indexes on expressions with null literals by @westonpace in https://github.com/lancedb/lance/pull/4815

## New Contributors
* @wayneli-vt made their first contribution in https://github.com/lancedb/lance/pull/4788
* @huyuanfeng2018 made their first contribution in https://github.com/lancedb/lance/pull/4852
* @ColdL made their first contribution in https://github.com/lancedb/lance/pull/4539
* @jtuglu1 made their first contribution in https://github.com/lancedb/lance/pull/4871

**Full Changelog**: https://github.com/lancedb/lance/compare/v0.37.0...v0.38.0
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 17 releases: ['Node/Rust LanceDB v0.22.3-beta.4', 'Python LanceDB v0.25.3-beta.4', 'Node/Rust LanceDB v0.22.3-beta.3', 'Python LanceDB v0.25.3-beta.3', 'Node/Rust LanceDB v0.22.3-beta.2', 'Python LanceDB v0.25.3-beta.2', 'Node/Rust LanceDB v0.22.3-beta.1', 'Python LanceDB v0.25.3-beta.1', 'Node/Rust LanceDB v0.22.3-beta.0', 'Python LanceDB v0.25.3-beta.0', 'Node/Rust LanceDB v0.22.2', 'Python LanceDB v0.25.2', 'Node/Rust LanceDB v0.22.2-beta.2', 'Python LanceDB v0.25.2-beta.2', 'Node/Rust LanceDB v0.22.2-beta.1', 'Python LanceDB v0.25.2-beta.1', 'ci-support-binaries']
### Release: lancedb [Node/Rust LanceDB v0.22.3-beta.4](https://github.com/lancedb/lancedb/releases/tag/v0.22.3-beta.4)
## 🎉 New Features

- feat(voyageai): update voyage integration by @fzowl in https://github.com/lancedb/lancedb/pull/2713

## 📚 Documentation

- docs: remove DynamoDB commit store section by @ozkatz in https://github.com/lancedb/lancedb/pull/2715

## 🔧 Build and CI

- ci: add agents and add reviewing instructions by @wjones127 in https://github.com/lancedb/lancedb/pull/2754


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


### Release: lancedb [Node/Rust LanceDB v0.22.2](https://github.com/lancedb/lancedb/releases/tag/v0.22.2)
## 🎉 New Features

- feat: add use_index parameter to merge insert operations by @wjones127 in https://github.com/lancedb/lancedb/pull/2674
- feat(rust): support namespace backed database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2664
- feat: allow bitmap indexes on large-string, binary, large-binary, and bitmap by @westonpace in https://github.com/lancedb/lancedb/pull/2678
- feat: add support for test_remote_connections by @cmccabe in https://github.com/lancedb/lancedb/pull/2666
- feat: upgrade lance to 0.38.2 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2705

## 🐛 Bug Fixes

- fix: use correct nodejs path for ci by @AyushExel in https://github.com/lancedb/lancedb/pull/2689
- fix: inflated release size due to lance-namespace transitive dependency by @jackye1995 in https://github.com/lancedb/lancedb/pull/2691
- fix: have CI download from ci-support-binaries by @cmccabe in https://github.com/lancedb/lancedb/pull/2692
- fix(node): allow undefined/omitted values for nullable vector fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2656
- fix: use stdlib override when possible by @edrogers in https://github.com/lancedb/lancedb/pull/2699
- fix: federated database should not pass namesapce to listing database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2702
- fix(node): support specifying arrow field types by name by @tlamarre91 in https://github.com/lancedb/lancedb/pull/2704
- fix: add name to index config and fix create_index typing by @wkalt in https://github.com/lancedb/lancedb/pull/2660

## 📚 Documentation

- docs: transition to new docs by @AyushExel in https://github.com/lancedb/lancedb/pull/2681
- docs: attempt fix doc deployment and remove recipes workflow trigger by @AyushExel in https://github.com/lancedb/lancedb/pull/2688
- docs: add custom redirect for storage page by @AyushExel in https://github.com/lancedb/lancedb/pull/2706

## 🔧 Build and CI

- ci(nodejs): lint for unused imports by @wjones127 in https://github.com/lancedb/lancedb/pull/2673
- ci: fix test failure on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2677
- ci: automatic issue creation for failed publish workflows by @wjones127 in https://github.com/lancedb/lancedb/pull/2694
- ci: run remote tests on PRs only if they aren't a fork by @wjones127 in https://github.com/lancedb/lancedb/pull/2697
- ci: fix Python and Node CI on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2700


### Release: lancedb [Python LanceDB v0.25.2](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.2)
## 🎉 New Features

- feat: add use_index parameter to merge insert operations by @wjones127 in https://github.com/lancedb/lancedb/pull/2674
- feat(rust): support namespace backed database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2664
- feat: allow bitmap indexes on large-string, binary, large-binary, and bitmap by @westonpace in https://github.com/lancedb/lancedb/pull/2678
- feat: add support for test_remote_connections by @cmccabe in https://github.com/lancedb/lancedb/pull/2666
- feat: upgrade lance to 0.38.2 by @jackye1995 in https://github.com/lancedb/lancedb/pull/2705

## 🐛 Bug Fixes

- fix: use correct nodejs path for ci by @AyushExel in https://github.com/lancedb/lancedb/pull/2689
- fix: inflated release size due to lance-namespace transitive dependency by @jackye1995 in https://github.com/lancedb/lancedb/pull/2691
- fix: have CI download from ci-support-binaries by @cmccabe in https://github.com/lancedb/lancedb/pull/2692
- fix(node): allow undefined/omitted values for nullable vector fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2656
- fix: use stdlib override when possible by @edrogers in https://github.com/lancedb/lancedb/pull/2699
- fix: federated database should not pass namesapce to listing database by @jackye1995 in https://github.com/lancedb/lancedb/pull/2702
- fix(node): support specifying arrow field types by name by @tlamarre91 in https://github.com/lancedb/lancedb/pull/2704
- fix: add name to index config and fix create_index typing by @wkalt in https://github.com/lancedb/lancedb/pull/2660

## 📚 Documentation

- docs: transition to new docs by @AyushExel in https://github.com/lancedb/lancedb/pull/2681
- docs: attempt fix doc deployment and remove recipes workflow trigger by @AyushExel in https://github.com/lancedb/lancedb/pull/2688
- docs: add custom redirect for storage page by @AyushExel in https://github.com/lancedb/lancedb/pull/2706

## 🔧 Build and CI

- ci(nodejs): lint for unused imports by @wjones127 in https://github.com/lancedb/lancedb/pull/2673
- ci: fix test failure on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2677
- ci: automatic issue creation for failed publish workflows by @wjones127 in https://github.com/lancedb/lancedb/pull/2694
- ci: run remote tests on PRs only if they aren't a fork by @wjones127 in https://github.com/lancedb/lancedb/pull/2697
- ci: fix Python and Node CI on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2700


### Release: lancedb [Node/Rust LanceDB v0.22.2-beta.2](https://github.com/lancedb/lancedb/releases/tag/v0.22.2-beta.2)
## 🐛 Bug Fixes

- fix(node): allow undefined/omitted values for nullable vector fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2656

## 🔧 Build and CI

- ci: automatic issue creation for failed publish workflows by @wjones127 in https://github.com/lancedb/lancedb/pull/2694
- ci: run remote tests on PRs only if they aren't a fork by @wjones127 in https://github.com/lancedb/lancedb/pull/2697
- ci: fix Python and Node CI on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2700


### Release: lancedb [Python LanceDB v0.25.2-beta.2](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.2-beta.2)
## 🐛 Bug Fixes

- fix(node): allow undefined/omitted values for nullable vector fields by @naaa760 in https://github.com/lancedb/lancedb/pull/2656

## 🔧 Build and CI

- ci: automatic issue creation for failed publish workflows by @wjones127 in https://github.com/lancedb/lancedb/pull/2694
- ci: run remote tests on PRs only if they aren't a fork by @wjones127 in https://github.com/lancedb/lancedb/pull/2697
- ci: fix Python and Node CI on main by @wjones127 in https://github.com/lancedb/lancedb/pull/2700


### Release: lancedb [Node/Rust LanceDB v0.22.2-beta.1](https://github.com/lancedb/lancedb/releases/tag/v0.22.2-beta.1)
## 🎉 New Features

- feat: allow bitmap indexes on large-string, binary, large-binary, and bitmap by @westonpace in https://github.com/lancedb/lancedb/pull/2678
- feat: add support for test_remote_connections by @cmccabe in https://github.com/lancedb/lancedb/pull/2666

## 🐛 Bug Fixes

- fix: use correct nodejs path for ci by @AyushExel in https://github.com/lancedb/lancedb/pull/2689
- fix: inflated release size due to lance-namespace transitive dependency by @jackye1995 in https://github.com/lancedb/lancedb/pull/2691
- fix: have CI download from ci-support-binaries by @cmccabe in https://github.com/lancedb/lancedb/pull/2692

## 📚 Documentation

- docs: transition to new docs by @AyushExel in https://github.com/lancedb/lancedb/pull/2681
- docs: attempt fix doc deployment and remove recipes workflow trigger by @AyushExel in https://github.com/lancedb/lancedb/pull/2688


### Release: lancedb [Python LanceDB v0.25.2-beta.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.25.2-beta.1)
## 🎉 New Features

- feat: allow bitmap indexes on large-string, binary, large-binary, and bitmap by @westonpace in https://github.com/lancedb/lancedb/pull/2678
- feat: add support for test_remote_connections by @cmccabe in https://github.com/lancedb/lancedb/pull/2666

## 🐛 Bug Fixes

- fix: use correct nodejs path for ci by @AyushExel in https://github.com/lancedb/lancedb/pull/2689
- fix: inflated release size due to lance-namespace transitive dependency by @jackye1995 in https://github.com/lancedb/lancedb/pull/2691
- fix: have CI download from ci-support-binaries by @cmccabe in https://github.com/lancedb/lancedb/pull/2692

## 📚 Documentation

- docs: transition to new docs by @AyushExel in https://github.com/lancedb/lancedb/pull/2681
- docs: attempt fix doc deployment and remove recipes workflow trigger by @AyushExel in https://github.com/lancedb/lancedb/pull/2688


### Release: lancedb [ci-support-binaries](https://github.com/lancedb/lancedb/releases/tag/ci-support-binaries)

## Project: [duckdb/duckdb](https://duckdb.org/), 1 releases: ['v1.4.1 Bugfix Release']
### Release: duckdb [v1.4.1 Bugfix Release](https://github.com/duckdb/duckdb/releases/tag/v1.4.1)
This is a bug fix release for various issues discovered after we released 1.4.0. 

## What's Changed
* Fix attach to right DB when using DuckLake by @pdet in https://github.com/duckdb/duckdb/pull/19011
* set default value of MAIN_BRANCH_VERSIONING to false by @c-herrewijn in https://github.com/duckdb/duckdb/pull/19014
* ComplexJSON: parse all valid JSON correctly by @Mytherin in https://github.com/duckdb/duckdb/pull/19024
* Issue #19016: ICU Offset Parsing by @hawkfish in https://github.com/duckdb/duckdb/pull/19029
* Throw if we detect a quoted new line with the null padding set in parallel mode by @pdet in https://github.com/duckdb/duckdb/pull/19012
* Bump iceberg & ducklake by @carlopi in https://github.com/duckdb/duckdb/pull/19037
* Build Fix: `unordered_map<enum class` is not supported in all compilers, use `map<` instead by @Mytherin in https://github.com/duckdb/duckdb/pull/19046
* Disable emitting versioned libraries by default by @Mytherin in https://github.com/duckdb/duckdb/pull/19047
* Re-add aliased settings to duckdb_settings() view, and some fixes for aliased settings by @Mytherin in https://github.com/duckdb/duckdb/pull/19050
* Fix threading issues in metadata manager, and expand concurrent attach / detach fuzz test by @Mytherin in https://github.com/duckdb/duckdb/pull/19054
* Correctly re-align all child column segments of the ColumnData on Deserialize, and add logging to checkpoints by @Mytherin in https://github.com/duckdb/duckdb/pull/19055
* [unittest] Fixes so that '{BASE_TEST_NAME}' can be used within --on-new-connection by @carlopi in https://github.com/duckdb/duckdb/pull/19056
* add a bunch of expected error messages to old macro tests and fix iss… by @lnkuiper in https://github.com/duckdb/duckdb/pull/19042
* Always execute cast and try_cast if they are not invertible by @DinosL in https://github.com/duckdb/duckdb/pull/19010
* Switching core extension upload to dedicated credentials by @hannes in https://github.com/duckdb/duckdb/pull/19061
* Include BeginQuery in latency metric by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19064
* [Dev] Bit of code cleanup in (parquet) ColumnWriter by @Tishj in https://github.com/duckdb/duckdb/pull/19063
* Add config: one_schema_per_test.json by @carlopi in https://github.com/duckdb/duckdb/pull/19059
* Change bucket name for core extensions by @hannes in https://github.com/duckdb/duckdb/pull/19083
* Moved test data into testing dir by @NiclasHaderer in https://github.com/duckdb/duckdb/pull/19102
* Bump httpfs by @carlopi in https://github.com/duckdb/duckdb/pull/19104
* Fix example syntax in `variant_typeof()` function by @krlmlr in https://github.com/duckdb/duckdb/pull/18977
* Avoid throwing on unset extension setting by @Mytherin in https://github.com/duckdb/duckdb/pull/19117
* Fix internal issue 5975 by @lnkuiper in https://github.com/duckdb/duckdb/pull/19101
* Properly initialize `StringStats` in Parquet reader by @lnkuiper in https://github.com/duckdb/duckdb/pull/19139
* Remove HTTPFS tests and setup scripts by @Mytherin in https://github.com/duckdb/duckdb/pull/19140
* Validate JSON in Parquet reader by @lnkuiper in https://github.com/duckdb/duckdb/pull/19143
* Fix bug in merge into when condition is in parenthesis by @pdet in https://github.com/duckdb/duckdb/pull/19137
* Allow implicit casts from `JSON[]` to `JSON` again by @lnkuiper in https://github.com/duckdb/duckdb/pull/19141
* [ci] Change logic for saving caches: Github variable that decides what gets cached by @carlopi in https://github.com/duckdb/duckdb/pull/19150
* Fix handling of quotes in ToString() of search_path in current_setting by @Mytherin in https://github.com/duckdb/duckdb/pull/19162
* Delay throwing `NotImplementedException` in `ExpressionBinder` by @lnkuiper in https://github.com/duckdb/duckdb/pull/19153
* Issue #18303: AsOf NLJ Nulls by @hawkfish in https://github.com/duckdb/duckdb/pull/19173
* HTTPUtil: response might be null, perform check by @carlopi in https://github.com/duckdb/duckdb/pull/19179
* Handle malformed schema index in Parquet reader by @Mytherin in https://github.com/duckdb/duckdb/pull/19191
* ATTACH IF NOT EXISTS: avoid looping waiting for DETACH to finish, wait only for an ATTACH operation to finish by @Mytherin in https://github.com/duckdb/duckdb/pull/19193
* Implement duckdb_connection_count table function by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19187
* Disable ALP for non-default block sizes by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19197
* Check for unresolved parameters when binding `CREATE MACRO ... AS TABLE` by @lnkuiper in https://github.com/duckdb/duckdb/pull/19196
* https://duckdb-blobs.s3.amazonaws.com -> https://blobs.duckdb.org by @carlopi in https://github.com/duckdb/duckdb/pull/19206
* [chore] Attempt at restoring workflow for MinGW Static libs  by @carlopi in https://github.com/duckdb/duckdb/pull/19205
* Simple no default region return 301 response by @Tmonster in https://github.com/duckdb/duckdb/pull/19087
* [Fix] Correctly reset the gate status during ART merging by @taniabogatsch in https://github.com/duckdb/duckdb/pull/19204
* build spatial extension for mingw by @c-herrewijn in https://github.com/duckdb/duckdb/pull/19207
* Fixup templated version of TryGetSecretKeyOrSetting by @carlopi in https://github.com/duckdb/duckdb/pull/19218
* Bump: delta by @samansmink in https://github.com/duckdb/duckdb/pull/19220
* Autoloading helper file system: allow either autoloading or proper errors in more file operations by @carlopi in https://github.com/duckdb/duckdb/pull/19198
* Eargerly destroy sort buffers in Window by @lnkuiper in https://github.com/duckdb/duckdb/pull/19224
* [Transaction] Delete and drop of a table can now happen in the same transaction without error by @Tishj in https://github.com/duckdb/duckdb/pull/18918
* PRAGMA's MissingEntry: Suggest CALL might be an option by @carlopi in https://github.com/duckdb/duckdb/pull/18815
* Bump: aws, ducklake, iceberg by @samansmink in https://github.com/duckdb/duckdb/pull/19228
* Issue 18603 by @Tmonster in https://github.com/duckdb/duckdb/pull/19227
* Bump DuckLake to latest of V1.4 by @pdet in https://github.com/duckdb/duckdb/pull/19237
* Bump mysql and sqlite by @staticlibs in https://github.com/duckdb/duckdb/pull/19240
* Don't write parquet-native `GEOMETRY` by default, add option to control GeoParquet version by @Maxxen in https://github.com/duckdb/duckdb/pull/19244
* When executing a relation, generate a query to set if it is not a query relation by @Mytherin in https://github.com/duckdb/duckdb/pull/19234
* add support for writing geoparquet with v2 metadata too by @Maxxen in https://github.com/duckdb/duckdb/pull/19246
* Bump: iceberg by @samansmink in https://github.com/duckdb/duckdb/pull/19250
* Bump: avro, httpfs by @samansmink in https://github.com/duckdb/duckdb/pull/19248
* bump duckdb-azure ref for 1.4.1 by @benfleis in https://github.com/duckdb/duckdb/pull/19275

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.4.0...v1.4.1
## Project: [trinodb/trino](https://trino.io/docs/current/release/release-{release}.html), 1 releases: ['Trino 478']
### Release: trino [Trino 478](https://github.com/trinodb/trino/releases/tag/478)
See https://trino.io/docs/current/release/release-478.html
