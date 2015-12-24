# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from ..models import Student


# Views for Test
def test(request):
		
		# делаем выборку QuerySet всех записей таблицы students_student - аналог SELECT *
		students = Student.objects.all()

		""" Блок сортировки QuerySet """

		# считываем критерий сортировки из url
		order_by = request.GET.get('order_by', '')

		# если критерий пустой (домашняя страница) - сортируем по фамилии
		if order_by == '':
			students = students.order_by('last_name') 

		#  если критерий указан, то сортируем по нему
		elif order_by in ('last_name', 'first_name', 'ticket', 'id'):
			students = students.order_by(order_by)

			# если в url указан критерий реверса, то делаем реверс сортировки
			if request.GET.get('reverse', '') == '1':
				students = students.reverse()

		""" Формируем постраничный вывод после сортировки """

		# считываем параметр page из url
		page = request.GET.get('page')

		try:
			page = int(page)
		except(ValueError, TypeError):
			page = 1

		# назначаем количество отображаемых записей на одной странице навигатора
		per_page = 3

		# определяем колво страниц навигатора и остаток - колво записей на последней странице
		number_of_pages, remainder = divmod(Student.objects.count(), per_page)

		if remainder != 0:
			number_of_pages += 1

		if page < 1:
			page = 1
		elif page > number_of_pages:
			page = number_of_pages

		# Вычисляем индексы начальной и конечной записей для вывода на текущей странице
		start = (int(page)-1)*per_page
		end = start + per_page		

		# формируем набор записей для запрашиваемой страницы
		students = students[start:end]

		""" Задаём тестовые переменные для отображения в шаблоне во время наладки """		
                  
		testparam1 = [start, end]
		testparam2 = Student.objects.count()
                                  
		""" Отправляем выходные параметры в шаблон """
                          
		return render(request, 'students/pages_without_paginator.html',
				{ 'students': students, 
					'pages': [x for x in range(1, number_of_pages+1)], 
					'page': page,
					'number_of_pages': number_of_pages,
					'testparam1': testparam1,
					'testparam2': testparam2
				})





