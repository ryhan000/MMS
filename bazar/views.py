from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Sum
from bazar.forms import BazarForm 

from .models import Bazar


def index(request):
    bazar_list = Bazar.objects.all()
    context = {
        'bazar_list': bazar_list,
        'total_bazar_amount': bazar_list.aggregate(Sum('amount'))['amount__sum']

    }

    return render(request, 'bazar/index.html', context)


def item(request, bazar_id):
    bazar = get_object_or_404(Bazar, pk=bazar_id)
    return render(request, 'bazar/item.html', {'bazar': bazar})


def bazar_indi(request, name):

    bazar_details_list = Bazar.objects.filter(name=name)
    total_bazar = bazar_details_list.aggregate(Sum('amount'))['amount__sum'] 
    return render(request, 'bazar/bazar_indi.html', {'bazar_details_list': bazar_details_list, 'total_bazar':total_bazar })


def bazar(request):
    
    if request.method == "POST":
        form = BazarForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                 
                return redirect('/bazar')
            except:
                pass
    else:
        form = BazarForm()

    

    return render(request,'bazar/index.html',{'form':form})