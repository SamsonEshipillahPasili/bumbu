from django.db import models

# Create your models here.
class ContactUsInfo(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=300)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)