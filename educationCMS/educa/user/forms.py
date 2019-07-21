from django import forms
from django.contrib.auth.models import User

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password',
#                                widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password',
#                                 widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}))
    first_name = forms.CharField(label="first_name", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'first_name'}))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'email'}))
    password = forms.CharField(label='Password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password'}))
    password2 = forms.CharField(label='Repeat password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password repeat'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'username'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'password'}))
    # captcha = CaptchaField(label='验证码')