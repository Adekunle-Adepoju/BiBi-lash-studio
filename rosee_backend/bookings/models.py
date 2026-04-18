from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail




class Booking(models.Model):
    PENDING = 'pending'; CONFIRMED = 'confirmed'; CANCELLED = 'cancelled'
    STATUS_CHOICES = [(PENDING,'Pending'),(CONFIRMED,'Confirmed'),(CANCELLED,'Cancelled')]
    SERVICE_CHOICES = [
        ('classic','Classic Set - N7000'),('hybrid','Hybrid Set - N10,000'),
        ('volume','Volume Set - N12,000'),('mega','Mega Volume - N15,000'),
        ('lift_tint','Lash Lift & Tint - N20,000'),('infill','Infill - from N25,000'),
        ('removal','Removal - N5000'),
    ]
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField()
    phone      = models.CharField(max_length=30, blank=True)
    service    = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    preferred_date = models.DateField()
    notes      = models.TextField(blank=True)
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_service_display()} on {self.preferred_date}"
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=Booking)
def send_booking_emails(sender, instance, created, **kwargs):
    try:
        if created:
            # Email to client when they submit
            send_mail(
                subject='Booking Received — BiBi Lash Studio',
                message=f'Hi {instance.first_name},\n\nWe have received your booking request for {instance.service} on {instance.preferred_date}.\n\nWe will confirm your appointment within 24 hours.\n\nBiBi Lash Studio',
                from_email=None,
                recipient_list=[instance.email],
            )
            # Email to BiBi Lash when a new booking comes in
            send_mail(
                subject='New Booking Request',
                message=f'New booking from {instance.first_name} {instance.last_name}\nService: {instance.service}\nDate: {instance.preferred_date}\nPhone: {instance.phone}\nEmail: {instance.email}',
                from_email=None,
                recipient_list=['bibilash@gmail.com'],  # replace with actual email
            )
            confirmed = models.BooleanField(default=False)

        if not created and instance.confirmed:
                send_mail(
                    subject='Booking Confirmed — BiBi Lash Studio',
                    message=f'Hi {instance.first_name},\n\nYour appointment for {instance.service} on {instance.preferred_date} has been confirmed.\n\nSee you soon!\nBiBi Lash Studio',
                    from_email=None,
                    recipient_list=[instance.email],
                )
    except Exception:
        pass