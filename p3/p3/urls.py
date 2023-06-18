from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("",include("a3.urls")),
    path("",include("accounts.urls")),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()