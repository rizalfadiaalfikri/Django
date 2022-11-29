"""
    To render html web pages
"""

from django import HttpResponse

HTML_STRING = """
    <hi>Hello World</h1>
"""

def home(request):
    """
        Take in a request (Django sends request)
        Return HTML as a response (We pick to return the response)
    """
    return HttpResponse(HTML_STRING)