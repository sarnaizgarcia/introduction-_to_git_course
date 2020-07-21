# Week 4 - Collaboration

## Pull requests

### Collaboration

[MUSIC] Welcome back. Over the past modules, we've learned
a whole about how to interact with Git. We've covered how to use it
both locally and remotely. We've seen how to rollback bad changes,
solve conflicts when collaborating with others, and
a bunch of other little nifty things. In this module, we'll keep exploring
the collaboration tools available in Git. We'll learn about tools that allow us to
send changes to projects that we aren't a member of, help us improve
the quality of our code, and let us track our work better. Some of these tools will
be specific to GitHub, but most of the Git repository hosting
services have similar tools. So the concepts will still apply if you
decide to use a different platform. In recent years, GitHub has become
a super popular platform for collaboration across many projects. It's used heavily for
open-source projects. These are projects that allow anyone
to use, copy, and modify their code. Having the code published online means
that anybody in the world can learn from what the project is doing, and even
collaborate on fixes and extra features. It also helps us learn from each other, because we can look at how others have
solved the problem that we're tackling. I regularly use GitHub to
look up code snippets for things that I'm interested in. Most recently, I looked up examples for
a movie theater seat finder because I was working on a similar
feature for a personal project of mine. If you're trying to learn a new
technology, it's a great idea to practice your skills by contributing to
a project that uses that technology. To do that, you'll need to know
how to interact with the project. This includes how to send bug fixes, how
to make sure that your fixes are applied, and even how to figure out
which fixes are needed. In this module,
we'll cover that and a lot more. So are you excited? I mean, I'm excited. Let's get started.

### A simple pull request on GitHub

[MUSIC] As we called out, we can use GitHub
to look at other people's code and collaborate with them. Let's see this in action by having to look
at one of the projects from our colleague, blue-kale. Okay, so our colleague has created the project
to include all validation functions. Let's have a look at
the validations.py file. We can see the code of a function
that validates username. But, if you look closely at
the functions documentation, you might notice that there's a typo. We can improve our colleague's code
by fixing that typo, Let's do that. We'll click on the little pencil icon
which let's us edit the file directly from the web interface. We're trying to edit a file in a project
that we don't have a right access to. GitHub tells us it created
a fork of this project for us, which we can commit our changes to. And if we submit changes to this file,
it will create a new branch so that we can send a pull request. But what exactly is a fork? Forking is a way of creating
a copy of the given repository so that it belongs to our user. In other words, our user will be able
to push changes to the forked copy, even when we can't push
changes to the other repo. When collaborating on projects hosted
on GitHub, the typical workflows, first, create a fork of the repo,
and then work on that local fork. A forked repo is just like a normal repo, except Github knows which
repo it forked from. So we can eventually merge our changes
back into the main repo by creating a pull request. A pull request is a commit or series
of commits that you send to the owner of the repository so
that they incorporate it into their tree. This is a typical way of working on
GitHub, because in most projects, only a few people have
commit rights to the repo. But anybody can suggest patches, bug fixes
or even new features by sending pull requests that people with
commit access can then apply. Typically, the owners of the repo will
review the changes before merging them. Checking that they match the development
guidelines for the project and that the license is valid and so on. Let's fix the typo in the file to see
what the pull request looks like. Once we're done making changes to
the file, we can make a change proposal, by scrolling down and
filling in the description of the change. In this case, we fix the typo
in the function documentation. Clicking on the Proposed file change
button, we'll create a commit in our forked repo, so that we can send
the change to our colleague. Let's do that now. We've created a commit on our forked repo. But we haven't yet
created the pull request that will send the changes to the owner
of the original repo. On this screen, we can see a lot
of information about our change. We can see what repositories and branches are involved in
the creation of the pull request. We can also see that GitHub automatically
created a branch called patch-1 for us. And that our change can automatically
be merged, yay, no conflicts. This window also lets us review the change
before we create an actual pull request. Once we're ready, we just click
the Create pull request button. This opens a text box where we can
enter comments about our change. In this case, a change is really simple,
we just fixed the typo so there's nothing extra to add. If we were suggesting
a more complex change, we could use this text box
to provide more context. The checkbox at the bottom lets
us allow edits from maintainers. This can be useful for example, if by
the time a project maintainer gets around the merging or change, there's been more
commits and our change needs rebasing. By allowing edits, the maintainer can
do it themselves instead of asking us to do it, less work, yes please. Okay, we're ready,
let's click Create pull request. Cool, we've created a pull
request with our change. Our colleague can now look at it and decide whether they want to
merge it to the project or not. In this video, we checked out
the simplest way of making pull requests, which is doing them directly
through the GitHub interface. By using this workflow, you can already
start contributing to projects on GitHub. Up next, we'll see how to do
more complex pull requests.

