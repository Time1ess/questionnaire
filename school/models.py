from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from const.models import School

# Create your models here.

class SchoolAdmin(models.Model):
    user = models.OneToOneField(User)
    school_belong = models.ForeignField(School)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u"校级管理员"
        verbose_name_plural = u"校级管理员"
    def __unicode__(self):
        return "%s" % self.name
