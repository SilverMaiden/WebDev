import webapp2

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
       self.response.out.write("Welcome, " + self.request.get('username'))

