from django.db import models
from django.utils import timezone
from phone_field import PhoneField


class Property(models.Model):
    code = models.CharField(unique=True, max_length=255, null=False)
    price = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=255, null=False)
    bedrooms = models.CharField(max_length=255, null=False)
    bathrooms = models.CharField(max_length=255, null=False)
    agent = models.CharField(max_length=255)
    agent_contact = PhoneField(blank=True, help_text='Contact phone number')
    agent_email = models.EmailField(max_length = 255)
    agent_company = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code
