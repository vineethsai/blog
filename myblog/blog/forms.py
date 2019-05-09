from django import forms
from django.forms import CharField

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200, required=True)
    text = forms.CharField(label="Text", required=True, widget=forms.Textarea)
    is_published = forms.BooleanField(label="Publish now?", required=True)