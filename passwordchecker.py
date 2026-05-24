def check_password_strength(password):
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars for c in password)
    
    score = sum([length, has_upper, has_lower, has_digit, has_special])
    
    if not length:
        print("Password must be at least 8 characters.")
    elif score <= 2:
        print("Weak password.")
    elif score == 3 or score == 4:
        print("Medium password.")
    else:
        print("Strong password!")


password = input("Enter password: ")
check_password_strength(password)