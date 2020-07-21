# Week 1

## Before version control

### Version control

When you work in IT, you manage information across a lot of different files.
You write automation scripts that might evolve over time. For example, you might
add new features to your script or take into account additional conditions or modify
the scope of systems where the script will be executed. You also manage configuration
related to your infrastructure like the default settings on an application or the
IP addresses assigned to the computers in your fleet. This information changes over
time as the security requirements increase.

The fleet grows or new versions of software gets deployed. When trying to manage
change in IT, it's super important to have detailed historical information for your
organization's configuration files and automation code. This let's the administrators
see what was modified and when, which can be critical to troubleshooting.

It also provides a documentation trail that will let future IT specialists know why
the infrastructure is the way it is, and it provides a mechanism for undoing a change
completely. This way, we don't have to undo changes from memory and there's less
chance of human error. We can see this in action when we talk about rollbacks.

Imagine this, your team has added a new feature to a script that checks the health
of all the computers that you're responsible for. The new check verifies that the
firmware of the computer, also known as the UEFI, is updated to the latest version.
When you roll this out, you suddenly realize that half the computers now say they're
broken. After some investigation, you discover that the check needs to take into
account different computer models.

You might be tempted to do a quick code fix, push it to the affected machines right
away especially if it seems like an easy fix. But more often than not, quick fixes
include their own bugs because we don't take the time to test a new code properly.
So after the first fix, you might end up doing a second or even third emergency
push until things are really working correctly.

To avoid these headaches, you can use a version control system to easily roll back
your code to the previous version. Since you know that this version was working
correctly before the change was made, it would be safe to go back to that one until
you had time to fix the code, run some tests, and make sure everything works correctly
for all machine models.

By releasing code only after properly testing, you avoid having to push quick-fix
after quick-fix. Version control systems let us do this and much more. They are
crucial to maintaining a healthy codebase for all kinds of IT resources, and for
letting multiple people collaborate on the same coding projects together.

This tool will let us keep track of the changes that we make to our scripts, our
configuration files, and any other kind of documents that need to be tracked. We'll
start by looking at what people tend to do when they don't know about version control
and then check out some related tools, like diff and patch.

### Keeping historical copies

Maybe you were working in a team and every day you'd email a part of the work to
the rest of the team. And then the other members on your team would add their own
work, and send it out to the whole team too. Or maybe you've worked on a very complex
project, that kept changing directions. And you felt that some of the things that
got removed one day, might have to be added later on. So anytime you're about to
delete a significant part, you made a copy of the whole thing, just in case.

If any of this sounds familiar, you've already worked on the most primitive form
of version control, keeping historical copies. These copies let you see what the
project was like before, and go back to that version if you end up deciding that
the latest changes were wrong. They also let you see the progress of the changes
over time, and maybe even help you understand why a change was made.

We say that this is primitive because it's very manual and not very detailed. First,
you need to remember to make the copy. Second, you usually make a copy of the whole
thing, even if you're only changing one small part. And third, even if you're emailing
your changes to your colleagues, it might be hard to figure out at the end who did
what, and more importantly, why they did it.

The principle behind version control is the same. It lets us keep track of the changes
in our files. These files can be code, images, configuration, or even a video editing
project, whatever it is you're working with. Throughout this course, we'll see the
many ways that Git helps us keep track of our changes, and also how we can use it to
collaborate with others or avert changes. We'll use a bunch of terms that have special
meanings in the world of version control, but don't let those intimidate you. In
the end, all we're doing is having better control over our historical copies.

### Diffing files

Imagine you had two copies of some code, and you wanted to see what the difference
was between them. How would you do it? You could open both files in the editor side
by side, look at one then look at the other to spot the differences, but that's
super error-prone. We're human and by comparing with our eyes we are bound to miss
some differences.

Fortunately, there's a better way. You can use some nifty tools that will do this
automatically. We can use the diff command line tool to take two files or even to
directories, and show the differences between them in a few formats. Let's check
it out with an example. We have two files [rearrange1.py](./rearrange1.py) and
[rearrange2.py](./rearrange2.py) which contain two different versions of the same
function. Let's use the **diff command** so that we don't have to strain our eyes trying
to spot the difference:

```
$ diff rearrange1.py rearrange2.py
7c7
<     result = re.search(r'^([\w .]*), ([\w .]*)$', name)
---
>     result = re.search(r'^([\w .-]*), ([\w .-]*)$', name)
```

