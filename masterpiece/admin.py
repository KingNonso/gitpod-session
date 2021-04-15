from django.contrib import admin

from masterpiece import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'created', 'updated')


