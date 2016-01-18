# simplegit
A python module for simple interaction with git via subprocess.

### How?
```
# pip install simplegit
```
(note: this doesn't work via pip yet. Working on that.)
```python
from simplegit import Git
git = Git()
output_lines, returncode, error_lines = git.status()
```

### Why?
In personal projects, I always find myself writing scripts to automate parts of the development process. One example is checking out a `gh-pages` branch for a Github Pages website, pushing to `gh-pages`, then checking out `master` again - usually I have a script called `push.py` which automates this. If you're conditionally ignoring files based on the branch, you have even more processing to do (including extra commits). It's kind of clumsy to execute these git commands using python's `subprocess`, so simplegit provides a nice wrapper.

### How does it work?
The `Git` class form simplegit simply takes a call to it (for example `Git().status("-s")`), builds a subprocess command, executes it, and returns the relevant information. Any git command (e.g. status, commit, push, pull) is available, since the python object blindly proxies the function name to build the command (e.g. `git.add("-A")` -> `git add -A`). Some examples:

```python
lines, rtncode, err_lines = git.status("-s")
lines, rtncode, err_lines = git.commit("-m 'A fun message'")
```

If you need to call a git command that would produce a python syntax error, like ls-files, you can use `Git().call`:

```python
git.call("ls-files", "--others --exclude-standard")
```

### Contributing
Right now, this is just a one-off side project that I started. If you'd like to contribute or have ideas, pull requests are welcome!
