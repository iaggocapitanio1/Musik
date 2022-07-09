from email.policy import default
from django.db import models


def generate_unique_code():
    import string
    import random
    length = 6
    while True:
        code = "".join(random.choice(string.ascii_uppercase, k=length ))
        if Room.objects.filter(code=code).count()==0:
            break
    return code 

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.ImageField(null=False, default=1)
    created_at = models.DateField(auto_now_add=True)

    
