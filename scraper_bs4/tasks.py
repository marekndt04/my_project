from __future__ import absolute_import, unicode_literals
import os

from celery import shared_task

import scraper_bs4.scrape_functions as scraper


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
import django

django.setup()

from .models import BudmiexInfo


@shared_task()
def store_budmiex_info():
    budimex_info = scraper.scrape_budim()

    for url, img_src, title in budimex_info:
        new_investment = BudmiexInfo()
        new_investment.invest_name = title
        new_investment.invest_img_src = img_src
        new_investment.invest_url = url
        new_investment.save()