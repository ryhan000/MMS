from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from meal.forms import MealForm
from bazar.models import Bazar

from  .models import Meal


# Create your views here.
def func():
    total_bazar = Bazar.objects.all().aggregate(Sum('amount'))['amount__sum']
    total_meal = Meal.objects.all().aggregate(Sum('meal_number'))['meal_number__sum']
    meal_rate = total_bazar / total_meal

    return {
        'total_bazar': total_bazar,
        'total_meal': total_meal,
        'meal_rate': meal_rate,

    }



def index (request):
    meal_list = Meal.objects.all()
    meal_info = func()


    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            try:
                form.save()

                return redirect('/meal')

            except:
                pass
    else:
        form = MealForm()

    return render(request, 'meal/index.html', {'form': form, 'meal_list': meal_list,
     'total_bazar': meal_info['total_bazar'], 'total_meal': meal_info['total_meal'], 'meal_rate': meal_info['meal_rate']})


def show_indi(request, name):

   meal_info = func()

   meal_details_list = Meal.objects.filter(name=name)
   total_bazar = Bazar.objects.filter(name=name).aggregate(Sum('amount'))['amount__sum']

   total_meal = meal_details_list.aggregate(Sum('meal_number'))['meal_number__sum'] 
   total_meal_amount =  total_meal*meal_info['meal_rate']

   return render(request, 'meal/show_indi.html', {'meal_details_list': meal_details_list,
    'total_meal': total_meal, 'meal_rate': meal_info['meal_rate'],
    'total_meal_amount':total_meal_amount, 'total_bazar':total_bazar })