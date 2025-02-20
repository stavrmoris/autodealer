from django.db import models

class Feedback(models.Model):
    phone_number = models.CharField(max_length=25, verbose_name="Номер телефона")
    user_name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    message = models.TextField(blank=True, null=True, verbose_name="Текст обращения")
    contact_method = models.CharField(
        max_length=20,
        choices=[
            ('call', 'Перезвонить'),
            ('whatsapp', 'Написать в WhatsApp'),
            ('tg', 'Написать в Telegram'),
        ],
        verbose_name="Способ обращения"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.user_name} ({self.phone_number})"

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"