from django.shortcuts import render
from django.views import View


class RenovationCategoriesView(View):
    def get(self, request):
        return render(request, 'renovation_costs/renovation_cost_main.html')


class PaintingCostView(View):
    def get(self, request):
        return render(request, 'renovation_costs/painting_cost_view.html')

