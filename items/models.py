from django.db import models
from django.contrib.auth import get_user_model

from .choices import COLOR_CHOICES, SIZE_CHOICES


class Item(models.Model):

    name = models.CharField(max_length=128,
                            verbose_name='Item name',
                            help_text='Enter item name')
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                verbose_name='Item price',
                                help_text='Enter item price')
    size = models.CharField(max_length=5,
                            verbose_name='Item size',
                            choices=SIZE_CHOICES,
                            help_text='Select the size',
                            default='N/A')
    color = models.CharField(max_length=20,
                             verbose_name='Item color',
                             choices=COLOR_CHOICES,
                             help_text='Select the color',
                             default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(),
                                   on_delete=models.SET_NULL,
                                   null=True)

    def __str__(self):
        return self.name
