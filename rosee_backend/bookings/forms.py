from django import forms
from .models import Booking
import datetime
class BookingForm(forms.ModelForm):
    preferred_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Booking
        fields = ['first_name','last_name','email','phone','service','preferred_date','notes']
    def clean_preferred_date(self):
        date = self.cleaned_data.get('preferred_date')
        if date and date <= datetime.date.today():
            raise forms.ValidationError('Please choose a future date.')
        return date
    def clean_email(self):
        return self.cleaned_data['email'].lower().strip()
