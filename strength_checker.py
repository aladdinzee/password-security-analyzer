import re
import math

min_length = 12
min_upper = 1
min_lower = 1
min_digit = 1
min_symbol = 1

#############################################
# These are the sub-functions               #
#############################################

def analyze_password_char(password):
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_symbol = bool(re.search(r"\W", password))
    has_digit = bool(re.search(r"\d",password))

    char_types = sum([has_upper,has_lower,has_symbol,has_digit])

    return char_types

#############################################
# These are the main functions!             #
#############################################

def is_strong(password):
    len_pass = len(password)

    if len_pass < min_length:
        return "Weak"

    result = analyze_password_char(password)
    if result >= 3:
        return "Strong"
    else:
        return "Weak"

def entropy_calc(password):
    charset_size = 0

    if (bool(re.search(r"[A-Z]", password)) == True):
        charset_size += 26
    if (bool(re.search(r"[a-z]", password)) == True):
        charset_size += 26
    if (bool(re.search(r"\W", password)) == True):
        charset_size += 32
    if (bool(re.search(r"\d",password)) == True):
        charset_size += 10

    try:
        entropy = math.log2(charset_size**len(password))
    except ValueError:
        entropy = 0

    return entropy