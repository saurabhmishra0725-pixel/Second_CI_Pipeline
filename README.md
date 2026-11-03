# Second_CI_Pipeline

Assignment 6: ten Python programs (31-40), pytest tests, and a GitHub Actions
workflow. Each program and its test must be committed on its own feature branch,
then merged into main through a pull request after CI passes.

## Folder structure

```text
Second_CI_Pipeline/
|-- code/
|   |-- 31_pangram.py
|   `-- ... programs 32 to 40
|-- testcase/
|   |-- __init__.py
|   |-- test_31_pangram.py
|   `-- ... tests 32 to 40
|-- .github/workflows/ci.yml
|-- __init__.py
|-- pytest.ini
|-- MAC_COMMANDS.md
|-- requirements.txt
|-- .gitignore
`-- README.md
```

`pytest.ini` discovers tests in `testcase` and adds `code` to the Python import
path, so the numbered modules can still be loaded with `importlib`.
`code` stays a plain folder without `__init__.py` to avoid shadowing Python's
standard-library `code` module, which pytest's debugger uses.

## Program behavior

- Pangram checks all 26 English letters, ignoring case.
- Word counting splits on whitespace; punctuation stays attached to words.
- First non-repeating character is case-sensitive and includes whitespace;
  returns `None` when no unique character exists.
- Sorted means ascending, allowing duplicates; an empty list is sorted.
- Moving zeros returns a new numeric list, preserving nonzero order.
- Most frequent accepts hashable items, resolves ties by first appearance,
  and returns `None` for an empty list.
- Rotation is to the left; negative positions rotate right.
- Missing number uses XOR and assumes distinct integers from `1..n` with exactly
  one missing, where `n = len(numbers) + 1`.
- Transpose requires rectangular rows; unequal row lengths raise `ValueError`.
- GCD is nonnegative and handles negative numbers and zero; `gcd(0, 0) = 0`.

## MacBook setup and command batches

Start with [MAC_COMMANDS.md](MAC_COMMANDS.md). It contains tool setup, a Python
virtual environment, GitHub sign-in, repository creation, all ten individual
program branches and pull requests, CI checks, merge commands, and final checks.

This is a fresh file copy for your own GitHub account. No existing Git history
or remote configuration is included. Run the commands yourself, one batch at a
time. Do not stage every program in the initial main commit.
