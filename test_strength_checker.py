from strength_checker import is_strong, entropy_calc

test_passwords = [
    "123456",
    "password",
    "Aa1!",
    "Aadin2025",
    "Aadin2025!",
    "ZxcvbN1234!",
    "!!@@##!!@@",
    "HelloWorld123",
    "SuperSecure@2025",
    "A@1zC@9x",
    "Welcome!",
    "LetMeIn123",
    "G@t3K33p3r!"
]

for test_pass in test_passwords:
    strength = is_strong(test_pass)
    entropy_value = entropy_calc(test_pass)

    print(f"Password : {test_pass}")
    print(f"Strength : {strength}")
    print(f"Entropy : {entropy_value:.2f}")
    print("\n")