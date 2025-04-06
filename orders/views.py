from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import BikeOrder
import urllib.parse

@csrf_exempt
def clear_orders(request):
    if request.method == 'GET':
        BikeOrder.objects.all().delete()
        return JsonResponse({'status': 'success', 'message': 'All orders cleared'})
    return JsonResponse({'status': 'error', 'message': 'Only GET allowed'}, status=405)

@csrf_exempt
def log_order(request):
    if request.method == 'GET':
        model_no = request.GET.get('model_no')
        bike_name = urllib.parse.unquote(request.GET.get('bike_name'))
        price = request.GET.get('price')
        qty = request.GET.get('qty')

        if not all([model_no, bike_name, price, qty]):
            return JsonResponse({'status': 'error', 'message': 'Missing parameters'}, status=400)

        sno = BikeOrder.objects.count() + 1
        order_no = f"ORD{1000 + sno}"

        order = BikeOrder.objects.create(
            order_no=order_no,
            model_no=model_no,
            bike_name=bike_name,
            price=float(price),
            qty=int(qty)
        )

        data = {
            'sno': order.sno,
            'order_no': order.order_no,
            'model_no': order.model_no,
            'bike_name': order.bike_name,
            'price': order.price,
            'qty': order.qty
        }

        return JsonResponse({'status': 'success', 'data': data})

    return JsonResponse({'status': 'error', 'message': 'Only GET allowed'}, status=405)

def show_orders(request):
    orders = BikeOrder.objects.all().order_by('-timestamp')  # Newest first
    return render(request, 'orders_table.html', {'orders': orders})
