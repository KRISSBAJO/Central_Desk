from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoListCreate(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterUserSerializer

@api_view(['POST'])
def register_user(request):
    serializer = RegisterUserSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)  # Important: hash the password
        user.save()
        data['response'] = "successfully registered a new user."
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics

class TodoUpdateDestroy(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics

from django.shortcuts import get_object_or_404

class UserProfile(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_object(self):
        """Override the default method to get object based on related User's username"""
        username = self.kwargs.get('username')
        return get_object_or_404(Profile, user__username=username)


