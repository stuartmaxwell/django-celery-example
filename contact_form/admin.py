from django.contrib import admin

from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "subject", "created_on")


admin.site.register(ContactForm, ContactFormAdmin)
