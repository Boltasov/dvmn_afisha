from django.urls import path

from places import views

urlpatterns = [
    path('', views.show_afisha),
    path('places/<int:id>/', views.get_places),
]