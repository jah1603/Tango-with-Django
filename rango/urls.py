from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about', views.aboutpage, name='about'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category')
    ]
