import webapp2
from google.appengine.ext import db
from secure import secure_val_p

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
       user_id_cookie = self.request.cookies.get('user_id')
     #  self.response.out.write(user_id_cookie)
       split_cookie = user_id_cookie.split('|')
       user_id = int(split_cookie[0])

       user_key = db.Key.from_path('User', user_id)
       #self.response.out.write(user_key.id_or_name())

       user = db.get(user_key)
       user_name = user.username
       user_salt = user.salt
       #def cookie_check():
        #   if secure_val_p()
       #self.response.out.write("Welcome, " + self.request.get('username'))
       if secure_val_p(user_id_cookie, user_salt):
           self.response.out.write("Welcome, " + user_name)
       else:
           self.redirect('/signup')


