from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from termoproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('termoapp:home'))),
    path('admin/', admin.site.urls),
    path('termo/', include('termoapp.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)