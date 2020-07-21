# Week 3 - Working with remotes

## Introduction to GitHub

### What is GitHub?

[MUSIC] In earlier videos, we called out that Git
is a distributed version control system. Distributed means that each developer
has a copy of the whole repository on their local machine. Each copy is a peer of the others. But we can host one of these
copies on a server and then use it as a remote repository for
the other copies. This lets us synchronize work
between copies through this server. Any of us can create a Git
server like this one, and many companies have
similar internal services. But if you don't want to set
up a Git server yourself and host your repositories,
you can use an online service like GitHub. GitHub is a web-based Git
repository hosting service. On top of the version
control functionality of Git, GitHub includes extra features like bug
tracking, wikis, and task management. GitHub lets us share and
access repositories on the web and copy or clone them to our local computer,
so we can work on them. GitHub is a popular choice with a robust
feature set, but it's not the only one. Other services that provide similar
functionality are BitBucket, and GitLab. For the rest of this course,
we'll be using GitHub for our examples. But feel free to use the tool
that best fits your needs. GitHub provides free access to
a Git server for public and private repositories. It limits the number of contributors for
the free private repositories, and offers an unlimited private
repository service for a monthly fee. We'll be using a free repository for
our examples, which is fine for educational use, small personal projects,
or open source development. A word of caution on how you
can manage these repos though. If hackers get hold of information about
your organization's IT infrastructure, they can use it to try and
break into your network. So make sure you treat this
information as confidential. For real configuration and development
work, you should use a secure and private Git server, and
limit the people authorized to work on it. To use GitHub, the first thing you need to do is create
an account if you don't have one already. Signing up online is free and
relatively simple. Once you've done that,
you can either create your own repos or contribute to repos from other projects. If you don't have a GitHub account yet,
now is a good time to create one. Visit github.com to sign up for
their service. Once you've done that,
meet me over in the next video, where we'll go over some basic
interactions with GitHub.

### Basic interaction with GitHub

As we called out, GitHub
is an online service. To use it, you first need to create an
account on the site. Once you have your account, you're ready to create your brand new repository on GitHub. Let's do this now.
Going step-by-step. We'll start by
clicking the Create a repository link on the left. This will take us to the
repo creation wizard. The wizard is pretty
straightforward. The first thing we need to do is give a name for our repo. We'll call this
repo health checks. After that comes a description of what the repo
will be used for. We'll say that'll be used for scripts that check the
health of our computers. Then we need to select
whether we want the repo to be public or private. We'll go with private for now. Finally, the wizard can
help us get started with some few initialization
files like a README, a gitignore, or license file. We'll go with just
the README for now, and then create the repo. Yeah. Using the wizard, we created the repo and have a fresh remote
repository ready to go. Just like magic.
Let's get to work. First step is to create a
local copy of the repository. We'll do that by using the git clone command followed
by the URL of the repo. GitHub conveniently lets
us copy the URL from our repo from the interface so that we don't have to type it. We're now ready to clone
the repo into our computer. We'll do that by calling git clone and paste
in the URL we copied. To do this, GitHub will ask for our username
and password. Just like that, we've
downloaded a copy of the remote repository from
GitHub onto the local machine. This means that we can perform all the git actions that
we've learned up till now. Since the repo is
called health checks, a directory with that name
was automatically created for us and now has the working
tree of the Repository in it. So let's change that directory
and look at the contents. Our repo is basically empty. It only has the README file
that GitHub created for us. This file is in a special
format called markdown. Let's add a bit
more content to it. We've changed this file. What do we need to do now? We need to stage the
change and committed. We've seen a couple of
different ways to do that. Let's use our shortcuts to
do this in just one command. Okay. We've modified
our README file. But we've seen all this before. We got to remote repository set up on GitHub. So let's use it. We can send our changes to that remote repository by using the git push command
which will gather all the snapshots we've taken and send them to
the remote repository. In this case, we've only
taken one snapshot. We'll talk more about what's going on behind the scenes with git push and remote
repositories in later videos. But the mechanics
are pretty simple. To push our modified
README up to GitHub, we'll just call git push. Once again, we're asked
for our password. After that, we see a bunch of messages from git
related to the push. When we access our project, we see the contents
of the README file. So if we check our
repository on GitHub, we should see the
updated message. Pretty cool, right? We've
taken the local changes on our computer and
pushed them out to a remote repository
hosted on GitHub. You've probably
noticed that we had to enter our password both when retrieving the repo and when
pushing changes to the repo. There are a couple ways to
avoid having to do this. One way is to create an
SSH key pair and store the public key in our profile so that GitHub recognizes
our computer. Another option is to use a
credential helper which caches our credentials for a
time window so that we don't need to enter our password
with every interaction. Git already comes with a credential helper baked in.
We just need to enable it. We do that by
calling git config - - global credential.helper cache. Now that we've enabled
the credential helper, we'll need to enter our
credentials once more. After that, they'll be
cached for 15 minutes. To check this, we can
try another git command, git pull which is the command we use to retrieve new changes
from the repository. We'll enter our credentials on the first call to the command
and they'll be cached, so we won't need to
enter them again. With that, we've seen how to create repositories on GitHub, clone our remote repository, push changes to it, and pull changes from it. There's a lot going on behind the scenes here and
we'll dive deeper into the details and
more collaboration techniques in later videos. For now, check out the next reading for a summary
of this basic workflow. Then there's a quick quiz to make sure this is making sense.

