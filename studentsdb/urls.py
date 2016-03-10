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
from students.views.groups import GroupCreateView, GroupUpdateView, GroupDeleteView
from students.views.journal import JournalView

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView

from django.contrib.auth.decorators import login_required


js_info_dict = {
	'packages': ('students',),
}


urlpatterns = [
 
# Students urls

  url(r'^$', 															students.views.students.students_list, name='home'),
	url(r'^trans/$', 												students.views.students.trans, name='trans'),
  url(r'^students/add/$', 								StudentCreateView.as_view(), name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$', 		StudentUpdateView.as_view(), name='students_edit'),
  url(r'^students/(?P<pk>\d+)/delete/$', 	StudentDeleteView.as_view(), name='students_delete'),

# Groups urls
  url(r'^groups/$', 										login_required(students.views.groups.groups_list), name='groups'),
	url(r'^groups/add/$', 								login_required(GroupCreateView.as_view()), name='groups_add'),
	url(r'^groups/(?P<pk>\d+)/edit/$', 		login_required(GroupUpdateView.as_view()), name='groups_edit'),
  url(r'^groups/(?P<pk>\d+)/delete/$', 	login_required(GroupDeleteView.as_view()), name='groups_delete'),

#Journal urls
	url(r'^journal/(?P<pk>\d+)?/?$', 			JournalView.as_view(), name='journal'),  

#Exams urls
	url(r'^exams/$', 											students.views.exams.exams_list, name='exams'),

# Admin
  url(r'^admin/', 											include(admin.site.urls)),

# Contact Admin Form
	url(r'^contact-admin/$', 							ContactView.as_view(), name='contact_admin'),

# Languages
	url(r'^jsi18n\.js$', 									'django.views.i18n.javascript_catalog', js_info_dict),
	url(r'^i18n/', 												include('django.conf.urls.i18n')),

# User Related urls
	url(r'^users/logout/$', 							auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
	url(r'^register/complete/$', 					RedirectView.as_view(pattern_name='home'), name='registration_complete'),
	url(r'^users/', 											include('registration.backends.simple.urls', namespace='users')),

#Test page
  url(r'^test/$', 											students.views.test.test,
    name='test'),
]


if DEBUG:
# serve files from media folder, bookpage-237 
  urlpatterns += [
  url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': MEDIA_ROOT})
  ]