When we call the diff command, we get only the lines that are different between
two files. It's much easier to find the difference when we just have two lines.
See the symbols at the beginning of each of those lines? The less than symbol tells
us that the first line was removed from the first file, and the greater than symbol
tells us that the second line was added to the second file. In other words, the old
line got replaced by the new one.

In this example, we had one line that was replaced with a new one. This is a common
change when modifying code, but not the only possibility. Let's check out another
example:

```
$ diff validations1.py validations2.py
5c5,6
<     assert (type(username) == str), 'username must be a string'
---
>     if type(username) != str:
>          raise TypeError('username must be a string')
11a13,15
>       return False
>     # Usernames can't begin with a number
>     if username[0].isnumeric():
```

Here there are more changes going on. We can see that diff splits the changes in
two separate sections. The section that starts with 5c5,6 shows a line in the first
file that was replaced by two different lines in the second file.

The number at the beginning of this section indicates the line number in the first
and second files. The **c** in between the numbers means that a line was **changed**.

The section that starts with 11a13,15 shows three lines that are new in the second
file. The **a** stands for **added**, but that block seems like we're adding a return
and an if condition but nobody for the if block. What's up with that?

To understand this better we can use the **-u** flag to tell diff to show the differences
in another format:

```
$ diff -u validations1.py validations2.py
---validations1.py      2020-01-05 07:03:46.999900910 -0800
+++validations2.py      2020-01-05 07:03:46.999900910 -0800
@@ -2,7 +2,8 @@


 def validate_user(username, minlen):
-   assert (type(username) == str), 'username must be a string'
+   if type(username) != str:
        raise TypeError('username must be a string')
    if minlen < 1:
        raise ValueError('minlen must be at least 1)

@@ -10,5 +11,8 @@
        return False
    if not username.isalnum():
        return False
+   # Usernames can't begin with a number
+   if username[0].isnumeric():
+   return False
    return True
```

This unified format is pretty different from the one that we saw before. It shows
the change lines together with some context, using the minus sign to mark lines
that were removed, and the plus sign to mark lines that were added. The extra context
let's us better know what's going on with the change that we're diffing.

We can see that the new file actually has a completely new if block that's part of
a chain of conditionals that looks very similar, and that's why with the diff output
that we saw before, it was a little confusing which lines had been added.

There are a lot of tools out there to compare files. Diff is the most popular one,
but not the only one available. For example, **wdiff** highlights the words that
have changed in a file instead of working line by line like diff does. To help us
even more, there are bunch of graphical tools that display files side by side and
highlight the differences by using color. Some examples of this include:
**meld**, **KDiff3**, or **vimdiff**. We can use these tools to give better contexts to the changes
that we see.

### Applying changes

Imagine a colleague sends you a script with a bug and asked you to help fix the issue.
Once you understood what was wrong with the script, you could describe to them what
they need to change. Something like, "Well, you can only return values inside functions.
I think you meant to use sys.exit instead. Also, you're converting to gigabytes twice,
so your script will always fail." But this could still be hard for them to understand
if the code is complex.

To make the change clear, you could send them a **diff** with the change so that they
can see what the modified code looks like. To do this, we typically use a command line
like **diff -u old_file new_file > change.diff**. As a reminder, the _> sign_ redirects
the output of the diff command to a file. So with this command, we're generating a
file called _change.diff_ with the contents of diff-u command. By using the -u flag,
we include more context which helps the person reading the file understand what's
going on with the change.

The generated file is usually referred to as a **diff file** or sometimes a **patch file**.
It includes all the changes between the old file and the new one, plus the additional
context needed to understand the changes and to apply those changes back to the original
file.

Now, say you're the one receiving a diff file with a change and you want to apply
it to a script you wrote. You could read the diff file you receive carefully and
then manually go through the file that needs to be changed, and apply the modifications.
But it sounds like a lot of manual work that could be automated, don't you think?
Well, it sure is. There's a command called **patch** to do exactly this. Patch takes
a file generated by diff and applies the changes to the original file. Let's check
this out in an example.

Say we have a small [script](./cpu_usage.py) that checks whether the computer is
under too much load, like this one:

```
#!/usr/bin/env python3

import psutil


def check_cpu_usage(percent):
    usage = psutil.cpu_percent()
    return usage < percent


if not check_cpu_usage(75):
    print('ERROR! CPU is overloaded')
else:
    print('Everything is ok')
```

This script uses the psutil module to check the percentage of the CPU that's currently
in use. When the load is above a threshold, in this case 75 percent, it prints a
message with an error. When it's under the threshold, it says that everything's okay.

