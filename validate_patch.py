import subprocess
import sys

# Get changed files compared to previous commit
result = subprocess.run(
    ["git", "diff", "--name-only", "HEAD~1"],
    capture_output=True,
    text=True
)

changed_files = result.stdout.strip().split("\n")

if "tests/test_math_utils.py" in changed_files:
    print("❌ Agent modified test file. Invalid fix.")
    sys.exit(1)

print("✅ Patch integrity validated.")
