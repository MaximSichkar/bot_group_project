import uuid

from django.db import models
from .user import User


class PromptVariable(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    prompt = models.CharField(max_length=100, default="1girl", null=False, blank=False) #Промпт пользователя
    batch_size = models.BigIntegerField(default=1)  #Колличество картинок
    width = models.BigIntegerField(default=480)    #Параметр размерности картинки (Ширина)
    height = models.BigIntegerField(default=800)  #Параметр размерности картинки (Висота)

    enable_hr = models.BooleanField(default=True)  #Включение и отключение хайресфикса

#    hr_upscaler = models.CharField(max_length=100)    #Апскелер
    hr_checkpoint_name = models.CharField(default='level4XL.safetensors', max_length=100)   #Модель нейронки


