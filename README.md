# GitHub Actions playground

Setup: create a new GitHub repo, push this folder to it, open the **Actions** tab.

## Exercises (in order)
1. **Watch CI run.** Push to main. Open the run, expand each step, see the 3 matrix jobs.
2. **Break a test.** On a branch, change `word_count` to return `len(text)`. Open a PR and watch the check fail. Fix it and push to see it go green.
3. **Break lint.** Add `import os` (unused) to `textutils.py`. See `ruff` fail.
4. **Run manually.** Actions > "Scheduled and manual" > Run workflow, type a name.
5. **Use a secret.** Add a repo secret `MY_SECRET`, re-run, notice it's masked as `***`.
6. **Cut a release.** `git tag v0.1.0 && git push --tags`, then check Releases.
7. **Stretch:** add branch protection requiring `all-green` before merge; add a `paths:` filter so CI skips README-only changes.
