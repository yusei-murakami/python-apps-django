from django.db import models

class Todo(models.Model):
    title = models.CharField('タスク名', max_length=200)
    description = models.TextField('詳細', blank=True, null=True)
    due_date = models.DateField('期限日', blank=True, null=True)
    is_completed = models.BooleanField('完了', default=False)
    created_at = models.DateTimeField('登録日', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # デフォルトソート（新しい順）

    def __str__(self):
        return self.title
