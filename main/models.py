from django.db import models

# Create your models here.
class Setting(models.Model):
    name = models.CharField(max_length=200)
    timeout = models.SmallIntegerField()
    interval = models.SmallIntegerField()
    def __unicode__(self):
        return self.name

class RecordType(models.Model):
    name = models.CharField(max_length=200)
    enabled = models.BooleanField()
    def __unicode__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=200)
    enabled = models.BooleanField()
    def __unicode__(self):
        return self.name

class ChangePoint(models.Model):
    domain = models.ForeignKey(Domain)
    record_type = models.ForeignKey(RecordType)
    time = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=200)
    def __unicode__(self):
        return str(self.time)+': '+str(self.value)
