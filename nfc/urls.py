from django.urls import path
from nfc import views


app_name = 'nfc'

urlpatterns = [
    path('scan/list/', views.scan_list, name='scan_list'),
    path('scan/<str:tag_id>/', views.register_scan, name='register_scan'),
    path('view/<int:tag_id>/', views.view_tag, name='view_tag'),
    path('not_scanned_tags/<int:kunden_id>/', views.not_scanned_tags, name='not_scanned_tags'),
    path('alltags/', views.view_all_tag, name='view_all_tag'),

]
