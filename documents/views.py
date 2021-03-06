from django.db.models import F
from dnollkse.viewHelper import render
from documents.models import Document


# Create your views here.
def index(request):
    """
    Retrieves all documents and renders them on the index view.
    """
    documents = Document.objects.all().order_by(
        F('ordering').asc(nulls_last=True))
    if len(documents) > 0:
        return render(request, "documents/index.dtl",
                      {'first_item': documents[0], 'items': documents[1:]})
    else:
        return render(request, "documents/index.dtl", {'items': None})
