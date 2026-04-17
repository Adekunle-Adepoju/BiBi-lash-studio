from django.shortcuts import render, redirect
from .forms import BookingForm
from .emails import send_confirmation_to_client, send_alert_to_studio
import logging
logger = logging.getLogger(__name__)
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            try:
                send_confirmation_to_client(booking)
                send_alert_to_studio(booking)
            except Exception as e:
                logger.error(f"Email failed for booking {booking.pk}: {e}")
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})
def booking_success(request):
    return render(request, 'bookings/booking_success.html')
