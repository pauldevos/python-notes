### Using Pyenv

- [Commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

```bash
# see versions of python you can install
pyenv install -l

# installs python version
pyenv install 3.7.1
pyenv global 3.7.1 # (sets python version for global)
pyenv virtualenv 2.7.17 .venv27
pyenv virtualenv 3.7.4 .venv37
```

```bash
# get versions installed
pyenv versions

# lists python versions you can install
pyenv install --list

# installs python 3.8.0
pyenv install 3.8.0

# make global
pyenv global python 3.8.0

# set local python -- can use in a local directory of your hcoice
# this will place .python-version file in that directory so it used it in that directory.
pyenv local 3.7.4

# to set the shell
pyenv shell 3.8.0

# to set multiple python versions for shell
python 3.8.0 2.7.6

python
# returns python 3.8.0
python2
# returns python 2.7.6
python3
# returns python 3.8.0

# 1. Set up the python version you want in your app IF you want the global, leave as is
# 2. e.g. pyenv local 3.8.0 # if you want version 3.8.0 and it's not your global default
# 3. run below, and that will be the python version for the app.
python -m venv .venv

```

### Using Poetry

```bash
poetry run flake8 <directory>

# run poetry in Docker
poetry config settings.virtualenv.create false

# I don't like in my home direcotry, like in the directory
python3.7 -m venv .venv
```

# Data Engineer - First Things First

If you're going to be a Python developer of any kind, e.g. Data Scientist, Web Developer, and/or Data Engineer there's a few things you should set up from the beginning. Many of these will help abstract away sensitive information (e.g. passwords) from your code repos so you don't accidently commit any sensitive info to Github. They also help make your workflows much faster.

Some potential things you should consider doing first:

1. Install Miniconda (latest version)
2. Set considerations for you in setting up environment variables
   - Customize your Bash terminal
   - Aliases for bash, awk, grep, sed, git commands
   - [Dotfiles](https://dotfiles.github.io/)
   - [Turbo charge your Mac development environment](https://www.mugo.ca/Blog/Turbo-charge-your-Mac-development-environment)

### 1. Installing Python

I recommend installing the latest stable version of [Miniconda](https://conda.io/miniconda.html), as of this post that was Python 3.x. You can still set up conda environments for Python 2.x and we'll get to that later. If you have any problems with installing, read the documentation, do a web search query (e.g. Google, DuckDuckGo, Brave, FireFox), or search for help on YouTube. You got this.

### 2. Setting Up conda & pip

In Python you're going to need an `environment manager` and a `package manager`. Conda is both. You can read more about Conda here: [Conda: Myths and Misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/), [Conda - Package Manager](https://conda.io/docs/user-guide/tasks/manage-pkgs.html), [Conda - Environment Manager](https://conda.io/docs/user-guide/tasks/manage-environments.html). My _personal recommendation_ is to use Conda to manage your environments, but **NOT** to manage your package installation. The main reason is because conda-forge (where Conda installs from) doesn't have all the packages Pypi does (where `pip` installs from). So for package management, I recommend using [pip](https://pypi.org/project/pip/).

### 3. Setting Environment Variables on your `*nix` machine

- Add these to your .bash_profile, your .aws config
- e.g. DB Credentials, AWS Credentials

e.g. update your `.bash_profile`

```#.bash_profile
export DB_USER = "my_username"
export DB_PASSWORD = "my_password"
```

Then you can access them in your Python scripts like so.

```python
import os

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")

```

Some other environment config variables examples should be stored accordingly in one of the following

- `.bashrc`
- AWS - `.aws/credentials`
- SSH - `.ssh` - here you will have your `id_rsa` secret and public ssh key files

So what's the difference between your `.bash_profile` and your `.bashrc` file? Well StackExchange has a great answer for that [here](https://apple.stackexchange.com/questions/51036/what-is-the-difference-between-bash-profile-and-bashrc), but simply put once you open up a terminal your `.bash_profile` is loaded immediately and you have access to all of those environment variables immediately. On a Mac and (I think) most Linux distros (I haven't tried them all) you start with some CLI tool, e.g. bash. So that is your "login" shell. When you type another interactive shell at that command line, e.g. `bash`, `python`, `python3`, or `ksh` you will now load the `.bashrc` file. This might be something you want say when you use Python at the CLI.

If you want to keep some environment variables separate, you can always put a statement into your `.bash_profile` to load variables from another area on `login`.

For example, put this in your `.bash_profile` and it will load all the environment variables from your `.bashrc` file. You can do this with any other file, e.g. `.aws/credentials`

```bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

### 4. Set up and Configure Git

You may use whatever version/source control you like. There's two main flavors, subversion and git. As of this writing, Git has 3 main hosting services: [Github](https://github.com/), [Bitbucket](https://bitbucket.org/), and [Gitlab](https://about.gitlab.com/).

```bash
# set up your keys for your email account
ssh-keygen -t rsa -C "email@work_mail.com" -f "id_rsa_work_user1"
```

Then you're going to need to generate an SSH key so you can SSH from your host (e.g. your laptop or an EC2) to your git responsitory (e.g. Github).

There's some instructiosn on how to this here: [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

#### If you have Multiple SSH Keys (often you will)

You have to do some magic to make it work. There's a few suggestions here: [SSHing into Multiple Github Accounts](https://gist.github.com/jexchan/2351996)

For example your `~/.ssh folder may have multiple keys:

```
~/.ssh/id_rsa
~/.ssh/id_rsa_home
~/.ssh/id_rsa_work
~/.ssh/id_rsa_aws
```

You will have to add all these keys to your SSH agent,
e.g.

```
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa_home
ssh-add ~/.ssh/id_rsa_work
ssh-add ~/.ssh/id_rsa_aws
```

Now to use each for a specific task you'll have to use the `-i` (identity) tag for the correct pairing.
e.g. `ssh -i ~/.ssh/id_rsa_aws ubuntu@aws-sdf-adfs-s112312.com`

If you need to add SSH keys to an EC2, you can find instructions for that here:

- [How do I add new user accounts with SSH access to my Amazon EC2 Linux instance?](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/)

------- Not yet organized

`brew upgrade brew` ## upgrades to all current packages
`brew upgrade` ## installs upgrades for any previously installed packages

### Best Practices

- [Gitlab Best Practices](https://docs.gitlab.com/ee/development/README.html#databases)
- [Advanced Git Tips for Python Developers](https://realpython.com/advanced-git-for-pythonistas/)

### AWS

- [Python, Boto3, and AWS S3: Demystified](https://realpython.com/python-boto3-aws-s3/)

### Task Schedulers - Airflow, Oozie, Dask, Celery

- [Dask and Celery Comparison](http://matthewrocklin.com/blog/work/2016/09/13/dask-and-celery)

### Dot Files

- [Getting Started with DotFiles](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789)
- [Donne Martin's DotFile](https://github.com/donnemartin/dev-setup)
- [Awesome DotFiles](https://github.com/webpro/awesome-dotfiles)
- [Mathias Bynens DotFiles](https://github.com/mathiasbynens/dotfiles)
- https://dotfiles.github.io/
- https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html

### Git

- [Interactive Git Cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)

### Git Q&A

- https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git?rq=1
- https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely?rq=1
- https://stackoverflow.com/questions/61212/how-to-remove-local-untracked-files-from-the-current-git-working-tree?rq=1
- https://stackoverflow.com/questions/1628088/reset-local-repository-branch-to-be-just-like-remote-repository-head?noredirect=1&lq=1
- https://stackoverflow.com/questions/32056324/there-is-no-tracking-information-for-the-current-branch
