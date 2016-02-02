from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exam import Exam

from ..util import paginate, get_current_group

def exams_list(request):
	# check if we need to show only one group of exam
	group = get_current_group(request)
	if group:
		exams = Exam.objects.filter(exam_group = group)
	else:
		# otherwise show all students
		exams = Exam.objects.all()


	order_by = request.GET.get('order_by', '')
	if order_by in ('title', 'date', 'teacher', 'exam_group'):
		exams = exams.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exams = exams.reverse()


	# apply pagination, 3 exam per page
	context = paginate(exams, 3, request, {}, var_name='exams')
	
	return render(request, 'students/exams.html', context)
