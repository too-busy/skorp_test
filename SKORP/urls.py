from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from allauth.account.views import LoginView
from zeiterfassung import views as zeiterfassung_views

app_name = 'skorp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('arbeitsplanung/', include(('arbeitsplanung.urls', 'arbeitsplanung'), namespace='arbeitsplanung')),
    path('zeiterfassung/', include(('zeiterfassung.urls', 'zeiterfassung'), namespace='zeiterfassung')),
    path('nfc/', include(('nfc.urls', 'nfc'), namespace='nfc')),  # Hinzufügen dieser Zeile
    path('accounts/login/', LoginView.as_view(template_name='login.html', success_url='/zeiterfassung'), name='account_login'),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
