"""
    To render html web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.shortcuts import render

def home_view(request):
    """
        Take in a request (Django sends request)
        Return HTML as a response (We pick to return the response)
    """
    name = "Rizal Fadia Al Fikri"
    my_list = [1,2,3,4,5,6]
    
    context = {
        "my_list": my_list,
        "title" : "this is title",
        "id" : "2"
    }

    # Django Templates
    # f = open("my-template.html",'r')
    # string = f.read()
    tmpl = get_template("home-view.html")
    tmpl_string = tmpl.render()
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = string.format(**context)

    return HttpResponse(HTML_STRING)