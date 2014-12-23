import webapp2

class LogoutPage(webapp2.RequestHandler):
    def get(self):
        self.response.set_cookie("user_id","")
        self.redirect('/signup')
