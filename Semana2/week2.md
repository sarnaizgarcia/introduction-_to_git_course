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

| Command           | Explanation & Link                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| git commit -a     | [Stages files automatically](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---all)                         |
| git log -p        | [Produces patch text](https://git-scm.com/docs/git-log#_generating_patch_text_with_p)                                        |
| git show          | [Shows various objects](https://git-scm.com/docs/git-show)                                                                   |
| git diff          | [Is similar to the Linux `diff` command, and can show the differences in various commits](https://git-scm.com/docs/git-diff) |
| git diff --staged | [An alias to --cached, this will show all staged files compared to the named commit](https://git-scm.com/docs/git-diff)      |
| git add -p        | [Allows a user to interactively review patches to add to the current commit](https://git-scm.com/docs/git-add)               |
| git mv            | [Similar to the Linux `mv` command, this moves a file](https://git-scm.com/docs/git-mv)                                      |
| git rm            | [Similar to the Linux `rm` command, this deletes, or removes a file](https://git-scm.com/docs/git-rm)                        |

There are many useful git cheatsheets online as well. Please take some time to research and study a few, such as [this one](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf).

#### .gitignore files

.gitignore files are used to tell the git tool to intentionally ignore some files in a given Git repository. For example, this can be useful for configuration files or metadata files that a user may not want to check into the master branch. Check out more at: https://git-scm.com/docs/gitignore.

A few common examples of file patterns to exclude can be found [here](https://gist.github.com/octocat/9257657).

## Undoing things

### Undoing changes before committing

Being able to revert our changes is one of the most powerful features offered by
version control systems. There's a bunch of different techniques available depending
on which changes we need to undo.

For example, you might find yourself in a situation where you've made a bunch of
changes to a file but decide that you don't want to keep them. You can change a
file back to its earlier committed state by using the `git checkout` command
followed by the name of the file you want to revert. So if you've made additional
changes to a file after you've staged it, you can restore the file to the earlier
stage version.

If you need to check out individual changes instead of the whole file, you can do
that using the `-p` flag. This will ask you change by change if you want to go back
to the previous snapshot or not. That's it for undoing unstaged changes.

What if you added the changes to the staging area already? If we realize we've added
something to the staging area that we didn't actually want to commit, we can unstage
our changes by using the `git reset` command. Staging changes that we don't actually
intend to commit happens all the time, especially if we use a command like `git add *`,
where the star is a file glob pattern used in Bash that expands to all files.

This command will end up adding any change done in the working tree to the staging area.
While sometimes that might be what we want, it can also lead to some surprises.

You can use `git reset -p` to get git to ask you which specific changes you want to
reset.

### Amending commits

In general, we try to
make sure our commits include all the right
changes and descriptions. But we're all human
and we make mistakes. It's not uncommon
for developers and IT specialists to
realize that there is an error in a recent commit, which is why it's important to know how to take
action and fix it. Let's say you just
finished committing your latest batch of work, but you've forgotten
to add a file that belongs to the same change. You'll want to update the
commit to include that change. Or maybe the files were correct, but you realize that
your commit message just wasn't descriptive enough. So you want to fix
the description to add a link to the bug that you're solving with that
commit. What can you do? We can solve problems
like these using the --amend option of
the git commit command. When we run git commit --amend, git will take whatever is currently in our staging area and run the git commit workflow to overwrite
the previous commit. Let's see this in an example. We'll go to our
scripts directory and create two new files
using the touch command. Then list the contents of
the directory using ls at our Python script and commit it saying that we've
added two files. As you can see, the
message printed by git says that only
one file was added. Our commit message said
that we added two files, but we forgot to add one of them. Ouch. Don't panic. We can fix it. We'll start by adding
the missing file and then amending our commit. We call git commit --amend
and an editor opened up showing the commit message and the stats about the commit
that we're working with. The list of added
files for this commit now includes both files
that we wanted to add. Yay. Now that the
files have been added, we can also improve our initial commit message
which was a bit too short. We'll keep the
existing description as the first sentence
of our commit, and then add a line
of description about the intended
purpose of each file. With that, our commit
is ready to be amended. Let's save the new
description as usual. We've amended our
previous commit to include both files
and a better message. You could also just
update the message of the previous commit
by running the git commit --amend command with no changes in the staging
area. An important heads up. While git --amend is okay
for fixing up local commits, you shouldn't use it
on public commits. Meaning, those that
have been pushed to a public or shared repository. This is because using
--amend rewrites the git history removing the previous commit and replacing it with
the amended one. This can lead to some
confusing situations when working with other people and should definitely be avoided. So remember, fixing up a
local commit with amend is great and you can push it to a shared repository
after you fixed it. But you should avoid amending commits that have already
been made public. If this sounds confusing
now, don't worry. We'll mention it again
when we talk about collaborating with others
through shared repositories. We've covered how to fix
staged and unstaged changes, and how to fix a commit
that was incomplete. Up next, we'll talk about
what to do if you come across a bad commit that needs
to be completely reverted.

### Rollbacks

Fixing your work before
you commit is good. But what happens if it's already
been snapshotted by Git? Let's say you host
to Git repository on a company server that contains all kinds of useful
automation scripts that you and your coworkers use. One morning before coffee, you make a few changes to one of these scripts and commit
the updated files. A few hours later, you start to receive
tickets from users indicating some part of
the script is broken. From the errors they describe, it sounds like the problem is related to your recent changes. Oh, you could look at the code you updated to see
if you can spot the bug. But more tickets are
pouring in and you want to fix the problem
as fast as possible. You decided it's
time for a rollback. There are a few ways to
rollback commits in Git. For now, we'll focus on using
the git revert command. Git revert doesn't
just mean undo. Instead, it creates a commit
that contains the inverse of all the changes made in the bad commit in order
to cancel them out. For example, if a particular line was
added in the bad commit, then in the reverted commit, the same line will be deleted. This way you get the effect
of having undone the changes, but the history of the commits
in the project remains consistent leaving a record
of exactly what happened. So git revert will
create a new commit, that is the opposite of
everything in the given commit. We can revert the
latest commit by using the head alias that
we mentioned before. Since we can think
of head as a pointer to the snapshot of
your current commit, when we pass head to the
revert command we tell Git to rewind that current
commit, makes sense? To check this out,
we'll first add a faulty commit to
our example repo. We've added some
code to our script. Let's save and commit this. So now, our code is committed. We didn't even test it which is a bad idea if you're
doing this for real. You might have already spotted
the problem with our code. This is where users start filing tickets and saying that
things are broken, and so we run our script
to see what happens. Oops, we use the function
that we forgot to define. Okay. It's rollback time. Let's get rid of
this faulty code by typing git revert head. So once we issue that
git revert command, we're presented with
the text editor commit interface that
we've all seen before. In this case, we can see
that git has automatically added some text to the command indicating it's a rollback. The first-line mentions that
it's reverting the commit we just did called Add call
to disk full function. The extra description even includes the identifier of
the commit that got reverted. While we could use this
description as is, it's usually a good idea to add an explanation of why
we're doing the rollback. Remember that the goal of
these descriptions is to help our future selves
understand why things happen. In this case, we'll explain
that the reason for the rollback is that the code was calling a function
that wasn't defined. Once we're done entering
the description, we can exit and save as usual. You'll notice the output that
we get from the git revert command looks like the output
of the git commit command. This is because git revert
creates a commit for us. Since a revert is
a normal commit, we can see both the commit and the reverted
commit in the log. Let's look at the last
two entries in the log using dash P and dash
two as parameters. As demonstrated before, the dash P parameter lets
us see the patch created by the commit while the dash two perimeter limits the output
to the last two entries. So in this log, we can see that when
we called revert, git created a new commit that's the inverse
of the previous one. This removes the lines that we added in the previous commit. We can see that the
original commit shows the lines we added by preceding
them with a plus sign. The same line shows up
with a minus sign in the newer commit message indicating that
they were removed. Just like that, the bad commit is reverted and the error stopped. In this example, we reverted the latest
commit in our tree. But what if we had to revert a commit that was
done before that? Rev up your time machines
because in the next video, we're turning back
the clock big-time.

### Identifying a commit

[MUSIC] So far we've used the head alias to
specify the most recently checked out commit in our Git history. In our bad snapshot example,
the error also happened to be in the most recently created commit, but errors can
sometimes take a while to be detected. And so, we might need to revert
other commits farther back in time. We can target a specific
commit by using its commit ID. We've seen commit IDs a few times already. They show up when we're running
the git log command, and we also saw the commit ID of
the reverted commit in our last example. Commit IDs are those complicated looking
strings that appear after the word commit in the log messages. Let's have a look at the latest
log entry in our checks repo. The commit ID is the 40 character
long string after the word commit, you really can't miss it. This long jumble of letters and numbers
is actually something called a hash, which is calculated using
an algorithm called SHA1. Essentially, what this algorithm does
is take a bunch of data as input and produce a 40 character string
from the data as the output. In the case of Git, the input is all
information related to the commit, and the 40 character string is the commit ID. Cryptographic algorithms like
SHA1 can be really complex, so we won't go too deep into what this means. If you're interested, you'll find links
to more information in the next reading. Still you might be wondering, why on earth
would you use a long jumble of letters as an ID for commit, instead of
incrementing an integer, like 123, etc? To answer that, let's take a quick look at the reason why Git uses a hash instead of
a counter, and how that hash is computed. Although SHA1 is a part of the class
of cryptographic hash functions, Git doesn't really use these hashes for
security. Instead, they're used to guarantee
the consistency of our repository. Having consistent data means that
we get exactly what we expect. To quote Git's creator, Linus Torvalds, you can verify the data you get back
out is the exact same data you put in. This is really useful in distributed
systems like Git because everyone has their own repository and
is transmitting their own pieces of data. Computing the hash keeps
data consistent because it's calculated from all
the information that makes up a commit. The commit message, date, author, and
the snapshot taken of the working tree. The chance of two different
commits producing the same hash, commonly referred to as a collision,
is extremely small. So small, it wouldn't happen by chance. It'd take a lot of processing power
to cause this to happen on purpose. If you use a hash to
guarantee consistency, you can't change anything in the Git
commit without the SHA1 hash changing too. Remember our discussion about fixing
commits with the dash dash amend command? Each time we amend a commit,
the commit ID will change. This is why it's important
not to use dash dash amend on commits that have been made public. The data integrity offered by the commit
ID means that if a bad disk or network link corrupt some data in
your repository, or worse, if someone intentionally corrupt some data, Git can
use the hash to spot that corruption. Aha, it will say, the data you've
got isn't the data you expected, something went wrong. Thank you, Detective Git,
you've saved the day once again. Okay, enough backstory. How can you use commit IDs to specify
a particular commit to work with, like during a rollback? Let's look at the last two entries in
our repo using the git log -2 command. Say we realized that we actually liked
the previous name of our script, and so we want to revert this
commit where we renamed it. First, let's look at that
specific commit using git show, which we mentioned in an earlier video. We've copied and pasted the commit ID that
we wanted to display, and that works. Alternatively, we could provide just
the first few characters identifying the commit to the command, and Git will
be smart enough to guess which commit ID starts with those characters, as long as
there's only one matching possibility. Let's try this out. Two characters is not enough, but usually
four to eight characters will be plenty. Okay, now that we've seen how we can
identify the commit that we want to revert, let's call the git revert
command with this identifier. As usual, this will open an editor where
we should add a reason for the rollback. In this case, we'll say that
the previous name was actually better. Hooray for flip-flopping. As we called out before,
when we generate the rollback, Git automatically includes the ID
of the commit that we're reverting. This is useful when looking at
a repo with a complicated history that includes a lot of commits. Now, once we save and
exit the commit message, Git will actually perform the rollback and
generate a new commit with its own ID. See how before the name of our commit
the revert command already shows the first eight characters of the commit ID? Let's use git show to look at it. All right, we've managed to revert
a commit that wasn't the most recent one. Well done, time travelers. Over the past several videos we've covered
a bunch of ways to undo things in Git. Whether for unstaged changes,
staged changes, amending commits, or rolling back changes. If anything still seems unclear, now's a great time to practice these
commands on your local computer, try things out, and come up with more
examples of use cases you want to test. Up next, we've spun up a handy
cheat sheet summarizing all the content we just covered. When you're ready,
move on to the next quiz and put all this new knowledge into practice. We've been learning a lot of complex
things over the past few videos, so once you're done with that quiz
you should reward yourself for getting through this technical
detail with a break. You earned it. Grab a coffee, tea, or snack and
let the concepts settle for a bit. I'll meet you over the next video.

### Git revert cheat sheet

[git checkout](https://git-scm.com/docs/git-checkout) is effectively used to switch branches.

[git reset](https://git-scm.com/docs/git-reset#_examples) basically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.

There are some other useful articles online, which discuss more aggressive approaches to [resetting the repo](https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html).

[git commit --amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend) is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

[git revert](https://git-scm.com/docs/git-revert) makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a [few ways](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1.

Feel free to read more here:

[https://en.wikipedia.org/wiki/SHA-1](https://en.wikipedia.org/wiki/SHA-1)
[https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/](https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/)

## Branching and merging

### What is a branch

Up until now, we've only
briefly mentioned branches. You might have seen the text on branch master and
commit messages, or you might remember
that we talked about branches in the context
of the head pointer. Branches are an important
part of the Git work flow. So we'll branch out and explore them more thoroughly
in the coming videos. So what is a branch? What is it used for? In Git, a branch at the most basic level is just a pointer to a
particular commit. But more importantly,
it represents an independent line of
development in a project. Of which the commit
it points to is the latest link in a chain
of developing history. The default branch that
Git creates for you when a new repository
initialized is called master. All of our examples and development have taken place
on this branch so far. The master branch
is commonly used to represent the known good
state of a project. When you want to
develop a feature or try something new
in your project, you can create a separate
branch to do your work without worrying about messing up this current working state. If this seems confusing, maybe an analogy will help. You can think of a Git project as an assignment your teacher
gives you in a class. You do all your work on the assignment in a
set of notebooks, each notebook representing
a different branch. You use some
notebooks to jot down rough drafts in experiments, but you keep one notebook
the master branch, in a tidy state and you copy the polish versions
of these drafts into it. No doodling in the master
note book, please. Branches make it really easy to experiment with new ideas
or strategies and projects. When you want to add a
feature or fix something, you can create a new branch and do your development there. You can merge back into
the master branch, when you've got
something you like, or discard your changes without negative impact if
they don't work out. In Git, branches are
used all the time, as a part of the normal
development workflow. As an example, think back to the problematic commit we
fixed in an earlier video. We added a call to the
disk full function, but forgot to actually
define the function. So we had to roll it back because our users
we're seeing errors. Knowing what we know now, we could have done that
work on a separate branch, maybe called something
like add disk full. In that case, we could
have iterated on our code there until it
was working correctly, without it effecting
the master branch. Only after the code is
ready to be deployed, we would merge those changes
back into the master branch. In the next few videos, we'll look into how to create new branches and merge their content into
the master branch. We'll also go over
what to do if you run into any scary
merge conflicts. Heads up, this is about to
get pretty complicated. So make sure that
you follow all of our exercises along
in your computer and keep practicing
coming up with new ways of using
branches and merging, until you're comfortable with
each of the steps we show.

### Creating new branches

As branches are essential
to how work is done in git, there's tons of different
ways to work with them. We can use the git
branch command to list, create, delete, and
manipulate branches. Running git branch
by itself will show you a list of all the
branches in your repository. Let's try it out in
our checks repo. Our list is looking pretty empty right now, but don't worry. Creating a branch is a snap. We do it by calling git branch with the name of the
new branch Let's create a new feature
branch and then list the branches
again with git branch. Our new branch was created
based on the value of head. Remember that this might not necessarily be the master branch. The list we get shows that we're still on the master branch. We can tell because the
current branch is indicated in the command's output with an asterisk in a different color. We'll look into other things that git branch lets us do
with branches later on, but right now we want to
switch to a new branch. To do that, we'll need to use
the git checkout command. We saw earlier how we
can use git checkout to restore a modified file
back to the latest commit. Checking out branches
is similar in that, the working tree is
updated to match the selected branch including both the files and
the git history. If this seems a bit confusing
at first, you're not alone. I also found it hard to wrap
my head around it first. But rest assured
that it will become clear after we use these
commands for awhile. It might help to remember that we use git checkout to check out the latest snapshot for both files and for
branches. All right. Let's switch to our
new feature branch by calling git checkout new feature, and then listing our
branches once again. Before we were working on the master branch but now that we've changed
to our new branch, the star has moved
to new feature. Creating a branch
and switching to it immediately is a
pretty common task. So common that git gives
us a useful shortcut to create a new branch and to switch to it in a single command. We can use the git checkout -b new branch to do
this. Take a look. See how the message says that we've switched to a new branch? Git created the new
branch and switched to it in just one command.
Super efficient. Now that we have our
shiny new branch, let's create a new file in. We'll create a new Python3 file, that will include the
usual shebang line and empty main function and
a call to that function. This file is empty because it's only the
beginning of our work. As it's in a separate branch, it's okay for it to
not be finished yet. Let's save our file and commit it to the
current branch now. We've added a commit in this branch and it's
looking better. Let's check the last
two entries in the log. We see the last two
commits in this branch. Notice how next to
the latest commit ID, git shows that this is
where head is pointing to and that the branch is
called even better feature. Next to the previous commit, git shows that both
the master and the new feature branches are pointing to that
snapshot of the project. In this way, we can see that the even better feature branch is ahead of the master branch. With that, we've seen how we can create new branches and
commit changes to them. You might say your knowledge
of branches has grown. Up next, we'll learn
even more things we can do to operate
with branches. So stick around.

### Working with branches

In our last video, we created
a new branch different than the master branch
and added a commit to it. Let's check out the current
status of our repo by calling git status and ls dash l. So we see that we're on a
clean working tree in the even better
feature branch, and that a new free
memory py file is in our working tree. Let's now change back to
the master branch using git checkout master and then lists the latest
two commits there. When we switch to a different
branch using git checkout, under the hood, git changes
where head is pointing. Thanks to this checkout, head went from pointing
to the latest commit in the even better feature branch to the most recent commit
of the master branch. The commit from even better feature doesn't show up at all, and the latest snapshot is the second entry
we've seen before. Remember that when
we switch branches, git will also change files
in our working directory or working tree to
whatever snapshot head is currently pointing at. Let's look at the current
contents of our directory. Free memory py isn't there. This demonstrates that when
we switch branches in git, the working directory and
commit history will be changed to reflect the snapshot of our project in that branch. When we check out a new
branch and commit on it, those changes will be added to the history of that branch. Since free memory py was
committed on another branch, it doesn't show up
in the history or working directory of
the master branch. One thing to note after
all this back and forth, is that each branch
is just a pointer to a specific commit in a
series of snapshots. It's very easy to
create new branches because there isn't any data that needs to be copied around. When we switch to another branch, we check out a different
commit and git updates both head and the contents
of our working directory. Head floats around with us. It's like a free spirit.
What a head trip. Okay. We've now seen how to create and switch
between branches. So what if we want to delete a branch that we
don't need anymore? We can do that by
using git branch dash d. Let's first list the
current branches in our repo and then get rid of the new feature branch by calling git branch dash d new-feature. Just like that, our
branch was trimmed. We can check with another call to git branch that is
not there anymore. If there are changes in the
branch we want to delete that haven't been merged back
into the master branch, git will let us
know with an error. Hopefully, git also
gives us the command to run if we were sure that we
wanted to delete the branch, even if it has unmerged changes. But we won't do that just yet. We actually want to merge those changes back
into the repo first. How do we do that? It's all
coming up in our next video

### Merging

In our last video, we created
a new branch different than the master branch
and added a commit to it. Let's check out the current
status of our repo by calling git status and ls dash l. So we see that we're on a
clean working tree in the even better
feature branch, and that a new free
memory py file is in our working tree. Let's now change back to
the master branch using git checkout master and then lists the latest
two commits there. When we switch to a different
branch using git checkout, under the hood, git changes
where head is pointing. Thanks to this checkout, head went from pointing
to the latest commit in the even better feature branch to the most recent commit
of the master branch. The commit from even better feature doesn't show up at all, and the latest snapshot is the second entry
we've seen before. Remember that when
we switch branches, git will also change files
in our working directory or working tree to
whatever snapshot head is currently pointing at. Let's look at the current
contents of our directory. Free memory py isn't there. This demonstrates that when
we switch branches in git, the working directory and
commit history will be changed to reflect the snapshot of our project in that branch. When we check out a new
branch and commit on it, those changes will be added to the history of that branch. Since free memory py was
committed on another branch, it doesn't show up
in the history or working directory of
the master branch. One thing to note after
all this back and forth, is that each branch
is just a pointer to a specific commit in a
series of snapshots. It's very easy to
create new branches because there isn't any data that needs to be copied around. When we switch to another branch, we check out a different
commit and git updates both head and the contents
of our working directory. Head floats around with us. It's like a free spirit.
What a head trip. Okay. We've now seen how to create and switch
between branches. So what if we want to delete a branch that we
don't need anymore? We can do that by
using git branch dash d. Let's first list the
current branches in our repo and then get rid of the new feature branch by calling git branch dash d new-feature. Just like that, our
branch was trimmed. We can check with another call to git branch that is
not there anymore. If there are changes in the
branch we want to delete that haven't been merged back
into the master branch, git will let us
know with an error. Hopefully, git also
gives us the command to run if we were sure that we
wanted to delete the branch, even if it has unmerged changes. But we won't do that just yet. We actually want to merge those changes back
into the repo first. How do we do that? It's all
coming up in our next video

### Merge conflicts

From time to time, we might find that both the branches we're trying to merge have edits to the same
part of the same file. This will result in something
called a merge conflict. Normally, Git can automatically
merge files for us. But when we have
a merge conflict, it will need a little help
to figure out what to do. To see how this would look, let's edit the free_memory.py file in the master
branch and replace the pass statement with a comment about what the
main function should do. Cool, we made the change so let's save it and commit it back
to our master branch. Next, Let's check out the even-better-feature
branch and make a change in the same place. In this case, we will replace the call to pass with
a call to print, saying that everything is okay. Now, we'll save this other change and commit it to this branch. We are primed for chaos with our file all setup
for a merge conflict. Let's check out the master
branch again and try to merge the even-better-feature
back into it. Git tells us it tried
to automatically merge the two versions
of the free memory file, but it didn't know how to do it. We can use Git's status to get more information about
what's going on. As usual, git status gives us a lot of
additional information. It tells us that we have files that are
currently unmerged, and that we need to
fix the conflicts or abort the merge if we
decide it was a mistake. It also tells us that we need to run Git add on each unmerged file to mark that the
conflicts have been resolved. Let's get to work. To fix the conflict, let's open up free_memory.py
in our text editor. Thankfully, Git has added
some information to our files to tell us which parts of the
code are conflicting. The unmerged content
of the file at head, remember, in this case, head points to master, is the docstring stating what the main function should do. The unmerged content
of the file in the even-better-feature branch is the call to the print function. It's up to us to decide
which one to keep or if we should change the contents of the
file altogether. In this case, we'll keep both statements and delete
the merger markers. Now that we've
fixed the conflict, we'll mark it as resolved by
running git add on the file, and then call the git status to see how our merge is doing. See how Git now tells us that all conflicts
have been resolved. Woo-hoo, we just need to call git commit to
wrap up the merge. The comments that
git commit shows us look different
than other commits. That's because this is a
merge and Git tells us so. It also tells us which file had conflicts which have
now been resolved. The commit already
has a description saying that it's merging
the other branch. This description
was automatically created when we called
the git merge command. But we can add onto this
description if we want. For example, we
can say that we're keeping the lines
from both branches, and then just save
and exit as usual. The merge conflict is resolved. To see what the commit
history looks like now, we'll use a couple of handy options to the
git log command; --graph for seeing the
commits as a graph, and --oneline to only
see one line per commit. This format helps us
better understand the history of our commits
and how merges have occurred. We can see the new commit
that was added and also the two separate
commits that we merged. One coming from the master
branch and the other coming from the
even-better-feature branch. We can also see that master
is pointing to the merge commit but even-better-feature is still pointing to
the previous one. In our example, resolving the conflict was
straightforward and easy. But in the real world, this won't always be the case. Merge conflicts can
sometimes be tricky, complicated, and spread
across multiple files. If you want to throw the
merge away and start over, you can use the git merge --abort command as
an escape hatch. This will stop the merge
and reset the files in your working tree back to the previous commit before
the merge ever happened. So by now you know how to create, delete, and switch
between branches in Git. You've also seen that each
branch represents a pointer to a commit in a sequence
of independent snapshots. You know how to merge
these commits back into the main trunk by using the git merge command. Amazing work. Seriously, this isn't easy stuff. Up next, you'll find a cheat
sheet summarizing all of these branching
techniques followed by a quiz to consolidate
these concepts.

### Git branches and merging cheat sheet

| Command                   | Explanation & Link                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| git branch                | [Used to manage branches](https://git-scm.com/docs/git-branch)                                                                        |
| git branch <name>         | [Creates the branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)                                        |
| git branch -d <name>      | [Deletes the branch](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D)                                             |
| git branch -D <name>      | [Forcibly deletes the branch](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D)                                    |
| git checkout <branch>     | [Switches to a branch](https://git-scm.com/docs/git-checkout)                                                                         |
| git checkout -b <branch>  | Creates a new branch and [switches to it](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--bltnewbranchgt)       |
| git merge <branch>        | [Merge joins branches together](https://git-scm.com/docs/git-merge)                                                                   |
| git merge --abort         | If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action                          |
| git log --graph --oneline | [This shows a summarized view of the commit history for a repo](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) |
