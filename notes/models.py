from django.db import models

# Create your models here.
class note(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=500)


    def __str__(self):
        return self.title