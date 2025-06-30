import streamlit as st
import re

# Function to validate the password
def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    upper = bool(re.search(r'[A-Z]', password))
    lower = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'\d', password))
    special = bool(re.search(r'\W', password))

    if not upper:
        return False, "Password must contain at least one uppercase letter."
    if not lower:
        return False, "Password must contain at least one lowercase letter."
    if not digit:
        return False, "Password must contain at least one digit."
    if not special:
        return False, "Password must contain at least one special character."

    return True, "Password is valid."

# Function to assess password strength
def check_strength(password):
    score = 0
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'\W', password): score += 1

    if score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Streamlit UI
st.title("🔐 Password Validator & Strength Checker")

password = st.text_input("Enter your password:", type="password")
confirm_password = st.text_input("Re-enter your password:", type="password")

if password:
    valid, message = validate_password(password)
    if valid:
        st.success(message)
        strength = check_strength(password)
        st.info(f"Password strength: **{strength}**")

        if confirm_password:
            if password == confirm_password:
                st.success("✅ Passwords match.")
                st.write(f"Your password `{password}` has been set successfully.")
            else:
                st.error("❌ Passwords do not match.")
    else:
        st.error(message)
