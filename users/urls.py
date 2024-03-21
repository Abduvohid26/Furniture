from django.urls import path
from .views import SignUpView, LoginApiView, UsersView, UsersDetailView, LogoutView
urlpatterns = [
    path('', UsersView.as_view()),
    path('<uuid:id>/', UsersDetailView.as_view()),
    path('register/', SignUpView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/<uuid:id>/', LogoutView.as_view()),
]