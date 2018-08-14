from django import forms  
from bazar.models import Bazar  

class BazarForm(forms.ModelForm):
	
    class Meta:  
        model = Bazar 
        fields = "__all__" 
