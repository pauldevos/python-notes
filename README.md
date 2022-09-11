### Build Packages



### Testing
- pytest
- pycov (coverage)
- sphinx
- great expectations
- doctest

### Documentation
- [sphinx](https://www.sphinx-doc.org/en/master/)
- swagger
- pydoc
- [pdoc](https://pdoc.dev/docs/pdoc.html) - pdoc auto-generates API documentation that follows your project's Python module hierarchy.
- docstrings

### CI/CD, Build Packages
- Github Actions
- [Pre-Commit](https://pre-commit.com/)
- Black, flake8, mypy, commitizen

### Logging
- logging
- [python-json-logger](https://github.com/madzak/python-json-logger) - This library is provided to allow standard python logging to output log data as json objects. 
- Best Practices
    - [DataDog](https://www.datadoghq.com/blog/python-logging-best-practices/)
    - [Coralogic](https://coralogix.com/blog/python-logging-best-practices-tips/)
    - [Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

```
$ pytest --cov*
$ sphinx-build -n -W -q -b html docs docs/_build/html
$ pre-commit run -a (if you didn't install the pre-commit git hook)
```
