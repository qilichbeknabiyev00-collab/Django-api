from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('api/', include('api.urls')),
]
