from django.db import models
from datetime import datetime

from ckeditor.fields import RichTextField

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
    
    
    title_2 = models.CharField(max_length=300, blank=True)
    header_image_1 = models.ImageField(blank=True, upload_to='image/')
    created_at_1 = models.DateTimeField(default=datetime.now, blank=True)
    title_3 = models.CharField(max_length=300, blank=True)
    header_image_2 = models.ImageField(blank=True, upload_to='image/')
    created_at_2 = models.DateTimeField(default=datetime.now, blank=True)
    
    
    
    
   
    
    
    
    
class sales_pg(models.Model):
    title = models.CharField(max_length=300, blank=True)
    
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
    title_2 = models.CharField(max_length=300, blank=True)
    header_image_1 = models.ImageField(blank=True, upload_to='image/')
    created_at_1 = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    
    title_3 = models.CharField(max_length=300, blank=True)
    header_image_2 = models.ImageField(blank=True, upload_to='image/')
    created_at_2 = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    
    
    class Meta:
        ordering = ['-created_at']
    
    
    
class aff_mkt_pg(models.Model):
    title = models.CharField(max_length=300, blank=True)
    
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
    title_2 = models.CharField(max_length=300, blank=True)
    header_image_1 = models.ImageField(blank=True, upload_to='image/')
    created_at_1 = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    
    title_3 = models.CharField(max_length=300, blank=True)
    
    header_image_2 = models.ImageField(blank=True, upload_to='image/')
    created_at_2 = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    
    
    class Meta:
        ordering = ['-created_at']
    
    
class human_psy(models.Model):
    title = models.CharField(max_length=300, blank=True)
    
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
    title_2 = models.CharField(max_length=300, blank=True)
    header_image_1 = models.ImageField(blank=True, upload_to='image/')
    created_at_1 = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    
    title_3 = models.CharField(max_length=300, blank=True)
    header_image_2 = models.ImageField(blank=True, upload_to='image/')
    created_at_2 = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    
    
    class Meta:
        ordering = ['-created_at']
    
    
class sp1(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    

class sp2(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
class sp3(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')

class amp1(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
class amp2(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
class amp3(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
class hmp1(models.Model): 
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
class hmp2(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')
    
class hmp3(models.Model):
    title = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    writer = models.CharField(max_length=300, blank=True)
    header_image = models.ImageField(blank=True, upload_to='image/')

    
