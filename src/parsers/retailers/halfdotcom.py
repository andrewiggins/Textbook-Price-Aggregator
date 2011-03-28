#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        halfdotcom.py
# Purpose:     Contains all parsing functions for half.com website
#
# Author:      Andrew Stewart
#
# Created:     03/19/2011
# Copyright:   (c) Andre Wiggins, Jacob Marsh, Andrew Stewart 2011
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

import BeautifulSoup,urllib2,data,time

def parse_book_page_listing(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    #info1 = soup.findAll('table',{"border":"0","cellpadding":"0","class":"pdpbg"})[0]
    otherinfo = [str(a.findAll(text=True)[0]) for a in soup.findAll('td',{'style':'padding-top:10px;white-space:nowrap;'})[0].findAll('span')]
    form,isbn,isbn13,pubdate,publisher,lang = otherinfo[:5]+[otherinfo[-1]]
    bookData = soup.findAll('table',{"border":"0","cellpadding":"12","cellspacing":"0"})[0].findAll("table",{"width":"906","border":"0","cellpadding":"3","cellspacing":"0"})
    listings = []
    quality = map(str,[a.findAll(text=True)[0] for a in soup.findAll('span',{"class":"Header"})])
    for i,bookData2 in enumerate(bookData):
        for info in bookData2.findAll("tr",{"class":"tr-border"}):
            price = float(info.findAll("span",{"class":"ItemPrice"})[0].findAll(text=True)[0].replace("$",""))
            url = info.find("a",{"class":"MoreInfo"})["href"]
            listings.append(data.TextbookListing(url,kwargs={'retailer':'HalfDotCom','price':price,'condition':quality[i],'isbn':isbn,'isbn13':isbn13}))
    return listings

def parse_book_page_textbook(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    imgURL = soup.findAll("img",{"border":"0","class":"imageborder"})
    info1 = soup.findAll('table',{"border":"0","cellpadding":"0","class":"pdpbg"})[0]
    title = str(info1.findAll('h1',{"class":"pdppagetitle"})[0].findAll(text=True)[0])
    authors = [str(a.findAll(text=True)[0]) for a in info1.findAll('span',{"class":"pdplinks"})[0].findAll("a")]
    url = info1.find('a',{"class":"pdplinks"})["href"]
    otherinfo = [str(a.findAll(text=True)[0]) for a in soup.findAll('td',{'style':'padding-top:10px;white-space:nowrap;'})[0].findAll('span')]
    form,isbn,isbn13,pubdate,publisher,lang = otherinfo[:5]+[otherinfo[-1]]
    return data.Textbook(url,kwargs={'title':title,'author':','.join(authors),'publisher':publisher,'date':pubdate,'imageurl':imgURL,'language':lang,'format':form,'isbn':isbn,'isbn13':isbn13})


def parse_search_page(html):
    soup=BeautifulSoup.BeautifulSoup(html)
    info=soup.find('table',{"width":"100%","border":"0","cellpadding":"4","cellspacing":"0"})
    bookInfo=info.findAll("td",{"valign":"top","width":"100%"})
    numMatches = soup.find("span",{"class":"PageTitleRefresh"}).find(text=True)
    numMatches = str(numMatches).splitlines()[2].split(' ')[0][1:]
    textbooks=[]
    if numMatches == "0":return textbooks
    for book in bookInfo:
        titleTag,authorTag = book.findAll("a",{"class":"ProductInfo"})[:2]
        title = str(titleTag.find(text=True))
        url = titleTag["href"]
        author = str(authorTag.find(text=True))
        formatTag = book.find("a",{"class":"ProductFormatYear"})
        form,pubdate = formatTag.find(text=True).split(', ')
        textbooks.append(data.Textbook(url,kwargs={'title':title,'author':author,'date':pubdate,'format':form}))
    return textbooks


def search(title,param=1):
    url = "http://search.half.ebay.com/?m=books&sby=%s&query=%s"%(param,urllib2.quote(title))
    html = urllib2.urlopen(url).read()
    return parse_search_page(html)

def lookup(string):
    if "http://" in string:
        return parse_book_page_listing(urllib2.urlopen(string).read())
    else:
        return parse_book_page_listing(urllib2.urlopen("http://books.half.ebay.com/ws/web/HalfISBNSearch?isbn=%s"%urllib2.quote(string)).read())


if __name__=="__main__":
    t=time.clock()
    a=urllib2.urlopen("http://search.half.ebay.com/?m=books&sby=1&query=%09Galois%27+Theory+of+Algebraic+Equations")
    parse_search_page(a.read())
    isbns=[9781584883937,9780201633610,9780136021827]
    for isbn in isbns:
        c=urllib2.urlopen("http://books.half.ebay.com/ws/web/HalfISBNSearch?isbn=%s"%isbn).read()
        parse_book_page_listing(c)
        parse_book_page_textbook(c)
    search(urllib2.quote("asdfasdfasd"))
    print time.clock()-t