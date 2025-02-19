from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

from feedback.forms import FeedbackForm
from news.models import News
from .models import Car, Brand, Rating
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Car

def japanese_main(request):
     html = 'catalog/japanese_main.html'
     return page(request, html)

def chinese_main(request):
    html = 'catalog/chinese_main.html'
    return page(request, html)

def korean_main(request):
    html = 'catalog/korean_main.html'
    return page(request, html)

def japanese_catalog(request):
    return catalog(request, 'catalog/japanese_catalog.html', 'JP')

def chinese_catalog(request):
    return catalog(request, 'catalog/chinese_catalog.html', 'CN')

def korean_catalog(request):
    return catalog(request, 'catalog/korean_catalog.html', 'KR')

def f1(request):
    return filter(request, 'catalog/cars/jp.html', 'JP')

def f2(request):
    return filter(request, 'catalog/cars/ch.html', 'CN')

def f3(request):
    return filter(request, 'catalog/cars/kr.html', 'KR')

def main_page(request):
    html = 'catalog/index.html'
    return page(request, html)

def page(request, html):
    form = FeedbackForm()
    news = News.objects.all().order_by('-date')
    cars = Car.objects.prefetch_related('images').all()
    years = Car.objects.values_list('year', flat=True).distinct().order_by('-year')
    costs = Car.objects.values_list('final_cost', flat=True).distinct().order_by('final_cost')
    engine_volumes = Car.objects.values_list('engine_cc', flat=True).distinct().order_by('engine_cc')
    brands = Brand.objects.all()
    ratings = Rating.objects.all()

    return render(request, html, {
        'form': form,
        'cars': cars,
        'brands': brands,
        'ratings': ratings,
        'years': years,
        'costs': costs,
        'engine_volumes': engine_volumes,
        'news': news,
    })


def filter(request, html, code):
    cars = Car.objects.prefetch_related('images').filter(import_country=code)

    # Фильтрация
    form = FeedbackForm()
    brand_id = request.GET.get('brand')
    model = request.GET.get('model')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    cost_min = request.GET.get('cost_min')
    cost_max = request.GET.get('cost_max')
    engine_min = request.GET.get('engine_min')
    engine_max = request.GET.get('engine_max')
    rating = request.GET.get('rating')

    if brand_id and brand_id.isdigit():
        cars = cars.filter(brand_id=brand_id)
    if model:
        cars = cars.filter(name__icontains=model)
    if year_min:
        cars = cars.filter(year__gte=year_min)
    if year_max:
        cars = cars.filter(year__lte=year_max)
    if cost_min:
        cars = cars.filter(final_cost__gte=cost_min)
    if cost_max:
        cars = cars.filter(final_cost__lte=cost_max)
    if engine_min:
        cars = cars.filter(engine_cc__gte=engine_min)
    if engine_max:
        cars = cars.filter(engine_cc__lte=engine_max)
    if rating:
        cars = cars.filter(rating__value=rating)

    # Рендеринг частичного шаблона
    html = render_to_string(html, {'cars': cars, 'form': form})
    return JsonResponse({'html': html})


def filter_cars(request):
    cars = Car.objects.prefetch_related('images').all()

    # Фильтрация
    brand_id = request.GET.get('brand')
    model = request.GET.get('model')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    cost_min = request.GET.get('cost_min')
    cost_max = request.GET.get('cost_max')
    engine_min = request.GET.get('engine_min')
    engine_max = request.GET.get('engine_max')
    rating = request.GET.get('rating')

    if brand_id and brand_id.isdigit():
        cars = cars.filter(brand_id=brand_id)
    if model:
        cars = cars.filter(name__icontains=model)
    if year_min:
        cars = cars.filter(year__gte=year_min)
    if year_max:
        cars = cars.filter(year__lte=year_max)
    if cost_min:
        cars = cars.filter(final_cost__gte=cost_min)
    if cost_max:
        cars = cars.filter(final_cost__lte=cost_max)
    if engine_min:
        cars = cars.filter(engine_cc__gte=engine_min)
    if engine_max:
        cars = cars.filter(engine_cc__lte=engine_max)
    if rating:
        cars = cars.filter(rating__value=rating)

    # Рендеринг частичного шаблона
    html = render_to_string('catalog/car_list_partial.html', {'cars': cars})
    return JsonResponse({'html': html})


