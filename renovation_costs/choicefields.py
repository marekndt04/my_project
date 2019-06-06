from renovation_costs.models import Product

paints = Product.objects.filter(product_category_id=1).values_list('id', 'name')
bases = Product.objects.filter(product_category_id=2).values_list('id', 'name')
wallpaper = Product.objects.filter(product_category_id=3).values_list('id', 'name')
wallpaper_glue = Product.objects.filter(product_category_id=4).values_list('id', 'name')
