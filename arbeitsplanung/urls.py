from django.urls import path
from . import views

app_name = 'arbeitsplanung'

urlpatterns = [
    # ...
    path('einsatzplan/', views.einsatzplan_view, name='einsatzplan'),
    path('entries/', views.arbeitsplan_entries, name='arbeitsplan_entries'),
    path('entries/<int:entry_id>/details/', views.arbeitsplan_entry_details, name='arbeitsplan_entry_details'),
]
