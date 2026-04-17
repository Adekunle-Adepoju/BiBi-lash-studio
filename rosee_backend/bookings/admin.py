from django.contrib import admin
from django.utils.html import format_html
from .models import Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name','service_display','preferred_date','status_badge','email','created_at')
    list_filter = ('status','service','preferred_date')
    search_fields = ('first_name','last_name','email','phone')
    ordering = ('-created_at',)
    date_hierarchy = 'preferred_date'
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Client', {'fields':('first_name','last_name','email','phone')}),
        ('Appointment', {'fields':('service','preferred_date','notes')}),
        ('Status', {'fields':('status',)}),
        ('Meta', {'fields':('created_at',),'classes':('collapse',)}),
    )
    actions = ['mark_confirmed','mark_cancelled']
    @admin.action(description='Mark selected as Confirmed')
    def mark_confirmed(self, request, queryset): queryset.update(status=Booking.CONFIRMED)
    @admin.action(description='Mark selected as Cancelled')
    def mark_cancelled(self, request, queryset): queryset.update(status=Booking.CANCELLED)
    @admin.display(description='Service')
    def service_display(self, obj): return obj.get_service_display()
    @admin.display(description='Status')
    def status_badge(self, obj):
        colours = {Booking.PENDING:('#f59e0b','#fffbeb'),Booking.CONFIRMED:('#16a34a','#f0fdf4'),Booking.CANCELLED:('#dc2626','#fef2f2')}
        fg,bg = colours.get(obj.status,('#6b7280','#f9fafb'))
        return format_html('<span style="color:{};background:{};padding:3px 10px;border-radius:20px;font-size:0.75rem;font-weight:500;">{}</span>',fg,bg,obj.get_status_display())
admin.site.site_header = 'BiBi Lash Studio'
admin.site.site_title  = 'BiBi Admin'
admin.site.index_title = 'Booking Management'