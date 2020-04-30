from django.forms import ModelForm

from .models import ContactForm


class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "subject", "message"]
