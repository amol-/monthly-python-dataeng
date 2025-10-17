# Complete List of Projects
 * Project: apache/arrow has 1 releases
 * Project: posit-dev/great-tables has 1 releases
 * Project: ibis-project/ibis has 1 releases
 * Project: narwhals-dev/narwhals has 3 releases
 * Project: pola-rs/polars has 6 releases
 * Project: pandas-dev/pandas has 1 releases
 * Project: holoviz/panel has 2 releases
 * Project: cython/cython has 1 releases
 * Project: plotly/dash has 4 releases
 * Project: dask/dask has 2 releases
 * Project: delta-io/delta-rs has 1 releases
 * Project: rapidsai/cudf has 2 releases
 * Project: lancedb/lance has 9 releases
 * Project: lancedb/lancedb has 17 releases
 * Project: datafusion-contrib/datafusion-table-providers has 2 releases
 * Project: duckdb/duckdb has 2 releases
 * Project: trinodb/trino has 1 releases
 * Project: datafusion-contrib/datafusion-table-providers has 2 releases
 * Project: https://spark.apache.org/news/index.html has 2 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 2 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 2 articles
### Release: [Preview release of Spark 4.1.0](https://spark.apache.org/news/spark-4-1-0-preview2-released.html)

### Release: [Spark 3.5.7 released](https://spark.apache.org/news/spark-3-5-7-released.html)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 2 articles
### Release: [Apache DataFusion 50.0.0 Released](https://datafusion.apache.org/blog/2025/09/29/datafusion-50.0.0)

### Release: [Implementing User Defined Types and Custom Metadata in DataFusion](https://datafusion.apache.org/blog/2025/09/21/custom-types-using-metadata)

## Project: [apache/arrow](https://arrow.apache.org/docs/python/), 1 releases: ['Apache Arrow 22.0.0 RC0']
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

## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 3 releases: ['Narwhals v2.8.0', 'Narwhals v2.7.0', 'Narwhals v2.6.0']
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

## Project: [pola-rs/polars](https://docs.pola.rs/), 6 releases: ['Python Polars 1.34.0', 'Python Polars 1.34.0-beta.5', 'Python Polars 1.34.0-beta.4', 'Python Polars 1.34.0-beta.3', 'Python Polars 1.34.0-beta.1', 'Rust Polars 0.51.0']
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
## Project: [holoviz/panel](https://panel.holoviz.org/), 2 releases: ['Version 1.8.2', 'Version 1.8.1']
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

