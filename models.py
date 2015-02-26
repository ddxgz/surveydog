import datetime

from django.db import models
from django.utils import timezone


class Survey(models.Model):
    survey_head = models.CharField(max_length=100)
    survey_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    # num_question = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.survey_head
        # return u'%s %s' % (self.survey_head, self.survey_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class SingleChoiceQuestion(models.Model):
    survey = models.ForeignKey(Survey)
    question_text = models.CharField(max_length=200)
    # seq = models.PositiveSmallIntegerField(required=False)

    def __str__(self):
        return self.question_text


class MultiChoiceQuestion(models.Model):
    survey = models.ForeignKey(Survey)
    question_text = models.CharField(max_length=200)
    # seq = models.PositiveSmallIntegerField(required=False)

    def __str__(self):
        return self.question_text


class FreeQuestion(models.Model):
    survey = models.ForeignKey(Survey)
    question_text = models.CharField(max_length=200)
    answer_text = models.TextField(max_length=400)
    # seq = models.PositiveSmallIntegerField(required=False)

    def __str__(self):
        return self.question_text


class SingleChoice(models.Model):
    question = models.ForeignKey(SingleChoiceQuestion)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


class MultiChoice(models.Model):
    question = models.ForeignKey(MultiChoiceQuestion)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
