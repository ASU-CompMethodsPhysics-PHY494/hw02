# PHY 494: Homework assignment 2

* Due Tuesday 1/26 midnight.

* Follow the link in Canvas to set up your HW2 repository.

* `git clone` your repository to your laptop.

* Read the instructions ([assignment_02.md](assignment_02.md)) in your text editor or through GitHub.

* Work through the problem, check in your changes into your repository
  (`git add`, `git commit`), and `git push` your changes to the remote
  repository on GitHub.

**Tests and Autograding**: You can check that your answer is correct
by running the following command from the top of your working
directory:

     pytest

These tests are also ran automatically as soon as you push changes to
GitHub. Open "pull request 1" (the Feedback pull request) in your
repository on GitHub to see results.


## 2.1 Copy, rename, delete (10 points)

Work through the [Copy, rename, delete:
Activity](https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2021/01/14/01_Unix_Shell/#activity-homework)
**but work with the PHY494 directory in *this* repository**, i.e, you
will work under `hw02-USERNAME/PHY494` where USERNAME is your GitHub
username. Some files and directories under `PHY494` are already
present in the hw02 repository.

To be clear, all steps that are needed to complete the homework are
shown here:

1. Make a backup (call it `TODO.bak`) of the `TODO` list with the `cp`
   command (in the same directory as the original `TODO` file).
2. Rename `TODO` to `TODO.txt` with the `mv` command.
3. Make a directory `notes` under the `data` directory: You should now
   have a directory tree similar to

        hw02-USERNAME/PHY494/01_shell/
                          Documents/
                                    work/
                                         TODO.txt
                                         TODO.bak
                          data/
                              notes/

   Check with `ls -R`.
4. Put a copy of `TODO.txt` into the `notes` directory (using `cp`).
5. Create a new text file `data/notes/hints.txt` and write any
   [hints](https://en.wikipedia.org/wiki/Ice_planet)  for possible
   rebel bases into this file.
6. Open `notes/TODO.txt` in your editor (e.g., `atom`) and add a note to item 1 too look in the
   hints.txt file. Save and exit.
7. Make a copy of your `notes` directory in your `Documents/work` directory:

        hw02-USERNAME/PHY494/01_shell/
                          Documents/
                                    work/
                                         TODO.txt
                                         TODO.bak
                                         notes/
                                              TODO.txt
                                              hints.txt
                          data/
                              notes/
                                    TODO.txt
                                    hints.txt

8. Remove `data/notes/hints.txt` with `rm`.
9. Remove `data/notes` with `rmdir`. (Hint: Read the error message!)
10. Move `work/notes/hints.txt` into the `work` directory.
11. Remove the useless `work/notes` directory with `rm -r` (careful !)


After you completed the activity you should end up with a specific
directory structure under `./hw02-USERBAME/PHY494/01_shell`, which will be
tested.



## 2.2 (OPTIONAL) "In the beginning was the command line"

(Skim)read Neal Stephenson’s **In the Beginning... was the Command Line**
from 1999
([PDF](https://becksteinlab.physics.asu.edu/file_download/7/NealStephenson_Commandline.pdf?mimetype=pdf)). What
are the advantages and disadvantages of using the command line instead
of a graphical user interface?