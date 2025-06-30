import streamlit as st
import random

# Initialize session state variables
if 'secretnum' not in st.session_state:
    st.session_state.secretnum = random.randint(1, 20)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title("🎯 Welcome to the Number Guessing Game!")
st.write("Guess a number between 1 and 20.")

if not st.session_state.game_over:
    user_input = st.number_input("Enter your guess:", min_value=1, max_value=20, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if user_input == st.session_state.secretnum:
            st.session_state.message = "🎉 You guessed it right!"
            st.session_state.game_over = True
        elif user_input > st.session_state.secretnum + 5:
            st.session_state.message = "📈 Too high!"
        elif user_input > st.session_state.secretnum:
            st.session_state.message = "🔼 High!"
        elif user_input < st.session_state.secretnum - 5:
            st.session_state.message = "📉 Too low!"
        else:
            st.session_state.message = "🔽 Low!"

st.write(st.session_state.message)
st.write(f"🔁 Attempts: {st.session_state.attempts}")

if st.session_state.game_over:
    if st.button("Play Again"):
        # Reset session state
        st.session_state.secretnum = random.randint(1, 20)
        st.session_state.attempts = 0
        st.session_state.message = ""
        st.session_state.game_over = False
