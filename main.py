#!/usr/bin/env python
import os
import jinja2
import webapp2
import random


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class LotoNumbers(BaseHandler):
    def get(self):
        numbers = generacija_stevil(7)

        params = {"number1": numbers[0], "number2": numbers[1], "number3": numbers[2], "number4": numbers[3], "number5": numbers[4], "number6": numbers[5], "number7": numbers[6]}

        return self.render_template("loto_generator.html", params=params)

def generacija_stevil(izbira_stevil):
    seznam_stevil = []
    for it in range(0, izbira_stevil):
        while True:
            random_stevilo = random.randint(1,30)
            if random_stevilo not in seznam_stevil:
                break
        seznam_stevil.append(random_stevilo)
    return seznam_stevil


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/loto_generator', LotoNumbers),
], debug=True)
