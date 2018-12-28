from django.db import models


class Thief(models.Model):
    thief_name = models.CharField(max_length=50)
    name_1 = models.CharField(max_length=50)
    name_2 = models.CharField(max_length=50)
    mass_1 = models.IntegerField()
    mass_2 = models.IntegerField()
    prize_1 = models.IntegerField()
    prize_2 = models.IntegerField()
    car_load = models.IntegerField()

    class Meta:
        db_table = 'thief'

    def __str__(self):
        return self.thief_name
