from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=30, default='')
    price= models.FloatField()
    description = models.TextField(default='')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category_id': self.category_id
        }

class Category2(models.Model):
    name = models.CharField(max_length=30, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Author(models.Model):
    name = models.CharField(max_length=30, default='')
    category2_id = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='authors')
    books = models.TextField(default='')


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': self.books,
            'category2_id': self.category2_id
        }