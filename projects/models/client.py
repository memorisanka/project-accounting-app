from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=240)
    address = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=240)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
