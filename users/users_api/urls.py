from django.urls import path
from .views import SignUpView, SignInView, UserListView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('users/', UserListView.as_view(), name='user-list'),
]
