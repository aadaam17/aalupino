from django.db import models

# Create your models here.

class Product(models.Model):
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
    tag = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=50)
    previous_price = models.CharField(max_length=50)
    color = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    PRODUCT_STATUS = (
        ('j', 'Just In'),
        ('o', 'Out of Stock'),
    )

    status = models.CharField(
        max_length=1,
        choices=PRODUCT_STATUS,
        blank=True,
        default='a',
        help_text='Product availability',
    )

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
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