from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CategoryBooks(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category_books'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(CategoryBooks, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/', default='media/default_img/default_book_img.jpg')
    page = models.IntegerField()
    book_lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f'{self.book.title} - {self.author.first_name} - {self.author.last_name}'


class Review(models.Model):
    comment = models.CharField(max_length=300)
    star_given = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given} - {self.book.title} - {self.user.username}'
