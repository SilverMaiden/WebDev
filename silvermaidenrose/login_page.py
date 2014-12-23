import webapp2
from google.appengine.ext import db
from models import User
from login_form import form
from secure import make_secure_val



class LoginPage(webapp2.RequestHandler):
    def get(self):
        data = {
            "username_value":"",
            "username_error":"",
            "password_validity_error":""
                }

        new_form = form % data


        self.response.out.write(new_form)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        data = {
            "username_value":"",
            "username_error":"",
            "password_validity_error":""
                }

       # new_form = form % data

        q = User.all()
        q.filter('username', username)
        username_stuff = q.get()
        q.filter('password', password)
        password_stuff = q.get()
        #user_password = username_stuff.password


        def error_check(form):
            data["username_value"] = username
            if username_stuff is None:
                data["username_error"] = "Invalid username"
            if password_stuff is None:
                data["password_validity_error"] = "Invalid password"
            return form % data

        form_now_checked = error_check(form)


        def final_check(form_now_checked):
            if (data["username_error"] == "" and
                data["password_validity_error"] == ""):
                user_id = username_stuff.key().id()
                user_key = db.Key.from_path('User', user_id)
                user_salt = username_stuff.salt
                secure_val = make_secure_val(str(user_id), user_salt)
                hashed_thing = secure_val.split(',')[0]
                self.response.set_cookie("user_id", str(user_id) + '|' + hashed_thing)
                self.redirect('/welcome', code=302)
            return form_now_checked

        final_form = final_check(form_now_checked)

        self.response.out.write(final_form)










        #password == password_stuff and

      #  user_id_cookie = self.request.cookies.get('user_id')
       # self.response.out.write(user_id_cookie)


