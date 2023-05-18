from django.shortcuts import render, redirect
from .models import Book, Author, Publisher
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'mi_app/book_list.html', context)

def add_book(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    
    if request.method == 'POST':
        form = BookForm(request.POST)
    
        if form.is_valid():
            book = form.save()
            return redirect('book_list')
    
    return render(request, 'mi_app/add_book.html', {
        'authors': authors,
        'publishers': publishers,
        })

