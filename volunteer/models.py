from django.db import models
from django.utils import timezone

# Create your models here.
class Volunteer(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    created_date = models.DateTimeField(blank=True, null=True)

    def signup(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Committees(models.Model):
    name = models.CharField(max_length=200)
    slots_available = models.IntegerField()
    slots_taken = models.IntegerField()