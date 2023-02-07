from django.db import models
import datetime
import uuid
# from member.models import User
stockstatus = (
    ('available','available'),
    ('Not available','Not available')
)

class products(models.Model):
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    product_name = models.CharField(max_length=150)
    product_price = models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    product_description = models.CharField(max_length=500)
    stock = models.CharField(max_length=25,choices = stockstatus,default='available')
    created_date = models.DateField(default=datetime.date.today)
    product_image = models.ImageField(upload_to ='media/images')
    product_weight = models.IntegerField()

# class Deposit(models.Model):
#     name = models.ForeignKey(User,on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=10,blank=True,null=True)
#     member_id = models.CharField(max_length=100,blank=True,null=True)
#     purpose = models.CharField(max_length = 1000)
#     amount = models.IntegerField(blank=False,null=False)
#     date = models.DateField(default=datetime.date.today)

#     # def get_name(self):
#     #     user_name = User.objects.get(username = self.name).member_id
#     #     return user_name


    def __str__(self):
        return f"{self.product_id}"
