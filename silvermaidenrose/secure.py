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

def secure_val_p(value, salt):
    print "value is:" + value
    print "salt is:" + salt
    split_value = value.split('|')
    first_part = split_value[0]
    print "first_part is:" + first_part
    given_hash = split_value[1]
    print "given_hash is:" + given_hash
    calculated_hash = make_secure_val(str(first_part), salt).split(',')[0]
    print "calculated_hash is:" + calculated_hash
    return given_hash == calculated_hash

cookie = "5205088045891584|d4e8266e366640a73a7249444f69f5e5b7dde9d6b62b034bb0e3318acd58ce3a"
print secure_val_p(cookie,"bZiYR")
