from django.shortcuts import render
from .models import Order
from datetime import datetime, timedelta

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        items = request.POST.getlist('items')  # Handles multiple checkboxes
        payment = request.POST.get('payment')

        # 🕒 Estimate pickup time (current time + 15 minutes)
        now = datetime.now()
        pickup_time = (now + timedelta(minutes=15)).strftime('%H:%M')

        # 💾 Save order to database
        Order.objects.create(
            name=name,
            phone=phone,
            items=", ".join(items),
            payment_method=payment,
            pickup_time=pickup_time
        )

        # ✅ Render thank you page
        return render(request, 'thankyou.html', {
            'name': name,
            'pickup_time': pickup_time
        })

    # 🏠 If GET request, show home page
    return render(request, 'home.html')
