from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rekomendasi/', include('rekomendasi.urls')),
    path('', include('rekomendasi.urls')),  # Arahkan '/' ke rekomendasi
]