### The typical pull request workflow on GitHub

In our last video, we saw
how to create pull request directly on GitHub by using the web interface to edit files. This works for simple
changes like fixing typos or adding
documentation to a function, but it's not so great for making larger changes that we
want to preview or test. To do that, we'll normally
have a local copy of the repo in our computer and work with the forked repo as a remote. We'd need to use all the Git commands that we've learned
up till now to do this. Let's check out this process by creating a fork of another repo. On top of the validations repo, our colleague blue-kale has
created a rearrange repo, and we want to help them out. We'll go to the rearranged repo and create a fork by
pressing the Fork button. It takes a few seconds to create a copy of the repo for our user. The copy will contain
the current state of the repo including files
and commit history. Once the fork is created, we're shown a page
that corresponds to the same repo name, but it's under our user. See how it shows that it's
a forked repo by stating the original repo under
the name. All right. We've created a forked version
of the repo on GitHub. We can now get a local
copy of the repo on our computer by copying the URL and then calling the
git clone command with it. We now have a new directory
called rearrange with the contents of the repo. We can look at the
contents by changing into that directory
enlisting all files. We can look at the commit history using our old friend git log. Now that we have a
local copy of the repo, we can make any changes
we'd like to it. For example, this project doesn't currently have a README.md file. Let's improve the documentation
by creating that. To do that, we'll create a
new branch called Add README. Do you remember how to
create new branches? We do it by running git
checkout -b add -readme. We can now start editing
the README.md file. The MD extension indicates
that we're using markdown, which is a lightweight
markup language. We can use it to write
plain text files that are then formatted following
some simple rules. In this case, we'll start with a title with the module's name and a brief description that says it's used to rearrange names. Our README file is small, but it'll do for now, let's
save it and commit it. Now, to push the change
to our forked repo, we need to create the
corresponding remote branch. Do you remember the
command for that? Yes. It's git push -
u origin add -readme. So when we push the
change to the new branch, we got a message that we can create a pull request
if we want to. We'll do that in a
minute. First, let's check out how our file
looks when rendered. Yes. Our README file
rendered successfully. We're ready to create a pull
request for our change. To do that, let's look at
the top of the Project page. GitHub tells us that
our branch is ahead of the original repositories
master branch by one commit, which is the commit we just made. We can start our pull requests by clicking on the
Pull Request link. As we called out, before
creating a pull request, it's always important to check that the code will
merge successfully. GitHub tells us that
our change can be automatically merged,
which is great news. If this wasn't the case, we'd need to rebase
our change against the current branch
of the original repo so that it could be merged. The window is showing
us the TextBox where we can enter
comments about our change. As we mentioned before, we should use this to explain why we're creating
this pull request. This lets the person that
will approve the change understand why they should merge the change
into the main tree. Are we fixing a bug? This is a new feature to let the project support
more use cases. How will the project benefit
from including our change? Whatever info might be useful to the approver, record it here. We can also use this box to explain how the
change was tested. If the project includes
automatic test infrastructure, our pull request should
include a tests for our changes and we can state
that all test still pass. But if there's no
automatic testing, then we can use
this box to explain how we tested the
change manually. In this case, we've just added a README file that the
project was missing before. So we'll just say we're adding a README file that was
missing for the project. We should also check that the change we're
sending looks correct. It's always a good idea to double-check that we're
sending the right change. To do that, let's look at the diff that appears at
the bottom of the page. Yes, that's exactly what
we want. All right. We're ready. Let's click the
Create Pull Request button. Awesome. We've created
our second pull request. The number next to the name of our pull request
is the identifier that's used in GitHub to track
issues and pull requests. We can use this
identifying number to access this pull request
anytime we need it. But why would we need to access a pull request after we send it? It's pretty common for
project maintainers to come back with questions, comments, or even ask us
to fix our pull requests. Imagine you've just
finished preparing a pull request for a
great new feature, and you get a comment saying that it's missing some documentation. What would you do? We'll talk about that in our next video.

### Updating an existing pull request

