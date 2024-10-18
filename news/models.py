from django.db import models
from .validators import validate_title_news, validate_date_format


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    role = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, null=False, validators=[validate_title_news])
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='news')
    created_at = models.DateField(validators=[validate_date_format])
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField('Category', related_name='news', null=False)


    def __str__(self):
        return self.title