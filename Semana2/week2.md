# Week 2 - Using Git locally

## Advanced Git interaction

### Skipping the stagging area

If we already know that the current changes are the
ones that we want to commit, we can skip the staging step and go directly to the commit. We do this by using the `-a` flag to the git commit command. This flag automatically stages every file that's tracked and modified before doing the commit letting it skip the git add step. 

At first, you might think
that `git commit -a` is just a shortcut for
git add followed by git commit but that's
not exactly true. Git commit -a doesn't work on new files because
those are untracked. Instead, git commit -a
is a shortcut to **stage any changes to tracked files and commit them in one step**. 
If the modified file has never been committed to the repo, we'll still need to use
git add to track it first. 

These
shortcuts are useful when making small changes
that we know we'll want to commit directly
without keeping them in the staging area
and having to write long and complex descriptions. 

Keep in mind that when
you use the -m shortcut, you can only write short
messages and can't use the best practices regarding commit descriptions. So it's best reserved for
truly small changes that don't require extra context or explanation. 

Heads up, when you
use the -a shortcut, **you skip the staging area**. Meaning, you can't add any other changes before
creating the commit. So you need to be sure
that you've already included everything you want
to include in that commit. 

In the end, using a shortcut like -a is just like using the
regular commit workflow. The commit will
show up in the log along with the message
just as usual. 

Our latest commit will be added to the top of the list of
commits and notice how the **HEAD** indicator has now
moved to the latest commit. You might be wondering, what is this HEAD and
where is it heading? Git uses the HEAD
alias to represent the **currently checked out snapshot of your project**. 

This lets you know
what the contents of your working
directory should be. In this case, the
current snapshot is the latest commit
in the project. We'll soon learn about branches. In that case, HEAD can be a commit in a different
branch of the project. 

We can even use Git to go
back in time and have HEAD representing old commit from before the latest
changes were applied. In all cases, HEAD is used to indicate what the currently
checked out snapshot is. This is how Git marks your
place in the project. 

Think about it as a
bookmark that you can use to keep track
of where you are. Even if you have
multiple books to read, the bookmark allows you to pick up right where you left off. 


When you run Git commands
like diff, branch, or status, Git will use the HEAD bookmark as a basis for whatever
operation it's performing. It's
generally easy to think of HEAD as a **pointer to the current branch**, although it can be more
powerful than that. 

### Getting more information about our changes

We've seen how git log shows us the list
of commits made in the current Git repository. By default, it prints the commit message,
the author, and the date of the change. This is useful, but
if we're combing through a history of changes in a repo to try and
find what caused the latest outage, we'll probably also need to look at the
actual lines that changed in each commit. 

To do this with git log,
we can use the `-p flag`. The p comes from patch, because using this
flag gives us the patch that was created:

```
$ git log -p
```
The format is equivalent to the diff-u
output. It shows added lines with plusses and
remove lines with dashes. Because the amount of text is now
longer than what fits on your screen, Git automatically uses a paging tool
that allows us to scroll using page up, page down, and the arrow keys. 

We still have one commit below the other,
but now each commit takes up
a different amount of space, depending on how many lines were added or
removed in that commit. 

Using this option, we can quickly see what changes were
made to the files in our repository. This can be especially useful if we're
trying to track down a change that recently broke our tools. 

If we don't want to scroll down until
we find the commit that we're actually interested in, another option
is to use the `git show` command. This command takes a commit
ID as a parameter, and will display the information about
the commit and the associated patch. 

For now, remember that this ID is an identifier that
we see next to the word commit in the log. 

We've shown how we can use `git log` for
listing commits, and `git log -p` for showing the associated patches. Another interesting flag for
git log is the `--stat flag`. This will cause git log to show some
stats about the changes in the commit, like which files were changed and
how many lines were added or removed:

```
$ git log --stat
```
There are a bunch of other options to
git log. You can always use
the reference documentation or the manual pages to find out more. 

And as we called up before,
you don't need to memorize any of this, you'll learn the different commands and
flags by using them. The important thing to remember is
that all the information is stored in the repository and you have it at
your fingertips when you need it. 

