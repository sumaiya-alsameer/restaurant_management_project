import string
import secrets
from .models import Order 

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits  # A-Z, 0-9

    while True:
        # random code
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # check if it already exists in DB (adjust if you have a Coupon model)
        if not Order.objects.filter(coupon_code=code).exists():
            return code