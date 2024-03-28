from django import forms
from django.forms import NumberInput, TextInput,Textarea,IntegerField
from .models import UserComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComment

        fields = [
            'name',
            'comment',
            'image',

        ]
        widgets = {
            'name': TextInput(attrs={'class': 'container', 'placeholder': 'name'}),
            'comment': Textarea(attrs={'class': 'container', 'placeholder': 'Describe your experience(optional)'}),
        }

