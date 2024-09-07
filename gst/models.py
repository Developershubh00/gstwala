from django.db import models
from django.contrib.auth.models import User

# Define a model for storing user profile information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's built-in User model
    phone_number = models.CharField(max_length=15)
    business_name = models.CharField(max_length=100)
    business_address = models.TextField()
    gst_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.business_name

# Define a model for storing GST Filing information
class GSTFiling(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    filing_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status_choices = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='PENDING')
    payment_date = models.DateField(null=True, blank=True)
    payment_reference = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"GST Filing for {self.user_profile.business_name} on {self.filing_date}"

# Define a model for storing payment details
class Payment(models.Model):
    gst_filing = models.OneToOneField(GSTFiling, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, default='Online')
    payment_date = models.DateField(auto_now_add=True)
    payment_status_choices = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    ]
    payment_status = models.CharField(max_length=10, choices=payment_status_choices, default='PENDING')

    def __str__(self):
        return f"Payment for {self.gst_filing.user_profile.business_name} - {self.payment_status}"
