from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Study(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200,help_text='eg. Robotics study')
    text = models.TextField(help_text='eg. Our study goes on till the 30th. Visit http://doodle.com for more information')
    last_date=models. DateField (default=datetime.now()+timedelta(days=30))
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title