# Lab 6 coverage

| Run | Passing pytest cases | Executed lines | Decision outcomes |
| --- | ---: | ---: | ---: |
| Starter | 2 | 16/32 (50.0%) | 7/22 (31.8%) |
| Line suite | 13 | 32/32 (100%) | 22/22 (100%) |
| Branch suite | 19 | 32/32 (100%) | 22/22 (100%) |

The terminal transcripts and PNGs were produced using pytest and Python 3.13
`sys.monitoring` with [measure_coverage.py](measure_coverage.py).
The line suite checks error paths and regular results. The branch suite also
checks exact cutoffs and decision precedence, including whether reservations
take priority over overdue and renewal-limit checks.

The handout's Coverage.py commands are below. Coverage.py was unavailable for
the recorded runs. Its branch JSON shows the count for branch coverage and
the terminal report's Cover column combines statements and branches.

```sh
python -m pip install -r requirements-dev.txt
python -m coverage run -m pytest -q CodeCoverageTest_library_fines.py
python -m coverage report -m --fail-under=90 library_fines.py
python -m coverage run --branch -m pytest -q BranchCoverageTest_library_fines.py
python -m coverage report -m --fail-under=90 library_fines.py
python -m coverage json --pretty-print -o branch-coverage.json library_fines.py
```

Run `python -m pytest -q` to run both submissions together.
On Python 3.13, the verification script can independently measure either one
with `python measure_coverage.py <test-file.py>`.
