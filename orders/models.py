from django.db import models
import datetime
from customer.models import User
import uuid

orderStatus = (
    ('Pending','Pending'),
    ('Completed','Completed'),
    ('Cancelled','Cancelled'),
    ('Refunded','Refunded'),
    ('Shipped','Shipped'),
    ('Awaiting Payment','Awaiting Payment'),
    ('Awaiting Fulfillment','Awaiting Fulfillment'),
    ('Awaiting Shipment','Awaiting Shipment')


)

class order(models.Model):
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    order_address = models.CharField(max_length = 400)
    order_email = models.EmailField()
    order_date = models.DateField(default=datetime.date.today)
    order_status = models.CharField(max_length = 25,choices= orderStatus,default='Pending')

    # total_deposit =  models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    # total_Transaction = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    # total_Remaining = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    # date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.order_id}"

