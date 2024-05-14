from django.contrib import admin
from .models import User,Turf,Booking ,Review # Import your User model

# Register your User model with the admin site
admin.site.register(User)
admin.site.register(Turf)
admin.site.register(Booking)
admin.site.register(Review)
