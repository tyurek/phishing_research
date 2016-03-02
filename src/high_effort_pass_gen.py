import subprocess
import random
import string
import med_effort_pass_gen
def high_effort_pass_gen(min_char_len=0, max_char_len=16, enforce_numbers=0, enforce_special_chars=0, enforce_lowercase=0, enforce_uppercase=0):
    while 1:
        output = med_effort_pass_gen.med_effort_pass_gen(random.random())
        if len(output) < min_char_len:
            continue
        if len(output) > max_char_len:
            continue
        digit_count = 0
        for c in output:
            if c in string.digits:
                digit_count = digit_count + 1
        if digit_count < enforce_numbers:
            continue
        lcase_count = 0
        for c in output:
            if c in string.ascii_lowercase:
                lcase_count = lcase_count + 1
        if lcase_count < enforce_lowercase:
            continue
        ucase_count = 0
        for c in output:
            if c in string.ascii_uppercase:
                ucase_count = ucase_count + 1
        if ucase_count < enforce_uppercase:
            continue
        special_count = 0
        for c in output:
            if c in (" !#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"'):
                special_count = special_count + 1
        if special_count < enforce_special_chars:
            continue
        break
    return output
print (high_effort_pass_gen(enforce_numbers=1, enforce_special_chars=1))
