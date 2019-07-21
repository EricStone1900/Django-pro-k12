from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	name = forms.CharField(label="name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'name'}))
	email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email'}))
	body = forms.CharField(label="body", widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'body'}))

	class Meta:
	    model = Comment
	    fields = ('name', 'email', 'body')