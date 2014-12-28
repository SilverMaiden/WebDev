import webapp2
from main_page import MainPage






app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/welcome', WelcomeHandler),
    #('/testform', TestHandler),
                              ],debug=True)







