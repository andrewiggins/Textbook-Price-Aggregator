Collaborative Development Models
================================
*from [GitHub Help](http://help.github.com/pull-requests/)*

There are two popular models of collaborative development on GitHub:

  1. The **Fork + Pull Model** lets anyone fork an existing repository and push changes to their 
  personal fork without requiring access be granted to the source repository. The changes must then 
  be pulled into the source repository by the project maintainer. This model reduces the amount of 
  friction for new contributors and is popular with open source projects because it allows people to
  work independently without upfront coordination.
  2. The **Shared Repository Model** is more prevalent with small teams and organizations 
  collaborating on private projects. Everyone is granted push access to a single shared repository 
  and topic branches are used to isolate changes.

Pull requests are especially useful in the Fork + Pull Model because they provide a way to notify 
project maintainers about changes in your fork. However, they’re also useful in the Shared 
Repository Model where they’re used to initiate code review and general discussion about a set of 
changes before being merged into a mainline branch.

---

We are using the Shared Repository Model since I have listed everyone as a collaborator. So that 
means that everyone will clone my repository and push to my repository.

---

Setup Git:
========

Follow [this guide](http://help.github.com/set-up-git-redirect) to setup git on your computer.

---

Using Git:
==========
*[gitref] is a reference site for all Git commands [clone], [commit], [push], [pull], etc.*

  1. To have read/write access to your copy of the repository on your local computer, you must set 
  up SSH2 keys. See [this article](http://github.com/guides/providing-your-ssh-key) for step by 
  step guide
  2. [clone] my GitHub repository using the SSH link in my [project page].
     - only done the first time. use [pull] to update your local repository from your GitHub 
     repository
  3. do what ever changes you want
  4. [commit] the changes using -am "insert commit message here about what you did"
  5. when you want to [push] your commits to GitHub use the command [push] as outlined on the 
  reference page

[pull request]: http://help.github.com/pull-requests/ "Pull Request Guide"
[project page]: https://github.com/andrewiggins/Textbook-Price-Aggregator "Project Page"
[pull]: http://gitref.org/remotes/#pull "Pull Reference"
[push]: http://gitref.org/remotes/#push "Push Reference"
[commit]: http://gitref.org/basic/#commit "Commit Reference"
[clone]: http://gitref.org/creating/#clone "Clone Reference"
[fork]: http://help.github.com/fork-a-repo/ "Forking a Repository Guide"
[gitref]: http://gitref.org "Git Reference"