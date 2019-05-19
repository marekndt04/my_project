from __future__ import absolute_import, unicode_literals
import os

from celery import shared_task

import scraper_bs4.scrape_functions as scraper

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
import django

django.setup()

from .models import BudimexInfo


@shared_task()
def store_budmiex_info():
    budimex_info = scraper.scrape_budim()

    for url, img_src, title in budimex_info:
        try:
            test_obj = BudimexInfo.objects.get(invest_name=title)
            print(title)

        except BudimexInfo.DoesNotExist:
            new_investment = BudimexInfo()
            new_investment.invest_name = title
            new_investment.invest_img_src = img_src
            new_investment.invest_url = url
            new_investment.save()
