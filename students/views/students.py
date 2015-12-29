# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.students import Student
from ..models.groups import Group


# Views for Students
def students_list(request):
		students = Student.objects.all()

		# try to order students list
		order_by = request.GET.get('order_by', '')
		if order_by == '':
			students = students.order_by('last_name') 				
		elif order_by == 'ticket':
			students = students.extra(select={'ticket': 'CAST(ticket AS UNSIGNED)'}).extra(order_by = ['ticket'])					
		elif order_by in ('id', 'last_name', 'first_name'):
			students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()			
		
		per_page = 3		

		paginator = Paginator(students, per_page)
		page = request.GET.get('page')
		try:
			students = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			students = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver
			# last page of results.
			students = paginator.page(paginator.num_pages)

		# Добавка к forloop.counter при сортировке по полю №
		id_sort = per_page * (students.number - 1)
	
		# формирование списка номеров для поля № при реверсной сортировке
		id_reverse = []				
		if request.GET.get('reverse', '') == '1':		
			for i in range(paginator._count - id_sort, paginator._count - id_sort - per_page, -1):
					id_reverse.append(i)	
		
		test = 'none'		

		return render(request, 'students/students_list.html',
		{'students': students, 'id_sort': id_sort, 'id_reverse': id_reverse, 'test': test})




def students_add(request):

	# was form posted?
	if request.method == "POST":		

		# was form add button clicked?
		if request.POST.get('add_button') is not None:

			# TODO: validate input from user
			errors = {}

			if not errors:
				# create student object
				student = Student(
					first_name=request.POST['first_name'],
					last_name=request.POST['last_name'],
					middle_name=request.POST['middle_name'],
					birthday=request.POST['birthday'],
					ticket=request.POST['ticket'],
					student_group=
					Group.objects.get(pk=request.POST['student_group']),
					photo=request.FILES['photo'],
					notes=request.POST['notes'],
					)
				# save it to database
				student.save()
				# redirect user to students list
				return HttpResponseRedirect(reverse('home'))

			else:
				# render form with errors and previous user input
				return render(request, 'students/students_add.html',
				{'groups': Group.objects.all().order_by('title'),
				'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			return HttpResponseRedirect(reverse('home'))

	else:
		# initial form render
		return render(request, 'students/students_add.html', 
		{'groups': Group.objects.all().order_by('title')})




def students_edit(request, sid):
  return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
  return HttpResponse('<h1>Delete Student %s</h1>' % sid)
