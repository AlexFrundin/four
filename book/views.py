from django.shortcuts import render, Http404
from .models import Author, Book, Genre
from django.db.models.aggregates import Count
from django.db.models import F, Subquery,Q, OuterRef
# Subquery(u.filter(author__id__exact='author__id')
def book_gt(request):
    u = Book.objects.filter(author=OuterRef('id'))
    a = Author.objects.select_related('book_author')\
    .annotate(count_books=Count('book_author'),books=Subquery(u.values_list('id')[:2]))\
    .values('first_name', 'second_name',
            'id','count_books',
            'books',)
    raise Http404(a)

def book_detail(request):
    return render(request,'shop.html',{})