When we send a pull request, it's pretty common to
receive some comments from the project maintainers
asking for some improvements. The improvement could be to
add documentation or tests, or maybe we need to make
sure that change works for all cases or that it follows the project
style guidelines. There's nothing wrong with
getting these comments, it actually shows the
project maintainers are interested in our change. To get our change approved, it's important that you
address the comments. So if we're asked to add documentation for
example, we go and do it. So back to our change, looks like we got a comment
from one of our colleagues. We got a comment
saying that our README was too short and they'd
like us to add an example. To address this comment, will add more
details to our file. We'll start by explaining that the function rearranges LastName, FirstName into FirstName LastName and then we'll add an example. We'll say that calling
rearrange name with Turing, Alan as a parameter, will return Alan Turing. We fleshed out the
README file a bit. Now we can add our changes and commit them to the repo as usual. Let's run git commit and pass a commit message
saying that we've added more information
to the README, and after that, we'll push
the change to the repo. Now that we've pushed our
change back to the repo, let's check our pull
request in GitHub. In the Commit's tab, we can see our two commits. Our commit now shows up as a part of the same pull request. It's important to
notice here that we just pushed our commit
to the same branch as before and GitHub automatically added it to the pull request. If we wanted to create a
separate pull request, we would need to create
a new branch instead. If we go to the Files Change tab, we can see all files affected
by the pull request, no matter which commit
they were changed in. Whenever we look at the diff generated by a commit
or a chain of commits, GitHub will show a color diff for the changes
that we've made. It will use green for new lines and red for
lines that were deleted. If only a part of
the line changed, it will highlight that
specific part of the line. In this case, it's a new file, so all the lines are additions. Check out how we see only one file even when there
are two separate commits. What we're seeing is the
difference between our repo and the original repo we
created the pull request for. You can also click
on the preview icon and show the rendered
markdown contents. Github renders our file and
highlights the changes. Keep in mind that each project in GitHub may work
slightly differently. Some projects may ask you to have only one commit in
your pull requests, other projects may ask
you to rebase against the latest master branch when your pull request is ready to be merged back into the main tree. Github allows projects to set their contribution
guidelines. You'll find a link to
them whenever you create a new pull request or
issue in a project. So make sure you've read these guidelines and that your
pull requests match them. In this video, we saw how to update our pull requests
by doing new commits in our local Git repository and pushing them to
the remote repository. We'd seen before how to use the Git web interface to create new pull requests and we can use this interface to
update a pull request. This can be handy when the change that we
want to make is small like fixing a typo or adding an extra sentence to
the documentation. Up next, we'll talk about
what to do if you're asked to squash your changes
into a single commit.

### Squashing changes

As we've caught up before, you shouldn't rewrite history when the commits
have been published. That's because someone
else may have already synchronized that repo
with those contents. This rule is waived
with pull requests, since it's usually
only you who have cloned your fork
of the repository. So say the project maintainers ask us to create a
single commit that includes both changes and a more detailed description
than the one we submitted. We can do that by using the interactive version of the rebase command
called rebase-i, as the parameter to the command will pass the master branch. So we'll call git
rebase-i master. When we call an
interactive rebase, a text editor opens
with a list of all the selected commits from the oldest to
the most recent. By changing the first
word of each line, we can select what we want
to do with the commits. The default action here
is pick which takes the commits and rebases them against the
branch we selected. This is what we do
with git rebase in an earlier video when we called it without
the dash i flag. But now we can change the
action to something else. The comments in the file tells all the different commands
we can use for our commits. For example, we can reword a commit message keeping the changes as they are but
modifying the commit message. We can also edit the commit to add or
remove changes from it. We have two options
for combining commits, squash and fix up. In both cases, the contents of the selected commit are merged into the previous
commit in the list. The difference is what happens
with the commit messages. When we choose squash, the commit messages are
added together and an editor opens up to let us make
any necessary changes. When we choose fix up, the commit message for
that commit is discarded. For our example, we want to
use squash so that we can combine both commits but also modify the
commit description. So let's change the
pick command in the second line to squash
it into the first one, then we'll save and exit
the editor as usual. Once we've told git
that we want to squash a commit unto
the one before it, we're given another file to edit. In this case, it's the
combined commit message. As usual, git shows us some
helpful information in the comments including
which files are modified and what commits
are being combined. We want to improve
the description by adding more info
about our change. Let's add we're including
an example use case. All right. Now that our commit contains
the right information, we can save and exit as usual. Yes, our rebase worked. Let's check the
output of git show to see the latest commit
and the changes in it. Success, we got exactly
what we wanted here, our two changes have
been combined into one that contains the whole new file and the right commit message. Before we try to push
this change to our repo, let's call git status
to check the info that git gives us about
the current state. Git tells us that our local
branch has one commit, which is the rebase we just did. It also tells us that the origin/add-readme
branch has two commits. These are the two commits we had already pushed to the repo. Let's look at the
graph history of our commits by calling git log --graph --one line
--all for all branches, and -4 for just the
latest four commits. We can see that the
two commits pushed to the origin/add-readme
branch show up in a different path than
the commit that's currently in our local
add-readme branch. This is expected whenever we do a rebase because the old commits are in the remote repo and we have a different commit
in our local repo. What do you think will
happen when we call git push? Let's try that out. As we expected, git
doesn't like us trying to push our change because it
can't be fast-forwarded. But in this case, we don't
want to create a merge. Instead, we want to replace the old commits
with the new one. To do this, we will
call git push -f to force git to push the current snapshot
into the repo as is. This time, our push
completed successfully. Git tells us here that
we forced an update. Let's look once again our
history graph by running git log -- graph
--one line --all -4. This time, it's just one
commit on top of master. The divergence is gone. Now let's look at the
contents of the pull request. Success. We've managed to combine
both are commits into one by using the interactive
version of git rebase. Nice job in making it
through these first videos. You now know how to create
a pull request on GitHub, how to update a pull
request, and squash changes. These tools are all
super-helpful when using GitHub. Up next, you'll find a
reference of the commands we used and links to where
you find more information. After that, there's a quick quiz to check that everything
is making sense.

