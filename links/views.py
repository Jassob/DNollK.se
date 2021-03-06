from django.db.models import F
from dnollkse.viewHelper import render
from links.models import Link


# Create your views here.
def index(request):
    """
    Retrieves all links and renders them on the index view.
    """
    links = Link.objects.all().order_by(F('order').asc(nulls_last=True))
    if len(links):
        return render(request, "links/index.dtl",
                      {'first_item': links[0], 'items': links[1:]})
    else:
        return render(request, "links/index.dtl", {'items': None})
