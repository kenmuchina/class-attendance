from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index),

    # Login page
    path('login/', views.login),

    # attendees page
    path('attendees/', views.attendees),

]
