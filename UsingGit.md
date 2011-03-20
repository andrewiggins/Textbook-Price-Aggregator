Collaborative Development Models
================================
*from [GitHub Help](http://help.github.com/pull-requests/)*

There are two popular models of collaborative development on GitHub:

  1. The **Fork + Pull Model** lets anyone fork an existing repository and push
  changes to their personal fork without requiring access be granted to the 
  source repository. The changes must then be pulled into the source repository
  by the project maintainer. This model reduces the amount of friction for new 
  contributors and is popular with open source projects because it allows 
  people to work independently without upfront coordination.
  2. The **Shared Repository Model** is more prevalent with small teams and 
  organizations collaborating on private projects. Everyone is granted push 
  access to a single shared repository and topic branches are used to 
  isolate changes.

Pull requests are especially useful in the Fork + Pull Model because they 
provide a way to notify project maintainers about changes in your fork. 
However,they are also useful in the Shared Repository Model where they are used
to initiate code review and general discussion about a set of changes before 
being merged into a mainline branch.

---

We are using the Shared Repository Model since I have listed everyone as a 
collaborator. So that means that everyone will clone my repository and push to 
my repository.

---

Setup Git:
========

Follow [this guide](http://help.github.com/set-up-git-redirect) to setup git on
your computer.

To [clone] our repository to your local machine for editing, follow these steps:
*Note: These only have to be done once*

  1. To have read/write access to your copy of the repository on your local 
  computer, you must set up SSH2 keys. See 
  [this article](http://github.com/guides/providing-your-ssh-key) for step 
  by step guide
  2. Change your working directory to the directory you want to have your
  local repository.
  3. [clone] my GitHub repository using the SSH link in my [project page].
     - `$ git clone git@github.com:andrewiggins/Textbook-Price-Aggregator.git`

---

Using Git:
==========
*[gitref] is a reference site for all Git commands [clone], [commit], [push], 
[pull], etc.*

  1. [pull] to update your local repository from the GitHub repository
     - `$ git pull`
     - `$ git pull origin master`
  2. Do what ever changes you want
  3. [add] any new files you created and any files you want to commit.
    - In git, you have [add] newly created files.
    - Also, you have to [add] any modified file to the commit. For example, if
    you have modified files `file1` and `file2`, you could [add] `file1` to the
    commit and commit the changes to `file1`, then [add] `file2` to the commit 
    and then commit the changes to `file2`. Each of these is a separate commit.
    You can add multiple file to a commit as well.
    - If you want to commit all changes as one commit, just add the `-a` option
    to [commit] and it will add all modified files to the commit.  
  4. [commit] the changes
     - `$ git commit -m "insert commit message here about what you did"`
       - This command will commit any changes you have already added.
     - `$ git commit -am "insert commit message here about what you did"`
       - This command has the `-a` option meaning it will automatically add any
       changes to the commit.
  5. When you want to [push] your commits to GitHub use the command [push]
     - `$ git push`

---

Useful Git Commands:
====================

1. [status]
   - `git status`
   - `git staus -s`
     - `-s` option means short, so it is one line per file.
   - This command shows you the status of your current working directory. It
   will display which files are modified, new and added, etc. It will also
   display which files git is not tracking. 
   - It will also display which changes have been added to the current commit
   and which ones haven't. 
   - See the following `git status -s` example:
      
      <pre>
      $git status -s
      $ M UsingGit.md
      $M  src/main.py
      $?? src/retailers/
      $?? src/schools/
      $?? src/util/
      </pre>
   
   - The letters on the left are changes added to the current commit. The
   letters on the right are changes not added to the current commit. The question
   marks mean that the file is not tracked by git. 
   - 'M' means modified, 'A' means added, 'R' means renamed, 'C' means copied 
   and '?' means not tracked. See [status] for a more indepth review. 

[add]: http://gitref.org/basic/#add "Add Reference"
[status]: http://gitref.org/basic/#status "Status Reference"
[pull request]: http://help.github.com/pull-requests/ "Pull Request Guide"
[project page]: https://github.com/andrewiggins/Textbook-Price-Aggregator "Project Page"
[pull]: http://gitref.org/remotes/#pull "Pull Reference"
[push]: http://gitref.org/remotes/#push "Push Reference"
[commit]: http://gitref.org/basic/#commit "Commit Reference"
[clone]: http://gitref.org/creating/#clone "Clone Reference"
[fork]: http://help.github.com/fork-a-repo/ "Forking a Repository Guide"
[gitref]: http://gitref.org "Git Reference"