from django.db import models
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

# A Question has a question and a publication date. 
# A Choice has two fields: the text of the choice and a vote tally.
# Each Choice is associated with a Question.

# 3 steps to make models change:
# Change your models (in models.py).
# Run [python manage.py makemigrations] to create migrations for those changes
# Run [python manage.py migrate] to apply those changes to the database.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return timezone.now() - datetime.timedelta(days=1) <= self.pub_date 
    was_published_recently.admin_oder_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice_text


