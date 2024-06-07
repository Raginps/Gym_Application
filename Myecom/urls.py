
from django.contrib import admin
from django.urls import path,include
from home import urls
import home.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(home.urls)),
    path("product/",include("product.urls"))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
