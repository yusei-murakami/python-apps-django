from django.db import models


class Category(models.Model):
    """
    支出・収入で共通して使うカテゴリ
    例: 食費, 交通費, 給料, ボーナス など
    """
    name = models.CharField("カテゴリ名", max_length=100, unique=True)
    is_income = models.BooleanField("収入カテゴリか？", default=False)

    def __str__(self):
        return self.name


class Expense(models.Model):
    """
    支出データ
    """
    date = models.DateField("日付")
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    amount = models.IntegerField("金額")
    memo = models.CharField("メモ", max_length=200, blank=True)

    def __str__(self):
        return f"[支出] {self.date} {self.category} {self.amount}円"


class Income(models.Model):
    """
    収入データ
    """
    date = models.DateField("日付")
    category = models.ForeignKey(
        Category,
        verbose_name="カテゴリ",
        on_delete=models.CASCADE,
        limit_choices_to={"is_income": True},
    )
    amount = models.IntegerField("金額")
    memo = models.CharField("メモ", max_length=200, blank=True)

    def __str__(self):
        return f"[収入] {self.date} {self.category} {self.amount}円"
