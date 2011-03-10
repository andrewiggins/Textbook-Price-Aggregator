Using github:
=============
1. create a github account and let Andre know your user name and he will add you as a collaborator
2. [fork] the project from Andre's [project page]. You now have a copy of the repository in your repositories. Any changes you make will not be automatically added to the main repository (which is Andre's as he originally created it)
3. [clone], edit, [commit], [push] at will (all these commands will apply to your repository)
4. when you want to combine with main repository, submit a [pull request] from Andre's project page and he'll combine it.

---

Using git:
==========
*[gitref] is a reference site for all git commands [clone], [commit], [push], [pull], etc.*

1. To have read/write access to your copy of the repository on your local computer, you must set up SSH2 keys. See [this article](http://github.com/guides/providing-your-ssh-key) for step by step guide
2. [clone] your github repository using the SSH link in your project page.
   - only done the first time. use [pull] to update your local repository from your github repository
3. do what ever changes you want
4. [commit] the changes using -am "insert commit message here about what you did"
5. when you want to [push] your commits to github use the command [push] as outlined on the reference page
6. when you want all of your commits to be added to the main repository, submit a [pull request] on Andre's [project page]

[pull request]: http://help.github.com/pull-requests/ "Pull Request Guide"
[project page]: https://github.com/andrewiggins/Textbook-Price-Aggregator "Project Page"
[pull]: http://gitref.org/remotes/#pull "Pull Reference"
[push]: http://gitref.org/remotes/#push "Push Reference"
[commit]: http://gitref.org/basic/#commit "Commit Reference"
[clone]: http://gitref.org/creating/#clone "Clone Reference"
[fork]: http://help.github.com/fork-a-repo/ "Forking a Repository Guide"
[gitref]: http://gitref.org "Git Reference"