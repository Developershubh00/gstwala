from django.contrib import admin
from .models import UserProfile, GSTFiling, Payment
admin.site.register(UserProfile)
admin.site.register(GSTFiling)
admin.site.register(Payment)

