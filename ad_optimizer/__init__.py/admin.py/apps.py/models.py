from django.db import models
class Ad(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    clicks = models.IntegerField()
    conversions = models.IntegerField()
    def __str__(self):
        return self.name
