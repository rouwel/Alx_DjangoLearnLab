from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "This Library"

def is_admin(user):
    try:
        return user.userprofile.role == 'admin'
    except UserProfile.DoesNotExist:
        return False

def is_librarian(user):
    try:
        return user.userprofile.role == 'librarian'
    except UserProfile.DoesNotExist:
        return False

def is_member(user):
    try:
        return user.userprofile.role == 'member'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Add book view
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

# Edit book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# Delete book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
