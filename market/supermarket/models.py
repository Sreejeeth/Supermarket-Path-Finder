from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
# Create your models here.
from django_resized import ResizedImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])




class Productdb(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = ResizedImageField(size=[300, 300], upload_to='products/%Y/%m/%d', blank=True)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.id, self.slug])

class About(models.Model):
    image = ResizedImageField(size=[300, 300], upload_to='products/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=200, db_index=True)
    description = models.CharField(max_length=2000, db_index=True)

    def __str__(self):
        return self.name