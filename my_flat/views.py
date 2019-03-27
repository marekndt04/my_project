from django.shortcuts import render
from django.views import View
from scraper_bs4.scrape_functions import scrape_budim, scrape_dd


class MainPage(View):

    def get(self, request):
        return render(request, 'main_page.html')


class DevInvestmentBud(View):

    def get(self, request):
        scrape_budim()
        ctx = {
            "content": scrape_budim()
        }
        return render(request, 'dev_investment.html', ctx)


class DevInvestmentDD(View):

    def get(self, request):
        scrape_dd()
        ctx = {
            "content": scrape_dd()
        }
        return render(request, 'dev_investment.html', ctx)
