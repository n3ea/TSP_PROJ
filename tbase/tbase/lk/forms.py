
# tbase/tbase/lk/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from book.models import Clients

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['fio', 'tel_n', 'e_mail']
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_n': forms.TextInput(attrs={'class': 'form-control'}),
            'e_mail': forms.EmailInput(attrs={'class': 'form-control'}),
        }
