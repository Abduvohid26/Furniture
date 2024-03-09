from django.urls import path
from .views import RegisterView, LoginApiView, UsersView, UsersDetailView
urlpatterns = [
    path('', UsersView.as_view()),
    path('<uuid:id>/', UsersDetailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginApiView.as_view()),
]