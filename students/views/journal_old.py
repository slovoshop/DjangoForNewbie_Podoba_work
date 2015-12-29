# -*- coding: utf-8 -*-

#from django.shortcuts import render
#from django.http import HttpResponse

# Views for Journal
#def journal_list(request):
#  return HttpResponse(request, 'students/attendance.html', {})
#  return HttpResponse('<h1>Hello World</h1>')

from django.http import HttpResponse
from django.template import RequestContext, loader

def journal_list(request):
  template = loader.get_template('students/attendance.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))
