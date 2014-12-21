import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class BlogEntry(db.Model):
    subjectbox = db.StringProperty(required=True)
    blogpost = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add = True)




class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_main(self):
        entrys = db.GqlQuery("select * from BlogEntry order by created desc")
        self.render("mainblogpage.html", entrys = entrys)




class MainPage(Handler):
    def get(self):
        self.render_main()



class newentry(Handler):
    def render_blogpost(self, subjectbox="", blogpost="", error=""):
        self.render("blogpage.html", subjectbox=subjectbox, blogpost=blogpost, error=error )

    def get(self):
        self.render_blogpost()

    def post(self):
        subjectbox = self.request.get("subjectbox")
        blogpost = self.request.get("blogpost")

        if subjectbox and blogpost:
            be = BlogEntry(subjectbox = subjectbox, blogpost = blogpost)
            be.put()
            self.redirect("/blog/%s" % str(be.key().id()))

        else:
            error = "Both subject and text required."
            self.render_blogpost(subjectbox, blogpost, error)


class PermalinkHandler(webapp2.RequestHandler):
    def get(self, blogentry_id):
        blogentry = BlogEntry.get_by_id(int(blogentry_id))

        if blogentry:
            self.render("mainblogpage.html", subjectbox=blogentry.subjectbox, blogpost=blogentry.blogpost, error="")
        else:
            self.render("mainblogpage.html")







app = webapp2.WSGIApplication([('/blog', MainPage),
                               ('/blog/newpost', newentry),
                               ('blog/(\d+)', )
                               ],
                              debug=True)




