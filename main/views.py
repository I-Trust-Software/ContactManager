from django.shortcuts import render
# serializers
from django.core.serializers import serialize

from .models import Supplier

def index(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers,
        'suppliers_raw': serialize('json', list(suppliers))
    }
    return render(request, 'index.html', context)