"""
URL configuration for smallingo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import SmallingoVideoListView, SmallingoVideoCreateView, SmallingoVideoDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', SmallingoVideoListView.as_view(), name='video-list'),
    path('videos/latest/', SmallingoVideoDetailView.as_view(), name='video-list'),
    path('videos/<int:pk>/', SmallingoVideoDetailView.as_view(), name='video-list'),
    path('videos/create/', SmallingoVideoCreateView.as_view(), name='create-video'),
]

urlpatterns += static(settings.MEDIA_URL + settings.VIDEO_DIR + '/', document_root=settings.MEDIA_ROOT + settings.VIDEO_DIR)
urlpatterns += static(settings.MEDIA_URL + settings.AUDIO_DIR + '/', document_root=settings.MEDIA_ROOT + settings.AUDIO_DIR)
urlpatterns += static(settings.MEDIA_URL + settings.AUDIO_TRANSLATION_DIR + '/', document_root=settings.MEDIA_ROOT + settings.AUDIO_TRANSLATION_DIR)
urlpatterns += static(settings.MEDIA_URL + settings.THUMBNAIL_DIR + '/', document_root=settings.MEDIA_ROOT + settings.THUMBNAIL_DIR)
