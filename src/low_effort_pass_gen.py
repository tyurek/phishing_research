import random
import string
import math

def low_effort_pass_gen(randfrac=None):
    random.seed(a=randfrac)
    length = random.randint(5,16)
    return(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length)))
