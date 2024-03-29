import string
import random

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


def encode_uid(pk):
    return force_str(urlsafe_base64_encode(force_bytes(pk)))


def decode_uid(pk):
    return force_str(urlsafe_base64_decode(pk))


def generate_password(length: int) -> str:
    letters = string.ascii_letters
    numbers = string.digits
    punctuations = "*#$%&()+{}[]!@_|\\/><"

    password_string = list(letters + numbers + punctuations)
    random.shuffle(password_string)

    password = "".join(random.choice(password_string) for i in range(length))

    return password
