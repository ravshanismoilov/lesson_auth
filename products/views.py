from django.shortcuts import render
from django.views import View
from .models import Books


class ListView(View):
    def get(self, request):
        book = Books.objects.all().order_by('-created_at')
        return render(request, 'book/book_list.html', {'book': book})
