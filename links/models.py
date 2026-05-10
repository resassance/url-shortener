from django.db import models
from django.contrib.auth.models import User
import string
import secrets

class Link(models.Model):
    original_url = models.URLField(max_length=2048, verbose_name="Оригинальная ссылка")
    short_code = models.CharField(max_length=10, unique=True, db_index=True, verbose_name="Короткий код")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    clicks_count = models.PositiveIntegerField(default=0, verbose_name="Количество переходов")

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(secrets.choice(chars) for _ in range(6))
            if not Link.objects.filter(short_code=code).exists():
                return code

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"