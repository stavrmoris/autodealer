from django.db import models
from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    image = models.ImageField(upload_to='news_images/', verbose_name="Фото", blank=True, null=True)
    text = RichTextField(verbose_name="Текст")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"