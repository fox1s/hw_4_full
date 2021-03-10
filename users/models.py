from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


# Create your models here.

class UserModel(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    name = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,20}$', 'not valid name')])
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(150)])
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, default='m', blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
