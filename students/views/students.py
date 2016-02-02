# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.students import Student
from ..models.groups import Group

from datetime import datetime

from django.views.generic import CreateView, UpdateView, DeleteView
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, HTML
from crispy_forms.bootstrap import FormActions

from ..util import paginate, get_current_group

# класс формы добавления студента
class StudentCreateForm(ModelForm):
	class Meta:
		model = Student
		fields = "__all__"
    
	def __init__(self, *args, **kwargs):
		super(StudentCreateForm, self).__init__(*args, **kwargs)
        
		self.helper = FormHelper(self)
        
		# set form tag attributes
		self.helper.form_action = reverse('students_add')
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'
        
		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = True
		self.helper.label_class = 'col-sm-2 control-label'
		self.helper.field_class = 'col-sm-10'
        
		# add buttons
		self.helper.layout.append(FormActions(
			Div(css_class = self.helper.label_class),
			Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
			HTML(u"<a class='btn btn-link' name='cancel_button' \
			href='{% url 'home' %}?status_message=Додавання студента скасовано!'>Скасувати</a>"),
		))


# класс формы редактирования студента
class StudentUpdateForm(StudentCreateForm):

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('students_edit', kwargs = {'pk': kwargs['instance'].id})


# добавление студента
class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentCreateForm
    #success_url = 
    
    def get_success_url(self):
			return u'%s?status_message=Студента %s %s успішно додано!' % (reverse('home'),
      self.request.POST.get('first_name'), self.request.POST.get('last_name'))
       
        

# редактирование студента
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm
    
    def get_success_url(self):
        return u'%s?status_message=Студента %s %s успішно збережено!' % (reverse('home'),
            self.request.POST.get('first_name'), self.request.POST.get('last_name'))
        
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


# удаление студента
class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_confirm_delete.html'

	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!' % reverse('home')



# Views for Students
def students_list(request):
	# check if we need to show only one group of students
	current_group = get_current_group(request)

	if current_group:
		students = Student.objects.filter(student_group=current_group)
	else:
		# otherwise show all students
		students = Student.objects.all()

	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# apply pagination, 3 students per page
	context = paginate(students, 3, request, {}, var_name='students')

	return render(request, 'students/students_list.html', context)