Now, we've shared this script with a few colleagues and one of them tells us that the
script doesn't work correctly. Even if a computer is completely overloaded, the script
will say that everything's okay. Our colleague is so helpful that they sent us a
[diff](./cpu_usage.diff) with the fix for our problem:

```
--- cpu_usage.py        2020-07-04 13:04:50.809051583 +0200
+++ cpu_usage_review.py 2020-07-04 13:10:11.487000000 +0200
@@ -4,7 +4,8 @@


 def check_cpu_usage(percent):
-    usage = psutil.cpu_percent()
+    usage = psutil.cpu_percent(1)
+    print(f'DEBUG: usage: {usage}')
     return usage < percent
```

We can see that our colleague made two changes. They added a one as a parameter
to the CPU percent function and they added a debugging line, that prints the value
returned by the function. Our colleague explains that by calling the CPU percent
function without a parameter, we were not averaging over a period of time, and so
the call always returns zero.

So we have the diff file and we want to apply it to our script. How do we do that?
We'll use the **patch command**. We'll pass the name of the file that we want to
patch in this case, cpu*usage.py, as the first parameter to the command and then
we'll provide the diff file through standard input. We will use the *< symbol\_
to redirect the contents of the file to standard input:

```
$ patch cpu_usage.py < cpu_usage.diff
patching file cpu_usage.py
```

We told patch to apply the changes that come from cpu_usage.diff to our cpu_usage.py
file. We get one single line that says the file was patched, which means that we've
successfully applied the changes. We can see that our file was modified with the
changes that we got from our colleague.

The CPU percent function is being called with a parameter of one and the debugging
line is printed. Once we're happy with the script, we could remove the debugging line.

You might be wondering, why go through all this trouble diffing, and patching, and
not just send the whole file instead? There are a few reasons for this. The main
reason is that the original code could have changed. In our example, it's possible
that the code our colleague was using to prepare the fix wasn't the latest version.
By using a diff instead of the whole file, we can clearly see what they changed,
no matter which version they were using. The patch command can detect that there
were changes made to the file and will do its best to apply the diff anyways. It
won't always succeed but in many cases it will.

Another reason is structure. In this case we're patching a single small file. But
sometimes, you might be modifying a bunch of large files inside of a huge project.
Say you are changing four files in a project tree that contain 100 different files,
arranged in different directories according to what they do. If you were to send
the whole files, you'd need to specify where those files were supposed to be placed.
As we called out, we can diff whole directory structures and in that case the diff
file can specify where each change file should be without us having to do any manual
juggling.

### Practical application of diff and patch

Imagine this, a colleague is asking our help with fixing a script named [disk_usage.py](./disk_usage.py).
The goal of the script is to check how much disk space is currently used, and print
an error if it's too little space for normal operation. But the script is currently
broken because it has a few bugs. We’ll help our colleague fix those bugs to demonstrate
how to use diff and patch.

Before we change anything, let’s make a couple copies of the script. We'll add [_\_original_](./disk_usage_original.py)
to one copy, which we’ll keep unmodified and use for comparison and [_\_fixed_](./disk_usage_fixed.py)
to the other copy, which we’ll use to repair our fix:

```
$ cp disk_usage.py disk_usage_original.py
$ cp disk_usage.py disk_usage_fixed.py
```

Now that we have our copies, we'll edit the _\_fixed_ version and actually fix it.
This file has a bunch of code. Before we try to understand what it does and what's
wrong with it, let's execute it and see what we get:

```
$ chmod +x ./disk_usage.py
$ ./disk_usage.py
  File "./disk_usage.py", line 21
    return 1
    ^
SyntaxError: 'return' outside function
```

The Python interpreter isn't too happy. It's complaining that there's a return outside
of function. And if we look at the code, we can clearly see that there's a return
that's not inside any function. You might remember that in Python, we can only use
return statements inside functions. So how do we fix this? There's a couple options.
We could turn the current code into a function and then call that function from the
main part of our script. Or we could use sys.exit to make the return number of the
exit code of our script, which is the code that causes a program to exit with the
corresponding exit value. For now, let's go with the second option:

```
#!/usr/bin/env python3

import shutil
import sys


def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free
if not check_disk_usage('/', 2*2**30, 10):
    print('ERROR: Not enough disk space')
    sys.exit(1)

print('Everything ok')
sys.exit(0)
```

We fixed the syntax error:

