from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('accounts.urls')),
    path('', views.HomeView.as_view()),
    path('chat/', views.ChatView.as_view()),
]
