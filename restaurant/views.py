from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FoodOrder
from datetime import datetime
import urllib.parse

@csrf_exempt
def log_food_order(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        phone = request.GET.get('phone_number')
        persons = request.GET.get('persons')
        booking_date = request.GET.get('booking_date')
        booking_time = urllib.parse.unquote(request.GET.get('booking_time'))  # Fix here
        order = request.GET.get('order')

        if not all([name, phone, persons, booking_date, booking_time, order]):
            return JsonResponse({'status': 'error', 'message': 'Missing parameters'}, status=400)

        sno = FoodOrder.objects.count() + 1
        order_no = f"FOOD{1000 + sno}"

        new_order = FoodOrder.objects.create(
            order_no=order_no,
            name=name,
            phone_number=phone,
            persons=int(persons),
            booking_date=booking_date,
            booking_time=booking_time,
            order=order
        )

        return JsonResponse({'status': 'success', 'order_no': new_order.order_no})

    return JsonResponse({'status': 'error', 'message': 'Only GET allowed'}, status=405)


def view_food_orders(request):
    orders = FoodOrder.objects.all().order_by('-timestamp')
    return render(request, 'restaurant_orders.html', {'orders': orders})


def clear_food_orders(request):
    FoodOrder.objects.all().delete()
    return JsonResponse({'status': 'success', 'message': 'All food orders cleared'})
