from django.urls import path

from masterpiece import views

app_name = 'masterpiece'

urlpatterns = [
    path('', views.CreateContactView.as_view(), name='create_contact'),
]
