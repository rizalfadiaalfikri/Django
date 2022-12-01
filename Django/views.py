"""
    To render html web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello World')