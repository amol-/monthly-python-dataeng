# Complete List of Projects
 * Project: apache/arrow has 2 releases
 * Project: substrait-io/substrait-python has 2 releases
 * Project: narwhals-dev/narwhals has 2 releases
 * Project: pola-rs/polars has 3 releases
 * Project: pandas-dev/pandas has 2 releases
 * Project: holoviz/panel has 2 releases
 * Project: pyscript/pyscript has 2 releases
 * Project: plotly/dash has 3 releases
 * Project: dask/dask has 5 releases
 * Project: delta-io/delta-rs has 3 releases
 * Project: rapidsai/cudf has 2 releases
 * Project: lancedb/lance has 16 releases
 * Project: lancedb/lancedb has 8 releases
 * Project: datafusion-contrib/datafusion-table-providers has 1 releases
 * Project: duckdb/duckdb has 1 releases
 * Project: datafusion-contrib/datafusion-table-providers has 1 releases
 * Project: unionai-oss/pandera has 3 releases
 * Project: https://spark.apache.org/news/index.html has 4 releases
 * Project: https://blog.holoviz.org/index.xml has 1 releases
 * Project: https://datafusion.apache.org/blog/feed.xml has 4 releases


# Releases for each project
## Project: [https://spark.apache.org/news/index.html](https://spark.apache.org/news/index.html), 4 articles
### Release: [Spark 4.0.2 released](https://spark.apache.org/news/spark-4-0-2-released.html)

### Release: [Spark 3.5.8 released](https://spark.apache.org/news/spark-3-5-8-released.html)

### Release: [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview1-released.html)

### Release: [Spark 4.1.1 released](https://spark.apache.org/news/spark-4-1-1-released.html)

## Project: [HoloViz Blog](https://blog.holoviz.org/), 1 articles
### Release: [A Major Step Toward Structured, Auditable AI-Driven Data Apps: Lumen AI 1.0](https://blog.holoviz.org/posts/lumen_1.0/)

## Project: [Apache DataFusion Blog](https://datafusion.apache.org/blog/), 4 articles
### Release: [Optimizing SQL CASE Expression Evaluation](https://datafusion.apache.org/blog/2026/02/02/datafusion_case)

### Release: [Apache DataFusion Comet 0.13.0 Release](https://datafusion.apache.org/blog/2026/01/30/datafusion-comet-0.13.0)

### Release: [Apache DataFusion 52.0.0 Released](https://datafusion.apache.org/blog/2026/01/12/datafusion-52.0.0)

### Release: [Extending SQL in DataFusion: from ->> to TABLESAMPLE](https://datafusion.apache.org/blog/2026/01/12/extending-sql)

## Project: [apache/arrow](https://arrow.apache.org/docs/python/), 2 releases: ['Apache Arrow 23.0.0', 'Apache Arrow 23.0.0 RC2']
### Release: arrow [Apache Arrow 23.0.0](https://github.com/apache/arrow/releases/tag/apache-arrow-23.0.0)
Release Notes URL: https://arrow.apache.org/release/23.0.0.html
### Release: arrow [Apache Arrow 23.0.0 RC2](https://github.com/apache/arrow/releases/tag/apache-arrow-23.0.0-rc2)
Release Notes: Release Candidate: 23.0.0 RC2
## Project: [substrait-io/substrait-python](https://substrait.io/), 2 releases: ['v0.27.0', 'v0.26.0']
### Release: substrait-python [v0.27.0](https://github.com/substrait-io/substrait-python/releases/tag/v0.27.0)
## What's Changed
* docs: add RELEASING.md by @nielspardon in https://github.com/substrait-io/substrait-python/pull/146
* feat: remove generated protobuf code from substrait-python by @vbarua in https://github.com/substrait-io/substrait-python/pull/145

## Breaking Changes
* code under `substrait.gen.proto` is now found under `substrait`
* simple extension files have been moved from `extensions` to `extension_files`
* version information has been moved to `substrait.version` module

**Full Changelog**: https://github.com/substrait-io/substrait-python/compare/v0.26.0...v0.27.0
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
## Project: [narwhals-dev/narwhals](https://narwhals-dev.github.io/narwhals/), 2 releases: ['Narwhals v2.16.0', 'Narwhals v2.15.0']
### Release: narwhals [Narwhals v2.16.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.16.0)
## Changes

