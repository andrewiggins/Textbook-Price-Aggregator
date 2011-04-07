import cgi
import os
import urllib
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import urlfetch
import datetime,traceback

class MainPage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("HI THERE")
		
		
application = webapp.WSGIApplication(
                                     [('/',MainPage)],
                                     debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()