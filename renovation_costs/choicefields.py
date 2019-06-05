from renovation_costs.models import Paint, Bases

paints = Paint.objects.values_list('id', 'name')
bases = Bases.objects.values_list('id', 'name')
