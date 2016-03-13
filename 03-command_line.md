# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1 _cd_ - change directory gets you one down in folder paths. Cannot be used to go back in folder path. cd .. gets you up one folder in path

2 _rmdir_ - deletes a folder directly below the one you're in [rmdir <folder name>]. cannot be used to delete folders that have any contents

3 _ls_ - used below cd to list all folders and files in a folder - good for rmdir or further cd

4 _mkdir_ - makes a new folder in folder you are in

5 _pwd_ - shows you where you are in a path

6 _pushd/popd_ - pushd is like temp cd into a path, then type popd to move back to original folder. can push into further folders and pop back several times to get to original directory

7 _touch_ - creates empty file in directory

8 _man_ - shows what a command is all about

9 _help_ - shows help info for how to use a command

10 _rm_ removes a file within the folder you are in

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls lists all of the files and folders in a directory. ls -l lists files with details. ls -lh lists details for file in readable format. ls -a lets you view hidden files in the folder. ls -l -a and ls -lh -a are meaningful combinations. 

---


---

What does `xargs` do? Give an example of how to use it.

> > The xargs utility reads space, tab, newline and end-of-file delimited
     strings from the standard input and executes utility with the strings as
     arguments.

     Any arguments specified on the command line are given to utility upon
     each invocation, followed by some number of the arguments read from the
     standard input of xargs.  The utility is repeatedly executed until stan-
     dard input is exhausted.
     
     EX: $ xargs -t
         abcd
         [cntrl-d] 
         outputs bin/echo abcd

---

