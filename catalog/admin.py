from django.contrib import admin
from .models import Car, CarImage, Brand, Rating, BodyType, Drivetrain

# Inline модель для добавления нескольких изображений
class CarImageInline(admin.TabularInline):  # Можно использовать StackedInline, если нужно отображение одно под другим
    model = CarImage
    extra = 1  # Количество пустых форм, которые будут отображаться по умолчанию
    fields = ('image',)  # Показываем только поле изображения

# Основная модель автомобиля
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'body_type', 'import_country', 'drivetrain', 'rating', 'final_cost', 'auction_end_date')
    search_fields = ('name', 'brand__name', 'year')
    list_filter = ('import_country', 'brand', 'body_type', 'drivetrain', 'rating', 'year', 'auction_end_date')
    inlines = [CarImageInline]  # Добавляем Inline для изображений

admin.site.register(Car, CarAdmin)  # Регистрируем модель Car в админке

# Модель для изображений (CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image')
    search_fields = ('car__name',)

admin.site.register(CarImage, CarImageAdmin)

# Регистрация новых моделей
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    search_fields = ["value"]

@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Drivetrain)
class DrivetrainAdmin(admin.ModelAdmin):
    search_fields = ["name"]
