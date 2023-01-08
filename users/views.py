from .permissions import IsAccountOwner
from .serializers import UserSerializer
from .models import User  
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
