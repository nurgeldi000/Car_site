from category import Category
from django.db import models



class Marka(models.Model):
    marka_name = models.CharField(max_length=100)

    def __str__(self):
        return self.marka_name


class CarModel(models.Model):
    car_model = models.CharField(max_length=100)
    car_marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    COLOR_CHOICES = [
        ('black', 'Черный'),
        ('white', 'Белый'),
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('green', 'Зеленый'),
        ('gray', 'Серый'),
    ]
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')

    def __str__(self):
        return f"{self.car_model} ({self.car_marka.marka_name})"


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    category = models.ForeignKey(Marka, related_name='product', on_delete=models.CASCADE)
    region = models.CharField(max_length=50, verbose_name="Регион")
    description = models.TextField()
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    gearbox = models.CharField(max_length=50, verbose_name="Коробка")
    engine_power = models.CharField(max_length=100, verbose_name="Двигатель")
    mileage = models.PositiveIntegerField(verbose_name="Пробег (км)")
    ENGINE_TYPE_CHOICES = [
        ('electric', 'Электро'),

    ]
    engine_type = models.CharField(max_length=50, choices=ENGINE_TYPE_CHOICES, verbose_name="Тип двигателя")
    status = models.CharField(max_length=10, choices=[('new', 'New'), ('used', 'Used')])

    def __str__(self):
        return self.car_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class CarPhotos(models.Model):
    car_image = models.ImageField(upload_to='car_photos/')
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)


class Rating(models.Model):
    car = models.ForeignKey(Car,  related_name='ratings', on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг")

    def __str__(self):
        return f"{self.car} - {self.car_model} - {self.stars} stars"