- ci: Unpin `polars==1.34.0` in `--group typing` (#3434)
- ci: Bump `duckdb==1.4.4` in `--group typing` (#3433)
- test: DuckDB XPass (#3426)
- refactor: Simplify `pd.ArrowDtype` -> `nw.DType` (#3413)
- ci: Temporarily pin sqlglot, ignore pyspark warning (#3412)
- Remove interchange from non v1 (#3403)

## :sparkles: Enhancements

- feat: add `separator` argument in `read_csv`/`scan_csv` (#2989)
- feat: Allow nested structures in `lit` (#3424)
- enh: Introduce `narwhals.sql` (#3254)
- enh: Introduce (optional) `order_by` in `first` / `last` (#3372)
- feat: support window functions in filter (#3401)
- feat: Improve support for `Decimal` DType (#3377)
- feat: Support `concat(..., how="diagonal")` for `ibis` (#3404)
- feat: Enable`list.{sort, sum}` for sqlframe (#3400)
- feat: Add `str.pad_{start,end}` (#3395)
- feat: Add `{Expr,Series}.cos` (#3392)
- feat: Add `testing.assert_frame_equal` (#3220)

## 🐞 Bug fixes

- fix(test): Pin correct polars version in `lit_test` (#3438)
- refactor: Avoid subprocess to test TPCH queries, and fix q8 (#3419)
- ci(fix): Temporary pin numba & llvmlite for darts downstream test (#3406)
- fix(test): Change error message for polars, un-xfail sqlframe `list.mean` (#3397)

## :hammer_and_wrench: Other improvements

- ci: Pin `sqlglot<28.6.0` in `--group typing` (#3432)
- chore: pin sqlglot to get ci green (#3428)
- chore(typing): Improve `tpch` typing (#3420)
- ci: pin pandas in some downstream jobs (#3417)
- [pre-commit.ci] pre-commit autoupdate (#3275)

Thank you to all our contributors for making this release possible!
@FBruzzesi, @MarcoGorelli, @camriddell, @dangotbanned, @liamholmes31, and @raisadz
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

## Project: [pola-rs/polars](https://docs.pola.rs/), 3 releases: ['Python Polars 1.38.0', 'Python Polars 1.37.1', 'Python Polars 1.37.0']
### Release: polars [Python Polars 1.38.0](https://github.com/pola-rs/polars/releases/tag/py-1.38.0)
## ⚠️ Deprecations

- Deprecate `retries=n` in favor of `storage_options={"max_retries": n}` (#26155)

## 🚀 Performance improvements

- Enable zero-copy object\_store `put` upload for IPC sink (#26288)
- Resolve file schema's and metadata concurrently (#26325)
- Run elementwise CSEE for the streaming engine (#26278)
- Disable morsel splitting for fast-count on streaming engine (#26245)
- Implement streaming decompression for scan\_ndjson and scan\_lines (#26200)
- Improve string slicing performance (#26206)
- Refactor `scan_delta` to use python dataset interface (#26190)
- Add dedicated kernel for group-by `arg_max/arg_min` (#26093)
- Add streaming merge-join (#25964)
- Generalize Bitmap::new\_zeroed opt for Buffer::zeroed (#26142)
- Reduce fs stat calls in path expansion (#26173)
- Lower streaming group\_by n\_unique to unique().len() (#26109)

## ✨ Enhancements

- Avoid OOM for scan\_ndjson and scan\_lines if input is compressed and negative slice (#26396)
- Support annoymous agg in-mem (#26376)
- Add unstable `arrow_schema` parameter to `sink_parquet` (#26323)
- Improve error message formatting for structs (#26349)
- Remove parquet field overwrites (#26236)
- Enable zero-copy object\_store `put` upload for IPC sink (#26288)
- Improved disambiguation for qualified wildcard columns in SQL projections (#26301)
- Expose `upload_concurrency` through env var (#26263)
- Allow quantile to compute multiple quantiles at once (#25516)
- Allow empty LazyFrame in `LazyFrame.group_by(...).map_groups` (#26275)
- Use delta file statistics for batch predicate pushdown (#26242)
- Add streaming UnorderedUnion (#26240)
- Implement compression support for sink\_ndjson (#26212)
- Add unstable record batch statistics flags to `{sink/scan}_ipc` (#26254)
- Support CSE for python UDFs on the same address (#26253)
- Cloud retry/backoff configuration via `storage_options` (#26204)
- Use same sort order for expanded paths across local / cloud / directory / glob (#26191)
- Add streaming merge-join (#25964)
- Serialize optimization flags for cloud plan (#26168)
- Add compression support to write\_csv and sink\_csv (#26111)
- Add `scan_lines` (#26112)
- Support regex in `str.split` (#26060)
- Add unstable IPC Statistics read/write to `scan_ipc`/`sink_ipc` (#26079)
- Add unstable `height` parameter to `DataFrame`/`LazyFrame` (#26014)
- Remove old partition sink API (#26100)
- Expose ArrowStreamExportable on python collect batches iterator (#26074)
- Add nulls support for all rolling\_by operations (#26081)

## 🐞 Bug fixes

- Correct off-by-one in RLE row counting for nullable dictionary-encoded columns (#26411)
- Support very large integers in env var limits (#26399)
- Fix PlPath panic from incorrect slicing of UTF8 boundaries (#26389)
- Fix Float dtype for spearman correlation (#26392)
- Fix optimizer panic in right joins with type coercion (#26365)
- Don't serialize retry config from local environment vars (#26289)
- Fix `PartitionBy` with scalar key expressions and `diff()` (#26370)
- Add {Float16, Float32} -> Float32 lossless upcast (#26373)
- Fix panic using `with_columns` and `collect_all` (#26366)
- Add multi-page support for writing dictionary-encoded Parquet columns (#26360)
- Ensure slice advancement when skipping non-inlinable values in `is_in` with inlinable needles (#26361)
- Pin `xlsx2csv` version temporarily (#26352)
- Bugs in ViewArray total\_bytes\_len (#26328)
- Overflow in i128::abs in Decimal fits check (#26341)
- Make Expr.hash on Categorical mapping-independent (#26340)
- Clone shared GroupBy node before mutation in physical plan creation (#26327)
- Fixed "sheet\_name" typing for `read_ods` and `read_excel` (#26317)
- Improve Polars dtype inference from Python `Union` typing (#26303)
- Consider the "current location" of an item when computing `rolling_rank_by` (#26287)
- Reset `is_count_star` flag between queries in collect\_all (#26256)
- Fix incorrect is\_between filter on scan\_parquet (#26284)
- Make polars compatible with ty (#26270)
- Lower AnonymousStreamingAgg in group-by as aggregate (#26258)
- Avoid overflow in `pl.duration` scalar arguments case (#26213)
- Broadcast arr.get on single array with multiple indices (#26219)
- Fix panic on CSPE with sorts (#26231)
- Eager `DataFrame.slice` with negative offset and `length=None` (#26215)
- Use correct schema side for streaming merge join lowering (#26218)
- Overflow panic in `scan_csv` with multiple files and `skip_rows + n_rows` larger than total row count (#26128)
- Respect `allow_object` flag after cache (#26196)
- Raise error on non-elementwise PartitionBy keys (#26194)
- Allow ordered categorical dictionary in scan\_parquet (#26180)
- Allow excess bytes on IPC bitmap compressed length (#26176)
- Address a macOS-specific compile issue (#26172)
- Fix deadlock on `hash_rows()` of 0-width DataFrame (#26154)
- Fix NameError filtering pyarrow dataset (#26166)
- Fix concat\_arr panic when using categoricals/enums (#26146)
- Fix NDJSON/scan\_lines negative slice splitting with extremely long lines (#26132)
- Incorrect group\_by min/max fast path (#26139)
- Remove a source of non-determinism from lowering (#26137)
- Error when `with_row_index` or `unpivot` create duplicate columns on a `LazyFrame` (#26107)
- Panics on shift with head (#26099)

## 📖 Documentation

- Fix `Expr.get` referencing incorrect dtype for `index` parameter (#26364)
- Fix `Expr.quantile` formatting (#26351)
- Drop `sphinx-llms-txt` extension (#26285)
- Remove deprecated `cublet_id` (#26260)
- Update for new release (#26255)
- Update MCP server section with new URL (#26241)
- Fix unmatched paren and punctuation in pandas migration guide (#26251)
- Add observatory database\_path to docs (#26201)
- Note plugins in Python user-defined functions (#26138)

## 📦 Build system

- Address remaining Python 3.14 issues with `make requirements-all` (#26195)
- Address a macOS-specific compile issue (#26172)

## 🛠️ Other improvements

- Ensure local doctests skip `from_torch` if module not installed (#26405)
- Change linked timezones in test suite to canonical timezones (#26310)
- Implement various deprecations (#26314)
- Rename `Operator::Divide` to `RustDivide` (#26339)
- Properly disable the Pyodide tests (#26382)
- Remove unused field (#26367)
- Fix runtime nesting (#26359)
- Remove `xlsx2csv` dependency pin (#26355)
- Use outer runtime if exists in to\_alp (#26353)
- Make CategoricalMapping::new pub(crate) to avoid misuse (#26308)
- Clarify IPC buffer read limit/length paramter (#26334)
- Add dtype test coverage for delta predicate filter (#26291)
- Add AI policy (#26286)
- Unpin "pandas\<3" in dev dependencies (#26249)
- Remove all non CSV fast-count paths (#26233)
- Pin pandas to 2.x for now (#26221)
- Remove unnecessary xfail (#26199)
- Ensure optimization flag modification happens local (#26185)
- Simplify IcebergDataset (#26165)
- Reorganize unit tests into logical subdirectories (#26149)
- Lint leftover fixme (#26122)
- Improve backtrace for `POLARS_PANIC_ON_ERR` (#26125)
- Fix Python docs build (#26117)
- Disable `unused-ignore` mypy lint (#26110)
- Ignore mypy warning (#26105)
- Raise error on `file://hostname/path` (#26061)
- Disable debug info for docs workflow (#26086)
- Update docs for next polars cloud release (#26091)
- Support Python 3.14 in dev environment (#26073)

Thank you to all our contributors for making this release possible!
@Atarust, @EndPositive, @Kevin-Patyk, @LeeviLindgren, @MarcoGorelli, @Matt711, @MrAttoAttoAtto, @Voultapher, @WaffleLapkin, @agossard, @alex-gregory-ds, @alexander-beedie, @azimafroozeh, @bayoumi17m, @c-peters, @carnarez, @dependabot[bot], @dsprenkels, @hallmason17, @hamdanal, @ion-elgreco, @kdn36, @lun3x, @mcrumiller, @nameexhaustion, @orlp, @qxzcode, @r-brink, @ritchie46, @sweb and [dependabot[bot]](https://github.com/apps/dependabot)

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
## Project: [holoviz/panel](https://panel.holoviz.org/), 2 releases: ['Version 1.8.7', 'Version 1.8.6']
### Release: panel [Version 1.8.7](https://github.com/holoviz/panel/releases/tag/v1.8.7)
This patch release reverts two changes that were made in 1.8.6 that turned out to be more disruptive than expected. Additionally it ensures that Tabulator automatically recalculates page sizes on resize and resolves issues with patched versions of Plotly.

### 🐛 Bug fixes

- Rerun Tabulator page size calculation on resize ([#8395](https://github.com/holoviz/panel/pull/8395))
- Fix issues with monkey-patched versions of Plotly ([#8397](https://github.com/holoviz/panel/pull/8397))

### ⏪ Reverted

- Ensure `edit_readonly` resets both class- and instance-level parameters ([#8371](https://github.com/holoviz/panel/pull/8371))
- Validate ReactiveHTML missing id errors ([#8382](https://github.com/holoviz/panel/pull/8382))

### Release: panel [Version 1.8.6](https://github.com/holoviz/panel/releases/tag/v1.8.6)
This patch release includes several ESM and React-related fixes, UI behavior improvements, and enhanced robustness in form inputs and file handling. It also bumps key dependencies and improves support for custom deployments. Thanks to @philippjfr, @maximlt, @emunsing, @TheoMathurin, @dalthviz and @hoxbro for their contributions to this release!

### ✨ Enhancements

- Add `placeholder` parameter on `FloatInput` and `IntInput` ([#8360](https://github.com/holoviz/panel/pull/8360))
- Support for file extensions in `FileDropper.accepted_filetypes` ([#8380](https://github.com/holoviz/panel/pull/8380))
- Accept 2D arrays for stereo `Audio` ([#8381](https://github.com/holoviz/panel/pull/8381))

### 🐛 Bug Fixes

- Ensure collapsed `Card` still renders components to avoid child render issues ([#8274](https://github.com/holoviz/panel/pull/8274))
- **ESM & React Components**:
  - Fix errors when renamed parameters are linked on ESM components ([#8357](https://github.com/holoviz/panel/pull/8357))
  - Fix `rel_path` resolution in ESM components ([#8375](https://github.com/holoviz/panel/pull/8375))
  - Fix `autoreload` watcher setup for ESM apps ([#8361](https://github.com/holoviz/panel/pull/8361))
  - Delay removal of `ReactComponent` children until new ones are mounted ([#8358](https://github.com/holoviz/panel/pull/8358))
- Ensure `PathLike` is accepted for `requirements` in pyodide conversion calls ([#8366](https://github.com/holoviz/panel/pull/8366))
- Ensure `edit_readonly` resets both class- and instance-level parameters ([#8371](https://github.com/holoviz/panel/pull/8371))
- Fix `guest` endpoint validation at root path ([#8370](https://github.com/holoviz/panel/pull/8370))
- Don't attempt to refresh access token if there is no active user session ([#8384](https://github.com/holoviz/panel/pull/8384))
- Ensure OAuth state for user is reset after failing to refresh access token ([#8389](https://github.com/holoviz/panel/pull/8389))
- Ensure `config.design` value is respected by `Template` ([#8388](https://github.com/holoviz/panel/pull/8388))
- Improve robustness of `Tabulator.page_size` inference ([#8390](https://github.com/holoviz/panel/pull/8390))

### ⚠️ Compatibility & Deprecations

- Added compatibility for pandas 3.0 ([#8385](https://github.com/holoviz/panel/pull/8385))

### 📚 Documentation

- Update `Plotly` example to prevent flicker on load ([#8362](https://github.com/holoviz/panel/pull/8362))

### 🧪 Maintenance

- Bump `bokeh` to 3.8.2 in Django example app ([#8376](https://github.com/holoviz/panel/pull/8376))
- Bump `preact` to 10.26.10 ([#8367](https://github.com/holoviz/panel/pull/8367))
- Update pre-commit hooks ([#8363](https://github.com/holoviz/panel/pull/8363))

## Project: [pyscript/pyscript](https://pyscript.com/), 2 releases: ['2026.2.1', '2026.1.1']
### Release: pyscript [2026.2.1](https://github.com/pyscript/pyscript/releases/tag/2026.2.1)
* Removed warnings about `window` and `document` when `sync_main_only` config property is `true`: https://github.com/pyscript/pyscript/pull/2434
* Improved errors on bootstrap when the config cannot be parsed or contains errors: https://github.com/pyscript/pyscript/pull/2435
* Updated Pyodide to its 0.29.3 version: https://pyodide.org/en/stable/project/changelog.html
* Improved packages resolution by ignoring case-sensitive names: https://github.com/pyscript/polyscript/pull/168
* Removed the legacy, archived, toml-j0.4 parser https://github.com/pyscript/pyscript/pull/2442 in favor of our own improved basic-toml parser https://github.com/pyscript/polyscript/pull/171
* Improved `pyscript.web` API where `el.append("string")` will now work as expected: https://github.com/pyscript/pyscript/pull/2447 Thanks to new contributor @iliketocode2.
* Docstring fixes so Markdown API docs render properly: https://github.com/pyscript/pyscript/pull/2449
* Ensure the `remove` method for CSS classes is more forgiving (it logs a warning rather than throws an exception if the class to be removed does not exist): https://github.com/pyscript/pyscript/pull/2450
* Documentation updates given feedback by users: https://github.com/pyscript/docs/pull/209 https://github.com/pyscript/docs/pull/210 (thanks for the suggestion @clayote).
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
## Project: [plotly/dash](https://plotly.com/dash/), 3 releases: ['Dash Version 4.0.0', 'Dash Version 3.4.0', 'v4.0.0rc6']
### Release: dash [Dash Version 4.0.0](https://github.com/plotly/dash/releases/tag/v4.0.0)
## Added
- Redesigned dash core components

## Added since 4.0.0rc6
- Add a prop to sliders, `allow_direct_input`, that can be used to disable the inputs rendered with sliders.
- Improve CSS styles in calendar when looking at selected dates outside the current calendar month (`show_outside_days=True`)
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

## Project: [dask/dask](https://www.dask.org/), 5 releases: ['2026.1.2', '2025.3.1', '2025.9.2', '2026.1.1', '2026.1.0']
### Release: dask [2026.1.2](https://github.com/dask/dask/releases/tag/2026.1.2)
## Changes

- Require PyArrow >=16 @crusaderky (#12258)
- Better CPU affinity detection @crusaderky (#12221)
- Bump conda-incubator/setup-miniconda from 3.2.0 to 3.3.0 @[dependabot[bot]](https://github.com/apps/dependabot) (#12256)
- Run test suite with xarray but without zarr @crusaderky (#12254)
- Add 2025.9.2 backport to changelog @jacobtomlinson (#12253)
- change `zarr_read_kwargs` to `mode` argument @melonora (#12205)
- Ignore deprecationwarning on np.fix @TomAugspurger (#12248)
- Doctest fixes @TomAugspurger (#12246)
- Set the integer size in `test_merge_groupby_to_frame` @TomAugspurger (#12244)
- Update map\_meta test @TomAugspurger (#12243)
- Pin to sphinx\<9 until it's supported in sphinx-autosummary-accessors @jacobtomlinson (#12242)  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

### Release: dask [2025.3.1](https://github.com/dask/dask/releases/tag/2025.3.1)
## Changes

* No changes  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

### Release: dask [2025.9.2](https://github.com/dask/dask/releases/tag/2025.9.2)
## Changes

* No changes  

See the [Changelog](https://docs.dask.org/en/stable/changelog.html) for more information.

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

## Project: [delta-io/delta-rs](https://delta-io.github.io/delta-rs/usage/installation/), 3 releases: ['python-v1.4.0', 'python-v1.3.2', 'python-v1.3.1: read support deletion vectors, column mapping']
### Release: delta-rs [python-v1.4.0](https://github.com/delta-io/delta-rs/releases/tag/python-v1.4.0)
## What's Changed
* fix: report failed data in data checks by @roeap in https://github.com/delta-io/delta-rs/pull/4083
* refactor!: more logical writes by @roeap in https://github.com/delta-io/delta-rs/pull/4090
* chore(deps): update foyer requirement from 0.20.0 to 0.22.2 by @dependabot[bot] in https://github.com/delta-io/delta-rs/pull/4095
* fix: properly simplify delete predicate expressions for Datafusion by @rtyler in https://github.com/delta-io/delta-rs/pull/4098
* fix: add support for user names in azure URLs by @sebbegg in https://github.com/delta-io/delta-rs/pull/4100
* feat: enable deletion vector features for working with tables by @rtyler in https://github.com/delta-io/delta-rs/pull/4101
* fix(python): disable ident normalization in merge by @bellshun in https://github.com/delta-io/delta-rs/pull/4102
* feat: improve logical planning and migrate update op by @roeap in https://github.com/delta-io/delta-rs/pull/4096
* fix(python): object store registration missing in session by @JonatanMartens in https://github.com/delta-io/delta-rs/pull/4105
* refactor: avoid batch concatenation in write workers by @roeap in https://github.com/delta-io/delta-rs/pull/4107
* feat: centralize predicate parsing with literal coercion by @roeap in https://github.com/delta-io/delta-rs/pull/4106
* refactor: move normal and cdc writes into separate functions by @roeap in https://github.com/delta-io/delta-rs/pull/4108
* fix(datafusion): handle coalesced multi-file batches in next-scan by @ethan-tyler in https://github.com/delta-io/delta-rs/pull/4112
* refactor: move files scan to separate function by @roeap in https://github.com/delta-io/delta-rs/pull/4111
* feat: migrate delete by @roeap in https://github.com/delta-io/delta-rs/pull/4117
* chore: upgrade azurite and purge the need for a local az CLI to run tests by @rtyler in https://github.com/delta-io/delta-rs/pull/4121
* chore: allow integration tests to be run in parallel with nextest by @rtyler in https://github.com/delta-io/delta-rs/pull/4122
* chore(deps): upgrade datafusion to 52.0.0 by @ethan-tyler in https://github.com/delta-io/delta-rs/pull/4092
* chore: upgrade python version for the next release by @rtyler in https://github.com/delta-io/delta-rs/pull/4124

## New Contributors
* @sebbegg made their first contribution in https://github.com/delta-io/delta-rs/pull/4100
* @bellshun made their first contribution in https://github.com/delta-io/delta-rs/pull/4102
* @JonatanMartens made their first contribution in https://github.com/delta-io/delta-rs/pull/4105

**Full Changelog**: https://github.com/delta-io/delta-rs/compare/python-v1.3.2...python-v1.4.0
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
## Project: [rapidsai/cudf](https://docs.rapids.ai/api/cudf/stable/user_guide/10min/), 2 releases: ['v26.02.01', 'v26.02.00']
### Release: cudf [v26.02.01](https://github.com/rapidsai/cudf/releases/tag/v26.02.01)
<!-- Release notes generated using configuration in .github/release.yml at v26.02.01 -->

## What's Changed
### 🐛 Bug Fixes
* Backport #21301: Only serialize column slice by @pentschev in https://github.com/rapidsai/cudf/pull/21328


**Full Changelog**: https://github.com/rapidsai/cudf/compare/v26.02.00...v26.02.01
### Release: cudf [v26.02.00](https://github.com/rapidsai/cudf/releases/tag/v26.02.00)
<!-- Release notes generated using configuration in .github/release.yml at v26.02.00 -->

## What's Changed
### 🚨 Breaking Changes
* Avoid counting nulls and creating null mask in groupby aggregation `MERGE_M2` by @ttnghia in https://github.com/rapidsai/cudf/pull/20716
* Remove cudf::get_current_device_resource by @bdice in https://github.com/rapidsai/cudf/pull/20688
* Avoid creating null mask in groupby aggregation `M2` by @ttnghia in https://github.com/rapidsai/cudf/pull/20726
* Remove deprecated left semi- and anti- join APIs by @shrshi in https://github.com/rapidsai/cudf/pull/20668
* Inline and simplify some column methods by @vyasr in https://github.com/rapidsai/cudf/pull/20819
* Enable copy-on-write in cudf.pandas by @vyasr in https://github.com/rapidsai/cudf/pull/20401
* [FEA] Improve Null-Aware Operator Support in AST-Codegen by @lamarrr in https://github.com/rapidsai/cudf/pull/20206
* Remove legacy hash-combine logic and unify hashing with row hasher by @PointKernel in https://github.com/rapidsai/cudf/pull/20796
* Remove deprecated .from_pandas constructors by @mroeschke in https://github.com/rapidsai/cudf/pull/20925
* Remove deprecated Series.data by @mroeschke in https://github.com/rapidsai/cudf/pull/20914
* Remove all base attributes from ColumnBase by @vyasr in https://github.com/rapidsai/cudf/pull/20961
* Fix handling of unquoted strings in the CSV reader by @vuule in https://github.com/rapidsai/cudf/pull/20996
### 🐛 Bug Fixes
* Avoid duplicate streaming nodes for the rapidsmpf runtime by @rjzamora in https://github.com/rapidsai/cudf/pull/20586
* Handle scalar arguments in ternary expression by @Matt711 in https://github.com/rapidsai/cudf/pull/20600
* fix(noarch): use noarch build script in noarch build by @gforsyth in https://github.com/rapidsai/cudf/pull/20654
* fix(conda): matrix out noarch builds by cuda-major version by @gforsyth in https://github.com/rapidsai/cudf/pull/20678
* Include RMM in type checking environment and update type annotations for optional `stream` by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20636
* Add no-op path for `ArrowExtensionArray.astype` by @Matt711 in https://github.com/rapidsai/cudf/pull/20580
* Skip pytorch integration tests if CUDA is not available by @Matt711 in https://github.com/rapidsai/cudf/pull/20729
* Always delay CUDA Array Interface pointer access by @vyasr in https://github.com/rapidsai/cudf/pull/20719
* Fix various copy-on-write bugs by @vyasr in https://github.com/rapidsai/cudf/pull/20744
* Fix leaks in cuDF java tests by @abellina in https://github.com/rapidsai/cudf/pull/20767
* Fix plc.Scalar.from_py(datetime.datetime) incorrectly localizing naive datetimes by @mroeschke in https://github.com/rapidsai/cudf/pull/20769
* Don't remove double casts in cudf_polars by @mroeschke in https://github.com/rapidsai/cudf/pull/20773
* Fixes struct column handling in sort-merge joins by @shrshi in https://github.com/rapidsai/cudf/pull/20664
* Fix for `synccheck` compute-sanitizer errors across Parquet gtest by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20775
* Pin `numpy<2.4.0a0` in mypy pre-commit environment by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20781
* Raise when trying to run queries on different devices in same process by @wence- in https://github.com/rapidsai/cudf/pull/20617
* Ensure `min_periods=0` is passed through rolling aggregations by @Matt711 in https://github.com/rapidsai/cudf/pull/20653
* Fix racecheck errors in the ORC reader by @vuule in https://github.com/rapidsai/cudf/pull/20792
* Fix the crash of multi-threaded parquet reader benchmark by @kingcrimsontianyu in https://github.com/rapidsai/cudf/pull/20783
* Fix racecheck reported by DATA_CHUNK_SOURCE_TEST in inflate_kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20804
* Fix racecheck in the gpu_debrotli_kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20806
* Ensure literal groupby aggregations are broadcasted to key length in cudf_polars by @mroeschke in https://github.com/rapidsai/cudf/pull/20776
* Pin `aiobotocore<3` to fix CI failures by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20844
* Fix racecheck in parquet decode_page_data_generic kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20850
* Avoid generating empty `TableChunks` in streaming scan nodes by @rjzamora in https://github.com/rapidsai/cudf/pull/20815
* Fix dask imports in ``CudfFusedParquetIOHost`` by @rjzamora in https://github.com/rapidsai/cudf/pull/20845
* Fix UB due to OOM Exception in ParquetReaderTest.ManyLargeLists by @lamarrr in https://github.com/rapidsai/cudf/pull/20841
* Fix racecheck/synccheck in JSON parse_fn_string_parallel kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20856
* Fix racecheck in ORC decode_column_data_kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20853
* Disable flatbuffers tests in CMake configuration by @bdice in https://github.com/rapidsai/cudf/pull/20848
* Upper bound on aiosqlite in polars-upstream job by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20866
* Fix boolean casting consistency with Pandas (#20746) by @aryansri05 in https://github.com/rapidsai/cudf/pull/20747
* Add retries to requests made to PyPI's JSON API by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20865
* Fix `size_type` overflow in multiple APIs by @vuule in https://github.com/rapidsai/cudf/pull/20857
* Fix racecheck in parquet compute_string_page_bounds_kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20868
* Fix dictionary::encode to honor indices-type parameter by @davidwendt in https://github.com/rapidsai/cudf/pull/20842
* Add missing headers to row_ir.hpp, row_ir.cpp by @bdice in https://github.com/rapidsai/cudf/pull/20834
* Fix `parquet_options` in pdsh benchmark by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20893
* Add stream synchronize to tdigest generate_group_cluster_info by @davidwendt in https://github.com/rapidsai/cudf/pull/20846
* Only install RMM in mypy env on linux by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20878
* Make nvcomp export unconditional by @vyasr in https://github.com/rapidsai/cudf/pull/20828
* Ensure we have nvjitlink from the CUDA version used at build time or newer and upgrade numba-cuda lower bound by @bdice in https://github.com/rapidsai/cudf/pull/20873
* Fix size_type overflow in the ORC writer by @vuule in https://github.com/rapidsai/cudf/pull/20889
* Constrain pyparsing version by @vyasr in https://github.com/rapidsai/cudf/pull/20935
* Revert #20902 by @vyasr in https://github.com/rapidsai/cudf/pull/20955
* Add force-blocking-launches to run_compute_sanitizer_test script by @davidwendt in https://github.com/rapidsai/cudf/pull/20962
* Fix racecheck error in parquet delta_byte_array_decoder::string_scan by @davidwendt in https://github.com/rapidsai/cudf/pull/20967
* Fix racechecks reported in parquet gpuEncodePages kernel by @davidwendt in https://github.com/rapidsai/cudf/pull/20975
* Don't encode s3 paths for kvikio_remote_io in read_json by @mroeschke in https://github.com/rapidsai/cudf/pull/20976
* Allow sort merge join to go above int32 output row limits by @revans2 in https://github.com/rapidsai/cudf/pull/20960
* Correct stream ordered deallocation in `Join` by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20981
* Reintroduce `Buffer.nbytes` property by @pentschev in https://github.com/rapidsai/cudf/pull/21027
* Fix SHA hash OOB on strings that are exact multiples of message chunk size by @rishic3 in https://github.com/rapidsai/cudf/pull/21004
* Temporarily disable IWYU for nightly tests by @davidwendt in https://github.com/rapidsai/cudf/pull/21045
* Fix cudf-polars multi-partition distributed sort by @TomAugspurger in https://github.com/rapidsai/cudf/pull/21047
* Backport #21051 by @wence- in https://github.com/rapidsai/cudf/pull/21086
* Pin pandas for `pylibcudf` testing by @galipremsagar in https://github.com/rapidsai/cudf/pull/21124
* Hide pinned pool instantiation to avoid symbol conflicts with nvcomp by @vyasr in https://github.com/rapidsai/cudf/pull/21161
* Specialize field type checking for bool in Parquet thrift list decoder by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/21144
* Fix reading of CSV files with double quotes in unquoted strings by @vuule in https://github.com/rapidsai/cudf/pull/21151
* Revert the multithreaded optimization in the CSV reader by @vuule in https://github.com/rapidsai/cudf/pull/21198
* Pin sqlglot in third-party integration tests by @Matt711 in https://github.com/rapidsai/cudf/pull/21271
* Exclude sqlglot version 28.7 from CI by @Matt711 in https://github.com/rapidsai/cudf/pull/21293
### 📖 Documentation
* Add note to developer guide about null values being undefined by @bdice in https://github.com/rapidsai/cudf/pull/20645
* [DOC] Add cudf-polars to the example build command by @Matt711 in https://github.com/rapidsai/cudf/pull/20763
* Clarify internal API header placement guidelines for details headers by @PointKernel in https://github.com/rapidsai/cudf/pull/20985
* Clarify deprecation message for cudf::round by @nirandaperera in https://github.com/rapidsai/cudf/pull/20809
* Require nvcc 12.9 in contributing guide by @bdice in https://github.com/rapidsai/cudf/pull/21186
### 🚀 New Features
* Expose `cudf::compute_column_jit` to python by @Matt711 in https://github.com/rapidsai/cudf/pull/20697
* Add configuration option for max-io-threads by @quasiben in https://github.com/rapidsai/cudf/pull/20606
* Return stats from `lower_ir_graph` by @rjzamora in https://github.com/rapidsai/cudf/pull/20528
* Promote join_kind from detail namespace to public by @PointKernel in https://github.com/rapidsai/cudf/pull/20703
* Make DataFrameScan and DataFrameSourceInfo pickle-able by @rjzamora in https://github.com/rapidsai/cudf/pull/20732
* Add compute-sanitizer dispatch action by @bdice in https://github.com/rapidsai/cudf/pull/20542
* Add RapidsMPF AllGather manager to cudf-polars by @rjzamora in https://github.com/rapidsai/cudf/pull/20731
* Use metadata channel for the "rapidsmpf" runtime by @rjzamora in https://github.com/rapidsai/cudf/pull/20738
* Enable distributed execution with the "rapidsmpf" runtime by @rjzamora in https://github.com/rapidsai/cudf/pull/20662
* Filter row groups using byte range in the new experimental parquet reader by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20733
* Make row hasher 64-bit hashing compatible by @PointKernel in https://github.com/rapidsai/cudf/pull/20777
* Expose parquet JIT filter option to python by @Matt711 in https://github.com/rapidsai/cudf/pull/20790
* Add filter_join_indices by @PointKernel in https://github.com/rapidsai/cudf/pull/20385
* Add support for topk aggregation in libcudf groupby by @davidwendt in https://github.com/rapidsai/cudf/pull/20632
* Allow parquet readers to use existing `datasource`s and `metadata`s by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20693
* Reader and writer for a simple CudfTable format by @vuule in https://github.com/rapidsai/cudf/pull/20811
* Add support for dictionary types in the row hasher by @PointKernel in https://github.com/rapidsai/cudf/pull/20989
* Support left joins using sort-merge algorithm by @shrshi in https://github.com/rapidsai/cudf/pull/20787
* Implement `batch_null_count` to count nulls for multiple null masks by a single kernel call, and application in groupby aggregations by @ttnghia in https://github.com/rapidsai/cudf/pull/20872
* Support multiple roaring bitmap deletion vectors in parquet readers by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20840
* Add approx_distinct_count by @PointKernel in https://github.com/rapidsai/cudf/pull/20735
* Pin Polars>=1.30,<1.36 by @Matt711 in https://github.com/rapidsai/cudf/pull/20791
* Support `is_compressed` V2 flag in the Parquet writer by @vuule in https://github.com/rapidsai/cudf/pull/21050
* Example to demonstrate intra-parquet-file pipelining using hybrid scan APIs by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20918
### 🛠️ Improvements
* feat(conda): build noarch python packages separately by @gforsyth in https://github.com/rapidsai/cudf/pull/20613
* Fix rapidsmpf dependency updates by @bdice in https://github.com/rapidsai/cudf/pull/20624
* Print duckDB query plan and change Q17 join type by @Matt711 in https://github.com/rapidsai/cudf/pull/20615
* Update RapidsMPF imports  by @madsbk in https://github.com/rapidsai/cudf/pull/20665
* Forward-merge release/25.12 into main by @bdice in https://github.com/rapidsai/cudf/pull/20676
* Remove cudfjar install target by @vyasr in https://github.com/rapidsai/cudf/pull/20670
* Use `RAPIDS_BRANCH` in cmake-format invocations that need rapids-cmake configs by @bdice in https://github.com/rapidsai/cudf/pull/20415
* Merge release/25.12 into main by @vyasr in https://github.com/rapidsai/cudf/pull/20706
* Use strict priority in CI conda tests by @bdice in https://github.com/rapidsai/cudf/pull/20690
* Minor improvements to pylibcudf recipe by @bdice in https://github.com/rapidsai/cudf/pull/20684
* Remove unnecessary nanoarrow fetch by @vyasr in https://github.com/rapidsai/cudf/pull/20669
* Revert pytest pin by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20643
* Use real row-group sample to estimate partition size by @rjzamora in https://github.com/rapidsai/cudf/pull/20567
* Move rapidsmpf-specific testing in cudf-polars by @rjzamora in https://github.com/rapidsai/cudf/pull/20695
* Include thrust::pair headers by @bdice in https://github.com/rapidsai/cudf/pull/20708
* Remove sccache calls in noarch builds by @vyasr in https://github.com/rapidsai/cudf/pull/20710
* Replace rmm::mr::get_current_device_resource() with cudf::get_current_device_resource_ref() by @davidwendt in https://github.com/rapidsai/cudf/pull/20694
* Improved implementation for get_mask_offset_word utility by @davidwendt in https://github.com/rapidsai/cudf/pull/20622
* Remove unneeded cudaMemcpy() calls by @davidwendt in https://github.com/rapidsai/cudf/pull/20618
* Simplify broadcast-join algorithm in cudf-polars by @rjzamora in https://github.com/rapidsai/cudf/pull/20724
* Add spilling support to staged fanout chunks by @rjzamora in https://github.com/rapidsai/cudf/pull/20642
* Use rapidsmpf ShufflerAsync by @rjzamora in https://github.com/rapidsai/cudf/pull/20701
* Move thrust::tuple usages to cuda::std::tuple by @davidwendt in https://github.com/rapidsai/cudf/pull/20717
* Add job-specific timeouts to GHA test jobs by @bdice in https://github.com/rapidsai/cudf/pull/20730
* Compatibility updates for CCCL 3.2 by @bdice in https://github.com/rapidsai/cudf/pull/20725
* Move googlebench benchmarks to nvbench by @davidwendt in https://github.com/rapidsai/cudf/pull/20698
* Enable blocking mechanism to avoid proxy object transfers in `cudf.pandas` by @galipremsagar in https://github.com/rapidsai/cudf/pull/19805
* Remove googlebench dependency for libcudf by @davidwendt in https://github.com/rapidsai/cudf/pull/20739
* Upgrade nanoarrow by @vyasr in https://github.com/rapidsai/cudf/pull/20711
* Improve local pandas testing experience by @vyasr in https://github.com/rapidsai/cudf/pull/20753
* Use .plc_column instead of .to_pylibcudf in IO methods by @mroeschke in https://github.com/rapidsai/cudf/pull/20742
* Use .plc_column instead of .to_pylibcudf in indexing_utils, public objects by @mroeschke in https://github.com/rapidsai/cudf/pull/20758
* Add back previously failing json test with stream by @vyasr in https://github.com/rapidsai/cudf/pull/19865
* Add libcudf dictionary encode benchmark by @davidwendt in https://github.com/rapidsai/cudf/pull/20696
* Remove unneeded aggregation kind_to_type utility and macro by @davidwendt in https://github.com/rapidsai/cudf/pull/20682
* Test copy-on-write in CI by @vyasr in https://github.com/rapidsai/cudf/pull/20745
* Stop using Dtype annotation more internally in cudf classic by @mroeschke in https://github.com/rapidsai/cudf/pull/20760
* Parquet: Only fill in null values for string lengths and list offsets by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20671
* Enable mypy's disallow_untyped_defs = true in cudf.core.column.* by @mroeschke in https://github.com/rapidsai/cudf/pull/20759
* Improve groupby test utils to include the original location of failure by @ttnghia in https://github.com/rapidsai/cudf/pull/20718
* use CUDA 13 for third-party integration tests by @jameslamb in https://github.com/rapidsai/cudf/pull/20748
* Use strict priority in CI conda tests by @bdice in https://github.com/rapidsai/cudf/pull/20772
* Upgrade to nvcomp 5.1.0.21 by @bdice in https://github.com/rapidsai/cudf/pull/20770
* Use RapidsMPF's `reserve_device_memory_and_spill()` by @madsbk in https://github.com/rapidsai/cudf/pull/20778
* avoid passing `start` as keyword argument to `np.arange` by @jorenham in https://github.com/rapidsai/cudf/pull/20788
* Use env var to disable long tests when run with racecheck by @davidwendt in https://github.com/rapidsai/cudf/pull/20755
* Improve performance for small string gather by @tgujar in https://github.com/rapidsai/cudf/pull/20656
* Deprecate sort-merge join functional APIs by @shrshi in https://github.com/rapidsai/cudf/pull/20785
* Partially revert broadcast-join change by @rjzamora in https://github.com/rapidsai/cudf/pull/20779
* Type checking compatibility for numpy 2.4.0rc1 and other fixes by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20795
* Support pl.Expr.cast(strict=False) in cudf_polars by @mroeschke in https://github.com/rapidsai/cudf/pull/20784
* chore(noarch): standardize noarch artifact naming by @gforsyth in https://github.com/rapidsai/cudf/pull/20794
* Remove alpha specs from non-RAPIDS dependencies by @bdice in https://github.com/rapidsai/cudf/pull/20797
* Enable merge barriers by @KyleFromNVIDIA in https://github.com/rapidsai/cudf/pull/20813
* Update to numba-cuda `>=0.22.1,<0.23.0` by @brandon-b-miller in https://github.com/rapidsai/cudf/pull/20750
* Enable using multithreaded `setup_page_index` in hybrid scan reader by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20721
* Remove size and offsets from Column by @vyasr in https://github.com/rapidsai/cudf/pull/20824
* Add devcontainer fallback for C++ test location by @bdice in https://github.com/rapidsai/cudf/pull/20838
* Add cudf-polars option to control rapidsmpf Shuffle insertion method by @TomAugspurger in https://github.com/rapidsai/cudf/pull/19634
* Make null_count delegate to plc_column by @vyasr in https://github.com/rapidsai/cudf/pull/20854
* Replace thrust reductions in Parquet reader with CUB + pinned memory based implementations by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20821
* Reduce stream synchronization in `(mutable_)column_device_view::create()` and `(mutable_)table_device_view::create()` by @ttnghia in https://github.com/rapidsai/cudf/pull/20852
* Clean up hash-based groupby aggregation, reducing overhead and memory usage by @ttnghia in https://github.com/rapidsai/cudf/pull/20658
* Support decomposing Len expressions in cudf_polars streaming executor by @mroeschke in https://github.com/rapidsai/cudf/pull/20786
* Add parameter to disable native `read_parquet` node by @rjzamora in https://github.com/rapidsai/cudf/pull/20858
* Support arbitrary span-like data storage in pylibcudf Column by @vyasr in https://github.com/rapidsai/cudf/pull/20869
* Merge ExposureTrackedBuffer into Buffer to simplify class hierarchy by @vyasr in https://github.com/rapidsai/cudf/pull/20874
* Replace thrust logical functions with CUB + pinned memory based implementations in Parquet reader by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20822
* Sync stream in host_memory.cpp by @bdice in https://github.com/rapidsai/cudf/pull/20687
* Remove extra syncthreads() call from ORC DecodeRowPositions device function by @davidwendt in https://github.com/rapidsai/cudf/pull/20867
* Temporarily increase max_days_without_success for nightly CI check by @bdice in https://github.com/rapidsai/cudf/pull/20880
* Add zstd kernels to compute-sanitizer filter parameter by @davidwendt in https://github.com/rapidsai/cudf/pull/20875
* Replace `thrust::reduce_by_key` with CUB + pinned memory based wrapper by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20860
* cuml 26.2.0 compatibility by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20883
* Implement pandas 3.0, backward compatible changes by @mroeschke in https://github.com/rapidsai/cudf/pull/20803
* Improve column selection in the new experimental parquet reader by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20604
* Fix some gtests to not assume dictionary keys order by @davidwendt in https://github.com/rapidsai/cudf/pull/20827
* Parquet decode: Skip up to first_row for non-lists by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20835
* Disable DeeplyNestedArithmeticLogicalExpression jit gtest for driver < 12.9 by @davidwendt in https://github.com/rapidsai/cudf/pull/20894
* Make base_data and base_mask passthroughs by @vyasr in https://github.com/rapidsai/cudf/pull/20896
* Changes needed for CCCL 3.2 compatibility by @bdice in https://github.com/rapidsai/cudf/pull/20810
* Modify the default pinned pool to allow growth when the pool is exhausted by @vuule in https://github.com/rapidsai/cudf/pull/20839
* Empty commit to trigger a build by @bdice in https://github.com/rapidsai/cudf/pull/20922
* Fix clang-tidy errors by @vyasr in https://github.com/rapidsai/cudf/pull/20929
* Replace thrust `count_if` and `copy_if` with CUB + pinned memory based wrappers by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20861
* Parquet: Reuse string offset preprocessing when allocating output memory by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20902
* Clean up includes for rmm::mr::polymorphic_allocator by @bdice in https://github.com/rapidsai/cudf/pull/20371
* Convert to plc_column wherever possible by @vyasr in https://github.com/rapidsai/cudf/pull/20940
* Push more arrow conversion logic down to pylibcudf by @vyasr in https://github.com/rapidsai/cudf/pull/20919
* Simplify categorical column by @vyasr in https://github.com/rapidsai/cudf/pull/20942
* Remove get_ptr from buffer owner classes by @vyasr in https://github.com/rapidsai/cudf/pull/20949
* Fix null counts in mutating pylibcudf operations by @vyasr in https://github.com/rapidsai/cudf/pull/20950
* Add context manager to control access mode by @vyasr in https://github.com/rapidsai/cudf/pull/20952
* Convert column children computation from lazy to eager by @vyasr in https://github.com/rapidsai/cudf/pull/20953
* Use SPDX license identifiers in pyproject.toml, bump build dependency floors by @jameslamb in https://github.com/rapidsai/cudf/pull/20959
* Compatibility for cuML deprecation warnings by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20884
* Use larger node for cpp-linters job in nightly tests by @vyasr in https://github.com/rapidsai/cudf/pull/20963
* Fix min/max reduction logic for dictionary columns by @davidwendt in https://github.com/rapidsai/cudf/pull/20847
* Remove null masks for intermediate results when computing compound hash-based groupby aggregations by @ttnghia in https://github.com/rapidsai/cudf/pull/20736
* Fix warnings in dask-cudf test suite by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20951
* Add CUDA 13.1 support by @bdice in https://github.com/rapidsai/cudf/pull/20870
* Enable spill lock acquisition via context by @vyasr in https://github.com/rapidsai/cudf/pull/20964
* Restore string preprocess PR and fix memcheck by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/20969
* Enable sccache-dist for cpp-linters by @vyasr in https://github.com/rapidsai/cudf/pull/20968
* [pre-commit.ci] pre-commit autoupdate by @pre-commit-ci[bot] in https://github.com/rapidsai/cudf/pull/20971
* Clean up mixed join common utilities by @PointKernel in https://github.com/rapidsai/cudf/pull/20836
* Disable TRANSPOSE_TEST checking logic for CI racecheck runs by @davidwendt in https://github.com/rapidsai/cudf/pull/20970
* Use nosync execution policy everywhere by @bdice in https://github.com/rapidsai/cudf/pull/20807
* Remove `cuda.core.experimental` warnings filters by @brandon-b-miller in https://github.com/rapidsai/cudf/pull/20933
* Implement more flexible runtime to compile-time dispatching by @vyasr in https://github.com/rapidsai/cudf/pull/20927
* Use per-column context in place of acquire_spill_lock by @vyasr in https://github.com/rapidsai/cudf/pull/20977
* Fix cudf::clamp() for dictionary column types by @davidwendt in https://github.com/rapidsai/cudf/pull/20898
* Patch installed pandas for cudf.pandas, pandas unit test run with CoW fix by @mroeschke in https://github.com/rapidsai/cudf/pull/20973
* build and test against CUDA 13.1.0 by @jameslamb in https://github.com/rapidsai/cudf/pull/20972
* Add ``opaque_reservation`` utility by @rjzamora in https://github.com/rapidsai/cudf/pull/20885
* Remove exposure on column construction and unwrap buffers on pylibcudf conversion by @vyasr in https://github.com/rapidsai/cudf/pull/20980
* Apply nosync execution policy in tests, benchmarks, Python, Java, and add docs by @bdice in https://github.com/rapidsai/cudf/pull/20978
* Use `D` instead of `d` for time units by @galipremsagar in https://github.com/rapidsai/cudf/pull/20910
* Add missing standard library headers to groupby/hash and jit files by @bdice in https://github.com/rapidsai/cudf/pull/20982
* Add in key remapping for improved sort merge join performance by @revans2 in https://github.com/rapidsai/cudf/pull/20826
* Use pinned memory in PQ reader to avoid pageable copies by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20820
* Add Hybrid scan APIs for single-step table materialization by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/20906
* Add utility for deferring allocations on a stream by @TomAugspurger in https://github.com/rapidsai/cudf/pull/20987
* Remove CUDF_EXPORT from cudf::detail::contains by @davidwendt in https://github.com/rapidsai/cudf/pull/20991
* Restrict objects that construct cuDF Python Buffer  by @mroeschke in https://github.com/rapidsai/cudf/pull/20983
* Fix min/max groupby logic for dictionary columns by @davidwendt in https://github.com/rapidsai/cudf/pull/20887
* Centralize cudf Column creation as much as possible by @vyasr in https://github.com/rapidsai/cudf/pull/20999
* Empty commit to trigger a build by @jameslamb in https://github.com/rapidsai/cudf/pull/21014
* Rearrange variables to reduce padding by @pmattione-nvidia in https://github.com/rapidsai/cudf/pull/21016
* Clean up buffer and access context implementations by @vyasr in https://github.com/rapidsai/cudf/pull/21013
* Add missing thrust/tuple.h include for thrust::tie by @bdice in https://github.com/rapidsai/cudf/pull/21009
* Replace remaining small pageable copies in PQ reader with pinned by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/21006
* Add dictionary specialization to row comparators by @davidwendt in https://github.com/rapidsai/cudf/pull/20830
* Add no_sanitizer filter to compute-sanitizer script by @davidwendt in https://github.com/rapidsai/cudf/pull/20992
* Make test_json_writer compatible with pandas 3 by @mroeschke in https://github.com/rapidsai/cudf/pull/21015
* Use main shared-workflows branch by @jameslamb in https://github.com/rapidsai/cudf/pull/21038
* Improve usage of polymorphism in columns by @vyasr in https://github.com/rapidsai/cudf/pull/21030
* Increase memcheck timeout in nightly test script by @davidwendt in https://github.com/rapidsai/cudf/pull/21040
* wheel builds: react to changes in pip's handling of build constraints by @mmccarty in https://github.com/rapidsai/cudf/pull/21048
* Stop using non-pylibcudf children by @vyasr in https://github.com/rapidsai/cudf/pull/21057
* Backport #21033: Add new pinned vector factory functions by @mhaseeb123 in https://github.com/rapidsai/cudf/pull/21106
* Use a multi-level host thread pool to avoid deadlocks by @vuule in https://github.com/rapidsai/cudf/pull/21075
* fix(build): build package on merge to `release/*` branch by @gforsyth in https://github.com/rapidsai/cudf/pull/21181
* Fallback to numba-cuda with no extra CUDA packages if 'cuda_suffixed' isn't true by @trxcllnt in https://github.com/rapidsai/cudf/pull/21185

## New Contributors
* @jorenham made their first contribution in https://github.com/rapidsai/cudf/pull/20788
* @nirandaperera made their first contribution in https://github.com/rapidsai/cudf/pull/20809
* @rishic3 made their first contribution in https://github.com/rapidsai/cudf/pull/21004

**Full Changelog**: https://github.com/rapidsai/cudf/compare/v26.02.00a...v26.02.00
## Project: [lancedb/lance](https://lancedb.github.io/lance/), 16 releases: ['v3.0.0-beta.2', 'v2.0.0', 'v3.0.0-beta.1', 'v2.0.0-rc.4', 'v2.0.0-rc.3', 'v1.0.4', 'v1.0.4-rc.1', 'v2.0.0-rc.2', 'v1.0.3', 'v1.0.3-rc.1', 'v2.0.0-rc.1', 'v2.0.0-beta.10', 'v2.0.0-beta.9', 'v1.0.2', 'v2.0.0-beta.8', 'v1.0.2-rc.2']
### Release: lance [v3.0.0-beta.2](https://github.com/lance-format/lance/releases/tag/v3.0.0-beta.2)
<!-- Release notes generated using configuration in .github/release.yml at v3.0.0-beta.2 -->

## What's Changed
### Critical Fixes ‼️
* fix: deduplicate row addresses in take to prevent panic by @wjones127 in https://github.com/lance-format/lance/pull/5881
* fix: fts flat search drops rows when avg_doc_length < 1.0 by @wjones127 in https://github.com/lance-format/lance/pull/5897
### New Features 🎉
* feat: add RLE support for block by @yingjianwu98 in https://github.com/lance-format/lance/pull/4937
* feat: dictionary index always32 bits by @yingjianwu98 in https://github.com/lance-format/lance/pull/5011
* feat: abort dictionary encode if not useful by @yingjianwu98 in https://github.com/lance-format/lance/pull/5055
* feat(cdf): cdf support upsert for views by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5369
* feat(compaction): binary copy capability for compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5434
* feat: add alter column nullable to non-nullable support by @Xuanwo in https://github.com/lance-format/lance/pull/5589
* feat: evolute all_null_layout to constant layout by @Xuanwo in https://github.com/lance-format/lance/pull/5641
* feat(java): support building vector index distributively by @majin1102 in https://github.com/lance-format/lance/pull/5664
* feat(rust): add datafusion catalog_provider through namespace by @majin1102 in https://github.com/lance-format/lance/pull/5686
* feat: support List and Struct type for KeyValue in inserted_rows.rs by @wojiaodoubao in https://github.com/lance-format/lance/pull/5713
* feat: support tencent cos by @ztorchan in https://github.com/lance-format/lance/pull/5740
* feat: add Lance-HF docs to lance.org/integrations/huggingface/ by @prrao87 in https://github.com/lance-format/lance/pull/5748
* feat(python): support namespace for tensorflow by @yuqi1129 in https://github.com/lance-format/lance/pull/5750
* feat(java): support json extraction by scanning by @majin1102 in https://github.com/lance-format/lance/pull/5770
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
* feat: add plan/execute separation to FilteredReadExec by @LuQQiu in https://github.com/lance-format/lance/pull/5843
### Bug Fixes 🐛
* fix: support system columns in dataset.take* operations by @hamersaw in https://github.com/lance-format/lance/pull/5722
* fix: skip missing indices in compaction rewrite by @AndreaBozzo in https://github.com/lance-format/lance/pull/5739
* fix(lance-linalg): check fp16kernels feature before arch-specific code by @durch in https://github.com/lance-format/lance/pull/5747
* refactor: align blob behavior that write via file format version, read via layout by @Xuanwo in https://github.com/lance-format/lance/pull/5752
* fix: fix deletion when using file-object-store:// by @cmccabe in https://github.com/lance-format/lance/pull/5760
* fix: remove unreasonable nullable check for data types in hash_joiner during merge operation by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5784
* fix: allow unused_unsafe for __cpuid to support both stable and nightly by @jackye1995 in https://github.com/lance-format/lance/pull/5793
* fix: set JUnit dependency as test scope by @bryanck in https://github.com/lance-format/lance/pull/5815
* fix: fix remap so that it handles deletions correctly by @westonpace in https://github.com/lance-format/lance/pull/5828
* fix: inconsistent transposed pq code and metadata when build ivf_pq index distributedly by @yanghua in https://github.com/lance-format/lance/pull/5834
* fix(java): panic when reading CreateIndex transaction by @majin1102 in https://github.com/lance-format/lance/pull/5853
* fix: fix mini-block dictionary bitpacking panic by @Xuanwo in https://github.com/lance-format/lance/pull/5860
* fix: fix boolean inline constant decoding by @Xuanwo in https://github.com/lance-format/lance/pull/5862
* fix: open additional storage options provider related apis in lance dataset by @jackye1995 in https://github.com/lance-format/lance/pull/5869
* fix: flaky test test_ann_prefilter for HNSW by @BubbleCal in https://github.com/lance-format/lance/pull/5870
* fix(java): init allocator for new dataset when checkout branch/tag by @fangbo in https://github.com/lance-format/lance/pull/5876
* fix: avoid panic when repdef serializes empty offsets by @fenfeng9 in https://github.com/lance-format/lance/pull/5890
* fix: avoid bitmap range panic on inverted bounds by @fenfeng9 in https://github.com/lance-format/lance/pull/5893
* fix: split index_statistics to reduce rustc query depth by @Xuanwo in https://github.com/lance-format/lance/pull/5894
### Documentation 📚
* docs: fix issues in HF integration docs by @prrao87 in https://github.com/lance-format/lance/pull/5778
* docs: fix MkDocs protobuf reference for ConstantLayout by @Xuanwo in https://github.com/lance-format/lance/pull/5833
* docs: add array type support by @XuQianJin-Stars in https://github.com/lance-format/lance/pull/5884
### Performance Improvements 🚀
* perf: add vector throughput benchmark by @westonpace in https://github.com/lance-format/lance/pull/5644
* perf: add a full text search benchmark by @westonpace in https://github.com/lance-format/lance/pull/5665
* perf: don't concat the batches for writing posting lists by @BubbleCal in https://github.com/lance-format/lance/pull/5769
* perf: add a lightweight scheduler implementation by @westonpace in https://github.com/lance-format/lance/pull/5773
* perf: use cpu pool to process all posting lists by @BubbleCal in https://github.com/lance-format/lance/pull/5780
* perf: calculate cardinality lazily by @Xuanwo in https://github.com/lance-format/lance/pull/5783
* perf: replace flatmap in build_distance_table by @wkalt in https://github.com/lance-format/lance/pull/5898
### Other Changes
* refactor: change reader's get_range result to be a static future by @westonpace in https://github.com/lance-format/lance/pull/5755
* refactor(python): migrate torch.jit.script to torch.compile by @wjones127 in https://github.com/lance-format/lance/pull/5759
* test: fix tests broken by pandas 3 release by @westonpace in https://github.com/lance-format/lance/pull/5786

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/3.0.0-beta.N...v3.0.0-beta.2
### Release: lance [v2.0.0](https://github.com/lance-format/lance/releases/tag/v2.0.0)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0 -->

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
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
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
* fix: allow unused_unsafe for __cpuid to support both stable and nightly by @jackye1995 in https://github.com/lance-format/lance/pull/5793
* fix: fix remap so that it handles deletions correctly by @westonpace in https://github.com/lance-format/lance/pull/5828
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
* refactor(python): migrate torch.jit.script to torch.compile by @wjones127 in https://github.com/lance-format/lance/pull/5759
* test: fix tests broken by pandas 3 release by @westonpace in https://github.com/lance-format/lance/pull/5786

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0
### Release: lance [v3.0.0-beta.1](https://github.com/lance-format/lance/releases/tag/v3.0.0-beta.1)
<!-- Release notes generated using configuration in .github/release.yml at v3.0.0-beta.1 -->

## What's Changed
### New Features 🎉
* feat: add RLE support for block by @yingjianwu98 in https://github.com/lance-format/lance/pull/4937
* feat: dictionary index always32 bits by @yingjianwu98 in https://github.com/lance-format/lance/pull/5011
* feat: abort dictionary encode if not useful by @yingjianwu98 in https://github.com/lance-format/lance/pull/5055
* feat(cdf): cdf support upsert for views by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5369
* feat(compaction): binary copy capability for compaction by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5434
* feat: add alter column nullable to non-nullable support by @Xuanwo in https://github.com/lance-format/lance/pull/5589
* feat: evolute all_null_layout to constant layout by @Xuanwo in https://github.com/lance-format/lance/pull/5641
* feat(java): support building vector index distributively by @majin1102 in https://github.com/lance-format/lance/pull/5664
* feat(rust): add datafusion catalog_provider through namespace by @majin1102 in https://github.com/lance-format/lance/pull/5686
* feat: support List and Struct type for KeyValue in inserted_rows.rs by @wojiaodoubao in https://github.com/lance-format/lance/pull/5713
* feat: support tencent cos by @ztorchan in https://github.com/lance-format/lance/pull/5740
* feat: add Lance-HF docs to lance.org/integrations/huggingface/ by @prrao87 in https://github.com/lance-format/lance/pull/5748
* feat(python): support namespace for tensorflow by @yuqi1129 in https://github.com/lance-format/lance/pull/5750
* feat(java): support json extraction by scanning by @majin1102 in https://github.com/lance-format/lance/pull/5770
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
* feat: add plan/execute separation to FilteredReadExec by @LuQQiu in https://github.com/lance-format/lance/pull/5843
### Bug Fixes 🐛
* fix: support system columns in dataset.take* operations by @hamersaw in https://github.com/lance-format/lance/pull/5722
* fix: skip missing indices in compaction rewrite by @AndreaBozzo in https://github.com/lance-format/lance/pull/5739
* fix(lance-linalg): check fp16kernels feature before arch-specific code by @durch in https://github.com/lance-format/lance/pull/5747
* refactor: align blob behavior that write via file format version, read via layout by @Xuanwo in https://github.com/lance-format/lance/pull/5752
* fix: fix deletion when using file-object-store:// by @cmccabe in https://github.com/lance-format/lance/pull/5760
* fix: remove unreasonable nullable check for data types in hash_joiner during merge operation by @zhangyue19921010 in https://github.com/lance-format/lance/pull/5784
* fix: allow unused_unsafe for __cpuid to support both stable and nightly by @jackye1995 in https://github.com/lance-format/lance/pull/5793
* fix: set JUnit dependency as test scope by @bryanck in https://github.com/lance-format/lance/pull/5815
* fix: fix remap so that it handles deletions correctly by @westonpace in https://github.com/lance-format/lance/pull/5828
* fix: inconsistent transposed pq code and metadata when build ivf_pq index distributedly by @yanghua in https://github.com/lance-format/lance/pull/5834
* fix(java): panic when reading CreateIndex transaction by @majin1102 in https://github.com/lance-format/lance/pull/5853
* fix: fix mini-block dictionary bitpacking panic by @Xuanwo in https://github.com/lance-format/lance/pull/5860
* fix: fix boolean inline constant decoding by @Xuanwo in https://github.com/lance-format/lance/pull/5862
* fix: flaky test test_ann_prefilter for HNSW by @BubbleCal in https://github.com/lance-format/lance/pull/5870
* fix(java): init allocator for new dataset when checkout branch/tag by @fangbo in https://github.com/lance-format/lance/pull/5876
### Documentation 📚
* docs: fix issues in HF integration docs by @prrao87 in https://github.com/lance-format/lance/pull/5778
* docs: fix MkDocs protobuf reference for ConstantLayout by @Xuanwo in https://github.com/lance-format/lance/pull/5833
### Performance Improvements 🚀
* perf: add vector throughput benchmark by @westonpace in https://github.com/lance-format/lance/pull/5644
* perf: add a full text search benchmark by @westonpace in https://github.com/lance-format/lance/pull/5665
* perf: don't concat the batches for writing posting lists by @BubbleCal in https://github.com/lance-format/lance/pull/5769
* perf: use cpu pool to process all posting lists by @BubbleCal in https://github.com/lance-format/lance/pull/5780
* perf: calculate cardinality lazily by @Xuanwo in https://github.com/lance-format/lance/pull/5783
### Other Changes
* refactor: change reader's get_range result to be a static future by @westonpace in https://github.com/lance-format/lance/pull/5755
* refactor(python): migrate torch.jit.script to torch.compile by @wjones127 in https://github.com/lance-format/lance/pull/5759
* test: fix tests broken by pandas 3 release by @westonpace in https://github.com/lance-format/lance/pull/5786

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/3.0.0-beta.N...v3.0.0-beta.1
### Release: lance [v2.0.0-rc.4](https://github.com/lance-format/lance/releases/tag/v2.0.0-rc.4)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-rc.4 -->

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
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
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
* fix: allow unused_unsafe for __cpuid to support both stable and nightly by @jackye1995 in https://github.com/lance-format/lance/pull/5793
* fix: fix remap so that it handles deletions correctly by @westonpace in https://github.com/lance-format/lance/pull/5828
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
* refactor(python): migrate torch.jit.script to torch.compile by @wjones127 in https://github.com/lance-format/lance/pull/5759
* test: fix tests broken by pandas 3 release by @westonpace in https://github.com/lance-format/lance/pull/5786

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-rc.4
### Release: lance [v2.0.0-rc.3](https://github.com/lance-format/lance/releases/tag/v2.0.0-rc.3)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-rc.3 -->

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
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
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
* fix: allow unused_unsafe for __cpuid to support both stable and nightly by @jackye1995 in https://github.com/lance-format/lance/pull/5793
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
* refactor(python): migrate torch.jit.script to torch.compile by @wjones127 in https://github.com/lance-format/lance/pull/5759
* test: fix tests broken by pandas 3 release by @westonpace in https://github.com/lance-format/lance/pull/5786

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-rc.3
### Release: lance [v1.0.4](https://github.com/lance-format/lance/releases/tag/v1.0.4)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.4 -->

## What's Changed
### New Features 🎉
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
### Bug Fixes 🐛
* fix: remove credential vending features from python and java bindings by @jackye1995 in https://github.com/lance-format/lance/pull/5737

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.3...v1.0.4
### Release: lance [v1.0.4-rc.1](https://github.com/lance-format/lance/releases/tag/v1.0.4-rc.1)
<!-- Release notes generated using configuration in .github/release.yml at v1.0.4-rc.1 -->

## What's Changed
### New Features 🎉
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
* feat: add blob handling support for fragment by @Xuanwo in https://github.com/lance-format/lance/pull/5801
### Bug Fixes 🐛
* fix: remove credential vending features from python and java bindings by @jackye1995 in https://github.com/lance-format/lance/pull/5737

**Full Changelog**: https://github.com/lance-format/lance/compare/v1.0.3...v1.0.4-rc.1
### Release: lance [v2.0.0-rc.2](https://github.com/lance-format/lance/releases/tag/v2.0.0-rc.2)
<!-- Release notes generated using configuration in .github/release.yml at v2.0.0-rc.2 -->

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
* feat: expose blob handling APIs to python by @Xuanwo in https://github.com/lance-format/lance/pull/5790
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
* fix: allow unused_unsafe for __cpuid to support both stable and nightly by @jackye1995 in https://github.com/lance-format/lance/pull/5793
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
* refactor(python): migrate torch.jit.script to torch.compile by @wjones127 in https://github.com/lance-format/lance/pull/5759
* test: fix tests broken by pandas 3 release by @westonpace in https://github.com/lance-format/lance/pull/5786

**Full Changelog**: https://github.com/lance-format/lance/compare/release-root/2.0.0-beta.N...v2.0.0-rc.2
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
## Project: [lancedb/lancedb](https://lancedb.github.io/lancedb/basic/), 8 releases: ['Node/Rust LanceDB v0.25.0-beta.0', 'Python LanceDB v0.28.0-beta.0', 'Node/Rust LanceDB v0.24.1', 'Python LanceDB v0.27.1', 'Node/Rust LanceDB v0.24.0', 'Python LanceDB v0.27.0', 'Node/Rust LanceDB v0.24.0-beta.0', 'Python LanceDB v0.27.0-beta.0']
### Release: lancedb [Node/Rust LanceDB v0.25.0-beta.0](https://github.com/lancedb/lancedb/releases/tag/v0.25.0-beta.0)
## 🎉 New Features

- feat: allow the permutation builder memory limit to be configured by env var by @westonpace in https://github.com/lancedb/lancedb/pull/2946
- feat(python): adding VoyageAI v4 models by @fzowl in https://github.com/lancedb/lancedb/pull/2959

## 🐛 Bug Fixes

- fix: support pydantic list of structs or optional struct by @eddyxu in https://github.com/lancedb/lancedb/pull/2953
- fix: don't store all columns in the permutation table by @westonpace in https://github.com/lancedb/lancedb/pull/2957
- fix(python): uses PIL incorrectly and may raise AttributeError by @ddupg in https://github.com/lancedb/lancedb/pull/2954
- fix(rust): support embeddings in create_empty_table by @Mesut-Doner in https://github.com/lancedb/lancedb/pull/2961
- fix(python): cancel remote queries on sync API interruption by @amanharshx in https://github.com/lancedb/lancedb/pull/2913
- fix: include _rowid in hash and calculated split projections by @wjones127 in https://github.com/lancedb/lancedb/pull/2965

## 📚 Documentation

- docs:  update REST API link in README.md by @kysshsy in https://github.com/lancedb/lancedb/pull/2906

## Other Changes

- refactor: modularize table.rs and extract delete logic by @ChinmayGowda71 in https://github.com/lancedb/lancedb/pull/2952


### Release: lancedb [Python LanceDB v0.28.0-beta.0](https://github.com/lancedb/lancedb/releases/tag/python-v0.28.0-beta.0)
## 🎉 New Features

- feat: allow the permutation builder memory limit to be configured by env var by @westonpace in https://github.com/lancedb/lancedb/pull/2946
- feat(python): adding VoyageAI v4 models by @fzowl in https://github.com/lancedb/lancedb/pull/2959

## 🐛 Bug Fixes

- fix: support pydantic list of structs or optional struct by @eddyxu in https://github.com/lancedb/lancedb/pull/2953
- fix: don't store all columns in the permutation table by @westonpace in https://github.com/lancedb/lancedb/pull/2957
- fix(python): uses PIL incorrectly and may raise AttributeError by @ddupg in https://github.com/lancedb/lancedb/pull/2954
- fix(rust): support embeddings in create_empty_table by @Mesut-Doner in https://github.com/lancedb/lancedb/pull/2961
- fix(python): cancel remote queries on sync API interruption by @amanharshx in https://github.com/lancedb/lancedb/pull/2913
- fix: include _rowid in hash and calculated split projections by @wjones127 in https://github.com/lancedb/lancedb/pull/2965

## 📚 Documentation

- docs:  update REST API link in README.md by @kysshsy in https://github.com/lancedb/lancedb/pull/2906

## Other Changes

- refactor: modularize table.rs and extract delete logic by @ChinmayGowda71 in https://github.com/lancedb/lancedb/pull/2952


### Release: lancedb [Node/Rust LanceDB v0.24.1](https://github.com/lancedb/lancedb/releases/tag/v0.24.1)
## 🎉 New Features

- feat: check AZURE_STORAGE_ACCOUNT_NAME in remote conns by @cmccabe in https://github.com/lancedb/lancedb/pull/2918
- feat: update lance dependency to v1.0.4 by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2944

## 🔧 Build and CI

- ci(rust): fix MSRV check by @wjones127 in https://github.com/lancedb/lancedb/pull/2940


### Release: lancedb [Python LanceDB v0.27.1](https://github.com/lancedb/lancedb/releases/tag/python-v0.27.1)
## 🎉 New Features

- feat: check AZURE_STORAGE_ACCOUNT_NAME in remote conns by @cmccabe in https://github.com/lancedb/lancedb/pull/2918
- feat: update lance dependency to v1.0.4 by @lancedb-robot in https://github.com/lancedb/lancedb/pull/2944

## 🔧 Build and CI

- ci(rust): fix MSRV check by @wjones127 in https://github.com/lancedb/lancedb/pull/2940


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


## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers?tab=readme-ov-file#datafusion-table-providers), 1 releases: ['v0.9.3']
### Release: datafusion-table-providers [v0.9.3](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.3)
## What's Changed
* Bump bb8 from 0.9.0 to 0.9.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/514
* Bump bytes from 1.10.1 to 1.11.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/515
* Bump arrow-schema from 57.0.0 to 57.2.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/524
* Bump insta from 1.43.2 to 1.46.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/523
* Update the README file to include a development section. by @hozan23 in https://github.com/datafusion-contrib/datafusion-table-providers/pull/526
* Prevent invalid INSERT statements with empty batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/528


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.2...v0.9.3
## Project: [duckdb/duckdb](https://duckdb.org/), 1 releases: ['v1.4.4 Bugfix Release']
### Release: duckdb [v1.4.4 Bugfix Release](https://github.com/duckdb/duckdb/releases/tag/v1.4.4)
This is a bug fix release for various issues discovered after we released 1.4.3. Please excuse the erroneous release earlier.

## What's Changed
* Cast Fix: Correctly handle negative exponent with a number with a decimal in VARCHAR -> INTEGER cast by @Mytherin in https://github.com/duckdb/duckdb/pull/20098
* [Storage] Fix NULL filter check for constant segments by @Tishj in https://github.com/duckdb/duckdb/pull/20103
* fixing staged upload for install.duckdb.org - hopefully by @hannes in https://github.com/duckdb/duckdb/pull/20104
* Remove undefined loop by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/20105
* [Test] Adjust concurrent attach-detach test to expect write-write conflict by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20108
* Fix ALIAS function in filter pushdown to preserve column aliases(#20008) by @henry8128 in https://github.com/duckdb/duckdb/pull/20106
* Headers missing from http logs by @samansmink in https://github.com/duckdb/duckdb/pull/20030
* Bumping httpfs to include https://github.com/duckdb/duckdb-httpfs/pull/174 by @carlopi in https://github.com/duckdb/duckdb/pull/20145
* Issue #20136: Secondary IGNORE NULLS by @hawkfish in https://github.com/duckdb/duckdb/pull/20153
* Fix minio nightly tests by @c-herrewijn in https://github.com/duckdb/duckdb/pull/20132
* Fix use-after-free in mode aggregate Combine function by @victor-ab in https://github.com/duckdb/duckdb/pull/20146
* Only pushdown varchar if the arrow type is not a string view by @evertlammerts in https://github.com/duckdb/duckdb/pull/20165
* Quote filters in adbc_get_objects by @evertlammerts in https://github.com/duckdb/duckdb/pull/20172
* Issue #20156: Streaming Window Unions by @hawkfish in https://github.com/duckdb/duckdb/pull/20191
* MergeInto: correctly clean-up buffer and handle non trivial GetData by @carlopi in https://github.com/duckdb/duckdb/pull/20163
* Fix extentension-ci-tools to latest release version in the v1.4-andium branch by @carlopi in https://github.com/duckdb/duckdb/pull/20227
* [Chore] Clean up CI nightly run to prevent time outs by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20150
* Bump Julia to v1.4.3 by @maiadegraaf in https://github.com/duckdb/duckdb/pull/20248
* Internal #6881: 2025c Time Zones by @hawkfish in https://github.com/duckdb/duckdb/pull/20258
* Split statements by semicolon by @Dtenwolde in https://github.com/duckdb/duckdb/pull/20174
* [chore] Remove `numeric_cast.hpp` import and other tidy stuff by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20278
* [chore] Reduce latency of VARCHAR index creation test by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20277
* Reuse correct table-level metadata during checkpoints by @ywelsch in https://github.com/duckdb/duckdb/pull/20267
* Fix view resolution not being stable if the referenced table lives in a different schema by @Tishj in https://github.com/duckdb/duckdb/pull/20260
* ConstantOrNullFunction input validity mask overwrite bugfix by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/20283
* dbgen: use TaskExecutor framework by @Mytherin in https://github.com/duckdb/duckdb/pull/20284
* fix(adbc): return error when setting an empty sql query by @gishor in https://github.com/duckdb/duckdb/pull/20071
* Bump iceberg, and add wasm platforms! by @carlopi in https://github.com/duckdb/duckdb/pull/20205
* _extension_distribution: Pin to `v1.4-andium` branch of extension-ci-tools by @carlopi in https://github.com/duckdb/duckdb/pull/20294
* Optimize prepared statement parameter lookups by @EtgarDev in https://github.com/duckdb/duckdb/pull/20252
* Update `VectorType` in `ComputePartitionIndices` by @lnkuiper in https://github.com/duckdb/duckdb/pull/20343
* Add some defensive programming in `RadixPartitionedHashTable::Combine` and `RadixPartitionedHashTable::Finalize` by @lnkuiper in https://github.com/duckdb/duckdb/pull/20342
* Increase reserved size for paths in SetPathsInternal by @Flogex in https://github.com/duckdb/duckdb/pull/20340
* Use UTF-16 console output in Windows shell (1.4) by @staticlibs in https://github.com/duckdb/duckdb/pull/20339
* Force repartitioning in `RadixPartitionedHashTable::Combine` by @lnkuiper in https://github.com/duckdb/duckdb/pull/20357
* Fixup comparison to wrong iterator on abdc's driver by @carlopi in https://github.com/duckdb/duckdb/pull/20360
* [chore] dsdgen generation signed integer overflow fix by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20279
* Give preference do variables set in config by @pdet in https://github.com/duckdb/duckdb/pull/20396
* Add QueryContext also to Write(void *buffer, idx_t nr_bytes), so that BytesWritten are updated also there by @carlopi in https://github.com/duckdb/duckdb/pull/20393
* Fix Issue #20233: fix function chain in qualify by @ArNine in https://github.com/duckdb/duckdb/pull/20302
* Backport client data cleanup by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20403
* Add v1.4.4 to Storage Version by @maiadegraaf in https://github.com/duckdb/duckdb/pull/20404
* Parquet Reader: Ignore invalid UTF8 in string stats, instead of throwing an error by @Mytherin in https://github.com/duckdb/duckdb/pull/20405
* Don't add a semicolon to final query when splitting statements by @Dtenwolde in https://github.com/duckdb/duckdb/pull/20401
* Fixup BRANCHES_TO_BE_CACHED, vars are not available on PRs, so env it is by @carlopi in https://github.com/duckdb/duckdb/pull/20411
* [Fix] Defensive infinite loop guard and UTF-8 check in C API by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20348
* Add ducklake, httpfs and iceberg tests so they are run in CI by @carlopi in https://github.com/duckdb/duckdb/pull/20319
* [Stats] `date_trunc` stat propagation fix by @Tishj in https://github.com/duckdb/duckdb/pull/20421
* Refactor allowed path sanitize by @hannes in https://github.com/duckdb/duckdb/pull/20346
* Issue #20413: ASOF SEMI/ANTI Bindings by @hawkfish in https://github.com/duckdb/duckdb/pull/20433
* Fix #20410: fix for RIGHT SEMI/ANTI - cannot fully label chain as found if there are non-equality predicates present in the join condition by @Mytherin in https://github.com/duckdb/duckdb/pull/20435
* [Fix] Misaligned size in ART prefix count by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20455
* Wrap ccache in own action by @carlopi in https://github.com/duckdb/duckdb/pull/20466
* [Chore] Add `ORDER BY` to `AS OF` test by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20465
* Fix segfault in hive partitioning with NULL values by @Schwarf in https://github.com/duckdb/duckdb/pull/20468
* Nightly test encryption fixes by @ccfelius in https://github.com/duckdb/duckdb/pull/20461
* [C API] Fix error data creation by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20451
* Skip concurrent_encrypted_attach due to race in autoloading httpfs by @carlopi in https://github.com/duckdb/duckdb/pull/20471
* CI fixup: Comparisons needs to be done via strings (since input via workflow_call is a string) by @carlopi in https://github.com/duckdb/duckdb/pull/20464
* Add unity_catalog to extensions built by duckdb/duckdb by @carlopi in https://github.com/duckdb/duckdb/pull/20445
* Invert the setup of ccache and cleanup_runner by @carlopi in https://github.com/duckdb/duckdb/pull/20429
* bump spatial for andium by @Maxxen in https://github.com/duckdb/duckdb/pull/20479
* Reclaim disk space on MacOS runners by @lnkuiper in https://github.com/duckdb/duckdb/pull/20493
* Adding secure clear functions by @ccfelius in https://github.com/duckdb/duckdb/pull/20285
* rewrite unaligned scan by @artjomPlaunov in https://github.com/duckdb/duckdb/pull/20474
* Issue #20470: TIMESTAMPTZ to DATE by @hawkfish in https://github.com/duckdb/duckdb/pull/20498
* Reset cached dictionaries in `TRY` expression by @Maxxen in https://github.com/duckdb/duckdb/pull/20452
* [Copy] Fix #20324 `partition_by` option binding by @Tishj in https://github.com/duckdb/duckdb/pull/20509
* Bump multiple extensions by @maiadegraaf in https://github.com/duckdb/duckdb/pull/20504
* update azure ref for v1.4-andium by @benfleis in https://github.com/duckdb/duckdb/pull/20506
* [Fix] Directly retrieve the logical column index during `MERGE INTO` binding by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20503
* Sanitize pragmas by @samansmink in https://github.com/duckdb/duckdb/pull/20514
* Bump httpfs, ducklake and postgres by @carlopi in https://github.com/duckdb/duckdb/pull/20518
* Revert vortex bump for v1.4.4 by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20527
* Bump VSS by @taniabogatsch in https://github.com/duckdb/duckdb/pull/20542
* Bump Excel by @maiadegraaf in https://github.com/duckdb/duckdb/pull/20540
* Fix Issue #20233: Fix function chain in having and merge to v1.4 by @ArNine in https://github.com/duckdb/duckdb/pull/20532
* bump iceberg by @Tmonster in https://github.com/duckdb/duckdb/pull/20549
* Bump Iceberg v1.4 by @Tmonster in https://github.com/duckdb/duckdb/pull/20604
* Fix KeyValueSecretReader init by @NiclasHaderer in https://github.com/duckdb/duckdb/pull/20620
* Fail fast extensions by @carlopi in https://github.com/duckdb/duckdb/pull/20605

## New Contributors
* @victor-ab made their first contribution in https://github.com/duckdb/duckdb/pull/20146
* @gishor made their first contribution in https://github.com/duckdb/duckdb/pull/20071

**Full Changelog**: https://github.com/duckdb/duckdb/compare/v1.4.3...v1.4.4
## Project: [datafusion-contrib/datafusion-table-providers](https://github.com/datafusion-contrib/datafusion-table-providers), 1 releases: ['v0.9.3']
### Release: datafusion-table-providers [v0.9.3](https://github.com/datafusion-contrib/datafusion-table-providers/releases/tag/v0.9.3)
## What's Changed
* Bump bb8 from 0.9.0 to 0.9.1 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/514
* Bump bytes from 1.10.1 to 1.11.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/515
* Bump arrow-schema from 57.0.0 to 57.2.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/524
* Bump insta from 1.43.2 to 1.46.0 by @dependabot[bot] in https://github.com/datafusion-contrib/datafusion-table-providers/pull/523
* Update the README file to include a development section. by @hozan23 in https://github.com/datafusion-contrib/datafusion-table-providers/pull/526
* Prevent invalid INSERT statements with empty batches by @nuno-faria in https://github.com/datafusion-contrib/datafusion-table-providers/pull/528


**Full Changelog**: https://github.com/datafusion-contrib/datafusion-table-providers/compare/v0.9.2...v0.9.3
## Project: [unionai-oss/pandera](https://pandera.readthedocs.io/en/stable/index.html), 3 releases: ['Release 0.29.0: support list, dict, and tuple of dataframes', 'v0.28.1: Fix regressions in Check behavior', 'Release 0.28.0: Add support for Pyspark 4']
### Release: pandera [Release 0.29.0: support list, dict, and tuple of dataframes](https://github.com/unionai-oss/pandera/releases/tag/v0.29.0)
## ⭐️ Highlight

Pandera now supports collection types containing dataframes, shoutout to @garethellis0 with an amazing first contribution!

```python
@pa.check_types
def process_tuple_and_return_dict(
    dfs: tuple[DataFrame[OnlyZeroesSchema], DataFrame[OnlyOnesSchema]],
) -> dict[str, DataFrame[OnlyZeroesSchema]]:
    return {
        "foo": dfs[0],
        "bar": dfs[0]
    }


result = process_tuple_and_return_dict((
    pd.DataFrame({"a": [0, 0]}),
    pd.DataFrame({"a": [1, 1]}),
))
print(result)
```

## What's Changed
* feature/1078: Added Support For List, Dict, And Tuples Of Dataframes by @garethellis0 in https://github.com/unionai-oss/pandera/pull/2204
* pin sphinx version by @cosmicBboy in https://github.com/unionai-oss/pandera/pull/2208
* Add map datatype to the Ibis engine implementation by @deepyaman in https://github.com/unionai-oss/pandera/pull/2206

## New Contributors
* @garethellis0 made their first contribution in https://github.com/unionai-oss/pandera/pull/2204

**Full Changelog**: https://github.com/unionai-oss/pandera/compare/v0.28.1...v0.29.0
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
