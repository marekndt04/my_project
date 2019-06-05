from renovation_costs.models import Paint, Base, Wallpaper, WallpaperGlue

paints = Paint.objects.values_list('id', 'name')
bases = Base.objects.values_list('id', 'name')
wallpaper = Wallpaper.objects.values_list('id', 'name')
wallpaper_glue = WallpaperGlue.objects.values_list('id', 'name')
