from wizard_builder.models import QuestionPage

from django.contrib.sites.models import Site
from django.test import TestCase
from django.conf import settings


class TempSiteID():
    '''
        with TempSiteID(1):
            ...
    '''
    def __init__(self, site_id):
        self.site_id_temp = site_id

    def __enter__(self):
        self.site_id_stable = getattr(settings, 'SITE_ID', 1)
        settings.SITE_ID = self.site_id_temp

    def __exit__(self, *args):
        settings.SITE_ID = self.site_id_stable


class SitePageTest(TestCase):

    def test_created_question_page_comes_with_a_site(self):
        page = QuestionPage.objects.create()
        self.assertEqual(page.site.domain, 'example.com')

    def test_on_site_increments_for_default_site(self):
        count_before = QuestionPage.objects.on_site().count()
        QuestionPage.objects.create()
        count_after = QuestionPage.objects.on_site().count()
        self.assertEqual(count_before + 1, count_after)

    def test_on_site_does_not_increment_for_alternate_site(self):
        count_before = QuestionPage.objects.on_site().count()
        page = QuestionPage.objects.create()
        page.site = Site.objects.create()
        page.save()
        count_after = QuestionPage.objects.on_site().count()
        self.assertEqual(count_before, count_after)

    def test_question_page_responds_to_site_id_changes(self):
        site_1_pages = 3
        site_2_pages = site_1_pages + 1
        site_2 = Site.objects.create()
        for i in range(site_1_pages):
            QuestionPage.objects.create()
        for i in range(site_2_pages):
            QuestionPage.objects.create(site=site_2)

        self.assertEqual(QuestionPage.objects.on_site().count(), site_1_pages)
        with TempSiteID(site_2.id):
            self.assertEqual(QuestionPage.objects.on_site().count(), site_2_pages)