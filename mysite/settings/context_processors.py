from settings.models import Sidebar

def sidebar(request):
    return {
        "sidebars": Sidebar.objects.all()
    }
