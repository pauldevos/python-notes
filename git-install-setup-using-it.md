### Starting a New Project
1. Go to Github and create a new project (give it a name), create a `.gitignore` (e.g. Python), a `LICENSE.txt` and a `README.md`.
2. Then locally (or on wherever you're going to do development), create that directory and then do a `git clone git@github.com:<username>/<repo_name>.git`
3. Then add your files. In doing so this foregoes all the possible entanglements of `git init`, `git commit`, `git remote add origin master` and various issues with the `git pull` and your current directory.


### Git Resources
- http://rogerdudler.github.io/git-guide/
- https://github.com/joshnh/Git-Commands


### Set up and Configure Git
You may use whatever version/source control you like. There's two main flavors, subversion and git. As of this writing, Git has 3 main hosting services: [Github](https://github.com/), [Bitbucket](https://bitbucket.org/), and [Gitlab](https://about.gitlab.com/).

Then you're going to need to generate an SSH key so you can SSH from your host (e.g. your laptop or an EC2) to your git responsitory (e.g. Github).

There's some instructiosn on how to this here: [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)


```bash
# set up your keys for your email account, the -f is for the output filename
ssh-keygen -t rsa -C "email@work_mail.com" -f "id_rsa_work_user1"

# -b is for bytes of your encryption key, e.g. 1024, 2048, 4096 like so...
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```


#### If you have Multiple SSH Keys (often you will)
You have to do some magic to make it work. Follow these directions. You'll basically need to add both id_rsa's (or however many you have), then go through cloning (from each account) into that account and setting up a push from there. Once done, as long as you're in that repository directory locally, git will recognize the correct account and be able to pull/push from the correct account. 
- [How to manage multiple GitHub accounts on a single machine with SSH keys](https://www.freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca/)

If none of that doesn't work for you for some reason, there's a few suggestions here:
- [SSHing into Multiple Github Accounts](https://gist.github.com/jexchan/2351996)

An example your `~/.ssh` folder may have multiple keys:
```
~/.ssh/id_rsa
~/.ssh/id_rsa_home
~/.ssh/id_rsa_work
~/.ssh/id_rsa_aws
```

You will have to add all these keys to your SSH agent,
```
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa_home
ssh-add ~/.ssh/id_rsa_work
ssh-add ~/.ssh/id_rsa_aws
```


### for EC2s - you will use an identity

The `-i` (identity) tag for the correct pairing.
e.g. `ssh -i ~/.ssh/id_rsa_aws ubuntu@aws-sdf-adfs-s112312.com`


If you need to add SSH keys to an EC2, you can find instructions for that here:
- [How do I add new user accounts with SSH access to my Amazon EC2 Linux instance?](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance/)


### Learn Git Commands

### Learn Git Workflows

### Make Pull Requests to Open Source Repos
- [How to make your first pull request (and how I made mine) (YouTube)](https://www.youtube.com/watch?v=L8Sd1rRGcOw)
- [The beginner's guide to contributing to a GitHub project](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)


Git Commands
============

_A list of my commonly used Git commands_

*If you are interested in my Git aliases, have a look at my `.bash_profile`, found here: https://github.com/joshnh/bash_profile/blob/master/.bash_profile*

--

### Getting & Creating Projects

| Command | Description |
| ------- | ----------- |
| `git init` | Initialize a local Git repository |
| `git clone ssh://git@github.com/[username]/[repository-name].git` | Create a local copy of a remote repository |

### Basic Snapshotting

| Command | Description |
| ------- | ----------- |
| `git status` | Check status |
| `git add [file-name.txt]` | Add a file to the staging area |
| `git add -A` | Add all new and changed files to the staging area |
| `git commit -m "[commit message]"` | Commit changes |
| `git rm -r [file-name.txt]` | Remove a file (or folder) |

### Branching & Merging

| Command | Description |
| ------- | ----------- |
| `git branch` | List branches (the asterisk denotes the current branch) |
| `git branch -a` | List all branches (local and remote) |
| `git branch [branch name]` | Create a new branch |
| `git branch -d [branch name]` | Delete a branch |
| `git push origin --delete [branchName]` | Delete a remote branch |
| `git checkout -b [branch name]` | Create a new branch and switch to it |
| `git checkout -b [branch name] origin/[branch name]` | Clone a remote branch and switch to it |
| `git checkout [branch name]` | Switch to a branch |
| `git checkout -` | Switch to the branch last checked out |
| `git checkout -- [file-name.txt]` | Discard changes to a file |
| `git merge [branch name]` | Merge a branch into the active branch |
| `git merge [source branch] [target branch]` | Merge a branch into a target branch |
| `git stash` | Stash changes in a dirty working directory |
| `git stash clear` | Remove all stashed entries |

### Sharing & Updating Projects

| Command | Description |
| ------- | ----------- |
| `git push origin [branch name]` | Push a branch to your remote repository |
| `git push -u origin [branch name]` | Push changes to remote repository (and remember the branch) |
| `git push` | Push changes to remote repository (remembered branch) |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git pull` | Update local repository to the newest commit |
| `git pull origin [branch name]` | Pull changes from remote repository |
| `git remote add origin ssh://git@github.com/[username]/[repository-name].git` | Add a remote repository |
| `git remote set-url origin ssh://git@github.com/[username]/[repository-name].git` | Set a repository's origin branch to SSH |

### Inspection & Comparison

| Command | Description |
| ------- | ----------- |
| `git log` | View changes |
| `git log --summary` | View changes (detailed) |
| `git diff [source branch] [target branch}` | Preview changes before merging |



### Dot Files
- [Getting Started with DotFiles](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789)
- [Donne Martin's DotFile](https://github.com/donnemartin/dev-setup)
- [Awesome DotFiles](https://github.com/webpro/awesome-dotfiles)
- [Mathias Bynens DotFiles](https://github.com/mathiasbynens/dotfiles)
- https://dotfiles.github.io/
- https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html
- 


### Git
- [Interactive Git Cheatsheet](http://www.ndpsoftware.com/git-cheatsheet.html)

### Git Q&A
- https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git?rq=1
- https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely?rq=1
- https://stackoverflow.com/questions/61212/how-to-remove-local-untracked-files-from-the-current-git-working-tree?rq=1
- https://stackoverflow.com/questions/1628088/reset-local-repository-branch-to-be-just-like-remote-repository-head?noredirect=1&lq=1
- https://stackoverflow.com/questions/32056324/there-is-no-tracking-information-for-the-current-branch