### Git fork and pull request cheat-sheet

Check out the following link for more information:

https://help.github.com/en/articles/about-pull-request-merges

## Code reviews

### What are code reviews?

[MUSIC] GitHub and other repository
hosting services offer tools for doing code reviews on their platform. And while this is called code reviews,
we can actually use the same tool and process to do reviews of any text file
including configuration and documentation. Doing a code review means going through
someone else's code, documentation or configuration and
checking that it all makes sense and follows the expected patterns. The goal of a code review is to
improve the project by making sure that changes are high quality. It also helps us make sure that
the contents are easy to understand. That the style is consistent
with the overall project. And that we don't forget
any important cases. Reviews increased the number of
eyes that have checked the code. This increases the code quality and
reduces the amount of bugs. It doesn't mean that there'll be no bugs,
but at least the most obvious
bugs will be caught. Also, this helps spread knowledge
since both the code writers and the code reviewers now know
what the code is doing. When we work in the same office as our
teammates, we can do reviews in person by looking together at the changes and
discussing how the contents fit together. But when the person that we're working
with is in a different office or time zone We're better
off using a Coder V tool. Coder V tools let us comment
on someone else's code. These let us leave feedback on how
they could make their code better. Common code issues are unclear names
that makes the code hard to understand. Forgetting to add a test, or
forgetting to handle a specific condition. If we're writing documentation,
our reviewer can help us catch typos and things that aren't totally clear. On platforms like Github, it's common for projects to only requires reviews for
people that don't have commit access while the project maintainers
can commit directly. But doing code reviews improves
the code's overall quality. Today, some open source projects and lots of companies require code reviews for
everybody. This isn't because they don't trust them,
but because they want
the highest quality code. And code reviews are how they get there. One thing to always remember, code
reviews are not about us being good or bad coders,
they're about making our code better. And not only that specific review,
but in general. By getting feedback,
we can keep improving our code techniques. And by reviewing other people's code,
we can also learn new and different ways of achieving results. Like everybody else after toiling for
hours on a problem and finally solving it, all I want to do
is submit my code and be done with it. But this rarely happens. Code reviews usually send me back to
the drawing board with small errors and nitpicks, but that's a good thing. These code reviews point out things that
we might have missed along the way and ensure that our code
makes sense to others. One example that springs to mind is
back when I was writing a script for an Android bug report parser. After hours of fiddling with the code and
writing tests to back up what I did, I finally sent it to her code review and
thought I was done. It turns out had a bunch of little style
guilders that my reviewer wouldn't let me get away with. More importantly, while fixing this style
errors, I noticed I forgotten a major use case in my script that would have
stopped my code from working. So I fixed both the style errors and
the missing use case and could submit my change with a smile. At Google, we believe deeply in
the value of reviewing everything we do. Even the content of these courses
have been reviewed by lots of people. These reviews and make sure that
the contents makes sense are technically correct with no significant gaps and
follow the established guidelines. Shout out to my colleagues for
keeping us on our toes and making sure that these
videos are top rate. Up next we'll talk about
the typical reviewing workflow and how to get the most from
the review process.