### Basic interaction with GitHub Cheat-Sheet

There are various remote repository hosting sites:

- [GitHub](https://github.com/)
- [BitBucket](https://bitbucket.org/product)
- [Gitlab](https://about.gitlab.com/)

Follow the workflow at https://github.com/join to set up a free account, username, and password. After that, [these steps](https://docs.github.com/en/github/getting-started-with-github/create-a-repo) will help you create a brand new repository on GitHub.

Some useful commands for getting started:

| Command   | Explanation & Link                                                                                              |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| git clone | [URL Git clone is used to clone a remote repository into a local workspace](https://git-scm.com/docs/git-clone) |
| git push  | [Git push is used to push commits from your local repo to a remote repo](https://git-scm.com/docs/git-push)     |
| git pull  | [Git pull is used to fetch the newest updates from a remote repository](https://git-scm.com/docs/git-pull)      |

This can be useful for keeping your local workspace up to date.

- https://help.github.com/en/articles/caching-your-github-password-in-git
- https://help.github.com/en/articles/generating-an-ssh-key

## Using a remote repository

### What is a remote

When we clone the newly
created GitHub repository, we had our local Git Repo interact with a
remote repository. Remote repositories
are a big part of the distributed nature
of Git collaboration. It let lots of developers
contribute to a project from their own workstations
making changes to local copies of the project
independently of one another. When they need to
share their changes, they can issue git
commands to pull code from a remote repository or
push code into one. There are a bunch of ways to
host remote repositories. As we called out, there is many internet-based Git hosting providers like GitHub, BitBucket or GitLab which
offer similar services. We can also set up
a Git server on our own network to host
private repositories. A locally hosted Git
server can run on almost any platform
including Linux, mac OS, or Windows. This has benefits like increased privacy, control,
and customization. To understand remote
repositories, and Git's distributed
nature a bit better, imagine you're
working together with some friends to design
a computer game, each of you has a
different portion of the game you're
responsible for. One person is
designing the levels, another the characters
while others are writing the code for the
graphics, physics, and gameplay. All these areas will
have to come together into a single place
for the final product. Although your friends
might work on their parts by themselves, from time to time, everyone needs to
send out progress updates to let each other know what they've
been working on. You will then need to
combine their work into your own portion of the project to make sure it's all compatible. Using Git to manage a project helps us collaborate
successfully. Everyone will develop
their piece of the project independently in their own local repositories maybe even using
separate branches. Occasionally they'll
push finished code into a central remote
repository where others can pull it and incorporate it into their new developments. So how does this work? Alongside the local development
branches like master, Git keeps copies of the
commits that have been submitted to the remote
repository and separate branches. If someone has updated
a repository since the last time you
synchronize your local copy, Git will tell you that
it's time to do an update. If you have your
own local changes when you pull down the
code from the remote repo, you might need to fix merge conflicts before you can
push your own changes. In this way Git let's multiple people work on the same project
at the same time. When pulling new code it will merge the changes
automatically if possible or will
tell us to manually perform the integrating
if there are conflicts. So when working with remotes the workflow for making
changes has some extra steps. Will still modify stage and
commit our local changes. After committing, we'll fetch any new changes from the
remote repo manually merge if necessary and only then will push our changes
to the remote repo. Git supports a variety of ways to connect to a
remote repository. Some of the most common
are using the HTTP, HTTPS and SSH protocols and
their corresponding URLs. HTTP is generally used to allow read only
access to a repository. In other words, it lets
people clone the contents of your repo without letting
them push new contents to it. Conversely HTTPS and SSH, both provide methods
of authenticating users so you can control who
gets permission to push. If all this protocol talk
is making your head spin you might want to
review the video on the subjects made by
my colleague Gian. You'll find the link to this in the next reading.The distributed nature of the work means
that there are no limits to how many people can push
code into a repository. It's a good idea to control
who can push codes to repos and to make sure you give access only to people you trust. Web services like GitHub, offer a bunch of
different mechanisms to control access
to Repositories. Some of these are available
to the general public while others are only
available to enterprise users. By now you have an idea of
what a remote repository is and how it interacts with
local Git repositories. Up next, we'll dive into some of the commands that let us
interact with remotes.

### Working with remotes

[MUSIC] When we call a git clone to get
a local copy of a remote repository, Git sets up that remote repository
with the default origin name. We can look at the configuration for that remote by running git remote
-v in the directory of the repo. Here we see the URLs associated
with the origin remote. There are two URLs. One will be used to fetch data
from the remote repository, and the other one to push
data to that remote repo. They'll usually point at the same place. But in some cases, you can have the fetch
URL use HTTP for read only access, and the push URL use HTTPS or
SSH for access control. This is fine as long as the contents
of the repo that you read when fetching are the same that you write to in pushing. Remote repositories have a name
assigned to them, by default, the assigned name is origin. This lets us track more than one
remote in the same Git directory. While this is not the typical usage,
it can be useful when collaborating with different teams on projects
that are related to each other. We won't look at how to do that here,
but we'll include a link for more information in the next reading. If we want to get even more
information about our remote, we can call git remote show origin. There's a ton of information here,
and we don't need all of it right now. We can see the fetch and push URLs
that we saw before, and the local and remote branches too. For now we only have a master branch
that exists locally and remotely. So the information here
seems a bit repetitive. Once you start having more branches,
especially different branches in the local and remote repo, this
information starts becoming more complex. So what are these remote branches
that we're talking about anyways? Whenever we're operating with remotes,
Git uses remote branches to keep copies of the data that's
stored in the remote repository. We could have a look at
the remote branches that our Git repo is currently tracking
by running git branch -r. These branches are read only. We can look at the commit history,
like we would with local branches, but we can't make any changes
to them directly. To modify their contents, we'll have to go
through the workflow we called out before. First, we pull any new
changes to our local branch, then merge them with our changes and
push our changes to the repo. Remember how we've been using git status
to check the status of our changes? We can also use git status to check
the status of our changes in remote branches as well. Now that we're working
with a remote repository, git status gives us
additional information. It tells us that our branch is up to
date with the origin/master branch, which means that the master branch in
the remote repository called origin, has the same commits as
our local master branch. But what if it wasn't up to date? We'll talk about that in the next video.

### Fetching new changes

While we were learning
about remotes, our colleague Blue Kale added
some files to our repo. We could always use
the GitHub website to browse the changes
that were submitted. But we want to learn how to
do it by interacting through the command line because you might need to do it
this way at your job, and it'll work the same no matter which platform you use
to interact with Git. So first, let's look at the output of the Git
remote show origin command. Check out how it says that the local branches out of date. This happens when
there were commits done to the repo that aren't
yet reflected locally. Git doesn't keep remote
and local branches in sync automatically, it waits until we execute commands to move data
around when we're ready. To sync the data, we use
the git fetch command. This command copies
the commits done in the remote repository
to the remote branches, so we can see what other
people have committed. Let's call it now and
see what happens. Fetched content is downloaded to the remote branches
on our repository. So it's not automatically
mirrored to our local branches. We can run git checkout on these branches to see
the working tree, and we can run git log to
see the commit history. Let's look at the current
commits in the remote repo by running git log origin/master. Looking at this output, we can see that the
remote origin/branch is pointing to the latest commit. While the local master
branch is pointing to the previous commit
we made earlier on. Let's see what happens if
we run git status now. Git status helpfully
tells us that there's a commit that we
don't have in our branch. It does this by letting
us know our branches behind their remote
origin/master branch. If we want to integrate the branches into
our master branch, we can perform a merge operation, which merges the
origin/master branch into our local master branch. To do that, we'll call
git merge origin/master. Great. We've merged
the changes of the master branch of
the remote repository into our local branch. See how Git tells
us that the code was integrated
using fast-forward? It also shows that
two files were added, all checks and disk_usage.py. If we look at the log
output on our branch now, we should see the new commit. We see that now our
master branch is up to date with the remote
origin/master branch. With that, we've updated our branch to the latest changes. We can use git fetch like this to review the changes that happen
in the remote repository. If we're happy with them, we can use git merge to integrate them into
the local branch. Fetching commits from
a remote repository and merging them into
your local repository is such a common
operation in Git that there's a handy command to let us do it all in one action. We'll check that out
in our next video.

### Updating the local repository

[MUSIC] Earlier, we took a look
at the basic workflow for working with remotes when we want to fetch
the changes manually, merge if necessary, and only then push any changes of our own. Since fetching and merging are so common, Git gives us the git pull
command that does both for us. Running git pull will fetch the remote
copy of the current branch and automatically try to merge it
into the current local branch. Let's check if our friend Blue Kale
has made any new changes to the repo. We'll run git pull and
see what changes we get. If you look closely at this output,
you'll see that it includes the output of the fetch and
merge commands that we saw earlier. First, Git fetched the updated
contents from the remote repository, including a new branch. And then it did a fast forward
merge to the local master branch. We'll see that the all_checks
file was updated as well. We can look at the changes
by using git log -p -1. We see that our colleague added
a check_disk_full function that includes the code from the other
disk_usage py file that we saw earlier. So now I'll exit the editor with q. When we called git pull, we saw that there was also a new
remote branch called experimental. Our friend Blue Kale told us that they've
started working on a new feature in that branch. Let's check out the output of
git remote show origin and see what it says about that new branch. We see that there's a new remote
branch called experimental, which we don't have a local branch for
yet. To create a local branch for it,
we can run git checkout experimental. When we checked out
the experimental branch, Git automatically copied the contents of
the remote branch into the local branch. The working tree has been updated to
the contents of the experimental branch. Now we're all set to work on
the experimental feature together with our colleague. In this last example, we got the contents of the experimental
bunch together with those of the master branch when we called git pull, which also
merged new changes onto the master branch. If we want to get the contents of remote
branches without automatically merging any contents into the local branches,
we can call git remote update. This will fetch the contents
of all remote branches, so that we can just call checkout or
merge as needed. We've now seen a bunch of
different ways that we can use to interact with remote repositories. We've seen how to check their status,
how to push and pull changes into repositories, and
even how to get new branches out of them. There's still more to come, but you're probably starting to see how useful
this can be for collaborating with others. In our past examples, we've only looked at
what happens with changes when they can be solved through fast forward. In upcoming videos, we'll look at what
happens when we try to push changes, especially when our changes
generate conflicts. But before we do that,
check out the reading for the list of all the commands involved, and then take the
quiz to put this knowledge into practice.

### Git remotes cheat-sheet

| Command                | Explanation & Link                                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| git remote             | [Lists remote repos](https://git-scm.com/docs/git-remote)                                                                                                           |
| git remote -v          | [List remote repos verbosely](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt--v)                                                                  |
| git remote show <name> | [Describes a single remote repo](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem)                                                         |
| git remote update      | [Fetches the most up-to-date objects](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem)                                                  |
| git fetch              | [Downloads specific objects](https://git-scm.com/docs/git-fetch)                                                                                                    |
| git branch -r          | [Lists remote branches](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r); can be combined with other branch arguments to manage remote branches |

You can also see more in the video Cryptography in Action from the course IT Security: Defense against the digital dark arts.## Solving conflicts

## Solving congflicts

### The pull-merge-push workflow

[MUSIC] We've now looked at
the details of fetching and pulling data from a remote repositories
without any local changes. We saw earlier how we can
use the git push command to send our changes to the remote repo. But what if when we go
to push our changes, there are new changes to the remote repo? To find out, let's start by making
a change to our all checks py script. Remember way back to
the beginning of the course, when we fixed the bug in the function
that checks the disk space? The one that was doing
gigabyte conversion twice? Part of the reason why our code was so
buggy, was that we were passing numbers around without saying what
those numbers were for. We could have made our code clearer by
renaming our min absolute parameter to min GB. So that it's obvious that
the function expects gigabytes. With that,
we've clarified the code of the function. Another way we can make
the code invocation clearer, we can use the name of the parameters
in the call to the function, like this. By using the names of the parameters,
our invocation is clear, and we can even alter the order of
the values and our code would still work. All right, we've made the change. Let's stage it and commit it as usual. We'll first use git add -p to look at
the changes we made and accept them. Then we'll create a commit message to show
that we've renamed min absolute to min GB, and that we're using parameter names for
the invocation. We've made our change,
staged it, and committed it. We should be ready to push
into the remote repo, except now we have a collaborator
also making changes. Let's see what happens when
we try running git push. And it failed. Can you work out what went wrong here? There are a few hints. When we tried to push,
Git rejected our change, that's because the remote repository
contains changes that we don't have in our local branch that
Git can't fast-forward. Maybe you remember when we talked
about Git's merging algorithms? As usual, Git gives us some helpful
information along with the error message, especially the part about integrating
remote changes with git pull. This means we need to sync
our local remote branch with the remote repository
before we can push. We learned earlier that we
can do this with git pull. Let's do this now. [SOUND] Git tried to
automatically merge the local and remote changes to all_checks.py,
but found a conflict. Let's first look at the tree
of commits on all branches as represented by git log
--graph --oneline --all. This graph shows us the different
commits and positions in the tree. We can see the master branch,
the origin/master branch, and the experimental branch. The graph indicates that our current
commit and the commit in the origin/master branch share a common ancestor,
but they don't follow one another. This means that we'll need
to do a three-way merge. To do this,
let's look at the actual changes in that commit by running git
log -p origin/master. So our colleague decide to reorder
the conditional clauses in the function to match the order that the parameters
are passed to the function. They happen to change in the same line
that we changed when we renamed the min_gb variable, which caused the conflict
that Git couldn't resolve. Let's fix it by editing the file
to remove the conflict. So first, let me exit with Q. We see that the problem
occurred in the conditional. On the first line, we see our change,
where min_absolute was renamed to min_gb. In the second line, we see the old variable names,
with the checks done in a different order. We need to decide what to do to this. For example, we can keep the new order,
but use min_gb. One thing to notice is that Git will try
to do all possible automatic merges and only leave manual conflicts for us to
resolve when the automatic merge fails. In this case, we can see that the other
changes we made were merged successfully without intervention. Only the change that happened in the same
line of the file needed our input. We fixed the conflict here, and
the file is short enough that we can very quickly check that there
are no other conflicts. For larger files, it might make sense
to search for the conflict markers, greater than, greater,
greater than, in the whole file. This lets us check that there
are no unresolved conflicts left. Nice, now that we fixed the conflict,
you can finish the merge. Do you remember how to do it? We need to add the all_checks.py file, and
then call git commit to finish the merge. But first, we're going to save and close. The editor message shows that it's
performing a merge of the remote branch with the local branch. We can add extra information
to this message. For example, we can say that we fixed
the conditional in the check disk usage function to use the new
variable name and the new order. Our merge is finally ready,
we can try pushing to the remote again. Yes, after fixing the conflict, we were
able to push our work to the remote repo. Let's look at the commit history
of the master branch now, by calling git log --graph --oneline. We see that the latest commit is the
merge, followed by the two commits that caused the merge conflict,
which are on split paths in our graph. As we called out before,
when Git needs to do a three-way merge, we end up with a separate commit for merging
the branches back into the main tree. Now we know how to successfully
complete a pull, merge, and push cycle, even when it means
doing some manual merges. This was a complex exercise, and it's okay
if some things still seem a bit scary. We all felt panic the first time
we encountered a merge conflict. But don't worry,
it gets easier with practice. To practice dealing with merge conflicts, you want to have two copies of your
repository in separate directories, then try editing the same
lines of the same files. You can follow along with the examples
shown here, or come up with your own. Up next, we'll talk about using
branches with a remote repositories.

### Pushing remote branches

As we called up before, when using Git to work on a new feature or a big
refactor of some kind, it's recommended best practice to create separate branches. There are many advantages
to doing this. For example, it might
take you a while to finish a new feature
and in the meantime, there could be a
critical bug that needs fixing in the main
branch of the code. By having separate branches, you can fix the bug
in the main branch, release a new version and
then go back to working on your feature without having to integrate your code
before it's ready. Another advantage of working in separate branches
is that you could even release two or more
versions out of the same tree. One being the stable version and the other being
the beta version. That way, any disruptive
changes can be tested on a few users or computers
before they're fully released. So let's start a new
branch to work on a small refactor of our code. Do you
remember how to do that? You could create
the branch first, and then check it out or we can just create
it and check it out with git checkout-b and
the new branch name. We're ready to start
working on our refactor. Let's open up the file,
and have a look at it. We've noticed there's
a pattern of repeating code in our all
checks pi script. For each check that we call, we check if it returns
true or false. When it returns true, we print an error and exit. If we add a new check, we'll have to repeat
this pattern again. On top of the repeated pattern, if a computer has more
than one problem, only the error for the
first one will be printed. So let's refactor
our code to avoid the duplication and print
all relevant errors. We'll do it step-by-step making each commit
self-contained. The first thing we'll do is create a function that
checks if the disk is full without any parameters
so it matches the pattern. This new wrapper function will pass the right parameters for us. Then we'll change the code to
call this function instead. We'll also change
the error message to something more accurate. We've changed the function, let's save and test our code. Awesome, it's working. Let's commit the change. We're ready for the next
step in our refactor. To avoid code repetition, we'll create a list
containing the names of the functions that
we want to call, and then message to print
if the function succeeds. After that, we'll
add a for loop that iterates over the list
of checks and messages. Then we'll call check, and if the return value is true, print the message and exit
with an error code of one. After doing that we can delete the old code that we've
already replaced. With this change made, let's save once again and tests that our script still runs. Yes, it's still working. Let's commit the new change. By now, we've re-factored our code to avoid
code duplication. The current code does the
same as the old code. Once we're ready
to add new checks, we can do that by adding the function name and error message to
the list of checks. The last change that we want to do is to let our script show more than one message if more
than one check is failing. To do that, we add
a Boolean variable called "Everything Ok"
before the iteration. Changes variable to false if one of the checks
finds a problem, and then exit with an error code only after having
done all the checks. All right, one last time. Let's save and test
to see if this works. Let's now do a file
commit for this change. With that, we have three commits
and our refactor branch. Before we merge any of this
into the master branch, we want to push this
into the remote repo, so that our collaborators
can view the code, test it, and let us know
if it's ready for merging. The first time we push a
branch to a remote repo, we need to add a
few more parameters to the Git push command. We'll need to add the -u flag to create the branch upstream, which is another way of referring
to remote repositories. We'll also have to
say that we want to push this to the origin repo, and that we're pushing
the refactor branch. Whoa, that's a lot of information
that Git's giving us. It's telling us if we want, we can create a pull request. We'll talk more about
pull requests later on. For now, we're happy to see that new refactor branch has been created in the remote repo,
which is what we wanted. This was a super
complex example that incorporated a lot of concepts that we've learned
about in this course, and also carried out some
interesting Python concepts. If anything is still unclear, feel free to re-watch this
video and follow along in your computer until you're comfortable
with these steps. So now that our branch is
pushed to the remote repo, it can be reviewed by
our collaborators. Assuming they say it's okay, how should this branch get merged back into
the master branch? We'll talk about that
in our next video.

### Rebasing your changes

[MUSIC] In our last video, we mentioned that once
our branch has been properly reviewed and tested, it can get merged
back into the master branch. This can be done by us or by someone else. One option is to use the git merge
command that we discussed earlier. Another option is to use
the git rebase command. Rebasing means changing the base
commit that's used for our branch. To understand what this means, let's quickly recap what we've
learned about merges up till now. As we've seen in a lot
of our earlier examples, when we create a branch at a certain
point in the repo's history, Git knows the latest commit that
was submitted on both branches. If only one of the branches has new
changes when we try to merge them, Git will be able to fast forward and
apply the changes. But if both branches have new
changes when we try to merge, Git will create a new merge commit for
the three way merge. The problem with three way merges is
that because of the split history, it's hard for us to debug when
an issue is found in our code, and we need to understand where
the problem was introduced. By changing the base where our
commits split from the branch history, we can replay the new commits
on top of the new base. This allows Git to do a fast forward
merge and keep history linear. So how do we do it? We run the command git rebase, followed by the branch that we
want to set as the new base. When we do this, Git will try to replay our commits
after the latest commit in that branch. This will work automatically if
the changes are made in different parts of the files, but will require manual intervention if
the changes were made in other files. Let's check out this process by
rebasing our refactor branch onto the master branch. First, we'll check out
the master branch and pull the latest changes
in the remote repo. Git tells us that it's updated the master
branch with some changes that our colleague had made. At this point, the changes that we have
in the refactor branch can no longer be merged through fast forwarding
into the master branch. That's because there's now
an extra commit in the master that's not present in the refactor. Let's see how this looks by asking the log
command to show us the current graph of all branches. It might take a bit to follow everything
that's going on with this graph. But it can be really useful to
understand complex history trees. As you can see, the refactor branch has
three commits before the common ancestor, with the current commit that's at
the head of the master branch. If we merged our branch now,
it would cause a three way merge. But we want to keep our history linear. We'll do this with a rebase of
the refactor against master. As usual, Git gives us a bunch
of helpful information. It says that it rewound head and
replayed our work on top of it. And luckily, everything succeeded. Let's look at the output of
git log --graph --oneline for our branch right now. Now we can see the master branch and
linear history with our list of commits. We're ready to merge our commits back
onto the main trunk of our repo and have this fast forwarded. To do that, we'll check out the master
branch and merge the refactor branch. Awesome, we were able to merge our
branch through a fast forward merge and keep our history linear. We're now done with our refactor and can get rid of that branch,
both remotely and locally. To remove the remote branch, we'll call
git push --delete origin refactor. To remove the local branch,
we'll call git branch -d refactor. Yes, we're done with our refactor. We can now push changes
back into the remote repo. All right, we've just gone through
an example using the git rebase command. We had a feature branch created
against an older commit from master. So we rebased our feature branch against
the latest commit from master and then merged the feature
branch back into master. That was a complicated exercise. So if you're still confused about what's
going on, take your time to review, and maybe come up with your own
examples when you'd use a rebase. Up next, we'll look at another
example of how to use rebase.

### Another rebasing example

In our last video, we looked at an example use case
for git rebase. Where we used it to rebase a feature branch so that it
could be cleanly integrated. There are many other
possible uses of rebase. One common example is to rebase the changes
in the master branch when someone else also made changes and we want to
keep history linear. This is a pretty
common occurrence when you're working on
a change that's small enough not to need a
separate branch and your collaborators just happened to commit something
at the same time. Let's check out how this
would work in practice. First, we'll make a
change to our script. Now that we've made it
easy to add new checks, will add a check to warn when
there's no working network. There's a ton of things to check for this but for now we'll keep it simple and just
check whether we can resolve the google.com URL. To do this, we'll use
the socket module. We'll add a new
function called check no network that will return true if it fails to resolve the URL and false if it succeeds. This socket.gethostbyname
function raises an exception on failure. So we'll use it try except
block to wrap the call to the function and
return false when the call succeeds or
true when it fails. With this new function defined, we can now add the check
to our list of checks. We'll just add the name of the function and the message will be, "No working network." We've made the change, let's
save it and commit it. Once more we'll use the
git commit -a shortcut and pass a message saying that we've added a simple network
connectivity check. We want to check if one of our teammates also made a change in the master branch while we
were working on our change. In an earlier video, we showed how to do that
by running git pull which will automatically create a
three-way merge if necessary. In this example,
we want to look at a different approach to keep
our project history linear. So we'll start by calling git fetch which you might
remember we'll put the latest changes
into the origin slash master branch but we won't apply them to our
local master branch. We see that we fetched
some new changes. This means that if we tried
to merge our changes, we end up with a three-way merge. Instead, we'll now run
git rebase against our origin/master to
rebase our changes against those made by our colleague and
keep history linear. We've got a conflict and
we'll need to fix it. Git is giving us a
lot of info on what it tried to do
including what worked, what didn't work and
what we can do about it. Since we asked it to rebase, it tried to rewind our
changes and apply them on top of what was in the
origin/master branch. The first commit made
by our colleague, renamed all_checks.py
to health_checks.py. Git detected this
and automatically merged our changes into
the new file name. But when trying to
merge our changes with the changes made by our
colleague in the file, there was a merge conflict. The output gives us a bunch of instructions on
how to solve this. We could fix the conflict, skip the conflicting commit or even abort the
rebased completely. In this example, we want
to fix the conflict. So let's do that. We'll
start by looking at the current state of the
health_checks.py file. We see that while we were
adding the connectivity check, our colleague was adding a check for the CPU
being constrained. We want both functions
and the end result. So let's remove the
conflict markers, cleaning up our file. This looks good. Let's save
and test our script out. So close it looks like
our colleague forgot to import the psutil module.
Let's do that now. Let's hope this works. We fix the conflict and our
script is working again. We now need to add the
changes made to the health_checks.py file and
continue with the rebase. Now, the rebase has finished successfully let's
check out the output of git log --graph --oneline to see what the history
looks like at this point. We see that we've applied
our change on top of the other changes without
needing a three-way merge. What we did just now to
resolve the conflict is very similar to what we did
earlier to merge our changes. The difference is, that
the commit history ended up being linear
instead of branching out. We're now ready to push our
new check to the remote repo. In this example, we've
seen how we can use the fetch rebase push workflow to merge our changes with
our collaborators changes while keeping the
history of our changes linear. As we called out, keeping history linear helps with
debugging especially when we're trying to
identify which commit first introduced a
problem in our project. We've now seen two examples of how to use the
git rebase command. One for merging feature
branches back into the main trunk of our code
and one for making sure that our commits made in the master branch
apply cleanly on top of the current state of the master branch and
it doesn't stop there. We can also use git rebase
to change the order of the commits or even squash
two commits into one. This is a very powerful tool but don't worry you don't need to memorize all of its possible uses you'll learn them
as you need them. Up next, we'll do a
round up of some of the best practices for operating with git when
collaborating with others.

### Best practices for collaboration

[MUSIC] Over the past few videos, we've looked at
a lot of things we can do with Git and remote repositories. It's worth spending some time
talking about best practices for collaborating with others. It's a good idea to always synchronize
your branches before starting any work on your own. That way,
whenever you start changing code, you know that you're starting
from the most recent version and you minimize the chances of conflicts or
the need for rebasing. Another common practice is to try and avoid having very large changes that
modify a lot of different things. Instead, try to make changes as
small as possible as long as they're self-contained. For example, if you are renaming
a variable for clarity reasons, you don't want to have code that adds
new functionality in the same commit. It's better if you split
it into different commit. This makes it easier to understand
what's going on with each commit. On top of that, if you remember
to push your changes often and pull before doing any work, you reduce
the chances of getting conflict. We called out already that
when working on a big change, it makes sense to have
a separate feature branch. This lets you work on new changes
while still enabling you to fix bugs in the other branch. To make the final merge of the feature
branch easier, it makes sense to regularly merge changes made on the master
branch back onto the feature branch. This way, we won't end up with
a huge number of merge conflicts when the final merge time comes around. If you need to maintain more than one
version of a project at the same time, it's common practice to have
the latest version of the project in the master branch and a stable version
of the project on a separate branch. You'll merge your changes into
the separate branch whenever you declare a stable release. When using these two branches,
some bug fixes for the stable version may be done
directly on the stable branch if they aren't relevant to
the latest version anymore. In the last couple of videos, we looked at how we can use rebase
to make sure our history is linear. Rebasing can help a lot with identifying
bugs, but use it with caution. Whenever we do a rebase,
we're rewriting the history of our branch. The old commits get replaced with new
commits, so they'll be based on different snapshots than the ones we had before and
they'll have completely different hash sums. This works fine for local changes,
but can cause a lot of trouble for changes that have been published and
downloaded by other collaborators. So as a general rule, you shouldn't rebase changes that
have been pushed to remote repos. The Git server will
automatically reject pushes that attempt to rewrite
the history of the branch. It's possible to force Git
to accept the change, but it's not a great idea unless you really
know what the implications will be. In our feature branch example,
we rebased the branch. Merged it to the master and
then deleted the old one. That way, we didn't push the rebase
changes to the refactor branch, only to the master branch that
hadn't seen those changes before. Early in our Git journey, we mentioned that having good
commit messages is important. It's already important
when you're working alone since good commit messages help the future
you understand what's going on, but it's even more important when
you're collaborating with others since it gives your collaborators more
context on why you made the change and can help them understand how to
solve conflicts when necessary. So commit to being a good collaborator and
remember to add those commit messages. Whenever we collaborate with others, there's bound to be some merge
conflicts and they can sure be a pain. I've definitely been frustrated when
encountering complex merge conflicts and trying to debug the results. If I'm dealing with this type of merge
conflict, my first step is to work backward and disable everything I've done
and then see if the source still works, then I slowly add pieces of
code until I hit the problem. That usually gets me
through the tough times and has definitely highlighted
some weird occurrences. Up next, we have a reading that puts
together all the commands related to solving conflicts and
then a quick practice quiz.

### Conflic resolution cheat-sheet

Merge conflicts are not uncommon when working in a team of developers, or on Open Source Software. Fortunately, GitHub has some good documentation on how to handle them when they happen:

- https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts
- https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line

You can also use git rebase branchname to change the base of the current branch to be branchname

The git rebase command is a lot more powerful. Check out this link for more information.
