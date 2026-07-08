from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer, RegisterSerializer

# ViewSet for Book CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Anyone can view, only authenticated users can modify
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Setup for searching, filtering, and ordering
    filterset_fields = ['author']
    search_fields = ['title']
    ordering_fields = ['price']

# View for User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer