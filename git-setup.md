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

