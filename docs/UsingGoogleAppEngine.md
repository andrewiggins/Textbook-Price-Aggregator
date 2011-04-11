Google App Engine
=================

---

Setting Up Google App Engine and Eclipse
----------------------------------------
1. Setup Google App Engine Python SDK

2. Setup Eclipse

3. Setup PyDev using Eclipse Marketplace

4. Setup PyDev Compiler if not already done
   1. (On Eclipse for Windows) Windows -> Preferences -> PyDev -> Interpreter Python
   2. You can try Auto-Config or just adding the directory to the python directory yourself

5. Setup Google App Engine in Eclipse
   1. See this [Google App Engine Eclipse] guide.
   2. Add the directories under the external libraries tab of Eclipse
   3. Add Run Configuration as specified on the above guide.

---

Special Notes about Google App Engine
-------------------------------------

###Reserved URLs:
The following URLs are [reserved][Reserved URLs] by Google App Engine.

- /_ah/
- /form

###Inbound Services
These [inbound services] are available to us to enable:

- Email
- XMPP chat
- warmup request

###Custom Error Responses
Google App Engine allows us to setup [custom error responses] for the following errors:

- over_quota
  - Indicates the app has exceeded a resource quota
- dos\_api\_denial
  - Served to any client blocked by your app's DoS Protection configuration
- timeout
  - Served if a deadline is reached before there is a response from your app.

[Google App Engine Eclipse]: http://code.google.com/appengine/articles/eclipse.html "Google App Engine in Eclipse for Python"
[Reserved URLs]: http://code.google.com/appengine/docs/python/config/appconfig.html#Reserved_URLs "Reserved URLs"
[Inbound Services]: http://code.google.com/appengine/docs/python/config/appconfig.html#Inbound_Services "Inbound Services"
[Custom Error Responses]: http://code.google.com/appengine/docs/python/config/appconfig.html#Custom_Error_Responses