### The code review workflow

[MUSIC] In our last video,
we explained what code reviews are and how they can make our code better. Now, we'll check out a typical code
review using a reviewing tool. Imagine we've just finished
a bunch of code changes, now, we'll ask a reviewer to look at our code. The reviewer might say that everything
is okay and our changes approved, but usually they'll find something
that needs improving. So they'll add comments to our changes
explaining what needs to be fixed and how. When we get the review comments will
address them by fixing our typos, adding any missing tests and so on. After addressing a comment,
we can mark it as resolved so that we know it's been taken care of. If there's something that
we aren't sure how to do or we think a different approach might be
better, we can reply to the comment and ask our reviewer for more information
without marking the comment as resolved. Once all comments have been resolved and
our viewer is satisfied with the results, they'll approve the change and
we'll be able to merge it. You may be wondering, what are all
of these comments that I receive? There's a wide range of things
your reviewer might have to say about your code. Sometimes, you might have forgotten to
take into account something important and you'll need to do
significant work to fix it. Sometimes, your reviewer might
point out something small, that's not really critical. And the comment is mostly a suggestion for
making the code better. These comments are usually prefixed,
saying that it's a Nit. Whatever it is, it's important that
you take the time to understand what the comment is and
what you need to do to address it. For example,
if you've written a piece of code and your reviewer asks you to explain why or
how the code is doing something, it might be tempting to just answer their question
in the comment and mark it as resolved. But this isn't a great idea, because only
the reviewer gets to see your answer. Instead, it's better to take this as
an opportunity to make the code clearer. For example, you could do this by
using better variable names or splitting a large piece of
code into smaller functions. On top of that, you can add comments
to the code and documentation to your functions to make sure that
the how and why are clearly explained. It's common for code reviews to include several
comments about the style of the code. To avoid a lot of back and forth, it's
a good idea to refer to a style guide that explains the preferred coding style for
the project. For example, lots of Python projects,
use the PEP8 style guide. If the project you're contributing
to doesn't include a style guide, make sure that you ask for one. And in case you need inspiration, we've included links to some common
style guides in the next reading. There are a bunch of code
reviewing systems out there. And while they all follow
the same patterns, they don't all work exactly the same way. In some code reviewing tools, you'll need
one of the project maintainers to approve your code before it's submitted. In other tools, you'll just need to
get a couple +1s from contributors to the project before you can submit. The goal is to always ensure that your
code has been reviewed by people who are familiar with the project, so
that it's ready to be submitted. Can you think of a project you've worked
on in the past where code reviews could have been helpful? Maybe you worked as a part of a team and had trouble making sure that everyone
agreed on how things should be done. Or maybe you were learning
how to use a new tool and you would have benefited from
a second pair of eyes on your work. No matter how simple or
complex a project is, it can always be improved
with good code reviews. Up next, we'll dive into how this code
reviewing process works on GitHub.

### How to use code reviews in GitHub

