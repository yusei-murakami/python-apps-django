from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodEntryForm, MeasurementForm
# from .models import FoodEntry, Entry, Food, Profile
from django.http import JsonResponse

from tracker.forms import MeasurementForm
from tracker.models import Measurement, Profile, FoodEntry, Entry, Food

def get_profile():
    profile, _ = Profile.objects.get_or_create(pk=1)
    return profile

def index(request):
    # toggle view mode
    view = request.GET.get('view','card')
    measurements = Measurement.objects.order_by('-date')
    return render(request,'tracker/index.html',{'measurements':measurements,'view':view})


def add_measurement(request):
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            # ① 日付から Entry を取得 or 作成
            entry_date = form.cleaned_data["date"]
            entry, created = Entry.objects.get_or_create(date=entry_date)

            # ② Measurement を保存（Entry に紐付け、Measurement.date も同期）
            measurement = form.save(commit=False)
            measurement.entry = entry
            measurement.date = entry.date  # ★ここ重要（これでunique衝突を防ぐ）
            measurement.save()

            # ③ 食品入力の処理
            idx = 1
            while True:
                name = request.POST.get(f"food_name_{idx}")
                qty = request.POST.get(f"food_qty_{idx}")
                cal = request.POST.get(f"food_cal_{idx}")

                if not name:
                    break

                try:
                    qty = float(qty)
                    cal = float(cal)
                except:
                    idx += 1
                    continue

                food, _ = Food.objects.get_or_create(
                    name=name,
                    defaults={"kcal_per_100g": cal}
                )

                if food.kcal_per_100g != cal:
                    food.kcal_per_100g = cal
                    food.save()

                FoodEntry.objects.create(
                    entry=entry,
                    measurement=measurement,
                    food=food,
                    amount=qty
                )

                idx += 1

            return redirect("tracker_home")

    else:
        form = MeasurementForm()

    return render(request, "tracker/add.html", {"form": form})


def view_measurement(request, pk):
    measurement = Measurement.objects.get(pk=pk)
    food_entries = FoodEntry.objects.filter(measurement=measurement)

    return render(request, 'tracker/view_measurement.html', {
        'measurement': measurement,
        'food_entries': food_entries
    })


def api_calendar(request):
    measurements = Measurement.objects.all()

    data = []
    for m in measurements:
        data.append({
            "id": m.id,
            "date": m.entry.date.strftime("%Y-%m-%d"),
            "total_calories": m.total_calories,
        })

    return JsonResponse(data, safe=False)


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
    