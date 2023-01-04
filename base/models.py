from django.db import models
from django.template.defaultfilters import slugify

import uuid, string, random

# Create your models here.

class Product(models.Model):
    id = models.CharField(max_length=200, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    sm_image_x1 = models.ImageField(null=True, blank=True)
    sm_image1 = models.ImageField(null=True, blank=True)
    sm_image_x2 = models.ImageField(null=True, blank=True)
    sm_image2 = models.ImageField(null=True, blank=True)
    sm_image_x3 = models.ImageField(null=True, blank=True)
    sm_image3 = models.ImageField(null=True, blank=True)
    sm_image_x4 = models.ImageField(null=True, blank=True)
    sm_image4 = models.ImageField(null=True, blank=True)
    sm_image_x5 = models.ImageField(null=True, blank=True)
    sm_image5 = models.ImageField(null=True, blank=True)
    sm_image_x6 = models.ImageField(null=True, blank=True)
    sm_image6 = models.ImageField(null=True, blank=True)
    sm_image_x7 = models.ImageField(null=True, blank=True)
    sm_image7 = models.ImageField(null=True, blank=True)
    tag_slug = models.SlugField(blank=True)
    category = models.CharField(max_length=200)
    cat_slug = models.SlugField(blank=True)
    description = models.TextField(null=True, blank=True)
    pro_slug = models.SlugField(blank=True)
    price = models.CharField(max_length=50)
    previous_price = models.CharField(max_length=50)
    color = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    PRODUCT_TAG = (
        ('m', 'Men'),
        ('w', 'Women'),
        ('k', 'Kids'),
    )

    tag = models.CharField(
        max_length=1,
        choices=PRODUCT_TAG,
        blank=True,
        default='m',
        help_text='Product tags',
    )

    PRODUCT_STATUS = (
        ('j', 'Just In'),
        ('o', 'Out of Stock'),
    )

    status = models.CharField(
        max_length=1,
        choices=PRODUCT_STATUS,
        blank=True,
        default='a',
        help_text='Product status',
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    #override the save method to have slug automatically generated
    def save(self, *args, **kwargs):
        if not self.id:
            newid = (uuid.uuid4().hex)[:9]
            if not type(self).objects.filter(id=newid).exists():
                self.id = newid
        if not self.cat_slug:
            self.cat_slug = slugify(self.category)
        if not self.tag_slug:
            self.tag_slug = slugify(self.tag)
        if not self.pro_slug:
            self.pro_slug = slugify(self.description+ ' ' +self.id)

        return super().save(*args, **kwargs)

    


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    banner = models.ImageField(null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    timeTaken = models.CharField(max_length=50, null=False, blank=False)
    parag1 = models.TextField(null=False, blank=False)
    parag2 = models.TextField(null=True, blank=True)
    parag3 = models.TextField(null=True, blank=True)
    parag4 = models.TextField(null=True, blank=True)
    qoute = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    author_image = models.ImageField(null=True, blank=True)
    author_details = models.TextField(null=True, blank=True)
    author_instagram = models.CharField(max_length=50, null=True, blank=True)
    author_facebook = models.CharField(max_length=50, null=True, blank=True)
    author_twitter = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)