from strength_checker import is_strong, entropy_calc
from breach_checker import check_pass_pwned
import getpass

print("---------------------------------")

while(True):
    print("Password Analyzer")
    print("---------------------------------")
    print(" ")
    user_password = getpass.getpass("Enter a password (Q to quit): ")
    print(" ")

    if(user_password == "Q"):
        break

    user_password_strength = is_strong(user_password)
    user_password_entropy = entropy_calc(user_password)
    user_password_is_breached = check_pass_pwned(user_password)

    print(f"Password          : {user_password}")
    print(f"Strength          : {user_password_strength}")
    print(f"Entropy           : {user_password_entropy} bits")
    print(f"Breach Status     : {user_password_is_breached}")
    print(" ")

    print("---------------------------------")
