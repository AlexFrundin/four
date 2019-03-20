from django.db import models

class Author(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    second_name = models.CharField(verbose_name='Фамилия', max_length=20)
    owner = models.ManyToManyField('Book', related_name='owner_book',  blank=True)
    def __str__(self):
        return f"{self.first_name} {self.second_name}"
    def author_all(self):
        return self.objects.select_related('book_author')

class Genre(models.Model):
    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
    copy = models.CharField(verbose_name="Издательство", max_length=30)
    def __str__(self):
        return self.copy

class Book(models.Model):
    g = ((1,'Комедия'),(2,'Фэнтези'),(3,'Фантастика'),
        (4,'Приключение'),(5,'Детектив'),(6,'Драма'),(7,'Публицистика'),)

    title = models.CharField(verbose_name='Название', max_length=40)
    author = models.ManyToManyField('Author',verbose_name='Автор', related_name='book_author')
    genre = models.SmallIntegerField(choices=g,verbose_name="Жанр")
    copy = models.ForeignKey('Genre', related_name='copy_book', on_delete=models.DO_NOTHING)
    price = models.DecimalField(verbose_name='Стоимость', decimal_places=2, max_digits=10)
    length = models.SmallIntegerField(verbose_name='Объем')
