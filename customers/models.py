from django.db import models

# Create your models here.
class CustomerProfile(models.Model):
    CUSTOMER_TYPES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
    ]

    name = models.CharField(max_length=255)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='individual')

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    address = models.JSONField(default=dict, blank=True, null=True)
    shipping_address = models.JSONField(default=dict)
    billing_address = models.JSONField(default=dict, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.customer_type})"