Up till now, we've talked about the general process of
doing code reviews. This process applies to any platform with
code reviewing tools. Now, let's check out how this process looks on
GitHub, specifically. Remember, a while
back in this module, we created a pull request
that added a read me file. Conveniently, our colleague just replied with a few comments.
Let's have a look. The code review has
one overall comment, and line by line, comments, highlighting the things
that we need to get done. We can view all
changes requested for the file we created by clicking on the view
changes button. Our reviewer made three
comments about our file. The first one is asking us to add a period at the
end of the sentence. The second one asks us to add another hashtag which will make the title render
and a smaller font. The last one will require a bit more work since it's asking us to include a couple more
examples. Let's fix these. We'll add a period at the
end of the second sentence, and then add a second hashtag
before the example title, and finally, add a
few more examples. To do that, we'll use
the star character, which is another feature of the markdown language that lets us easily create bullet points. So we'll add a couple
of more lines with the same format, and
say that Hopper, Grace M. turns into
Grace M. Hopper, and that Voltaire
stays as Voltaire. All right. We've addressed all the comments in
our code review. Let's save our file and
then commit the changes. Since we want this change to be a part of the previous commit, we'll call Git commit dash A with the dash
dash amend flag, which will edit the
original commit. Once we've done that, let's call Git status to see what Git has to
say about our repo Just like before, we
see that our change has diverged from the origin
slash master branch. You might remember
that git commit dash dash amend modifies commits. So it's not safe to do with commits that have been
pushed to the repo. Using amend is pretty much the same as creating a new commit, and then using an interactive
rebase to fix up a change. So, the commit gets replaced by a completely new commit with a completely different commit ID. This means that to push it, we'll need to use the
dash F flag again. Remember that forcing
pushes is fine for pull request branches because nobody else should
have cloned it. But this isn't something
that we want to do with public repos. All right. We've done what our
colleague asked. Let's now go back to look at the pull request and
resolve the comments. See that comment
that says outdated, that's because we've pushed a new version since
we've made the change. But, since we've taken
care of their request, we can ignore the
outdated comment and just resolve
the conversation. Cool, we've addressed
all the comments. We can leave a message in our conversation to
let our reviewer know that we've resolved
all the comments and ask them to
take another look. Our reviewer can now check out the new changes and approve
them if they're satisfied. As with lots of other
topics we've covered, making the most out of the code review process
will require some practice. It's great to have
some tips but in the end we need to
learn by experience. So don't be afraid to
practice practice practice. Up next, you'll find some
resources to learn more about code reviews and a quiz to put this knowledge into action. After that, you can try out doing a code
review on GitHub.

### More information on code reviews

Check out the following links for more information:

- http://google.github.io/styleguide/
- https://help.github.com/en/articles/about-pull-request-reviews
- https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31
- https://smartbear.com/learn/code-review/what-is-code-review/

## Managing projects

### Managing collaboration

Over the past few videos, we've looked at how we can
collaborate with others using tools provided by
platforms like GitHub. These tools can be
very helpful but some coordination outside of the platform is always
going to be needed. For example, the project you're working on might need
up medium or large refactor that will affect multiple lines of code
across several files. It's important to
give your colleagues the heads up that this
refactor is coming. If possible, try to do the refactor while the other
developers are working on a different part of the
project because this helps avoid large and
complicated conflicts. We've called on a
bunch of times that documenting your work
is super important. When working together with
a large group of people, documenting what you do and why you do it becomes even more important otherwise
you'll spend most of your time answering
everybody else questions. Also, say there's a problem with your service while
you're on vacation or the person who
developed the code is on the other side of the
world and currently sleeping. In these situations,
the documentation needs to be good enough to help
someone else fix the problem. The most basic form of this
is writing clear code with good comments and documentation for those functions in the code. On top of that,
you'll want to create documentation files to
let others know how they can interact with
your project like the readme.md file that we
created an earlier video. If you're a project maintainer, it's important that you are reply promptly to pull requests
and don't let them stagnate. The more time that passes until a pull request gets reviewed, the more likely it is that
there's a new commit that causes a conflict when you
try to merge in the change. On top of this, if the person contributing
the changes of volunteer that's
just trying to help, they may lose their
motivation to work on the project if you make them
wait too long for feedback. Another thing to
remember when you maintain a project
especially if it's an open source project that volunteers are contributing to is that it's important that you understand any
changes you accept. You never know if the
other person is going to stick around to
maintain the code after you merge it in so you better make
sure you can do that. You should also be careful with which patches
you accept or reject. Accepting everything
that gets sent your way might make your
project grow too much and become unmanageable or it
might take into account too many corner cases and cause complicated code that's
hard to maintain. On the flip side,
if you don't accept any pull requests
you'll discourage contributors and
miss out on keeping your project active and relevant. We've talked about style
guides a few times already. If you're contributing
to a project, you want to check
out the style guide and make sure you follow it. If you own a project, it makes sense to create
a style guide so that others know what you're
expecting from them. In our next reading, we'll
include links to some of the most common style
guides and pointers and how to include a style
guide in your own project. When it comes to coordinating
who does what and when, a common strategy for active software projects is
to use an issue tracker. This is a super useful tool and we'll find out more about
it in the next video. On top of that, when the
project is large enough, it's important to
have another way of communicating and coordinating
between contributors. For many years, most projects used mailing list and IRC
channels for communication. Recently, new forms of
communicating have gained popularity like Slack
channels or Telegram groups. If you're managing
your own project, choose whatever
communication medium best fits your needs and those
of your contributors. If you're collaborating with
a project you don't own, you'll want to find out
what channels are being used for collaboration and with that you now have a
rough idea of how to collaborate with others
across the internet. Up next, we'll talk about two important tools that can
help us collaborate better, tracking issues and
continuous integration.

