# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.groups import Group

from django.contrib import messages
from django.views.generic import DeleteView

from ..util import paginate, get_current_group

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.student_set.exists():
            messages.error(self.request, u'Помилка. Група %s не порожня.' % self.object)
        else:
            self.object.delete()
            messages.success(self.request, u'Групу успішно видалено!')
        return HttpResponseRedirect(reverse('groups'))


# Views for Groups

def groups_list(request):
	groups = []

	# check if we need to show only one student of groups
	current_group = get_current_group(request)
	if current_group:
		groups.append(current_group)
	else:
		# otherwise show all groups
		groups = Group.objects.all()

	# try to order group list
	order_by = request.GET.get('order_by', '')
	if order_by in ('title', 'leader', 'id'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()
			
	# apply pagination, 3 students per page
	context = paginate(groups, 3, request, {}, var_name='groups')
	
	return render(request, 'students/groups_list.html', context)


def groups_add(request):
  return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
  return HttpResponse('<h1>Edit Group %s</h1>' % gid)


