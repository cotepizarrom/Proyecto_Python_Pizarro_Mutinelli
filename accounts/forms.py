from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birthday', 'avatar']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }