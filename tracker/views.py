from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodEntryForm, MeasurementForm
# from .models import FoodEntry, Entry, Food, Profile
from django.http import JsonResponse

from tracker.forms import MeasurementForm
from tracker.models import Measurement, Profile, FoodEntry

def get_profile():
    profile, _ = Profile.objects.get_or_create(pk=1)
    return profile

def index(request):
    # toggle view mode
    view = request.GET.get('view','card')
    measurements = Measurement.objects.order_by('-date')
    return render(request,'tracker/index.html',{'measurements':measurements,'view':view})

def add_measurement(request):
    profile = get_profile()
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            # calculate BMI if weight provided and profile.height_cm exists
            if m.weight:
                height_m = profile.height_cm / 100
                try:
                    m.bmi = float(m.weight) / (height_m * height_m)
                except Exception:
                    m.bmi = None
            m.save()
            # handle food entries sent as repeated POST fields
            idx = 1
            total_intake = 0
            while True:
                name = request.POST.get(f'food_name_{idx}')
                qty = request.POST.get(f'food_qty_{idx}')
                cal = request.POST.get(f'food_cal_{idx}')
                if not name:
                    break
                try:
                    qty_f = float(qty)
                except (TypeError, ValueError):
                    qty_f = 0
                try:
                    cal_f = float(cal)
                except (TypeError, ValueError):
                    cal_f = 0
                fe = FoodEntry(measurement=m, name=name, quantity=qty_f, calories_per_100g=cal_f)
                fe.save()
                total_intake += float(fe.total_calories or 0)
                idx += 1
            if total_intake:
                m.intake_calories = int(total_intake)
                m.save()
            return redirect('tracker:index')
    else:
        form = MeasurementForm()
    food_form = FoodEntryForm()
    return render(request,'tracker/add.html',{'form':form,'food_form':food_form,'profile':profile})

def view_measurement(request, pk):
    m = get_object_or_404(Measurement, pk=pk)
    foods = m.foods.all()
    return render(request,'tracker/view.html',{'m':m,'foods':foods})

def api_calendar(request):
    # return events for FullCalendar
    qs = Measurement.objects.all()
    events = []
    for m in qs:
        title = []
        if m.weight: title.append(f'W:{m.weight}kg')
        if m.temperature: title.append(f'T:{m.temperature}℃')
        if m.steps: title.append(f'S:{m.steps}歩')
        events.append({
            'title': ' '.join(title),
            'start': m.date.isoformat(),
            'url': f'/measurement/{m.pk}/'
        })
    return JsonResponse(events, safe=False)

def api_charts(request):
    # provide data for charts: weight, intake/burned, bmi
    qs = Measurement.objects.order_by('date')
    labels = [m.date.isoformat() for m in qs]
    weight = [float(m.weight) if m.weight is not None else None for m in qs]
    intake = [m.intake_calories for m in qs]
    burned = [m.burned_calories for m in qs]
    bmi = [float(m.bmi) if m.bmi is not None else None for m in qs]
    data = {
        'labels': labels,
        'weight': weight,
        'intake': intake,
        'burned': burned,
        'bmi': bmi,
    }
    return JsonResponse(data)
    