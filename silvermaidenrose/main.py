import webapp2
from main_page import MainPage
from welcome_page import WelcomeHandler
from login_page import LoginPage
from logout_form import LogoutPage

app = webapp2.WSGIApplication([
    ('/signup', MainPage),
    ('/welcome', WelcomeHandler),
    ('/login', LoginPage),
    ('/logout', LogoutPage)
    #('/testform', TestHandler),
                              ],debug=True)
