from django.db import models
from django.forms import ModelForm

# -----------------------------
# 1. Food モデル
# -----------------------------
class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kcal_per_100g = models.FloatField(help_text='kcal per 100g')

    def __str__(self):
        return f"{self.name} ({self.kcal_per_100g} kcal/100g)"


# -----------------------------
# 2. Entry（1日分の健康記録）
# -----------------------------
class Entry(models.Model):
    date = models.DateField()

    temperature = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    bp_sys = models.IntegerField("Systolic BP", null=True, blank=True)
    bp_dia = models.IntegerField("Diastolic BP", null=True, blank=True)

    sleep_hours = models.FloatField(null=True, blank=True)

    calorie_in = models.FloatField("摂取カロリー", null=True, blank=True)
    calorie_burned = models.IntegerField(null=True, blank=True)
    steps = models.IntegerField(null=True, blank=True)

    def bmi(self, height_m=1.7):
        if self.weight:
            try:
                return round(self.weight / (height_m ** 2), 2)
            except Exception:
                return None
        return None

    def __str__(self):
        return f"Entry {self.date}"


# -----------------------------
# 3. FoodEntry（食事記録）
# -----------------------------
class FoodEntry(models.Model):
    measurement = models.ForeignKey(
        'Measurement',
        related_name='foods',
        on_delete=models.CASCADE,
        null=True,  # 既存行用に null を許可
        blank=True
    )
    name = models.CharField(
        max_length=100,
        default='不明'  # 既存行に入れるデフォルト値
    )
    calories_per_100g = models.FloatField(default=0)
    grams = models.FloatField(default=0)

    @property
    def total_calories(self):
        return (self.calories_per_100g * self.grams) / 100


# -----------------------------
# 4. Profile（身長）
# -----------------------------
class Profile(models.Model):
    height_cm = models.FloatField(default=170)

    def __str__(self):
        return f"Profile (height={self.height_cm})"


# -----------------------------
# 5. Measurement（個別測定）
#    ※ Entry を使うなら消して OK。残すならこのままでも動く。
# -----------------------------
class Measurement(models.Model):
    date = models.DateField()
    temperature = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    bp_sys = models.IntegerField("Systolic BP", null=True, blank=True)
    bp_dia = models.IntegerField("Diastolic BP", null=True, blank=True)
    sleep_hours = models.FloatField(null=True, blank=True)
    burned_calories = models.IntegerField(null=True, blank=True)
    steps = models.IntegerField(null=True, blank=True)
    intake_calories = models.IntegerField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Measurement {self.date}"


# -----------------------------
# 6. Measurement Form
# -----------------------------
class MeasurementForm(ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'date', 'temperature', 'weight',
            'bp_sys', 'bp_dia',
            'sleep_hours', 'burned_calories', 'steps'
        ]
