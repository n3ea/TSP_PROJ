
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_zori.urls')),
    path('book/', include('book.urls')),
    path('lk/', include('django.contrib.auth.urls')),
    path('lk/', include('lk.urls')),
    # path('', include('image.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
