# Windows PowerShell commands ? Second_CI_Pipeline

Run batches in order in PowerShell; stop if a command fails. Use your own GitHub account.

## Batch 0: Check tools and run tests

Install Git, Python 3.12+, and GitHub CLI (https://cli.github.com/) if needed.

~~~powershell
cd "$HOME\Downloads\Second_CI_Pipeline"
git --version
python --version
gh --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -v
~~~

Expect 66 passing tests. If script activation is blocked, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` and activate again.

## Batch 1: Sign in

~~~powershell
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh api user --jq .login
gh auth setup-git
~~~

Confirm the displayed username is yours.

## Batch 2: Initialize Git and set your identity

~~~powershell
git init -b main
git config user.name "YOUR NAME"
git config user.email "YOUR GITHUB EMAIL"
~~~

Replace the placeholders with your name and GitHub email.

## Batch 3: Commit base files, create your repo, push main

This creates a public repository named Second_CI_Pipeline in your GitHub account.
Use --private if your instructor allows a private repository. The name must be available.
Do not run git add . or git add -A: programs are committed one by one below.

~~~powershell
git add __init__.py testcase/__init__.py pytest.ini requirements.txt .gitignore README.md WINDOWS_COMMANDS.md .github/workflows/ci.yml
git commit -m "Initial setup with CI workflow"
gh repo create Second_CI_Pipeline --public --source=. --remote=origin
git push -u origin main
~~~

CI starts when you open a pull request targeting main; a branch push alone does not start it.

## Program branches

Finish each branch's PR and merge before starting the next. Only merge after CI passes.
If checks have not appeared, rerun the check command after a few seconds. Stop on failures.
Keep all ten branches; do not delete them or enable automatic branch deletion.

### Program 31: pangram check

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 31-pangram
git add code/31_pangram.py testcase/test_31_pangram.py
git commit -m "Add pangram check program and tests"
git push -u origin 31-pangram
gh pr create --base main --head 31-pangram --fill
gh pr checks 31-pangram --watch
~~~

After CI passes:

~~~powershell
gh pr merge 31-pangram --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 32: count words

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 32-count-words
git add code/32_count_words.py testcase/test_32_count_words.py
git commit -m "Add count words program and tests"
git push -u origin 32-count-words
gh pr create --base main --head 32-count-words --fill
gh pr checks 32-count-words --watch
~~~

After CI passes:

~~~powershell
gh pr merge 32-count-words --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 33: first non-repeating character

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 33-first-non-repeating
git add code/33_first_non_repeating.py testcase/test_33_first_non_repeating.py
git commit -m "Add first non-repeating character program and tests"
git push -u origin 33-first-non-repeating
gh pr create --base main --head 33-first-non-repeating --fill
gh pr checks 33-first-non-repeating --watch
~~~

After CI passes:

~~~powershell
gh pr merge 33-first-non-repeating --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 34: check sorted list

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 34-check-sorted
git add code/34_check_sorted.py testcase/test_34_check_sorted.py
git commit -m "Add check sorted list program and tests"
git push -u origin 34-check-sorted
gh pr create --base main --head 34-check-sorted --fill
gh pr checks 34-check-sorted --watch
~~~

After CI passes:

~~~powershell
gh pr merge 34-check-sorted --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 35: move zeros

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 35-move-zeros
git add code/35_move_zeros.py testcase/test_35_move_zeros.py
git commit -m "Add move zeros program and tests"
git push -u origin 35-move-zeros
gh pr create --base main --head 35-move-zeros --fill
gh pr checks 35-move-zeros --watch
~~~

After CI passes:

~~~powershell
gh pr merge 35-move-zeros --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 36: most frequent element

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 36-most-frequent
git add code/36_most_frequent.py testcase/test_36_most_frequent.py
git commit -m "Add most frequent element program and tests"
git push -u origin 36-most-frequent
gh pr create --base main --head 36-most-frequent --fill
gh pr checks 36-most-frequent --watch
~~~

After CI passes:

~~~powershell
gh pr merge 36-most-frequent --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 37: rotate string

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 37-rotate-string
git add code/37_rotate_string.py testcase/test_37_rotate_string.py
git commit -m "Add rotate string program and tests"
git push -u origin 37-rotate-string
gh pr create --base main --head 37-rotate-string --fill
gh pr checks 37-rotate-string --watch
~~~

After CI passes:

~~~powershell
gh pr merge 37-rotate-string --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 38: missing number XOR

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 38-missing-number-xor
git add code/38_missing_number_xor.py testcase/test_38_missing_number_xor.py
git commit -m "Add missing number XOR program and tests"
git push -u origin 38-missing-number-xor
gh pr create --base main --head 38-missing-number-xor --fill
gh pr checks 38-missing-number-xor --watch
~~~

After CI passes:

~~~powershell
gh pr merge 38-missing-number-xor --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 39: transpose matrix

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 39-transpose-matrix
git add code/39_transpose_matrix.py testcase/test_39_transpose_matrix.py
git commit -m "Add transpose matrix program and tests"
git push -u origin 39-transpose-matrix
gh pr create --base main --head 39-transpose-matrix --fill
gh pr checks 39-transpose-matrix --watch
~~~

After CI passes:

~~~powershell
gh pr merge 39-transpose-matrix --merge
git checkout main
git pull --ff-only origin main
~~~

### Program 40: GCD

~~~powershell
git checkout main
git pull --ff-only origin main
git checkout -b 40-gcd
git add code/40_gcd.py testcase/test_40_gcd.py
git commit -m "Add GCD program and tests"
git push -u origin 40-gcd
gh pr create --base main --head 40-gcd --fill
gh pr checks 40-gcd --watch
~~~

After CI passes:

~~~powershell
gh pr merge 40-gcd --merge
git checkout main
git pull --ff-only origin main
~~~

## Final verification

~~~powershell
python -m pytest -v
git branch -a
gh pr list --state merged --base main --limit 10
git status
~~~
