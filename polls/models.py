from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    publication_date = models.DateTimeField('published date')
    def __str__(self):
        return self.question_text

    def was_publish_recentaly(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now

    was_publish_recentaly.admin_order_field = 'publication_date'
    was_publish_recentaly.boolean = True
    was_publish_recentaly.short_description = 'Published Recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text