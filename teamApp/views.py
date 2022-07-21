from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Member
from .forms import AddMemberForm, EditMemberForm

# Display list of members
class MemberListView(ListView): 
    model = Member
    context_object_name = 'allmembers'
    template_name = 'teamApp/member_list.html'

# Display form to add new member
class AddMemberView(CreateView): 
    model = Member
    form_class = AddMemberForm
    template_name = 'teamApp/member_form.html'
    success_url = reverse_lazy("member_list")

# Display form to edit chosen member
class EditMemberView(UpdateView):
    # specify the model you want to use
    model = Member
    form_class = EditMemberForm
    context_object_name = 'member'
    template_name = 'teamApp/member_update_form.html'
    success_url = reverse_lazy("member_list")

class MemberDeleteView(DeleteView):
    # specify the model you want to use
    model = Member
    context_object_name = 'member'
    template_name = 'teamApp/member_confirm_delete.html'
    success_url = reverse_lazy("member_list")