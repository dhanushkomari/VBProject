from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # path('voice/',),
    # path('voice/', ),
    # path('voice/', ),

    path('voice/all', views.all, name = 'all-voices'),
    path('voice/post-voice', views.postVoice, name = 'post-voice'),
    path('voice/upload', views.FileView.as_view(), name='file-upload'),

    path('version/latest', views.recent, name = 'latest-version'),
    path('version/<str:ver_name>', views.ByVerName, name = 'by-ver-name'),

    path('flat-version/latest', views.recent_flat, name = 'recent-flat'),
    path('flat-version/by-name/<str:ver_name>', views.ByFlatVerName, name = 'by-flat-name'),

    path('show-voices/', views.VoiceDownload, name = 'voice-download'),
]