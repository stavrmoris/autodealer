from django.db import models

class Brand(models.Model):
    COUNTRIES = (
        ('JP', 'Япония'),
        ('CN', 'Китай'),
        ('KR', 'Корея'),
    )
    name = models.CharField(max_length=100, unique=True, verbose_name="Марка")
    origin = models.CharField(
        max_length=2,
        choices=COUNTRIES,
        verbose_name="Страна происхождения",
        null=True,  # Allow NULL values
        blank=True  # Allow empty values in forms
    )

    def __str__(self):
        return self.name

class Rating(models.Model):
    value = models.CharField(max_length=50, unique=True, verbose_name="Оценка")

    def __str__(self):
        return self.value

class BodyType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Тип кузова")

    def __str__(self):
        return self.name

class Drivetrain(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Привод")

    def __str__(self):
        return self.name


class Car(models.Model):
    IMPORT_COUNTRIES = (
        ('JP', 'Япония'),
        ('CN', 'Китай'),
        ('KR', 'Корея'),
    )

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Марка",
                              related_name="cars")
    auction_end_date = models.DateField(blank=True, null=True, verbose_name="Дата завершения аукциона")
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Тип кузова",
                                  related_name="cars")
    year = models.IntegerField(blank=True, null=True, verbose_name="Год")
    engine_cc = models.IntegerField(blank=True, null=True, verbose_name="Объем двигателя (cc)")
    transmission = models.CharField(max_length=100, blank=True, null=True, verbose_name="Трансмиссия")
    drivetrain = models.ForeignKey(Drivetrain, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Привод",
                                   related_name="cars")
    chassis_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер кузова")
    mileage = models.IntegerField(blank=True, null=True, verbose_name="Пробег")
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Оценка",
                               default=None)
    import_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Тип ввоза")
    final_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,
                                     verbose_name="Итоговая стоимость")
    auction_sheet = models.ImageField(upload_to='auction_sheets/', blank=True, null=True,
                                      verbose_name="Аукционный лист")

    # Новое поле для страны ввоза
    import_country = models.CharField(
        max_length=2,
        choices=IMPORT_COUNTRIES,
        verbose_name="Страна ввоза",
        default='JP'  # По умолчанию Япония
    )

    def __str__(self):
        return self.name if self.name else "Неизвестный автомобиль"


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images', verbose_name="Автомобиль")
    image = models.ImageField(upload_to='car_images/', verbose_name="Фото автомобиля")

    def __str__(self):
        return f"Фото для {self.car.name}" if self.car.name else "Фото автомобиля"
