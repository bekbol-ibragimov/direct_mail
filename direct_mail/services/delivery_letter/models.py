from django.db import models

# Create your models here.
class DeliveryType(models.Model):
    name = models.CharField(max_length=32)
    price = models.ImageField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Letter(models.Model):
    file = models.FileField(null=True, blank=True)
    delivery_type = models.ForeignKey(DeliveryType, default=1)
