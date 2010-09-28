import prorogue

from google.appengine.ext import db
from google.appengine.ext import webapp

class List(prorogue.Handler):

	def get(self):
		items = prorogue.Item.gql('ORDER BY date DESC LIMIT 50')
		context = { 'items': items }
		self.render('list', context)

class Save(prorogue.Handler):

	def get(self):
		self.redirect('/')
	
	def post(self):
		item = prorogue.Item()
		item.url = self.request.get('url')
		item.description = self.request.get('description')
		item.date = datetime.utcnow()
		key = item.put()
		self.redirect('/')