```
$ ./disk_usage_fixed.py
ERROR: Not enough disk space
```

But now the script is telling us we don't have enough space on our disk. But we
know that we actually do have some free space. What's up with that? If you look
closely at the code, you might notice that the script is converting to gigabytes
twice. The function call to check_disk_usage is passing 2 times 2 double star 30.
You might remember that the double star operator is used to calculate powers. In
this case, 2 to the power of 30, which is how many bytes are in a gigabyte. So, this
would be 2 gigabytes, but that be if the check_disk_usage function was expecting
a value in bytes. If we look at the code of the function, we can see that it's already
dividing the amount of free bytes by 2 to the power of 30.

So in other words, we're doing the gigabyte conversion twice. Once when calling the
function and once inside the function. We need to get rid of one of them. Let's
change how we call the function:

```
#!/usr/bin/env python3

import shutil
import sys


def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free
if not check_disk_usage('/', 2, 10):
    print('ERROR: Not enough disk space')
    sys.exit(1)

print('Everything ok')
sys.exit(0)
```

It works now:

```
$ ./disk_usage_fixed.py
Everything ok
```

Now we need to send a fixed to our colleague so that they can fix their script.
To do that, we'll use a technique to generate a diff file, like this:

```
$ diff -u disk_usage.py disk_usage_fixed.py > disk_usage.diff
```

Let's check the contents of the diff using the cat command:

```
$ cat disk_usage.diff
--- disk_usage.py       2020-07-04 13:43:44.774371024 +0200
+++ disk_usage_fixed.py 2020-07-04 13:47:21.620078064 +0200
@@ -1,6 +1,7 @@
 #!/usr/bin/env python3

 import shutil
+import sys


 def check_disk_usage(disk, min_absolute, min_percent):
@@ -16,9 +17,9 @@


 # Check for at least 2 GB and 10% free
-if not check_disk_usage('/', 2*2**30, 10):
+if not check_disk_usage('/', 2, 10):
     print('ERROR: Not enough disk space')
-    return 1
+    sys.exit(1)

 print('Everything ok')
-return 0
+sys.exit(0)
```

So this is what we need to send to our colleague to have them patch their file.
They would run the patch command like this:

```
$ patch disk_usage.py < disk_usage.diff
patching file disk_usage.py
```

By calling _patch_ with the diff file, we've applied the changes that were necessary
to fix the bugs. Let's check that disk_usage.py now executes successfully:

```
$ ./disk_usage.py
Everything ok
```

This is still a very manual process, where version control systems can really help.

### diff and patch cheat sheet

**diff**
diff is used to find differences between two files. On its own, it’s a bit hard to use; instead, use it with diff -u to find lines which differ in two files:

**diff -u**
diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output. See below:

```
~$ cat menu1.txt
Menu1:

Apples
Bananas
Oranges
Pears

~$ cat menu2.txt
Menu:

Apples
Bananas
Grapes
Strawberries

~$ diff -u menu1.txt menu2.txt
--- menu1.txt   2019-12-16 18:46:13.794879924 +0900
+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900
@@ -1,6 +1,6 @@
-Menu1:
+Menu:

 Apples
 Bananas
-Oranges
-Pears
+Grapes
+Strawberries
```

**Patch**
Patch is useful for applying file differences. See the below example, which compares two files. The comparison is saved as a .diff file, which is then patched to the original file!

```
~$ cat hello_world.txt
Hello World
~$ cat hello_world_long.txt
Hello World

It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt
--- hello_world.txt     2019-12-16 19:24:12.556102821 +0900
+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900
@@ -1 +1,3 @@
 Hello World
+
+It's a wonderful day!
~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff
~$ patch < hello_world.diff
patching file hello_world.txt
~$ cat hello_world.txt
Hello World

It's a wonderful day!
```

There are some other interesting patch and diff commands such as patch -p1, diff -r !

Check them out in the following references:

- http://man7.org/linux/man-pages/man1/diff.1.html
- http://man7.org/linux/man-pages/man1/patch.1.html

## Version control systems

### What is version control?

A Version Control System keeps track of the changes that we make to our files.
By using a VCS, we can know when the changes were made and who made them. It also
lets us easily revert a change if it turned out not to be a good idea. It makes
collaboration easier by allowing us to merge changes from lots of different sources.

At first-look, a Version Control System can seem like a complicated, possibly intimidating
tool. But if you look closer, you'll see that it's really just a system that stores
files. However, unlike a regular file server which only saves the most recent version
of a file, a VCS keeps track of all the different versions that we create as we
save our changes.

