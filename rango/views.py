# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.http import HttpResponse

from rango.models import Category, Page

def index(request):
    # Request the context of the request.
# The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
# Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    category_name = category_name_url.replace('_',' ')

    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)

        pages = Page.objects.filter(category=category)

        context_dict[':pages'] = pages

        context_dict[':category'] = category

    except:
        Category.DoesNotExist:
            pass

    return render_to_response('rando/category.html', context_dict, context)




def aboutpage(request):
    return HttpResponse('Rango says: "Here is the about page." <a href="/rango/">Index</a>')
