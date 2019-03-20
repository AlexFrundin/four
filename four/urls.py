from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core_app.urls')),
    path('', RedirectView.as_view(url='shop/')),
    path('shop/', include('shop.urls')),
    path('user/', include('profiles.urls')),
    path('load/', include('load.urls')),
    path('add_js/', include('addjs.urls')),
    path('book/', include('book.urls')),
    path('drf/', include('drf.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