There are many different version control systems, each with their own implementation
and with their own advantages and disadvantages. But, no matter how the VCS is implemented
internally, they always access the history of our files. Let us retrieve past versions
of the file or directory and see who changed which files, how each file was changed and
when the file was changed. On top of this, we can make edits to multiple files and
treat that collection of edits as a single change which is commonly known as a, **commit**.

A VCS even provides a mechanism to allow the author of a commit to record why the
change was made, including what bugs, tickets or issues were fixed by the change.
This information can be a lifesaver when trying to understand a complex series of
changes, or to debug some obscure issue. So, be sure to record this extra info in
your commits to be truly committed to better code.

In any organization that produces software, a VCS is a key part of managing the code.
Files are usually organized in **repositories** which contains separate software projects
or just group all related code. If there's a lot of people involved in developing
software, some developers may have access to only some of the repositories.
A single repository can have as little as one person using it. And it can go up to
thousands of contributors.

A Version Control System can be used to store much more than just code. We can use
it to store configuration files, documentation, data files, or any other content that
we may need to track. Because of the way tools like diff and patch work, a VCS is
especially useful when tracking text files, which can be compared with diff and
modified with patch.

We can also store images, videos or any other complex file
formats in a VCS, but, it won't be easy to check the differences between versions
when comparing these file formats. It might not be possible to automatically merge
changes made to older versions of a file.

### Version control and automation

At first glance, using a VCS might seem like a lot of work for an IT specialist to
set up and learn. It might especially seem like overkill, if you're the only member
of your IT team that writes code or maybe even the only member period.

So can a VCS help, even if you don't need to share your scripts or collaborate on
them with others? The short answer is yes. A VCS can be invaluable, even in a one-person
IT department. A VCS stores your code and configuration. It also stores the history
of that code and configuration.

A version control system can function a lot like a time machine, giving you insights
into the decisions of the past. Whenever you write a commit message, after making
a change, it's as if the current version of yourself is explaining your decisions
to a future you or others who might work on the same scripts and configurations
in the future.

This can help you avoid finding yourself staring at a piece of code that you or
someone else wrote three months ago and puzzling over how it works or even why it
exists.

With a VCS, you can view, track and select snapshots from the history of your project.
So nothing you do is lost, and since we can use a VCS to store both code and configuration
files, we can make the overall IT systems more scalable and reliable. For example,
let's say you've stored the DNS zone file for your company in a VCS. A DNS zone
file is a configuration file that specifies the mappings between IP addresses and
host names in your network.

When you update the zone information, always use good explanatory commit messages.
That way, you'll have access to meta information about your new IP addresses and
host names present in the zone file, like when they were added and for what purpose.

If anything breaks after you add a new entry, you can rely on the VCS to tell you
what the file looked like before the change. You can then revert to the old version
quickly, so you can fix the problem fast and figure out what went wrong later.
This functionality enhances the reliability of systems you operate. Because of the
audit trail provided by the VCS, you know exactly what version of the zone file
to rollback to, which reduces the time it takes to fix the problem.

It's generally better to quickly roll back first and stop errors before spending
time figuring out what went wrong. You can curb the fix after the bleeding has stopped.
Figuring out the bug might take up valuable time or worse, your first attempt at a
solution can have its own bugs.

Let's look at a different example. The configuration for a DHCP damon can be replicated
in two or more machines, where one acts as a primary server and the other one acts
as standby machine. The standby machines won't do much while the primary is up.
But if the primary goes down for any reason, a standby machine can become primary
and start responding to DHCP queries. For this to work, the configuration files
on all machines need to be identical.

This is because the DHCP protocol doesn't provide a way for standby machines to
get an up-to-date version of the configuration files and the way DNS does. To deal
with this, we can keep the up-to-date version of the DHCP configuration in a version
control system and have the machines download the configuration from the VCS. This
means all the machines will have the exact same files. That's already handy enough.
But after using it for a while, you're bound to see other benefits. Say you get
an urgent alert over the weekend, telling you that your DHCP server isn't responding
to any queries. You look at the history of the changes and you find that one of
the changes added on Friday evening, included a duplicated entry causing the server
to misbehave.

By using a VCS, you can easily roll back the change and have the servers back to
health in no time. You might come across a second unexpected benefit, when it's
time to replace the server with a new one. By having all the server configuration
and a version control system, it's much easier to automate the task of deploying
a new server.

