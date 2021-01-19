from django.urls import path

from user import views

urlpatterns = [
    path("users/", views.UserAPIView.as_view()),
    path("computers/", views.ComputerAPIView.as_view()),
]
