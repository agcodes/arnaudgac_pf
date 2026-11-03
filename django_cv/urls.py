from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cv.views import home, portfolio, health_check, handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('portfolio/', portfolio, name='portfolio'),
    path('healthz/', health_check, name='health_check'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Handler pour les erreurs 404
handler404 = handler404
