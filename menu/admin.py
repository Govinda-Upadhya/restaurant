from django.contrib import admin
from .models import FoodItem, orderDetail,GrandOrder
# Register your models here.

class orderDetailAdmin(admin.ModelAdmin):
    list_display = ('fooditem', 'quantity', 'total_price','grandorder_id')
    def grandorder_id(self, obj):
        grandorder_ids = obj.grandorder_set.values_list('id', flat=True)
        return grandorder_ids[0] if grandorder_ids else None
    grandorder_id.short_description = 'GrandOrder ID'

class GrandOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'grand_total','phone_number', 'item_name','item_quantity') 

    def item_name(self, obj):
        return ",".join([str(order.fooditem) for order in obj.orders.all()])
    def item_quantity(self,obj):
        return ",".join([str(order.quantity) for order in obj.orders.all()])
admin.site.register(FoodItem)
admin.site.register(GrandOrder,GrandOrderAdmin)
admin.site.register(orderDetail,orderDetailAdmin)