from django.db import models
from django.utils import timezone

# Create your models here.
class Committee(models.Model):
    committee_id = models.IntegerField(unique=True, null=True)
    name = models.CharField(max_length=200)
    slots_available = models.IntegerField()
    slots_taken = models.IntegerField()

    def __unicode__(self):
        return u'%s %s' % (self.committee_id, self.name)

class Volunteer(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contactno = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    created_date = models.DateTimeField(blank=True, null=True)
    committee_id = models.ForeignKey('Committee', to_field='committee_id', null=True, blank=True)

    def signup(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class CommitteeChair(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    committee_id = models.ForeignKey('Committee', to_field='committee_id', null=True, blank=True)