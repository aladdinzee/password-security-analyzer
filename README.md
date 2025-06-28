# 🔐 Password Security Analyzer

A Python-based command-line tool that checks if a password is **strong** and whether it has been **exposed in real-world data breaches**. It uses entropy-based strength evaluation and queries the [Have I Been Pwned (HIBP)](https://haveibeenpwned.com/API/v3#PwnedPasswords) API to check password safety.

---

## 📌 Features

- Checks **password strength** based on length and character variety
- Calculates **entropy** to estimate resistance to brute-force attacks
- Verifies if the password has been **pwned** in public breaches using HIBP API
- Uses `getpass` to securely input passwords to maintain the confidentiality
- Clean and clear terminal output

---

## 🎯 Purpose of the Project

This project demonstrates:
- Use of external APIs securely
- Password hashing and entropy calculation
- Real-world application of cybersecurity principles
- Modular, testable Python code structure

---

## 🧪 Sample Output

🔐 Password Security Analyzer
───────────────────────────────────────────────
🔑 Password Entered: **************

✅ Strength         : Strong
🔢 Entropy Score    : 82.54 bits
🛡️  Breach Status   : ✅ Not found in any known data breaches!

💡 Recommendation   : Excellent choice! This password is strong and unique.
───────────────────────────────────────────────


