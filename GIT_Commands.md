# GIT Overview

git is a version-control software system for software development. 

(Note: git is not to be confused with github. github is a hosting site for code repositories. Github has git interface to check-in code.)

git allows people to collaborate more easily when coding by maintaining a master version in a central place (like github) and "clones" that can checked out.


For reference on commands: https://gist.github.com/jedmao/5053440

## From PythonAnywhere dev console

You run git commands in pythonanywhere by opening a new Bash console. Go to a safe directory and perform git commands. 
For instance, I wanted to clone aryam git. So I went to /home/bpudiped. Then I cloned aryam git right there.

## Cloning

A git clone is an identical copy of all the files from github (or wherever your master version is). 
In this manner, git allows you to develop in your local computer or network for independence and speed. 

Any changes in central place (say, made by another user) can be "pulled into" your cloned version by using "git pull" command.

* git clone https://github.com/<username>/foo foo  # where foo is a directory or a file

## Adding and Modifying

To add new files or modify code, you first add or modify in your local version. 
Then, you need to move this to a "staging" version (which is also local) where the changes are "committed."
Then, finally, you "push" them into the master version on github (or central repository wherever it is).

### For adding:

* git add foo.py

* git commit -m "updates to foo.py"   # Here -m is the message for the commits

* git push origin master   # if you are pusing into the master version and not a branch (branch is a topic we will cover later)

### For modifying:

* git commit -m "updates to foo.py"   # Here -m is the message for the commits

* git push origin master   # if you are pusing into the master version and not a branch (branch is a topic we will cover later)







