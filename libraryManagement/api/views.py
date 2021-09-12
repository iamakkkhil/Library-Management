from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from book.models import Book
from api import serializers


@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book(request, id):
    books = Book.objects.get(id=id)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)
