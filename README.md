Textbook Price Aggregator
=========================

1. Searches several (half.com, amazon, Barnes and Noble, coop, with room for more later) online bookstores for the desired books.
2. Can take as input either textbook name, ISBN, or select classes from LSU (room for expansion) which will then pick the needed books
   a. Course offerings website scraper already written.
   b. Need a scraper for LSU Bookstore to get actual books (http://lsu.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&storeId=19057&langId=-1)
3. Sort the books based on quality and price (which will hopefully include shipping)
4. Could augment prices by a small amount ($0.50 maybe) and have the application purchase the books from the original seller in order to monetize the service

---

Using github:
=============
1. create a github account and let Andre know your username and he will add you as a collaborator
2. fork the project from Andre's project page (https://github.com/andrewiggins/Textbook-Price-Aggregator). You know have a copy of the repository in your repositories. Any changes you make will not be automatically added to the main repository (which is Andre's as he created it)
3. clone, edit, commit, push at will
4. when you want to combine with main repository, submit a pull request from Andre's project page and he'll combine it.

---

Using git:
==========
*http://gitref.org/ is a reference site for the git commands clone, commit, push, pull, etc.*

1. To have read/write access to your copy of the repository on your local computer, you must set up SSH2 keys. See this article for step by step guide (http://github.com/guides/providing-your-ssh-key)
2. **clone** your github repository using the SSH link in your project page.
   - only done the first time. use **pull** to update your local repository from your github repository
3. do what ever changes you want
4. **commit** the changes using -am "<insert commit message here about what you did>"
5. when you want to **push** your commits to github use the command **push** as outlined on the reference page
6. when you want all of your commits to be added to the main repository, submit a pull request on Andre's project page