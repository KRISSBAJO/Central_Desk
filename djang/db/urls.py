from django.urls import path
from .views import ToDoListCreate, TodoUpdateDestroy, UserProfile, register_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('todos/', ToDoListCreate.as_view(), name='todo-list-create'),
    path('register/', register_user, name='register'),
    path('login/', obtain_auth_token, name='api_token_auth'),  # <-- login endpoint
    path('todos/<int:pk>/', TodoUpdateDestroy.as_view(),
         name='todo-update-destroy'),
    # urls.py
    path('profile/<str:username>/', UserProfile.as_view(), name='user-profile')

]
