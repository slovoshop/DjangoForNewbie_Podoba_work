
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, HTML
from crispy_forms.bootstrap import FormActions

from ..models.groups import Group
from ..util import paginate, get_current_group

from django.utils.translation import ugettext as _

class GroupCreateForm(ModelForm):
    class Meta:
				model = Group
				fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(GroupCreateForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        
        # set form tag attributes
        self.helper.form_action = reverse('groups_add')
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
            Submit('add_button', _(u'Save'), css_class="btn btn-primary"),
            HTML(u"<a class='btn btn-link' name='cancel_button' href='{% url 'groups' %}?status_message= \
						Group adding canceled!'>Cancel</a>"),
        ))
        # self.fields['leader'].queryset = self.fields['leader'].queryset.none()

class GroupUpdateForm(GroupCreateForm):

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('groups_edit', kwargs = {'pk': kwargs['instance'].id})
        self.fields['leader'].queryset = self.instance.student_set.all().order_by('last_name')
        
class GroupCreateView(CreateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupCreateForm
    
    def get_success_url(self):
        messages.info(self.request, u'%s %s %s' % (_(u"Group"), self.object.title, _(u"was added successfully!")))
        return reverse('groups')

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm
    
    def form_valid(self, form):
        leader = form.cleaned_data['leader']
        if not leader or leader.student_group_id == form.instance.id:
            return super(GroupUpdateView, self).form_valid(form)
        else:
            messages.error(self.request, _(u'The student reffer to another group'))
            return super(GroupUpdateView, self).form_invalid(form)

    def get_success_url(self):
        messages.info(self.request, u'%s %s %s' % (_(u"Group"), self.object.title, _(u"was saved successfully!")))
        return reverse('groups')

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.student_set.exists():
            messages.error(self.request, u'%s %s %s' % (_(u"Mistake.Group "), self.object, _(u"is not empty!")))
        else:
            self.object.delete()
            messages.success(self.request, _(u'Group was deleted successfully!'))
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


