import web
from pprint import pprint
web.config.debug = False

urls = (
  '/count', 'count',
  '/reset', 'reset',
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count', 0})

print type(session)
pprint(vars(session))

class count:
	def GET(self):
		session.count += 1
		return str(session.count)

class reset:
	def GET(self):
		session.kill()
		return ""

if __name__ == "__main__":
    app.run()
