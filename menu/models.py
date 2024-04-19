from typing import Iterable
from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to="menu")
    type=models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} "
class orderDetail(models.Model):
    fooditem=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField(default=0)

    def save(self,*args, **kwargs) :
        self.total_price=int(self.quantity)*int(self.fooditem.price)
        print(self.total_price)
        super(orderDetail, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.quantity} {self.fooditem.name}"
class GrandOrder(models.Model):
    orders = models.ManyToManyField(orderDetail,blank=True)
    grand_total = models.IntegerField(default=0)
    table_number = models.IntegerField()
    phone_number = models.CharField(max_length=15)

    # def save(self, *args, **kwargs):
    #     if self.orders is not None:
    #         self.grand_total = sum(order.total_price for order in self.orders.all())
    #         print(self.grand_total)
    #         super(GrandOrder, self).save(*args, **kwargs)
    #     else:
    #         super(GrandOrder, self).save(*args, **kwargs)


    def __str__(self):
        return f"Orderid {self.id}, Total: ${self.grand_total}"