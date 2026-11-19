# Lab 6 — Code and Branch Coverage

This lab tests the [library fine calculator](library_fines.py) with separate suites for [line coverage](CodeCoverageTest_library_fines.py) and [branch coverage](BranchCoverageTest_library_fines.py). The tests cover invalid inputs, fine limits, and the order in which borrowing and renewal rules are applied.

## Run the tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

To reproduce the recorded measurements, run these commands with Python 3.13.

```sh
python measure_coverage.py CodeCoverageTest_library_fines.py
python measure_coverage.py BranchCoverageTest_library_fines.py
```

## Results

| Run | Tests passed | Line coverage | Branch coverage |
| --- | ---: | ---: | ---: |
| [Starter](baseline_coverage.txt) | 2 | 50.0% | 31.8% |
| [Line suite](line_coverage.txt) | 13 | 100% | 100% |
| [Branch suite](branch_coverage.txt) | 19 | 100% | 100% |

The recorded runs used Python's built-in `sys.monitoring`. See the [verification guide](verification.md) for Coverage.py commands and the [line coverage](line_coverage.png) and [branch coverage](branch_coverage.png) output images.
