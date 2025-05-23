from django.db import models


# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
