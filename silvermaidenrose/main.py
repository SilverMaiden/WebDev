import webapp2
from main_page import MainPage
from welcome_page import WelcomeHandler
from login_page import LoginPage

app = webapp2.WSGIApplication([
    ('/signup', MainPage),
    ('/welcome', WelcomeHandler),
    ('/login', LoginPage)
    #('/testform', TestHandler),
                              ],debug=True)
