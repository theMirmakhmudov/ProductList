from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.i18n import set_language
from .settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('i18n', set_language, name="set_language")
]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)
