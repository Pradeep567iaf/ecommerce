from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


gender_choices = (
    ('male','male'),
    ('female','female')
)
class User(AbstractUser):
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length = 25,choices= gender_choices,default='male')
    billing_address = models.CharField(max_length = 400)
    customer_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.username