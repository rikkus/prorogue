import cgi

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp

import prorogue
from prorogue import handlers

application = webapp.WSGIApplication(
	[
		('/', prorogue.handlers.List),
		('/add', prorogue.handlers.Add),
		('/save', prorogue.handlers.Save)
	],
	debug=True
)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()