def car_list(request):
    cars = Car.objects.prefetch_related('images').filter(import_country='jp')

    # Фильтрация
    brand_id = request.GET.get('brand')
    model = request.GET.get('model')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    cost_min = request.GET.get('cost_min')
    cost_max = request.GET.get('cost_max')
    engine_min = request.GET.get('engine_min')
    engine_max = request.GET.get('engine_max')
    rating = request.GET.get('rating')

    if brand_id and brand_id.isdigit():
        cars = cars.filter(brand_id=brand_id)
    if model:
        cars = cars.filter(name__icontains=model)
    if year_min:
        cars = cars.filter(year__gte=year_min)
    if year_max:
        cars = cars.filter(year__lte=year_max)
    if cost_min:
        cars = cars.filter(final_cost__gte=cost_min)
    if cost_max:
        cars = cars.filter(final_cost__lte=cost_max)
    if engine_min:
        cars = cars.filter(engine_cc__gte=engine_min)
    if engine_max:
        cars = cars.filter(engine_cc__lte=engine_max)
    if rating:
        cars = cars.filter(rating__value=rating)

    # Уникальные значения для фильтров
    years = Car.objects.values_list('year', flat=True).distinct().order_by('-year')
    costs = Car.objects.values_list('final_cost', flat=True).distinct().order_by('final_cost')
    engine_volumes = Car.objects.values_list('engine_cc', flat=True).distinct().order_by('engine_cc')

    brands = Brand.objects.all()
    ratings = Rating.objects.all()

    return render(request, 'catalog/car_list.html', {
        'cars': cars,
        'brands': brands,
        'ratings': ratings,
        'years': years,
        'costs': costs,
        'engine_volumes': engine_volumes,
    })

def catalog(request, html, code):
    cars = Car.objects.prefetch_related('images').filter(import_country=code)

    # Фильтрация
    form = FeedbackForm()
    brand_id = request.GET.get('brand')
    model = request.GET.get('model')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    cost_min = request.GET.get('cost_min')
    cost_max = request.GET.get('cost_max')
    engine_min = request.GET.get('engine_min')
    engine_max = request.GET.get('engine_max')
    rating = request.GET.get('rating')

    if brand_id and brand_id.isdigit():
        cars = cars.filter(brand_id=brand_id)
    if model:
        cars = cars.filter(name__icontains=model)
    if year_min:
        cars = cars.filter(year__gte=year_min)
    if year_max:
        cars = cars.filter(year__lte=year_max)
    if cost_min:
        cars = cars.filter(final_cost__gte=cost_min)
    if cost_max:
        cars = cars.filter(final_cost__lte=cost_max)
    if engine_min:
        cars = cars.filter(engine_cc__gte=engine_min)
    if engine_max:
        cars = cars.filter(engine_cc__lte=engine_max)
    if rating:
        cars = cars.filter(rating__value=rating)

    # Уникальные значения для фильтров
    years = Car.objects.values_list('year', flat=True).distinct().order_by('-year')
    costs = Car.objects.values_list('final_cost', flat=True).distinct().order_by('final_cost')
    engine_volumes = Car.objects.values_list('engine_cc', flat=True).distinct().order_by('engine_cc')

    brands = Brand.objects.all()
    ratings = Rating.objects.all()

    return render(request, html, {
        'form': form,
        'cars': cars,
        'brands': brands,
        'ratings': ratings,
        'years': years,
        'costs': costs,
        'engine_volumes': engine_volumes,
    })

def get_models(request):
    brand_id = request.GET.get('brand_id')
    if brand_id and brand_id.isdigit():
        # Получаем уникальные названия моделей для выбранного бренда
        models = Car.objects.filter(brand_id=brand_id).values_list('name', flat=True).distinct()
        print(f"Models for brand {brand_id}: {list(models)}")  # Отладочная информация
        return JsonResponse({'models': list(models)})
    return JsonResponse({'models': []})

def company(request):
    form = FeedbackForm()
    return render(request, 'catalog/company.html', {'form': form,})

def car_detail(request, car_id):
    form = FeedbackForm()
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'catalog/car_detail.html', {'car': car, 'form': form,})
