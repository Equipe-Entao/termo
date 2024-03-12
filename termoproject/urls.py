from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('termoapp:home'))),
    path('admin/', admin.site.urls),
    path('termo/', include('termoapp.urls'))
]
