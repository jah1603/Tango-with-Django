# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import User

from rango.models import Category, Page, UserProfile
from rango.forms import CategoryForm, PageForm
from rango.forms import UserForm, UserProfileForm


class RangoRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return '/rango/'


def add_page(request, category_slug_url):
	print category_slug_url
	try:
		category = Category.objects.filter(slug=category_slug_url)[0]
	except Category.DoesNotExist:
		category = None

	print category
	form = PageForm()
        cat_list = get_category_list()
	if request.method == 'POST':
		form = PageForm(request.POST)
		if category:
			page = form.save(commit=False)
			page.category = category
			page.views = 0
			page.save()
			return show_category(request, category_slug_url)
		else:
			print form.errors
	_context = {
		'form': form,
		'category': category,
		'title' : 'Add a Page',
        'cat_list': cat_list
	}
	return render(request, 'rango/add_page.html', context=_context)


def add_category(request):
        cat_list = get_category_list()
	form = CategoryForm()



	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print(form.errors)


	return render(request, 'rango/add_category.html', {'form':form, 'cat_list': cat_list})


def show_category(request, category_name_url):
	_context = {}

        cat_list = get_category_list()

	try:
		category = Category.objects.get(slug=category_name_url)
		pages = Page.objects.filter(category=category)
		_context['category'] = category
		_context['pages'] = pages
	except Category.DoesNotExist:
		_context['category'] = None
		_context['pages'] = None
        _context['cat_list'] = cat_list


	return render(request, 'rango/category.html', context=_context)

def get_category_list():
    cat_list = Category.objects.all()
    for cat in cat_list:
        cat.url = cat.slug
        return cat_list


@login_required
def profile(request):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {'cat_list': cat_list}
    u = User.objects.get(username=request.user)

    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up

    return render(request, 'rango/profile.html', context_dict)

def index(request):

	category_list = Category.objects.order_by('-likes')[:5]
	pages_list = Page.objects.order_by('-views')[:5]
        cat_list = get_category_list()
	_context = {
		'categories': category_list,
		'most_viewed_pages': pages_list,
		'title' : 'Welcome to Tango with Django',
        'cat_list': cat_list
	}

	response = render(request, 'rango/index.html', context=_context)

        visits = int(request.COOKIES.get('visits', '0'))

        if request.session.get('last_visit'):
# Yes it does! Get the cookie's value.
            last_visit_time = request.session.get('last_visit')
            print(last_visit_time)
            visits = request.session.get('visits', 0)
# If it's been more than a day since the last visit...
            if  (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
# ...reassign the value of the cookie to +1 of what it was before...
                request.session['visits'] = visits + 1
                request.session['last_visit'] = str(datetime.now())
        else:
# Cookie last_visit doesn't exist, so create it to the current date/time.
            request.session['last_visit'] = str(datetime.now())
            request.session['visits'] = 1
# Return response back to the user, updating any cookies that need changed.

	return render(request, 'rango/index.html', _context)


def about(request):

    cat_list = get_category_list()

    if request.session.get('visits'):
        count = request.session.get('visits')
        print(count)
    else:
        count = 0
# remember to include the visit data

    _context = {'visits': count, 'cat_list': cat_list}

    return render(request, 'rango/about.html', _context)


def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit = False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print user_form.errors
			print profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'rango/register.html', {
			'user_form': user_form,
			'profile_form': profile_form,
			'registered': registered
		})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('rango:index'))
			else:
				return HttpResponse("Your account has been disabled. Please contact the admin.")
		else:
			return HttpResponse("Invalid username/password.")
	else:
		return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('rango:index'))


@login_required
def restricted(request):
        cat_list = get_category_list()
	return render(request, 'rango/restricted.html', {'cat_list': cat_list})
