from django.shortcuts import render
from django.views import View

from renovation_costs.forms import PaintingCostForm, DoorWindowSizeCalc


class RenovationCategoriesView(View):
    def get(self, request):
        return render(request, 'renovation_costs/renovation_cost_main.html')


class PaintingCostView(View):
    def get(self, request):
        form = PaintingCostForm()
        form_calc = DoorWindowSizeCalc()
        ctx = {
            'form': form,
            'form_door_window_calc': form_calc
        }
        return render(request, 'renovation_costs/painting_cost_view.html', ctx)
