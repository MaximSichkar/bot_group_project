import uuid

from django.db import models
from django.utils import timezone

class User(models.Model):
   user_id = models.BigIntegerField(primary_key=True)
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100, null=True)
   user_name = models.CharField(max_length=100, null=True)

   created_at = models.DateTimeField(default=timezone.now)
   is_admin = models.BooleanField(default=False)
