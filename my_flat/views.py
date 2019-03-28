from django.shortcuts import render
from django.views import View
from scraper_bs4.scrape_functions import scrape_budim, scrape_dd, scrape_victoria


class MainPage(View):

    def get(self, request):
        return render(request, 'my_flat/main_page.html')


# Think about how to split this three functions into one.
class DevInvestmentBud(View):

    def get(self, request):
        scrape_budim()
        ctx = {
            "ctx": scrape_budim()
        }
        return render(request, 'my_flat/dev_investment.html', ctx)


class DevInvestmentDD(View):

    def get(self, request):
        scrape_dd()
        ctx = {
            "ctx": scrape_dd()
        }
        return render(request, 'my_flat/dd_invest.html', ctx)


class DevInvestmentVictoria(View):

    def get(self, request):
        scrape_victoria()
        ctx = {
            "ctx": scrape_victoria()
        }
        return render(request, 'my_flat/victoria_invest.html', ctx)
