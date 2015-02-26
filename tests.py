import datetime

from django.test import TestCase
from django.utils import timezone
from django.test.client import Client
from django.core.urlresolvers import reverse

from surveydog.models import Survey

class SurveyMethodTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        """
        should return False when pub_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Survey(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        should return true when date is in recent
        """
        time = timezone.now() - datetime.timedelta(days=1)
        recent_question = Survey(pub_date=time)
        print('recent qu time: ', time)
        self.assertEqual(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        should return False when date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Survey(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def setUp(self):
        self.client = Client()

    def test_view_index(self):
        resp = self.client.get('/surveydog/')
        self.assertEqual(resp.status_code, 200)

  