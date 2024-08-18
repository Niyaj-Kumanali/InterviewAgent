from django import forms
from django.forms import TextInput,EmailInput

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control input1'}), max_length=100)
    from_email = forms.EmailField(label = 'Email', widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com', 'class':'form-control input1'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control input1'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message here', 'class':'form-control input1'}))
