import random
import string
def low_effort_pass_gen(randfrac):
    length = random.randint(5,16)
    return(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length)))

print(low_effort_pass_gen(random.random()))
