from django.db import models


# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to='static/blog_images/')
    para1 = models.TextField()
    img2 = models.ImageField(upload_to='static/blog_images/', null=True, blank=True)
    para2 = models.TextField(blank=True, null=True)
    img3 = models.ImageField(upload_to='static/blog_images/', null=True, blank=True)
    para3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} / {self.title}"
    
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.id} / {self.name} / {self.phone}"