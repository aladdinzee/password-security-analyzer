import hashlib
import requests

##############################################
# This function checks if the passwords      #
# have been pawned and cracked.              #
##############################################

def check_pass_pwned(password):
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()    
    
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    headers = {
        "User-Agent" : "AadinZeeshanBreachChecker/v1.0"
    }

    response = requests.get(url,headers=headers)

    if(response.status_code != 200):
        raise RuntimeError(f"Error fetching data : {response.status_code}")

    hashes = (line.split(":") for line in response.text.splitlines())

    for h, count in hashes:
        if suffix == h:
            return f"Your password has been found {count} times. Please change it immediately"
    
    return f"Your password has not been pawned and is safe to use!"