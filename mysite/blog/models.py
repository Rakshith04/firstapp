from django.utils import timezone
from django.db import models

class Post(models.Model):

    author = models.ForeignKey('auth.user')
    tittle = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.tittle
