from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    lk = BookSerializer