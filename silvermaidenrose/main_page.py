import webapp2
import re
from form import form

class MainPage(webapp2.RequestHandler):
    def get(self):
        data = {
            "username_value":"",
            "username_error":"",
            "password_validity_error":"",
            "verify_error":"",
            "email_value":"",
            "email_error":""
                }
        new_form = form % data

        self.response.out.write(new_form)


    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        data = {
            "username_value":"",
            "username_error":"",
            "password_validity_error":"",
            "verify_error":"",
            "email_value":"",
            "email_error":""
                }

        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        def valid_username(username):
            return USER_RE.match(username)
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        def valid_email(email):
            return EMAIL_RE.match(email)
        PW_RE = re.compile(r"^.{3,20}$")
        def valid_password(password):
            return PW_RE.match(password)

        def replacee(form):
            data["username_value"] = username
            data["email_value"] = email
            if not valid_username(username):
                data["username_error"] = "That is not a valid username"
            if password != verify:
                data["verify_error"] = "Your passwords do not match"
            if not valid_password(password):
                data["password_validity_error"] = "Not a valid password"
            if not valid_email(email):
                data["email_error"] = "Not a valid email"
            return form % data

        form1 = replacee(form)

        def check(form1):
            if (data["username_error"] == "" and
                data["password_validity_error"] == "" and
                data["verify_error"] == "" and
                data["email_error"] == ""):
                self.redirect('/welcome?username='+username, code=302)
            return form1
        form2 = check(form1)


        self.response.out.write(form2)

