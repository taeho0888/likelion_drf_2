from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('create-user/', UserCreateView.as_view()),
    path('update-user/<str:name>/', UserUpdateView.as_view()),
    path('delete-user/<str:name>/', UserDeleteView.as_view()),
    path('user/<str:name>/', UserRetreiveView.as_view()),
]