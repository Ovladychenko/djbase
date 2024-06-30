from django.db import models

# Create your models here.
from django.urls import reverse


class Notes(models.Model):
    title = models.CharField(max_length=255)
    date_change = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_note', kwargs={'note_id': self.pk})

    class Meta:
        ordering = ['id']

class Currencies(models.Model):
    code = models.CharField(max_length=3, db_index=True, primary_key=True)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExchangeRates(models.Model):
    currencie = models.ForeignKey('Currencies', on_delete=models.PROTECT)
    date = models.DateField()
    value = models.DecimalField('value', null=False,max_digits=10, decimal_places=5,default=0)
    multiplicity = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['-date'])
        ]
