import streamlit as st
import random
import string
import pyttsx3

# Text-to-Speech Initialization
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed

# Streamlit UI
st.set_page_config(page_title="Pronounceable Password Generator", layout="centered")
st.title("🔐 Pronounceable Password Generator with Accessibility")
st.write("Generate secure, readable, and speakable passwords with optional symbols and numbers.")

# User Inputs
length = st.slider("Select password length", 6, 24, 12)
include_digits = st.checkbox("Include numbers (0-9)", value=True)
include_symbols = st.checkbox("Include special characters (!@#$%^)", value=True)
read_aloud = st.checkbox("Read the password aloud (Text-to-Speech)", value=True)

# Syllable structures
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

def generate_password(length, digits=True, symbols=True):
    password = ""
    while len(password) < length:
        syllable = random.choice(consonants) + random.choice(vowels)
        password += syllable.capitalize() if random.random() > 0.5 else syllable

    password = password[:length]

    if digits:
        password += str(random.randint(10, 99))
    if symbols:
        password += random.choice("!@#$%^&*")

    return password[:length]

if st.button("🔁 Generate Password"):
    final_password = generate_password(length, include_digits, include_symbols)
    st.success("Generated Password:")
    st.code(final_password)

    if read_aloud:
        engine.say(f"Your generated password is {final_password}")
        engine.runAndWait()
