# import forms
from django import forms
from .models import Member

# Form for adding new member
class AddMemberForm(forms.ModelForm):
    # Specify that role selection will be radio button widget
    role = forms.ChoiceField(choices=Member.ROLETYPES, widget=forms.RadioSelect(), initial='regular')

    # Specify model to be used
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone', 'email', 'role']

# Form for editing chosen member
class EditMemberForm(forms.ModelForm):
    # Specify that role selection will be radio button widget
    role = forms.ChoiceField(choices=Member.ROLETYPES, widget=forms.RadioSelect())

    # Specify model to be used
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone', 'email', 'role']