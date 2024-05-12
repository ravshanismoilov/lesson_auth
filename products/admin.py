from django.contrib import admin
from .models import CategoryBooks, Language, Books, Author, BookAuthor, Review


admin.site.register(Author)
admin.site.register(CategoryBooks)
admin.site.register(Books)
admin.site.register(BookAuthor)
admin.site.register(Review)
admin.site.register(Language)