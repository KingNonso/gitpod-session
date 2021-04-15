from django import forms
from django.core.exceptions import ValidationError

from masterpiece.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'body']

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        body = cleaned_data.get('body')
        if subject is None or subject == '':
            self.add_error('Subject', ValidationError('Subject is required'))
        return cleaned_data

