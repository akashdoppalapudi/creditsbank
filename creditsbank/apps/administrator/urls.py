from django.urls import path

from . import views

app_name = 'administrator'
urlpatterns = [
    path('update', views.update, name='update'),
    path('update-submission', views.update_submission, name='update-submission'),
]