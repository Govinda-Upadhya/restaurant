from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    menu_items=FoodItem.objects.all()

    return render(request,"menu/home.html",{
        "foods":menu_items
    })
def order(request):
    if request.method=="POST":
        order_quantity=request.POST.getlist('num1')
        items=request.POST.getlist('food_name')
        table_number=request.POST.get('tableno')
        
        phoneno=request.POST.get('phoneno')
    
        grand_order=GrandOrder.objects.create(table_number=table_number,phone_number=phoneno)
        
        for i in range(len(order_quantity)):
            food=items[i]
            
            if int(order_quantity[i])>0:
                fooditem=FoodItem.objects.get(name=food)
                
                quantity=order_quantity[i]
            
                order_details=orderDetail(fooditem=fooditem,quantity=quantity)
                order_details.save()
                grand_order.orders.add(order_details)
        
        grandprice=0
        for order in grand_order.orders.all():
            grandprice+=order.total_price
        print(grandprice)
        grand_order.grand_total=grandprice
        grand_order.save()
        
        
        
        return render(request,"menu/order.html",{
            "grandorders":grand_order
        })
    menu_items=FoodItem.objects.all()

    return render(request,"menu/home.html",{
        "foods":menu_items
    })