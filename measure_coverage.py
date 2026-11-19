"""Measure library_fines.py with Python 3.13's built-in monitoring API."""
import dis
import importlib
from pathlib import Path
import sys

import pytest

module = importlib.import_module("library_fines")
functions = [module.late_fine, module.can_borrow, module.renewal_status]
codes = {function.__code__ for function in functions}
# Direct import executes the module-level constant and definitions.
executed = {
    line for offset, line in dis.findlinestarts(
        compile(Path("library_fines.py").read_text(), "library_fines.py", "exec")
    )
    if offset and line and line > 0
}
expected = executed.copy()
outcomes = set()
choices = set()
for code in codes:
    instructions = list(dis.get_instructions(code))
    for index, op in enumerate(instructions):
        if op.opname != "RESUME" and op.starts_line:
            expected.add(op.positions.lineno)
        if op.opname.startswith("POP_JUMP_IF"):
            choices.add((code, op.offset, op.jump_target))
            choices.add((code, op.offset, instructions[index + 1].offset))
tool = 3
sys.monitoring.use_tool_id(tool, "library lab coverage")

def record_line(code, line):
    executed.add(line)

def record_branch(code, source, destination):
    outcomes.add((code, source, destination))

try:
    sys.monitoring.register_callback(tool, sys.monitoring.events.LINE, record_line)
    sys.monitoring.register_callback(tool, sys.monitoring.events.BRANCH, record_branch)
    for code in codes:
        sys.monitoring.set_local_events(
            tool, code, sys.monitoring.events.LINE | sys.monitoring.events.BRANCH
        )
    result = pytest.main(["-q", "-p", "no:cacheprovider", *sys.argv[1:]])
finally:
    for code in codes:
        sys.monitoring.set_local_events(tool, code, 0)
    sys.monitoring.free_tool_id(tool)

line_count = len(expected & executed)
branch_count = len(choices & outcomes)
print(f"Line coverage: {line_count}/{len(expected)} ({line_count / len(expected):.1%})")
print(f"Branch coverage: {branch_count}/{len(choices)} ({branch_count / len(choices):.1%})")
print("Uncovered lines:", sorted(expected - executed))
if result:
    raise SystemExit(result)