What about changes that
haven't been committed yet? Until now, whenever we've made
changes to our files, we've either added them to the staging area with 
`git add` and committed them with `git commit`, or committed them directly
using `git commit -a`. This works fine, but it means we have to
know exactly which changes we've made. Sometimes it can take a while
until we're ready to commit. 

Imagine you've been working on adding
a new complex feature to a script and it requires thorough testing. Before committing it, you need to
make sure that it works correctly. Check that all the test cases
are covered and so on and so on. So while doing this you find bugs
in your code that you need to fix. It's only natural that by the time
you get to the commit step you don't really remember
everything you changed. 

To help us keep track git
gives us the `git diff` command. Let's make a new change to our script and
then try this command out. 

```
$ git diff
```

Again, this format is equivalent to
the `diff -u` output that we saw. If our change is big and included several files, we could pass
a file by parameter to see the differences relevant to that specific file instead
of all the files at the same time. 

Something else we can do to review changes
before adding them is to use the `-p` flag with the git add command. When we use this flag, git will
show us the change being added and ask us if we want to stage it or not. This way we can detect if there's any
changes that we don't want to commit. 

We've staged our change and
it's now ready to be committed. If we call `git diff` again,
it won't show any differences, since git diff shows only
unstaged changes by default. Instead, we can call `git diff -- staged`
to see the changes that are staged but not committed. With this command, we can see the actual
stage changes before we call git commit. 

### Deleting and renaming files

Let's say that you've decided
to clean up some old scripts and want to remove them from your repository. Or you've done some refactoring, which
makes that particular file, obsolete. You can remove files from your repository
with the `git rm` command, which will stop the file from being tracked by
git and remove it from the git directory. 

File removals go through the same
general workflow that we've seen. So you'll need to write a commit
message as to why you've deleted them. 

Well first look the contents
of the directory with ls, then delete the file with git rm,
then check the contents with ls again, and finally check the status with git status. 

So, we'll see that by calling `git rm`, the
file was deleted from the directory, and the change was also staged to be
committed in our next commit by calling `git commit` and sending a message indicating that
we've deleted the unneeded file. 

As usual, we get a bunch of
stats when we do the commit. Check out all the deletions that reported. These are all lines in the file
that are no longer there. And it states the file itself was deleted. What if you have a file that
isn't accurately named? This can happen. For example, if you start writing a script
that you thought would only do one thing, and then expands to cover more use cases. Or conversely, if you named your script
thinking that it would be very generic, but it ends up being more specific. You can use the `git mv` command to
rename files in the repository:

```
$ git mv old_name new_name
```
Let's check what git status
has to say about that. The status shows us that the file was
renamed and clearly displays the old and new names. As with the previous example,
the change is staged, but **not committed**. Let's commit it by calling
`git commit` once again. 

The git mv command works in a similar
way to the mv command on Linux and so can be used for
both **moving and renaming**. If our repository included
more directories in it, we can use the same git mv command
to move files between directories. 

As you can probably tell from
our examples, the output of `git status` is a super useful tool to help
us know what's up with our files. It shows us which files have tracked or
untracked changes, and which files were added,
modified, deleted or renamed. It's important that the output of
these commands stays relevant to what we're doing. 

If we have a long list of untracked files, we might lose an important
change in the noise. If there are files that get automatically
generated by our scripts, or our operating system generates artifacts
that we don't want in our repo, we'll want to ignore them so that they don't
add noise to the output of `git status`. To do this, we can use the **gitignore file**. Inside this file, we'll specify rules
to tell git which files to skip for the current repo. 

For example,
if we're working on an OSX computer, we'll probably want to ignore
the dot DS store file, which is automatically generated
by the operating system. To do this, we'll create a .gitignore
file containing the name of this file. Remember that the dot prefix
in a Unix-like file system indicates that the file or directory is hidden and won't show up
when you do the normal directory listing. That's why we have to use
ls -la to see all files. 

We've added a gitignore file to our
repo but we haven't committed it yet. This file needs to get tracked just
like the rest of the files in the repo.

### Advanced Git cheat sheet

