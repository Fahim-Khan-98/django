
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('contact/', include('contact.urls')),
    path('authentication/', include('authentication.urls')),
    path('', include('index.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)