Textbook Price Aggregator
=========================
A project to aggregate the price of online textbook retailers on one easy website.

Basic Idea
==========

1. Searches several (half.com, amazon, Barnes and Noble, coop, with room for 
   more later) online bookstores for the desired books.
2. Can take as input either textbook name, ISBN, or select classes from LSU 
   (room for expansion) which will then pick the needed books
   a. Course offerings website scraper already written.
   b. Need a scraper for LSU Bookstore to get actual books 
      (http://lsu.bncollege.com/webapp/wcs/stores/servlet/TBWizardView?catalogId=10001&storeId=19057&langId=-1)
3. Sort the books based on quality and price (which will hopefully include shipping)
4. Could augment prices by a small amount ($0.50 maybe) and have the application 
   purchase the books from the original seller in order to monetize the service
