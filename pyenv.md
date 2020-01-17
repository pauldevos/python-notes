### Using Pyenv

```bash
# see versions of python you can install
pyenv install -l

# installs python version
pyenv install 3.7.1

pyenv global 3.7.1 # (sets python version for global)

pyenv virtualenv 2.7.17 .venv27

pyenv virtualenv 3.7.4 .venv37
```

### Using Poetry
```bash
poetry run flake8 <directory>

# run poetry in Docker
poetry config settings.virtualenv.create false

# I don't like in my home direcotry, like in the directory
python3.7 -m venv .venv
```