### What is Git?

Git is a VCS created in 2005 by Linus Torvalds, the developer who started the Linux
kernel. Git is a **free open source system** available for installation on Unix based
platforms, Windows and macOS.

Linus originally created get to help manage the task of developing the Linux kernel.
This was difficult because a lot of geographically distributed programmers were
collaborating to write a whole bunch of code. Linus had some requirements for the
way that the system worked, and its performance that weren't being met by the VCS
tools at a time. So he decided to write his own.

Git is now one of the most popular version control systems out there and is used
in millions of projects.

Unlike some version control systems that are centralized around a single server,
Git has a **distributed architecture**. This means that every person contributing
to a repository has full copy of the repository on their own development machines.
Collaborators can share and pull in changes that others have made as they need.

And because the repositories are all local to the computer being used to create the
files, most operations can be done really fast. If you want to collaborate with others,
it usually makes sense to set up a repository on a server to act as a kind of hub
for everyone to interact with.

But Git doesn't rely on any kind of centralized server to provide control organizations
to its workflow. **Git can work as a standalone program as a server and as a client**.
This means that you can use Git on a single machine without even having a network
connection. Or you can use it as a server on a machine where you want to host your
repository. And then you can use Git as a client to access the repository from another
machine or even the same one.

Git clients can communicate with Git servers over the network using HTTP, SSH or
Git's own special protocol.

So you can use Git with or without a network connection. You can use it for small
projects with like one developer or huge projects with thousands of contributors.
You can use it to track private work that you can keep to yourself or you can share
your work with others by hosting a code on public servers like Github, Gitlab or
others.

