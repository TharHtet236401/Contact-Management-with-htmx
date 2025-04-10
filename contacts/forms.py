from django import forms
from .models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full mb-2',
            'placeholder': 'Contact Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input input-bordered w-full mb-2',
            'placeholder': 'Email Address'
        })
    )    

    document = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'file-input file-input-bordered w-full mb-2',
        }),
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        # Check if the email already exists for this user
        if name.startswith('X'):
            raise ValidationError("No names beginning with X!")
        return name    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Contact.objects.filter(email=email, user=self.initial.get('user')).exists():
            raise ValidationError("You already have a contact with this email address.")
        return email

    class Meta:
        model = Contact
        fields = (
            'name', 'email','document'
        )