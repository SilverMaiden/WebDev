import hashlib
import random
import string

def make_salt():
    return_string = ""
    x = 0
    all_letters = string.letters
    while x != 5:
        return_string += random.choice(all_letters)
        x += 1
    return return_string

def make_secure_val(name, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + salt).hexdigest()
    return '%s,%s' % (h, salt)
