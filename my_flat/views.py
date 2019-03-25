from django.shortcuts import render
from django.views import View
from scraper_bs4.scrape_functions import scrape


class MainPage(View):

    def get(self, request):
        scrape()
        ctx = {
            "content": scrape()
        }
        return render(request, 'index.html', ctx)
