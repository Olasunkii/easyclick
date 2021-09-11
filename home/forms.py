from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label='Enter name', min_length=2, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    phone = forms.CharField(
        label='Enter Number', min_length=2, max_length=50)
    message = forms.CharField(label='Enter message', help_text='Required', widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Phone'})
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Message'})
