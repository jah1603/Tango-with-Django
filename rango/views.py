# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token

from django.http import HttpResponse

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

def decode_url(url):
    return url.replace('_', ' ')

def encode_url(url):
    return url.replace(' ', '_')

@csrf_protect
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

    for category in category_list:
        category.url = category.name.replace(' ', '_')

    return render_to_response('rango/index.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)

    print(category_name_url + " URL HERE")

    category_name = decode_url(category_name_url)

    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category

        context_dict['category_name_url'] = category_name_url

    except Category.DoesNotExist:
            pass

    return render_to_response('rango/category.html', context_dict, context)

@csrf_protect
@requires_csrf_token
def add_category(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = CategoryForm(request.POST)


        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print form.errors
    else:
        form = CategoryForm()

# NEED TO USE RENDER (OBSERVE PARAMETER ORDER) TO FIX CSRF TOKEN ISSUE
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_url(category_name_url)


    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)

            cat = Category.objects.get(name=category_name)
            page.category = cat


            page.views = 0
            page.save()


            return category(request, category_name_url)
        else:
            print("I'm being diverted")
            print form.errors
    else:
        form = PageForm()

    return render(request, 'rango/add_page.html',
        {'category_name_url': category_name_url,
        'category_name': category_name, 'form': form})

def aboutpage(request):
    return HttpResponse('Rango says: "Here is the about page." <a href="/rango/">Index</a>')
