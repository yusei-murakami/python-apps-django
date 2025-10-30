# work10/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Todo(models.Model):
    STATUS_CHOICES = (
        ('open', '未完了'),
        ('done', '完了'),
    )

    title = models.CharField('タスク名', max_length=200)
    description = models.TextField('詳細', blank=True)
    created_by = models.ForeignKey(User, verbose_name='作成者', on_delete=models.CASCADE, related_name='todos')
    status = models.CharField('完了状態', max_length=10, choices=STATUS_CHOICES, default='open')
    due_date = models.DateField('期限日', null=True, blank=True)
    created_at = models.DateTimeField('登録日', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work10:todo_list')
