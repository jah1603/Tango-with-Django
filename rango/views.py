# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('Rango says hello! <a href="/rango/about">About</a>')

def aboutpage(request):
    return HttpResponse('Rango says: "Here is the about page." <a href="/rango/">Index</a>')