When looking for information online, you might notice that the official Git website
is called [git-scm.com](https://git-scm.com/). SCM it's actually another acronym
similar to VCS. It stands for Source Control Management. While both terms mean the
same, we generally prefer VCS, because as we call that already, these systems can
actually be used to store much more than just source code.

There are other VCS programs like Subversion or Mercurial.

Check out the following links for more information:

- https://git-scm.com/doc
- https://www.mercurial-scm.org/
- https://subversion.apache.org/
- https://en.wikipedia.org/wiki/Version_control

### Installing Git

There are versions of Git available for all popular operating systems.

The first step is to check whether you already have it installed. You can do this
by running **git --version**. If you're running a version number higher than 2.20,
then you can just use that one. If you get an error message or an older version
number, you'll need to install the current version. If you use a package management
system like apt or yum on Linux, Chocolatey on Windows, or Homebrew on Mac OS, you
can just install Git through that. If you don't use a package management system,
then you can download the latest executable installer from the official website and
deploy it on your computer.

On Linux, installing and using Git is pretty straightforward. You can install it
with the command **apt install git** or **yum install git**, and after that, you'll
have Git installed and ready to use. On Mac OS, you can even have it installed
when you run git --version. If Git isn't installed, this command will ask you if
you want to install it and then download it and install it for you.

Alternatively, you can also download it from the website and install it by following
the prompts.

Once it's installed, you'll be able to use it from the command line just like any
other tool. On Windows, after downloading and executing the installer, you'll need
to go through a bunch of different configuration options. These options come with
preselected defaults that usually makes sense to just keep. Pay attention to the
editor question though. You'll probably want to change the editor to one that you
feel comfortable with, like Notepad++ or Atom. One interesting thing about the Windows
installation is that it comes preloaded with an environment called MinGW64.

This environment lets us operate on Windows with the same commands and tools available
on Linux. So you can practice some Linux command line tools on your Windows machine.
After installing Git on your Windows machine, you'll be able to use Git from the
Linux command line. If you selected the default option for the path environment
question, you'll be able to also run it from the PowerShell command line.

[Git download page](https://git-scm.com/downloads)
[Git installation instructions for each platform](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Using Git

### First steps with Git

We said that a VCS tracks who made which changes, for this to work, we need to
tell Git who we are. We can do this by using the **git config** command and then setting the values of **user.email** and **user.name** to our email and our name
like this:

```
$ git config --global user.email "me@example.com"
$ git config --global user.name "My name"
```

We use the **--global** flag to state that we want to set this value for all git
repositories that we'd use. We could also set different values for different repositories.

With that done, there are two ways to start working with a git repository.
We can create one from scratch using the **git init** command or we can use the
**git clone** command to make a copy of a repository that already exists somewhere
else.

When we run **git init** we initialize an empty git repository in the current directory.
The message that we get mentions a directory called **.git**. We can check that
this directory exist using the **ls -la** command which lists files that start with
a dot. We can also use the **ls -l .git** command to look inside of it and see
the many different things it contains.

This is called a **Git directory**. You can think of it as a database for your Git
project that stores the changes and the change history. It contains a bunch of
different files and directories. We won't touch any of these files directly, we'll
always interact with them through Git commands.

So whenever you clone a repository, this git directory is copied to your computer.
Whenever you run git init to create a new repository like we just did, a new git
directory is initialized. The area outside the git directory is the **working tree**.

The working tree is the current version of your project. You can think of it
like a workbench or a sandbox where you perform all the modification
you want to your file. This working tree will contain all the files that are
currently tracked by Git and any new files that we haven't yet added to the
list of track files.

To make Git track our file, we'll add it to the project using the **git add**
command passing the file that we want as a parameter. With that, we've added our
file to the staging area. The **staging area** which is also known as the **index**
is a file maintained by Git that contains all of the information about what files
and changes are going to go into your next command.

We can use the **git status** command to get some information about the current
working tree and pending changes.

To get it committed into the .git directory, we run the **git commit**
command. When we run this command, we tell Git that we want to save our changes.
It opens a text editor where we can enter a commit message. If you want, you can
change the editor used to your preferred editor.

### Tracking files

The Git directory contains the history of all the files and changes.
The working tree contains the current state of the project, including any
changes that we've made. And the staging area contains the changes that have been
marked to be included in the next commit.

Each time you make a commit, Git records a new snapshot of the state
of your project at that moment. It's a picture of exactly how all these
files looked at a certain moment in time. Combined, these snapshots make up
the history of your project, and it's information that gets
stored in the Git directory.

When we operate with Git, our files can be either tracked or untracked.
**Tracked files** are part of the snapshots, while **untracked files** aren't
a part of snapshots yet. This is the usual case for new files.

Each track file can be in one of three main states, modified, staged or committed.
If a file is in the **modified** state, it means that we've made changes to
it that we haven't committed yet. The changes could be adding, modifying or
deleting the contents of the file. Git notices anytime we modify our files. But won't store any changes until
we add them to the staging area.

So, the next step is to stage those changes. When we do this,
our modified files become **stage files**. In other words, the changes to those files
are ready to be committed to the project. All files that are staged will be
part of the next snapshot we take.

And finally, when a file gets **committed**, the changes made to it are safely stored
in a snapshot in the Git directory.

This means that typically
a file tracked by Git, will first be modified when
we change it in any way. Then it becomes staged when we
mark those changes for tracking. And finally it will get committed when
we store those changes in the VCS.

### The basic Git workflow

We saw that each repository will have
a Git directory, a working tree, and a staging area. And we called out that files can
be in three different states, modified, staged, and committed.

Let's review these concepts one more
time by looking at the normal workflow when operating with Git
on a day to day basis. First, all the files we
want to manage with Git must be a part of a Git repository. We initialize a new repository by
running the **git init** command in any file system directory.

For example, let's use the **mkdir** command
to create a directory called scripts, and then change into it and
initialize an empty Git repository init. Our shiny new Git repository can
now be used to track changes to files inside of it.

But before jumping into that, let's check out our current configuration
by using the **git config -l command**. There's a bunch of info in there,
and we won't cover all of it. For now, pay special attention
to the user.email and the user.name lines. This information will appear
in public commit logs if you use a shared repository.
For privacy reasons, you might want to use
different identities when dealing with your private work and when submitting
code to public repositories.

Okay, our repo is ready to work,
but it's currently empty. Let's create a file in it,
we'll start with a basic skeleton for a Python script, which will help
us demonstrate the Git workflow. As with any Python [script](./checks/all_checks.py),
we'll start with the shebang line. For now, we'll add an empty main function,
which we'll fill in later. And at the end,
we'll just call this main function:

This is a script that we'll want to
execute, so let's make it executable. And then let's check the status of
our repo using **git status** command.

As we called out before,
when we create a new file in a repository, it starts off as **untracked**. We can make all kinds of
changes to the file, but until we tell Git to track it, Git won't
do anything with an untracked file. We need to call the **git add** command. This command will immediately move a new
file from untracked to stage status. And it will also change a file in
the modified state to **staged** state.

Remember that when a file is staged, it
means it's been added to the staging area and it's ready to be committed
to the Git repository.

To initiate a commit of staged files,
we issue the **git commit** command. When we do this, Git will only commit the changes that
have been added to the staging area, untracked files or modified files
that weren't staged will be ignored.

Calling git commit with no parameters
will launch a text editor, this will open whatever has been
set as your default editor. If the default editor is not
the one you'd like to use, there are a bunch of ways to change it.

We'll say that our change is creating
an empty all_checks.py file, then save and exit.
We've just recorded
a snapshot of the code in our project, which is stored in the Git directory. Remember that every time we commit
changes, we take another snapshot, which is annotated with a commit
message that we can review later.

That's how we add new files, but
usually we'll modify existing ones. So let's add a bit more content to
our script to see that in action. We'll add a function called check_reboot, that will check if the computer
is pending a reboot. To do that, we'll check if
the run/reboot-required file exists. This is a file that's created on our
computer when some software requires a reboot. And of course,
since we're using os.path.exists, we need to add import os to our script.

Let's check the current status
using **git status** again. Our file's modified, but not staged. To stage our changes,
we need to call git add once again.

What do we need to do next? We have to call git commit to
store those changes to the Git directory. This time, we'll use the other way
of setting the commit message. We'll call **git commit -m**, and then pass
the commit message that we want to use. So in this case, we'll say that we've
added the check_reboot function.

### Anatomy of a commit message

Writing a clear
informative commit message is important when you use a VCS. Future you or other developers or IT specialists who might read
the commit message later on will really appreciate
the contextual information as they try and
figure out some of the parts of the code
or configuration.

So what makes a good
commit message? It can be helpful to keep your audience in mind when
you write commit messages. What would someone reading
a message weeks or months from now want to know about
the changes you've made? What might be
especially important or tricky to understand about them? Is there extra information that might help the reader out, like links to design documents or tickets in
your ticketing system?

Similarly to how style guides
exist for writing code, your company might have
specific rules for you to follow when you
write commit messages. Even if they don't, it's good to use a few
general guidelines to make sure your commit messages are as clear and useful as possible.

A commit message is generally broken up
into a few sections. The first line is
a short **summary** of the commit followed
by a **blank line**. This is followed by a
full **description** of the changes which
details why they're necessary and anything
that might be especially interesting about them or difficult to understand.

When you run the
git commit command, Git will open up a text editor of your choice so you can
write your commit message.

This text is intended to provide a detailed explanation of what's going on with the change. It can reference bugs or issues that will be
fixed with the change. It can also include links to more information when relevant. The line limits can be
annoying but they help in making the commit message be more digestible
for the reader.

There's a git command
used to display these commit messages called **git log**. This command will do any
line wrapping for us. Which means that if we don't stick to the recommended
line wrapping, long commit messages will run off the edge of the screen
and be difficult to read.

Now, take a look at the lines in the commit message that
start with the pound symbol. Just like in Python, this symbol indicates
that these lines are comments and won't get included
in the commit message. Git shows them to us
whenever we're writing a commit message as a reminder of what files
were about to commit.

Sometimes it can be
tempting to just write something
short like update, change or fix as the description of our commit
messages. Don't do it. It's super frustrating to go back to repositories history and discover that there's not enough context to understand
what was changed and why. It takes only a few more seconds to write a better description. This can be invaluable
down the line.

Following these
guidelines can help make your commit
message really useful, and the investment of work now
will really pay off later. There are plenty of resources
out there to read including the Linux kernel
documentation itself along with impassioned opinions
from other developers.

We said that we can
check the history of the commits of our project
using the git log command.

Take a look at what git
tracks as part of the log. It's packing a lot of
information in just a few lines. The first thing listed for
each commit is its **identifier**, which is a long string
of letters and numbers that uniquely
identify each commit. The first commit in the
list also says that the head indicator is pointing
to the master branch.

For each commit, we see
the name and the email of the person who made the commit which is indicated as the author. Then we get the date and
time the commit was made. Finally the commit
message is displayed.

Our commit messages are very brief as we're just starting
to work on our repository. As the work we do
becomes more complex, we'll probably write
longer descriptions with a lot more detail.

### Initial Git cheat sheet

Check out the following links for more information:

The [Linux kernel documentation](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process/submitting-patches.rst?id=HEAD) itself, as well as [impassioned](https://commit.style/) opinions from other [developers])https://thoughtbot.com/blog/5-useful-tips-for-a-better-commit-message.

You can check out ["Setting your email in Git"](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address) and ["Keeping your email address private"](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address) on the GitHub help site for how to do this.