### Release: panel [Version 1.8.1](https://github.com/holoviz/panel/releases/tag/v1.8.1)
Many thanks to [@ATL2001](https://github.com/ATL2001) (first contribution), [@Coderambling](https://github.com/Coderambling), [@philippjfr](https://github.com/philippjfr), and [@hoxbro](https://github.com/hoxbro) for their contributions.

### Enhancements

- Add configuration to disable container popup ([#8200](https://github.com/holoviz/panel/pull/8200))

### Bug Fixes

- Ensure Tabulator empty column has no width ([#8193](https://github.com/holoviz/panel/pull/8193))
- Add UTC timezone to default time for croniter ([#8199](https://github.com/holoviz/panel/pull/8199))

### Documentation

- Update indicators_performance.md to fix typo ([#8192](https://github.com/holoviz/panel/pull/8192))

## Project: [cython/cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html), 1 releases: ['3.1.4']
### Release: cython [3.1.4](https://github.com/cython/cython/releases/tag/3.1.4)

## Project: [plotly/dash](https://plotly.com/dash/), 4 releases: ['v4.0.0rc2', 'Dash Version 3.3.0rc1', 'Dash Version 3.3.0rc0', 'v4.0.0rc1']
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

## Project: [dask/dask](https://www.dask.org/), 2 releases: ['2025.10.0', '2025.9.1']
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

### Release: dask [2025.9.1](https://github.com/dask/dask/releases/tag/2025.9.1)
## Changes

- Bump scientific-python/issue-from-pytest-log-action from 1.3.0 to 1.4.0 @[dependabot[bot]](https://github.com/apps/dependabot) (#12077)
- Avoid unconditional pyarrow dependency in dataframe.backends @TomAugspurger (#12075)
- pandas 3.x compatibility for `.groups` @TomAugspurger (#12071)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

## Project: [delta-io/delta-rs](https://delta-io.github.io/delta-rs/usage/installation/), 1 releases: ['python-v1.2.0']
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
## Project: [rapidsai/cudf](https://docs.rapids.ai/api/cudf/stable/user_guide/10min/), 2 releases: ['v25.10.00', '[NIGHTLY] v25.12.00']
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
### Release: cudf [[NIGHTLY] v25.12.00](https://github.com/rapidsai/cudf/releases/tag/v25.12.00a)
## 🔗 Links

- [Development Branch](https://github.com/rapidsai/cudf/tree/branch-25.12)
- [Compare with `main` branch](https://github.com/rapidsai/cudf/compare/main...branch-25.12)

## 🚨 Breaking Changes

- Change .str.starts/endswith with tuple argument to match any pattern instead of pairwise matching (#20249) @mroeschke
- Remove DataFrame.apply_chunks, Groupby.apply_grouped (#20194) @mroeschke
- [cudf-polars] CUDA stream (#20154) @madsbk
- Remove compatibility with nvCOMP versions before 5.0 (#20140) @vuule
- Rewrite JNI functions to use `JNI_TRY`/`JNI_CATCH` (#19053) @ttnghia

## 🐛 Bug Fixes

- We need this to pacify mypy (#20285) @wence-
- Add Proxy for `SparseAccessor` (#20278) @galipremsagar
- Add private attributes for `cudf.pandas` proxy objects (#20276) @galipremsagar
- Pin ibis-framework&lt;11.0.0 (#20267) @Matt711
- Pin `deltalake` in cudf-polars-polars-tests CI job (#20255) @TomAugspurger
- Add `stream` and `mr` arguments to `Column.from_arrow` type stub (#20244) @TomAugspurger
- Fix the host-device tdigest offsets by using cuda::std::span (#20220) @PointKernel
- Deallocation should be noexcept (#20219) @bdice
- Change stream_checking_resource_adaptor::do_deallocate to noexcept (#20218) @vyasr
- Fix a race condition in the decode of delta encoded Parquet columns (#20216) @vuule
- Handle NVMLError_NotSupported in cudf-polars (#20179) @TomAugspurger
- Require passing memory resources to from_libcudf methods (#20171) @vyasr
- Fix RMM JNI pinned_fallback_host_memory_resource for CCCL 3.1.0 (#20160) @bdice
- Fix arrow timestamp frequency cases in `cudf.pandas` (#20128) @galipremsagar
- Fix cudf.date_range with non-iso start and end date strings (#20116) @mroeschke
- Unproxy few unnecessary testing utilities in pandas (#20088) @galipremsagar
- Fix create_distinct_rows_column to create non-nullable columns (#20082) @davidwendt
- Handle missing nightly runs in pandas tests job (#20081) @galipremsagar
- Cast inputs to true division from decimal to float (#20077) @Matt711
- Copy `attrs` at correct place in `DataFrame` constructor (#20074) @galipremsagar
- Fix numpy ufunc for `DataFrame` (#20070) @galipremsagar
- Align decimal dtypes in predicate before conditional join (#20060) @Matt711
- Enable hash-groupby for decimal32/64 type and MEAN aggregation (#20040) @davidwendt
- Fix libcudf groupby benchmarks to not include internal cache (#20038) @davidwendt

## 📖 Documentation

- Add note that --rmm-async only affects distributed scheduler. (#20129) @bdice

## 🚀 New Features

- Implement `ARGMIN` and `ARGMAX` aggregations for reduction (#20207) @ttnghia
- Add remaining memory resources (#20197) @vyasr
- Add memory resources to scalars (#20196) @vyasr
- Skip decompression of pruned parquet pages (#20192) @mhaseeb123
- Add memory resources to replace, json, and hashing (#20150) @vyasr
- Support decimal literals in cudf-polars (#20147) @Matt711
- Add pylibcudf is_valid_reduce_aggregation API (#20145) @davidwendt
- Add memory resources to I/O modules (#20136) @vyasr
- Add memory resources to reduce, column, column_factories, and contiguous_split (#20135) @vyasr
- Passthrough unary ops through Parquet predicate pushdown (#20127) @mhaseeb123
- Add memory resource to all strings modules (#20123) @vyasr
- Add memory resources to all nvtext APIs (#20119) @vyasr
- Add an example to inspect parquet files and dump row group and page level metadata information (#20117) @mhaseeb123
- Allow multiple calls to `cudf::initialize` and `cudf::deinitialize` (#20111) @vuule
- Remove rounding from cudf java (#20110) @pmattione-nvidia
- Add memory resources to groupby, datetime, and lists modules (#20102) @vyasr
- Add memory resources to search, reshape, and partitioning module (#20101) @vyasr
- Add memory resources to rolling, sorting, and quantiles modules (#20099) @vyasr
- Add memory resources to binaryop, copying, and stream_compaction (#20059) @vyasr
- Add memory resources to unary, transform, and filling modules (#20054) @vyasr
- Support `cum_sum(...).over(...)` expressions in cudf-polars (#19908) @Matt711
- Support forward/backward filling null values in a grouped window context (#19907) @Matt711
- [FEA] Implement JIT Filter for read_parquet (#19831) @lamarrr
- Add an example to demonstrate the use of next-gen parquet reader to read a parquet file with highly selective filters (#19469) @mhaseeb123
- Rewrite JNI functions to use `JNI_TRY`/`JNI_CATCH` (#19053) @ttnghia
- Add support for maintain_order param in joins (#17698) @Matt711

## 🛠️ Improvements

- Skip mypy in pre-commit.ci (#20286) @bdice
- Remove extraneous host_memory_resource include (#20284) @bdice
- Add numpy to the mypy pre-commit environment (#20282) @vyasr
- Add `MultiIndex.dtypes` (#20279) @galipremsagar
- Add more type annotations to cudf/core/column subclasses (#20277) @mroeschke
- Handle unordered grouped windows properly for null filling and cum sums (#20275) @Matt711
- Unpin DuckDB and Ibis in cudf.pandas thirdparty tests (#20269) @mroeschke
- Enable `sccache-dist` connection pool (#20264) @trxcllnt
- Update ``ConfigOptions`` for rapidsmpf-streaming integration (#20252) @rjzamora
- Add arm testing of cudf.pandas unit tests (#20251) @vyasr
- Add pylibcudf to pre-commit linting and fix outstanding errors (#20250) @vyasr
- Change .str.starts/endswith with tuple argument to match any pattern instead of pairwise matching (#20249) @mroeschke
- Move and rename ``ScanPartitionPlan`` (#20248) @rjzamora
- Standardize setting StructDtype field names post libcudf conversion (#20235) @mroeschke
- Prevent accidental copies of expensive-to-copy object types (#20226) @vuule
- More mypy and docs fixes (#20224) @vyasr
- Configuration for which metrics are enabled during tracing (#20223) @TomAugspurger
- Fix parquet row number check for page bounds (#20217) @pmattione-nvidia
- Rename `comparison_binop_generator` to `arg_minmax_binop_generator` and corresponding file to `nested_types_extrema_utils.cuh` (#20212) @Copilot
- Fix various typing errors (#20205) @vyasr
- Stop using libcudf default parameters in pylibcudf (#20204) @vyasr
- Pin pydantic&lt;2.12 in ci/test_cudf_polars_polars_tests.sh (#20200) @mroeschke
- Support binops between float scalar to decimal column (#20199) @mroeschke
- Add an overhead field to cudf-polars tracing (#20198) @TomAugspurger
- Remove DataFrame.apply_chunks, Groupby.apply_grouped (#20194) @mroeschke
- [pre-commit.ci] pre-commit autoupdate (#20189) @pre-commit-ci[bot]
- Revert &quot;Temporarily disable conda-java-tests&quot; (#20184) @bdice
- Don&#39;t assume cudf_polars benchmarking scale factor is always an integer (#20182) @mroeschke
- Remove unnecessary work from `read_parquet_metadata` (#20180) @vuule
- Reduce execution times for parquet dictionary tests (#20176) @mhaseeb123
- Skip filtering Parquet row groups with dictionaries if there are non-dict encoded pages (#20175) @mhaseeb123
- Improve performance of groupby tdigests gtests (#20173) @davidwendt
- Update to rapids-logger 0.2 (#20172) @bdice
- Split row operator header (#20166) @PointKernel
- Add PDSH benchmark runner for cudf.pandas (#20164) @mroeschke
- Temporarily disable conda-java-tests (#20162) @bdice
- Manual forward merger for Branch 25.12 - branch 25.10 (#20157) @galipremsagar
- [cudf-polars] CUDA stream (#20154) @madsbk
- Avoid NumericalColumn call from CategoricalColumn.children (#20153) @mroeschke
- Branch 25.12 merge branch 25.10 (#20152) @vyasr
- Make ListColumn._transform_leaves convert via pylibcudf (#20151) @mroeschke
- Make ColumnBase.as_*_column convert via pylibcudf (#20149) @mroeschke
- Make ColumnBase.deserialize construct via pylibcudf (#20142) @mroeschke
- Remove unused ColumnBase.view (#20141) @mroeschke
- Remove compatibility with nvCOMP versions before 5.0 (#20140) @vuule
- Adjust rmm pool handling in PDSH benchmarks (#20138) @TomAugspurger
- Fix slowdown in cudf-polars distributed tests (#20137) @TomAugspurger
- Disable async MR priming in cudf.pandas (#20133) @bdice
- Fix type annotations in cudf-polars (#20131) @TomAugspurger
- Add tests for AUTO and HYBRID (de)compression modes (#20126) @vuule
- Run cudf-polars wheels unit tests with more than 1 process (#20124) @mroeschke
- Add pyarrow stubs to mypy environment and fix associated errors (#20118) @vyasr
- Avoid running pandas unit tests for private functionality with cudf.pandas (#20115) @mroeschke
- Remove MultiIndex.from_pandas pytest benchmark (#20112) @mroeschke
- Use 8 processes for pandas tests, show top 10 test times (#20109) @bdice
- Reduce verbosity of running the pandas test suite (#20107) @vyasr
- Switch host_vector and host_span dependency (#20106) @davidwendt
- Make Column.set_mask go through pylibcudf (#20103) @mroeschke
- Have ListColumn.from_sequence go through pylibcudf (#20098) @mroeschke
- Deprecate legacy public row operators (#20097) @PointKernel
- Fix `RAPIDS_BRANCH` version and update script (#20091) @galipremsagar
- Reduce output buffer sizes for pruned pages of columns with a `list` parent (#20086) @mhaseeb123
- Avoid direct CategoricalColumn calls in dask_cudf (#20080) @mroeschke
- Rework reduction case statement as dispatch_type_and_aggregation (#20078) @davidwendt
- Avoid shadowing module names (#20071) @vyasr
- Fix typing issues in pylibcudf (#20069) @vyasr
- Avoid more explicit calls to IntervalColumn and StructColumn (#20064) @mroeschke
- Cleanup of some libcudf aggregation code (#20053) @davidwendt
- Prune entries in Sphinx nitpick_ignore (#20045) @mroeschke
- Deprecate .from_pandas constructor (#19996) @mroeschke
- Improve performance of string column size computation during parquet reads. (#19986) @nvdbaranec
- Run cudf-polars conda unit tests with more than 1 process (#19980) @mroeschke
- Clean up detail device atomic logic using atomic_ref (#19924) @PointKernel
- Pin polars version &lt;1.34 and &gt;=1.29 (#19912) @Matt711
- Trace node execution in cudf-polars (#19895) @TomAugspurger
- Cleanup parquet for simple columns (#19869) @pmattione-nvidia
- Update nvbench (#19619) @bdice
- Run polars tests with the streaming and in-memory executors (#19354) @Matt711
- Remove calling to `purge_nonempty_nulls` in `make_lists_column` (#12873) @ttnghia
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 9 releases: ['v0.38.3-beta.4', 'v0.38.3-beta.3', 'v0.38.3-beta.2', 'v0.38.3-beta.1', 'v0.38.2', 'v0.38.1', 'v0.38.0', 'v0.37.1-beta.1', 'v0.37.0']
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
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 17 releases: ['Node/Rust LanceDB v0.22.3-beta.0', 'Python LanceDB v0.25.3-beta.0', 'Node/Rust LanceDB v0.22.2', 'Python LanceDB v0.25.2', 'Node/Rust LanceDB v0.22.2-beta.2', 'Python LanceDB v0.25.2-beta.2', 'Node/Rust LanceDB v0.22.2-beta.1', 'Python LanceDB v0.25.2-beta.1', 'ci-support-binaries', 'Node/Rust LanceDB v0.22.2-beta.0', 'Python LanceDB v0.25.2-beta.0', 'Node/Rust LanceDB v0.22.1', 'Python LanceDB v0.25.1', 'Node/Rust LanceDB v0.22.1-beta.3', 'Python LanceDB v0.25.1-beta.3', 'Node/Rust LanceDB v0.22.1-beta.2', 'Python LanceDB v0.25.1-beta.2']
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
## Project: [duckdb/duckdb](https://duckdb.org/), 2 releases: ['v1.4.1 Bugfix Release', 'DuckDB 1.4.0 "Andium"']
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
