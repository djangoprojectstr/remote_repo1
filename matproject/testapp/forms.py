from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from testapp.models import Matr
# from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
     class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')
     def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class Studsform(forms.ModelForm):
    date_of_birth=forms.DateTimeField(help_text='DD/MM/YYYY H:M',input_formats=['%d/%m/%Y %H:%M'])
    caste = forms.CharField(max_length=36,help_text='WITH SUB CASTE', required=False)
    class Meta():
        model=Matr
        fields=('fullname','phone','age','gender','caste','date_of_birth','location','comments','photo')

class EditForm(forms.ModelForm):
     template_name='/something/else'

     class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')

class Estudsform(forms.ModelForm):
    template_name='/something/else'
    class Meta():
        model=Matr
        fields=('fullname','phone','age','gender','caste','date_of_birth','location','comments','photo')



class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
