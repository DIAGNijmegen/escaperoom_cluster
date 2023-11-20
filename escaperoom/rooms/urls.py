from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('room/<int:room_number>/', views.room, name='room'),
    path('restart/', views.clear_session, name='restart'),
        path('emergency/', views.emergency, name='emergency'),
]
