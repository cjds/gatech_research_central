from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Study(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    last_date=models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(
            default=datetime.now()+timedelta(days=30))
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title