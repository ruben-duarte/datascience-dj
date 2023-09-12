from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=110)
    logo = models.ImageField(upload_to='customers', default='no-image.jpg')

    def __str__(self):
        return str(self.name)

