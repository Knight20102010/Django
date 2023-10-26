from django.urls import path
from quality import views

urlpatterns = [
     path('',views.aboutUs),
     path('aboutUs/', views.aboutUs)
]
