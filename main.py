# In this code: 
# I'm going to learn github in detail
# In Sha Allah


# Git is a version Control System
# Version control help us to keep track of our code


# Folder == Repository
# Save = Commit

# Git Commands

# git init (initialize)
# git add. (add all Files)
# git commit -m " First comment
# git branch -M main
# git config --list
# git push -u origin main
# git clone (link orf repo here)
# git status 

# add repo from github
# remote add origin [link repo]
# git remote -v [verify branch]
# git branch [see on which branch we are currently working]

#  Branch
# git branch
# Master and main are not same
# git branch -M [branch name]


# after modification [Two way process]
# git add then git commit
# github don't store [git add] record, it only store [git commit]  


# Terminal Commands
# cd [folder name] (change directory )=> to go into the inner folder
# cd .. [to back]
# ls  [To see all file in the particular folder ]
# ls -a [to access hidden file in the folder]

print("Helo World")

num=int(input("Enter a number:"))
if num%2==0:
    print("Even Number",num)
else:
    print(f"Odd Number{num}")



# TODO local to remote
# create file and init git command
# git remote add origin [link of repo]
# change branch [git branch -M [name]]
# git push origin main

#TODO remote to local
# create file on github
# clone file [git clone (link orf repo here)]
# changes or write ur code then
# git add .
# git commit -m
# git push 
# git log (to see history of commit)

#  TODO Branches
#  git checkout -b [name]  (to create new branch)
# git checkout [branch name ] (to go to the next branch)
# git checkout -d [branch name] (delete branch)
#if we want to delete current branch , we should go to other branch first, and then delete the required branch
#  git pull origin main (use command to save changes of merge in local)


# Undo Changes 
# stage changes
    # we use it, when we delete lines accidentally and also we [git add .] so in this case we use reset to come back where we were before it.and this delete the last git add.
    # we use git status to show if works or not
    # git reset [file name] for individual file change
    # git reset for all reset

# Commit Changes (for 1 comment)
    #  we add and commit the change but we don't need to do this.

# commit changes for multiple backward commit
    # first we use [git log]to see list of commit
    # then copy the [hash value] of that commit, to which we move to back
    # then use 
    # git reset~[hash value]

