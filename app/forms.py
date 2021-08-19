from django.core.mail import send_mail, get_connection

from django.forms.widgets import TextInput

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
    attrs={'placeholder': 'Name', 'class': 'form-control', 'id':'c_name'}))

    email = forms.EmailField(label='email', widget=forms.TextInput(
    attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id':'c_email'}),
    required=False)

    message = forms.CharField(widget=forms.Textarea(
    attrs={"rows":5, 'placeholder': 'Message', 'class': 'form-control', 'id':'c_message'}))