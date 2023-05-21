from django.urls import path

from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("homepage/", views.homepage, name="homepage"),
    path("homepage/<str:pk>/", views.thread, name="thread"),
    path("create-thread", views.createThread, name="create-thread"),
    path("update-thread/<str:pk>/", views.updateThread, name="update-thread"),
    path("delete-thread/<str:pk>/", views.deleteThread, name="delete-thread"),

]