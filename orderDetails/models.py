from django.db import models
import datetime
from orders.models import order
from products.models import products
class Orderdetail(models.Model):
    order_id = models.ForeignKey(order,to_field='order_id',on_delete=models.CASCADE)
    product_id = models.ForeignKey(products,to_field='product_id',on_delete=models.CASCADE)
    price =  models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    quantity = models.IntegerField()


    # purpose = models.CharField(max_length = 1000)
    # amount = models.IntegerField(blank=False,null=False)
    # date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.product_id)
