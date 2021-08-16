from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from books.models import Book, Review
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from books.form import ReviewForm
# Create your views here.

class BookListView(ListView):    
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):   
    model=Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews']=context['book'].review_set.all().order_by('-created_at')
        context['authors']=context['book'].authors.all()
        context['form']=ReviewForm()
        return context


def author(request, author):
    books=Book.objects.filter(authors__name=author)
    context={'book_list':books}
    return render(request, 'books/book_list.html', context)


def review(request,id):
    if request.user.is_authenticated:
        newreview = Review(book_id=id, user=request.user)
        form = ReviewForm(request.POST, request.FILES, instance=newreview)
        if form.is_valid:
            form.save()
        else:
            print("Form is not valid")
        """body = request.POST['body']
        newreview=Review(body=body, book_id=id, user=request.user)    
        
        if len(request.FILES)!= 0:
            images=request.FILES['images']
            fs=FileSystemStorage()
            name = fs.save(images.name,images)            
            newreview.images=fs.url(name)
        newreview.save()"""
        
    return redirect(f"/books/{id}")


    