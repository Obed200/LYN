from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.get(id=1)
    except SiteSettings.DoesNotExist:
        settings = None
    
    return {'site_settings': settings}