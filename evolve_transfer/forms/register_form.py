from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label="Confirm Password")

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "username")

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
