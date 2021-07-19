from django.db import models

# Create your models here.

#model for data shown in blogpage
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    cover = models.ImageField(upload_to='images/')
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title #take the title as heading in admin login

#model created for customers who can connect with us
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
