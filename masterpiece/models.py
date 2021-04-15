from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subject)

    @property
    def speak(self):
        return f'{self.body}'


