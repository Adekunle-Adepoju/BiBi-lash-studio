# Rosee Lash Studio - Django Backend

## Quick start

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create an admin account
python manage.py createsuperuser

# 5. Start the dev server
python manage.py runserver
```

Booking form  ->  http://localhost:8000/
Admin panel   ->  http://localhost:8000/admin/

## Switching to real email (production)

In settings.py, comment out the console backend and uncomment the SMTP block.
Set EMAIL_HOST_USER and EMAIL_HOST_PASSWORD as environment variables — never
hardcode credentials in settings.py.

## Project structure

rosee_backend/
  manage.py
  requirements.txt
  README.md
  rosee_backend/        <- Django project config
    settings.py
    urls.py
    wsgi.py
  bookings/             <- The bookings app
    models.py           <- Booking model (SQLite)
    forms.py            <- BookingForm with validation
    views.py            <- Form handling + redirect
    urls.py             <- URL routes
    admin.py            <- Admin panel config
    emails.py           <- Client + studio email helpers
    templates/
      bookings/
        booking_form.html
        booking_success.html
