#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        halfdotcom.py
# Purpose:     Contains all parsing functions for half.com website
#
# Author(s):   Andrew Stewart
#
# Created:     03/19/2011
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

import urllib2,data,time
from lib import BeautifulSoup

def parse_book_page_listing(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    otherinfo = [str(a.findAll(text=True)[0]) for a in soup.findAll('td',{'style':'padding-top:10px;white-space:nowrap;'})[0].findAll('span')]
    isbn,isbn13 = (otherinfo[:5]+[otherinfo[-1]])[1:3]
    bookData = soup.findAll('table',{"border":"0","cellpadding":"12","cellspacing":"0"})[0].findAll("table",{"width":"906","border":"0","cellpadding":"3","cellspacing":"0"})
    listings = []
    quality = map(str,[a.findAll(text=True)[0] for a in soup.findAll('span',{"class":"Header"})])
    for i,bookData2 in enumerate(bookData):
        for info in bookData2.findAll("tr",{"class":"tr-border"}):
            price = float(info.findAll("span",{"class":"ItemPrice"})[0].findAll(text=True)[0].replace("$",""))
            url = info.find("a",{"class":"MoreInfo"})["href"]
            listings.append(data.TextbookListing(url, **{'retailer':'HalfDotCom','price':price,'condition':quality[i],'isbn':isbn,'isbn13':isbn13}))
    return listings

def parse_book_page_textbook(url):
    A=urllib2.urlopen(url)
    url=A.geturl()
    html=A.read()
    soup = BeautifulSoup.BeautifulSoup(html)
    imgURL = soup.findAll("img",{"border":"0","class":"imageborder"})[0]['src']
    info1 = soup.findAll('table',{"border":"0","cellpadding":"0","class":"pdpbg"})[0]
    title = str(info1.findAll('h1',{"class":"pdppagetitle"})[0].findAll(text=True)[0])
    try:authors = [str(a.findAll(text=True)[0]) for a in info1.findAll('span',{"class":"pdplinks"})[0].findAll("a")]
    except:authors =["Unknown"]
    otherinfo = [str(a.findAll(text=True)[0]) for a in soup.findAll('td',{'style':'padding-top:10px;white-space:nowrap;'})[0].findAll('span')]
    form,isbn,isbn13,pubdate,publisher,lang = otherinfo[:5]+[otherinfo[-1]]
    return data.Textbook(url, **{'title':title,'author':','.join(authors),'publisher':publisher,'date':pubdate,'imageurl':imgURL,'language':lang,'format':form,'isbn':isbn,'isbn13':isbn13})


def parse_search_page(html):
    soup=BeautifulSoup.BeautifulSoup(html)
    info=soup.find('table',{"width":"100%","border":"0","cellpadding":"4","cellspacing":"0"})
    bookInfo=info.findAll("td",{"valign":"top","width":"100%"})
    numMatches = soup.find("span",{"class":"PageTitleRefresh"}).find(text=True)
    numMatches = str(numMatches).splitlines()[2].split(' ')[0][1:]
    textbooks=[]
    if numMatches == "0":return textbooks
    images=info.findAll('img',{"class":"imageborder"})
    for i,book in enumerate(bookInfo):
        try:
            titleTag,authorTag = book.findAll("a",{"class":"ProductInfo"})[:2]
            author = str(authorTag.find(text=True))
            title = str(titleTag.find(text=True))
        except:
            titleTag = book.findAll("a",{"class":"ProductInfo"})[0]
            author = "Unknown"
            title = str(titleTag.find(text=True))
        url = titleTag["href"]
        imageURL=images[i]["src"]
        
        formatTag = book.find("a",{"class":"ProductFormatYear"})
        form,pubdate = formatTag.find(text=True).split(', ')
        textbooks.append(data.Textbook(url, **{'imageurl':imageURL,'title':title,'author':author,'date':pubdate,'format':form}))
    return textbooks


def search(term, param="Title"):
    url = "http://search.half.ebay.com/?m=books&sby=%s&query=%s"%({"Author":2,"Title":1,"Keyword":""}[param],urllib2.quote(term))
    html = urllib2.urlopen(url).read()
    return parse_search_page(html)


def lookup_listings(s):
    return parse_book_page_listing(urllib2.urlopen("http://books.half.ebay.com/ws/web/HalfISBNSearch?isbn=%s"%urllib2.quote(s)).read())


def lookup_isbn(isbn):
    if "http://" in isbn:
        return parse_book_page_textbook(isbn)
    else:
        return parse_book_page_textbook("http://books.half.ebay.com/ws/web/HalfISBNSearch?isbn=%s"%urllib2.quote(str(isbn)))


if __name__=="__main__":
    t=time.clock()
#    a=urllib2.urlopen("http://search.half.ebay.com/?m=books&sby=1&query=%09Galois%27+Theory+of+Algebraic+Equations")
#    parse_search_page(a.read())
#    isbns=[9781584883937,9780201633610,9780136021827]
#    for isbn in isbns:
#        c=urllib2.urlopen("http://books.half.ebay.com/ws/web/HalfISBNSearch?isbn=%s"%isbn).read()
#        parse_book_page_listing(c)
#        parse_book_page_textbook(c)
#    search(urllib2.quote("asdfasdfasd"))
#    print time.clock()-t
    a = search("n")
    print a
    
    #tried on isbn 9780553212587, got error
    print
    
'''
With ISBN: 9780791804308

Traceback (most recent call last):
  File "C:\Program Files\Google\google_appengine\google\appengine\ext\webapp\__init__.py", line 634, in __call__
    handler.get(*groups)
  File "C:\Users\Andre\My Dropbox\Documents\Coding\Python\Projects\Textbook Price Aggregator\src\server\book.py", line 83, in get
    listings = server.getjson(retailer.lookup_listings(isbn))
  File "C:\Users\Andre\My Dropbox\Documents\Coding\Python\Projects\Textbook Price Aggregator\src\parsers\retailers\halfdotcom.py", line 91, in lookup_listings
    return parse_book_page_listing(urllib2.urlopen("http://books.half.ebay.com/ws/web/HalfISBNSearch?isbn=%s"%urllib2.quote(s)).read())
  File "C:\Users\Andre\My Dropbox\Documents\Coding\Python\Projects\Textbook Price Aggregator\src\parsers\retailers\halfdotcom.py", line 32, in parse_book_page_listing
    bookData = soup.findAll('table',{"border":"0","cellpadding":"12","cellspacing":"0"})[0].findAll("table",{"width":"906","border":"0","cellpadding":"3","cellspacing":"0"})
IndexError: list index out of range'''
