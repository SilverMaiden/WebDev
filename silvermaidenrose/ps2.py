import webapp2
import cgi

form ="""
<form method="post" action="/testform">
    <h1>Enter some text to ROT13:</h1>
    <textarea rows='15' cols='60' name="text">%(user_text)s</textarea>
    <br>
    <input type="submit" value="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
  #      #self.response.headers['Content-Type'] = 'text/plain'
        user_text = ""
        self.response.out.write(form % {"user_text":user_text})


class TestHandler(webapp2.RequestHandler):

    def post(self):

        def replace(text):
            string = ""
            for letter in text:
                if letter == " " or letter =="\n":
                    string += " "
                if rot13(letter):
                    string += rot13(letter)

            return string

        def rot13(letter):
            num = ord(letter)

            if num in range(65,91):
                return chr((ord(letter) -65 +13)%26 +65)

            if num in range(97,123):
                return chr((ord(letter) -97 +13)%26 +97)

        user_text = self.request.get("text")
        user_text = replace(user_text)

        self.response.out.write(form % {"user_text":user_text})

        #self.response.headers['Content-Type'] = 'text/plain'
       # self.response.out.write(self.request)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testform', TestHandler)],
                              debug=True)





#Figure out how to use cgi with this

