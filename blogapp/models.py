from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=20, blank='TRUE')
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return '%s by %s' % (self.title, self.name)

    def summary(self):
        return self.body[:100]
    
    def time(self):
        return self.pub_date.strftime("%Y.%m.%d")