| Command |	Explanation & Link |
|---------|--------------------|
| git commit -a	| [Stages files automatically](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---all) |
| git log -p |	[Produces patch text](https://git-scm.com/docs/git-log#_generating_patch_text_with_p) |
| git show	| [Shows various objects](https://git-scm.com/docs/git-show) |
| git diff |	[Is similar to the Linux `diff` command, and can show the differences in various commits](https://git-scm.com/docs/git-diff) |
| git diff --staged	| [An alias to --cached, this will show all staged files compared to the named commit](https://git-scm.com/docs/git-diff) |
| git add -p | [Allows a user to interactively review patches to add to the current commit](https://git-scm.com/docs/git-add) |
| git mv |	[Similar to the Linux `mv` command, this moves a file](https://git-scm.com/docs/git-mv) |
| git rm |	[Similar to the Linux `rm` command, this deletes, or removes a file](https://git-scm.com/docs/git-rm) |

There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as [this one](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf).

#### .gitignore files

.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at: https://git-scm.com/docs/gitignore.

A few common examples of file patterns to exclude can be found [here](https://gist.github.com/octocat/9257657).

## Undoing things

### Undoing changes before committing

Being able to revert
our changes is one of the most powerful features offered by version
control systems. There's a bunch of different
techniques available depending on which
changes we need to undo. In this video and the
next few coming up, we'll talk about the most
common ways to revert changes in Git and when
to use each approach. For example, you might find yourself in a
situation where you've made a bunch of changes to a file but decide that you
don't want to keep them. You can change a file back to its earlier committed
state by using the git checkout command followed by the name of the
file you want to revert. Speaking of, let's try this out using our scripts repository. We'll edit our all
checks pi script and remove the check
reboot function, then save and go back
to the command line. Cool. We've made our change. Let's try our script
and see what happens. By deleting that function, we've actually broke the script. Let's see what git status
has to say about this. As expected, we see that our file is modified and the
changes aren't staged yet. Check out how git gives us a couple helpful tips
on what to do now. We can run git add to stage our changes or we can run git
checkout to discard them. If you need help remembering
what this command does, think of it this way, you're checking out
the original file from the latest storage
snapshot. Let's do that now. We'll check out at
the original file and then take a look at what git status has to say about it and finally retry our script. Looks like we have a typo. Let's go back and fix it. Done and done. With that, we've demonstrated how we
can use git checkout to revert changes to modify
files before they get staged. This command will restore the file to the latest
storage snapshot, which can be either
committed or staged. So if you've made additional changes to a file
after you've staged it, you can restore the file to
the earlier stage version. If you need to check
out individual changes instead of the whole file, you can do that using
the dash p flag. This will ask you
change by change if you want to go back to the
previous snapshot or not. That's it for undoing
unstaged changes. What if you added the changes to the staging area
already? Don't stress. If we realize we've
added something to the staging area that we didn't
actually want to commit, we can unstage our changes by using the git reset command. Staging changes that we don't actually intend to commit
happens all the time. Especially if we use a
command like git add star, where the star is a
file glob pattern used in Bash that
expands to all files. This command will end
up adding any change done in the working tree
to the staging area. While sometimes that
might be what we want, it can also lead
to some surprises. Let's try it out with an example. First, we'll pretend we're trying to debug a problem in our script. For that, we create a temporary file with the
output of our script. Then, we'll add all
unstaged changes in our working tree
using git add star. Finally, check the
status using git status. We can see that this output file, which was supposed to be a
temporary file for debugging, has now been staged in our repo but we didn't
want to commit it. Conveniently, the git
status command tells us how to unstage the file
right there in the output. The example output
mentions the head alias. Remember what that means? That's right. It's the
current checked out snapshot. So by running the
suggested command, we're resetting our
changes to whatever's in the current snapshot.
Let's try it out. The file is once
again untracked in our working tree and
no longer staged. You can think of reset as
the counterpart to add. With add, you can well add
changes to the staging area. With reset, you remove changes
from the staging area. You can use git
reset dash p to get git to ask you which specific
changes you want to reset. Get it. But wait, let's remember to
commit our typo fix. With that, we've seen
how we can revert unstaged and stage changes. But what if you've
already created a commit with the changes that
you want to undo? Great question. That's
coming up in the next video.

### Amending commits

### Rollbacks

### Identifying a commit

### Git revert cheat sheet

## Branching and merging

### What is a branch

### Creating new branches

### Working with branches

### Merging

### Git branches and merging cheat sheet