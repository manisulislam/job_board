from django.db import models
from django.contrib.auth.models import User
# Create your models here.
USER_TYPES=(
    ("EMPLOYER","EMPLOYER"),
    ("JOBSEEKER","JOBSEEKER")
)

class UserProfileInfo(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    user_types=models.CharField(max_length=20,choices=USER_TYPES, null=True, blank=True)
    
    def __str__(self):
        return self.user.username