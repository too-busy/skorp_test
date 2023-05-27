from django.urls import path
from . import views

app_name = 'zeiterfassung'

urlpatterns = [
    path('', views.zeiterfassung, name='zeiterfassung'),
    path('list/', views.zeiterfassung_list, name='zeiterfassung_list'),
]
