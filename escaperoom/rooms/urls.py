from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('room/<int:room_number>/', views.room, name='room'),
    path('room/<int:room_number>/download/<str:file_name>/', views.download_file, name='download_file'),
    path('restart/', views.clear_session, name='restart'),
        path('emergency/', views.emergency, name='emergency'),
]
