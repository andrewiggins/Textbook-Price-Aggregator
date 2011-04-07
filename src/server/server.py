from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import parsers.retailers
import pkgutil,json
class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("HI THERE")

class Vendors(webapp.RequestHandler):
    @staticmethod
    def get_vendors():
        return json.dumps([info[1] for info in pkgutil.walk_packages(parsers.retailers.__path__) if not info[2]])
    def get(self):
        self.response.out.write(Vendors.get_vendors())
    
application = webapp.WSGIApplication(
                                     [('/vendors',Vendors),
                                      ('/.*',MainPage)],
                                     debug=True)



def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()