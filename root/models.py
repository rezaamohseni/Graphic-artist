from django.db import models

class SpecialService(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    descriptions = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Business_Card_Portfolios(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    descriptions = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class Portfolios_children(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='root' , default='default.jpg')
    descriptions = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name