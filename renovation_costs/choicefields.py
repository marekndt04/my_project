from renovation_costs.models import Product

paints = Product.objects.filter(product_category_id=1).values_list('id', 'name')
bases = Product.objects.filter(product_category_id=2).values_list('id', 'name')
wallpaper = Product.objects.filter(product_category_id=3).values_list('id', 'name')
wallpaper_glue = Product.objects.filter(product_category_id=4).values_list('id', 'name')
wall_tiles = Product.objects.filter(product_category__name='płytki ścienne').values_list('id', 'name')
floor_tiles = Product.objects.filter(product_category__name='płytki podłogowe').values_list('id', 'name')
fugue = Product.objects.filter(product_category__name='fuga').values_list('id', 'name')
silicone = Product.objects.filter(product_category__name='silikon').values_list('id', 'name')
plaster = Product.objects.filter(product_category__name='gładź szpachlowa').values_list('id', 'name')
plaster_base = Product.objects.filter(product_category__name='grunt do gładzi').values_list('id', 'name')
layers_of_plaster = (
    (1, 'Jednokrotne szpachlowanie'),
    (2, 'Dwukrotne szpachlowanie'),
    (3, 'Trzykrotne szpachlowanie'),
)

