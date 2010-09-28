import tenjin

from tenjin.helpers import *

from google.appengine.ext import db
from google.appengine.ext import webapp

shared_cache = tenjin.GaeMemcacheCacheStorage()
engine = tenjin.Engine(cache=shared_cache)

class Item(db.Model):

	url = db.TextProperty()
	description = db.TextProperty()
	date = db.DateTimeProperty()

class Handler(webapp.RequestHandler):
	def render(self, template_name, context):
		self.response.out.write(
			engine.render('templates/' + template_name + '.html', context)
		)


