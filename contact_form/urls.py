from django.urls import path

from .views import ContactFormView

app_name = "contact_form"
urlpatterns = [
    path("", ContactFormView.as_view(), name="contact_form"),
]
