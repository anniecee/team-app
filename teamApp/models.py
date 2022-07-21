from django.db import models

# Member model
class Member(models.Model):
    ROLETYPES = (
        ('regular', 'Regular - Can\'t delete members'),
        ('admin', 'Admin - Can delete members'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, null = True, blank = True)
    role = models.CharField(max_length=10, choices=ROLETYPES)
