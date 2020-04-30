from django.db import models


class ContactForm(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "contactform"
        verbose_name = "contact form message"
        verbose_name_plural = "contact form messages"

    def __str__(self):
        return self.email
