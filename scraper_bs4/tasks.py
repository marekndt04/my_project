from __future__ import absolute_import, unicode_literals
import os

from celery import shared_task

import scraper_bs4.scrape_functions

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
# import django
#
# django.setup()


@shared_task()
def simple_function(x, y):
    return x * y
