from django.urls import include, path

from . import views

urlpatterns = [
    path('update', views.update, name='update'),
    path('register', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
]
