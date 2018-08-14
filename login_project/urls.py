
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bazar/', include('bazar.urls')),
    path('registration/', include('registration.urls')),
    path('meal/', include('meal.urls')),
]
