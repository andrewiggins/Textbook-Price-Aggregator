#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        amazon.py
# Purpose:     wrapper for using AWS offered by Amazon 
#
# Author(s):   Russell Jacob Marsh
#
# Created:     04/25/2011
# Copyright:   (c) Jacob Marsh, Andrew Stewart, Andre Wiggins 2011
# License:
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------

import data
from lib import ecs

# Global function calls
ecs.setLicenseKey('AKIAIHF4ICHMS5ME3LMQ')
ecs.setSecretKey('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')
ecs.setLocale('us')

def lookup_isbn(isbn):
    book = ecs.ItemSearch(isbn, IdType='ISBN', SearchIndex='Books', ResponseGroup='Large')
    return data.Textbook(book[0].DetailPageURL, 
      **{'title':book[0].Title,'author':book[0].Author,'publisher':book[0].Publisher,
      'date':book[0].PublicationDate,'imageurl':book[0].SmallImage.URL,
      'language':book[0].Languages.Language[0].Name,
      'format':book[0].Binding,'isbn':book[0].ISBN,
      'isbn13':book[0].EAN})

# amazon merchants/amazon price
# Brand New, Like New, Very Good, Good, Acceptable (possible conditions)
# New = Brand New
# Used = Very Good

def lookup_listings(isbn):
    bookList = []
    bookPage = "http://www.amazon.com/gp/offer-listing/%s" % (bookResults[0].ASIN)
    bookResults = ecs.ItemSearch(isbn, MerchantId='All', Condition='All', 
      SearchIndex='Books', ResponseGroup='Large')
    for i in bookResults[0].Offers.Offer:
        bookCondition = i.OfferAttributes.SubCondition
        if bookCondition == "mint":
            bookCondition = "Brand New"
        elif bookCondition == "verygood":
            bookCondition = "Very Good"
        elif bookCondition == "good":
            bookCondition = "Good"
        else:
            bookCondition = "Acceptable"
        bookList.append(data.TextbookListing(bookPage, 
          **{'retailer':'Amazon', 'price':i.OfferListing.Price.FormattedPrice.strip('$'),
          'condition':bookCondition, 'isbn':bookResults[0].ISBN,
          'isbn13':bookResults[0].EAN}))
    return bookList

# This will make a query given:
# query = string as function of type
# Type = Author, Title, or Keyword
# Add:  Handle exceptions
def search(query, Type='Title'):
    textBookList = []
    if Type == "Author":
        searchResult = ecs.ItemSearch(Keywords='None', Author=query, MerchantId='All',
          Condition='All', SearchIndex='Books', ResponseGroup='OfferFull, Large')
    elif Type == "Keyword":
        searchResult = ecs.ItemSearch(query, MerchantId='All', Condition='All',
          SearchIndex='Books', ResponseGroup='Large,OfferFull')
    else:
        searchResult = ecs.ItemSearch(Keywords='None', Title=query, MerchantId='All',
          Condition='All', SearchIndex='Books', ResponseGroup='OfferFull, Large')
          
    for i in searchResult:
        textBookList.append(data.Textbook(i.DetailPageURL, **{'imageurl':i.SmallImage.URL,
          'title':i.Title, 'author':i.Author, 'date':i.PublicationDate, 
          'format':i.Binding}))
    
    return textBookList
    
    
if __name__ == "__main__":
    req = AmazonReq()
    book = req.lookupISBN("0393327795")
    for i in book:
      print i.Title
