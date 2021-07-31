# Logging

- Loggers expose the interface that application code directly uses.
- Handlers send the log records (created by loggers) to the appropriate destination.
- Filters provide a finer grained facility for determining which log records to output.
- Formatters specify the layout of log records in the final output.

### Where to put Logging

- [Logging Per Function or Per Module](https://stackoverflow.com/questions/45063099/python-logger-per-function-or-per-module)

### Can use a ConfigFile

logging.conf or logging.ini

```python
import logging.config

logging.config.fileConfig('logging.config')


```

```python
import logging.config

logging.config.dictConfig('logging.config')

```

### Capturing Stacktraces

### Configuration files

e.g. `loggingConfig.ini`

A logging configuration file needs to contain three sections:

[loggers]: the names of the loggers you’ll configure.
[handlers]: the handler(s) these loggers should use (e.g., consoleHandler, fileHandler).
[formatters]: the format(s) you want each logger to follow when generating a log.
