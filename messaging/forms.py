from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.none(),  # lo definimos en __init__
        label='Para'
    )

    class Meta:
        model = Message
        fields = ['receiver', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje...'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        qs = User.objects.all()
        if user:
            qs = qs.exclude(id=user.id)
        self.fields['receiver'].queryset = qs.order_by('username')
