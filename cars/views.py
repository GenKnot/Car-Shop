from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from cars.models import Car


def cars(request):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 6)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    year_fields = Car.objects.values_list('year', flat=True).distinct()
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    body_fields = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'cars': paged_cars,
        'years': year_fields,
        'models': model_fields,
        'citys': city_fields,
        'bodys': body_fields
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    context = {
        'car': car
    }
    return render(request, 'cars/car-detail.html', context)


def search(request):
    all_cars = Car.objects.order_by('-created_date')

    year_fields = Car.objects.values_list('year', flat=True).distinct()
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    body_fields = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_fields = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_cars = all_cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            all_cars = all_cars.filter(model__iexact=model)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            all_cars = all_cars.filter(year__iexact=year)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            all_cars = all_cars.filter(city__iexact=city)

    if 'types' in request.GET:
        types = request.GET['types']
        if types:
            all_cars = all_cars.filter(body_style__iexact=types)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            all_cars = all_cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': all_cars,
        'years': year_fields,
        'models': model_fields,
        'citys': city_fields,
        'bodys': body_fields,
        'transmissions': transmission_fields
    }
    return render(request, 'cars/search.html', context)
