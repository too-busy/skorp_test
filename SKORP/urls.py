from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import views module from your project's root directory
from arbeitsplanung import views as arbeitsplanung_views

app_name = 'skorp'  # Add a namespace for your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('arbeitsplanung/', include(('arbeitsplanung.urls', 'arbeitsplanung'), namespace='arbeitsplanung')),
    path('zeiterfassung/', include(('zeiterfassung.urls', 'zeiterfassung'), namespace='zeiterfassung')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
