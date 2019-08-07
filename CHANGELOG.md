# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (to the best of our ability).

## Unreleased

### Added

- New check `PD901 'df' is a bad variable name. Be kinder to your future self.` ([#69](https://github.com/deppen8/pandas-vet/pull/69))
- An `--annoy` flag that can be used to activate checks that set to "off" by default. The off-by-default checks should use the convention `PD9xx` ([#69](https://github.com/deppen8/pandas-vet/pull/69))
- Added `PD901` to README along with an example use of the `--annoy` flag ([#69](https://github.com/deppen8/pandas-vet/pull/69))

### Changed

- `test_PD012.py` had test cases that used `df = <something>`, which conflicted with the new `PD901` check. These were changed to `employees = <something>` ([#69](https://github.com/deppen8/pandas-vet/pull/69))
- Applied the `black` formatter to the entire pandas-vet package.

### Deprecated

- None

### Removed

- A few extraneous variables ([455d1f0](https://github.com/deppen8/pandas-vet/pull/69/commits/455d1f0525dd4e9590cd10efdcd39c9d9a7923a2))

### Fixed

- None

### Security

- None


## [0.2.1] - 2019-07-27

### Added

- Leandro Leites added as contributor ([#66](https://github.com/deppen8/pandas-vet/pull/66))
- This CHANGELOG.md added ([#68](https://github.com/deppen8/pandas-vet/pull/68))

### Changed

- None

### Deprecated

- None

### Removed

- Unnecessary commented line from `setup.py` ([#67](https://github.com/deppen8/pandas-vet/pull/67))

### Fixed

- PD015 would fail if `node.func.value` did not have an `id`. Fixed with [#65](https://github.com/deppen8/pandas-vet/pull/65)
- `version.py` now correctly uses v0.2.x. This version file was not bumped with the last release. ([#67](https://github.com/deppen8/pandas-vet/pull/67))

### Security

- None
