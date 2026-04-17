from django.core.mail import send_mail
from django.conf import settings


def send_confirmation_to_client(booking):
    send_mail(
        subject="We have received your booking - BiBi Lash Studio",
        message=f"Hi {booking.first_name},\n\nThanks! We received your booking and will confirm within 24 hours.\n\n  Service: {booking.get_service_display()}\n  Date:    {booking.preferred_date.strftime('%A, %d %B %Y')}\n\nQuestions? Call 0814 1979 801.\n\nWith love,\nBiBi Lash Studio",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[booking.email],
        fail_silently=False,
    )

    
def send_alert_to_studio(booking):
    send_mail(
        subject=f"New booking: {booking.full_name} - {booking.get_service_display()}",
        message=f"New booking received.\n\n  Name:    {booking.full_name}\n  Email:   {booking.email}\n  Phone:   {booking.phone or 'Not provided'}\n  Service: {booking.get_service_display()}\n  Date:    {booking.preferred_date.strftime('%A, %d %B %Y')}\n  Notes:   {booking.notes or 'None'}\n\nAdmin: http://localhost:8000/admin/bookings/booking/{booking.pk}/change/",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.STUDIO_EMAIL],
        fail_silently=False,
    )