### Tracking issues

[MUSIC] Deciding who's going to do what is
critical when collaborating with others, with no coordination, two or more people
might spend time working on the same part of a project while nobody works
on the other critical parts. Imagine that you and your colleagues
decided that you'd work on building automation software, for keeping
the computers on your network up to date. But then instead of dividing
the task into smaller pieces and assigning them to different people, you just randomly started working
on some part of the infrastructure. The result would probably be total chaos,
with different pieces of software that won't work well together, and
lots of gaps that nobody worked on. For small teams, it's usually easy enough to discuss in
person who's going to be working on what. But as soon as the group starts growing,
talking about responsibilities and what to do next becomes more of a hassle. That's when a tool like
an issue tracker or bug tracker can help us
coordinate our work better. An issue tracker tells us the tasks that
need to be done, the state they're in and who's working on them. The system also let's us
add comments to the issue, these comments can be super helpful. They can give us more
details about the problem, explain a way to solve it, or
detail how to test if it's been solved. Issue trackers aren't just useful for
people actively working on projects. They also let users report bugs
when they come across them, even if they don't know
how to solve the problem. Sometimes users come across problems
that we never even thought possible. And having them report these issues
through a bug tracker can help make our projects better. And the tracker can also help volunteers
that want to start contributing to the project. Having a clear visible
list of the pending work, lets new contributors figure out
how to help and where to jump in. There are a bunch of different
solutions to track bugs or issues. There's a popular bug
tracker called Bugzilla, which is used by quite
a few open source projects. On the flip side, platforms like
GitHub have an issue tracker baked in. So, if you're hosting your project there, it can be very handy to
track work on your project. Like the problems to solve,
the features to add and the use cases to include it,
let's check it out. This is the list of issues for
our health-checks projects. For now, it only has one issue asking
us to update our documentation. One of our colleagues suggested that we
create a new health check that verifies if there are any critical error messages
inside the system logs like current log or syslog. Errors that appear there might help
troubleshoot some interesting problems. So, this sounds like a good idea for
a new check. Let's create an issue for this feature
by clicking on the New issue button. For the title of the issue,
we'll say that we want to check for critical errors in system logs. And for the issues description we'll
say that the new check should go through var/log/currentlog. And var/log/syslog and check if there are
any critical errors that need attention. When writing in issues description, it's
a good idea to include all the information that we have about the problem or missing
feature and any ideas on how to solve it. And if new information comes up later on, it can be added as additional
comments on the same issue. Great, we're now ready
to submit the new issue. Okay, we now have the new list
in our list of issues to solve. The issues in the list all have
numbers that identify them, as we called out in an earlier video,
in GitHub, each issue or pull request in a project has
a unique number associated with it. So, if we have a pull
request with the ID five, there won't be an issue with ID five. GitHub will automatically reference
issues and pull requests and comments when we mention them
using the hash tag number format. For example, if we use #2 in a comment, it will automatically reference
the issue we just created. If you're fixing an issue
through a pull request, it's possible to automatically close the
issue directly once the code is merged. To do this, you need to include
a string like closes:#4 in your commit message or as a part of
the description of your pull request. Once the code gets merged
into the main tree, GitHub will automatically close the issue with
a message linking it to the new commit. Let's try this out by
updating the documentation, like the #1 issue requested. This issue seems easy enough to fix,
we need to update the README file to use the new file name and explain a bit
more about how our script works. Before we start working on this,
let's get the issue assigned to us. Assigning issues to collaborators
helps us track who is working on what. By assigning the bug to yourself, you can
let others know that you're working on it, so they don't need to. All right, let's update the documentation. So, we're still using the old name
of the name file, all_checks.py, we renamed that file a while
back to healthchecks.py. Let's change our README to use a new
file name using inverted quotes to show monospace text. Then we'll add that the script will print
everything okay, if all checks pass and it will print the corresponding
error messages if something fails. We've updated the documentation, let's
save the file and commit this change. This time, we'll call git comit -a so that we can edit the commit
message in the text editor. We'll say that we've updated the README
to use the new name of our script. And in a longer description, we'll add that we've included more
info about how the script works. Finally, we'll wrap up by adding the
string closes #1, so that the issue will get automatically closed once this
commit is integrated into the main tree. Our commit message looks good,
let's save it and push it to the repo. Now let's go back to the issue
that we were addressing. We see that our issue is automatically
closed with the commit we pushed. We can click on the commit
ID to see the full commit. So here's the commit message we
created with the associated change. See how the #1 that we included as
a part of the commit message is automatically detected as
a link to the #1 issue. There's a bunch more to learn
about tracking issues, but this should be enough to get you started. Feel free to experiment on your own and
try more ways to interact with the system.

