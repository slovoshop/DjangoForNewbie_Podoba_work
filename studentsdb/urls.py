"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import students.views.students, students.views.groups, students.views.test, students.views.exams,  django.views.static 
from .settings import MEDIA_ROOT, DEBUG

from students.views.contact_admin import ContactView
from students.views.students import StudentCreateView, StudentUpdateView, StudentDeleteView
from students.views.groups import GroupDeleteView
from students.views.journal import JournalView


urlpatterns = [
 
# Students urls


  url(r'^$', students.views.students.students_list, name='home'),
  url(r'^students/add/$', StudentCreateView.as_view(), name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
  url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

# Groups urls
  url(r'^groups/$', students.views.groups.groups_list, name='groups'),
  url(r'^groups/add/$', students.views.groups.groups_add,
    name='groups_add'),
  url(r'^groups/(?P<gid>\d+)/edit/$', students.views.groups.groups_edit,
    name='groups_edit'),
  url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

#Journal urls
	url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),  
	# url(r'^journal/$', JournalView.as_view(), name='journal'),

#Exams urls
	url(r'^exams/$', students.views.exams.exams_list, name='exams'),

  url(r'^admin/', include(admin.site.urls)),

# Contact Admin Form
	url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),

#Test page
  url(r'^test/$', students.views.test.test,
    name='test'),
]


if DEBUG:
# serve files from media folder, bookpage-237 
  urlpatterns += [
  url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': MEDIA_ROOT})
  ]

