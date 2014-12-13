import webapp2
import cgi
import re
import Jinja2

form ="""
<form method="post" action="/">
    <h2> FIZZBUZZZY!!! :D </h2>
    <ol>
        {% for x in range(1, n+1) %}
            <li>
            {% if (x % 3 == 0 and x % 5 != 0) %}
                Fizz
            {% elif (x % 3 != 0 and x % 5 == 0) %}
                Buzz
            {% elif (x % 3 == 0 and x % 5 == 0) %}
                FizzBuzz
            {% else %}
                {{x}}
            {% endif %}
            </li>
        {% endfor %}
    </ol>
</form>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)


    #deif post(self):




app = webapp2.WSGIApplication([
    ('/', MainPage),
    #('/testform', TestHandler),
                              ],debug=True)








