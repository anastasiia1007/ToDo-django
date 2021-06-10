from django.db import models
from django.utils import timezone  # мы будем получать дату создания todo
from django.db import models

class stroka(models.Model):
    title = models.CharField('Название', max_length =50)#charfield только до 250 символов
    description = models.TextField('Описание', max_length =1000) # TextField может включать несколько тысяч символов.
    priority = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


