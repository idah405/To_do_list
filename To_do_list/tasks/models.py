from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)


    #status = models.BooleanField(default=False)
    def __str__(self):
        return self.name 
        

    