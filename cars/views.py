from django.shortcuts import render, redirect, reverse
from . import models
from .forms import ReviewForm


def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'cars/list.html', context=context)


def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('Primary key not found!!')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')


def rental_review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))

    else:
        form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'cars/rental_review.html', context)


def thank_you(request):
    return render(request, 'cars/thank_you.html')
