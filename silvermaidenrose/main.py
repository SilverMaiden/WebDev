import webapp2
from main_page import MainPage
from welcome_page import WelcomeHandler

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/welcome', WelcomeHandler),
    #('/testform', TestHandler),
                              ],debug=True)
