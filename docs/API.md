Textbook Price Aggregator API
=============================

---

URLs
----

- User URLs  
  *(Return HTML)*  
  *(Asterisks signify path parameter)*

  1. `/`
  2. `/search`
  3. `/coursesearch/*school*`
  4. `/book/*isbn*`
  5. `/error/*error_code*`

- API URLs  
  *(Return API Data, usually [JSON] objects)*  
  *(Asterisks signify path parameter)*

  1. `/textbook/*isbn*`
  2. `/testbooklistings/*retailer*`
  3. `/search/*retailer*`
  4. `/course/*school*`
  5. `/retailers`

- Web Data URLs

  1. `/static/*`

URL Definitions
---------------
*Asterisks - signify path parameter*

### User URLs

`/`

- Parameters  
  - None
- Calls
  - `/course/*school*` - to get available options for course input
- Action
  - Return the HTML of the home page of the website

`/search`

- Parameters
  - `q` - search term
  - `type` - search term type
- Calls
  - `/search/*retailer*` - to search the specified retailer for matching textbooks
- Action
  - Return the HTML of the search results page
  - Redirect to `/book/*isbn*` if search type is `isbn`

`/coursesearch/*school*`

- Parameters
  - `*school*` - (path parameter) the school to search courses on
- Calls
  - **Still Developing**
- Action
  - Returns the HTML of the course search page which displays the textbooks corresponding to inputed courses

`/book/*isbn*`

- Parameters
  - `*isbn*` - (path parameter) specifies the isbn of book to display
  - `url` - specifies url of a book whose isbn can be extracted from
  - `url-retailer` - specifies which retailer the url is to
- Calls
  - `/textbooklistings/*retailer*` - to get textbook listings from specified *retailer*
  - `/retailers` - to get a list of available retailers to get textbook listings from
  - `/textbook/*isbn*` - to get textbook details on the specified isbn
- Action
  - Redirect user to `/book/*isbn*` with the isbn extracted from `url` if `url` and `url-retailer` are present
  - Return the HTML of book page of the given isbn

`/error/*error_code*`

- Parameters
  - None
- Calls
  - None
- Action
  - Return HTML for the specified HTTP `error_code`

### API URLs

`/textbook/*isbn*`

- Parameters
  - `*isbn*` - (path parameter) the isbn of the book to return data on
- Called By
  - `/book/*isbn*` - to get textbook details
- Action
  - Return Textbook Object as JSON

`/testbooklistings/*retailer*`

- Parameters
  - `*retailer*` - (path parameter) retailer to get textbook listings from
  - `isbn` - (**Consistency Issue - Path Parameter in other URLs**) book to get textbook listings on
- Called By
  - `/book/*isbn*` - to get textbook listings for specified retailer
- Action
  - Return list of TextbookListings as JSON

`/search/*retailer*`

- Parameters
  - `*retailer*` - (path parameter) retailer to search for textbooks matching search term
  - `q` - search term
  - 'type' - search type
- Called By
  - `/search` - to get textbooks matching search term
- Action
  - Return list of Textbook Objects in JSON matching search term

`/course/*school*`

- Parameters
  - `*school*` - (path parameter) the school to search for the course data
  - `term` - ID for the term of the course
  - `dept` - ID for the department of the course
  - `num` - ID for the number of the course
  - `section` - ID for the section of the course
- Called By
  - `/` - to get available course data for user input
- Action
  - Return possible options for next course level if `term`, `dept`, or `num` is given
  - Return Course object as JSON if `section` is given

`/retailers`

- Parameters
  - None
- Called By
  - `/book/*isbn*` - to get retailers available to extract textbook listings from
- Action
  - Return list of retailers available to extract textbook listings from

### Web Data URLs

`/static/*`

- Parameters  
  - None
- Called By
  - All User URLs
- Action
  - Return static content such as images, CSS, JavaScript

[JSON]: http://www.json.org/ "JavaScript Object Notation"