### Continuous integration

Throughout this course, we've been making changes to our files, sometimes we ran them manually to test if they still worked after the change, sometimes we just forgot to do that. This is common for any software project no matter how big or small. As humans, we're not great at remembering to do lots of stuff so we can't rely on people remembering to test their code, not even ourselves. Luckily, we don't need to. We can write automated tests to test the code for us and then use a continuous integration or CI system to run those tests automatically. A continuous integration system will build and test our code every time there's a change. This means that it will run whenever there's a new commit in the main branch of our code. It will also run for any changes that come in through pull request. In other words, if we have continuous integration configured for our project, we can automatically run our tests using the code in a pull request. This way, we can verify that the test will pass after the new changes get merged back into the tree and that means instead of hoping our collaborators will remember to properly test their code, we can rely on our automated testing system to do it for us. Once we have our code automatically built and tested, the next automation step is continuous deployment which is sometimes called continuous delivery or CD. Continuous deployment means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time. This allows errors to be caught and fixed early. Typical configurations include deploying a new version whenever a commit is merged into the main tree or whenever a branch is tagged for release. There's a large world of tools and platforms related to CICD which is what the whole system is usually called. One popular option is Jenkins which can be used to automate lots of different types of projects. Some repository hosting services like GitLab provide their own infrastructure for doing continuous integration. GitHub doesn't offer an integrated solution. Instead, the popular alternative is to use Travis which communicates with GitHub and can access the information from GitHub projects to know which integrations to run. No matter which tool you use, there are a bunch of concepts that you'll need to deal with when creating your own CICD. The first one is a concept of pipelines. Pipelines specify the steps that need to run to get the result you want. For a simple Python Project, the pipeline could be to just run the automated tests. For a web service written in Go, the pipeline could be compiled the program, run the unit tests and integration tests and finally deploy the code to a test instance. Another concept that turns up when doing CICD is artifacts. This is the name used to describe any files that are generated as part of the pipeline. This typically includes the compiled versions of the code but can include other generated files like PDFs for the documentation or OS specific packages for easy installation. On top of this, you might want to keep the logs of the pipelines build and test stages to review if things fail. When setting up CICD, we have to be careful about how we manage secrets. If our pipeline includes deploying a new version of the software to a test server, we need to somehow give the software that's running the pipeline access to our test server. There are a bunch of different strategies to do this, like exchanging SSH keys or using application specific API tokens. For some pipelines, it might be unavoidable to use one of these methods but be aware that you're giving access to your test servers to the owner of the service that's running the pipeline for you. It's a bit like giving your house keys to the person checking your heating once a year. So two things to remember, first, make sure the authorized entities for the test servers are not the same entities authorized to deploy on the production servers. That way, if there's any kind of compromise in the pipeline, your production server is not affected. Second, always have a plan to recover your access in case your pipeline gets compromised. If you want to set up Travis for your GitHub project, you can do that by logging into the Travis website at www.travis-ci.com using your GitHub account then enable the projects that you want to continuously integrate. After that, you'll need to add a configuration file to your project written in YAML format that states the language your project is in, in which steps to take for the pipeline. This file can be very simple if your project files are typical configuration for the language you're using but can also become very complex if you want to run a complicated pipeline with lots of stages and steps outside the defaults. We won't go into a ton of detail here but there's more info in the next reading coming up. Feel free to read up on it and investigate on your own if you want to continuously integrate and deliver your project.

### Additional tools

Check out the following links for more information:

- https://arp242.net/diy.html
- https://help.github.com/en/articles/closing-issues-using-keywords
- https://help.github.com/en/articles/setting-guidelines-for-repository-contributors
- https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html
- https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/
- https://docs.travis-ci.com/user/tutorial/
- https://docs.travis-ci.com/user/build-stages/
