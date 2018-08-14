from django import forms
from registration.models import Registration

class RegistrationForm(forms.ModelForm):

    class Meta:
    	model= Registration
    	fields = "__all__"
