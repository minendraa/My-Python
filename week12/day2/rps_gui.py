# rock_paper_scissors_app.py

import random
import streamlit as st

def play_rps():
    st.title("🪨📄✂️ Rock, Paper, Scissors Game")
    st.write("Play against the computer. Make your choice below:")

    # Let user choose play
    user_choice = st.selectbox("Choose your move:", ["Rock", "Paper", "Scissors"])
    play_button = st.button("Play")

    if play_button:
        # Computer randomly chooses
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        # Determine the result
        result = ""
        if user_choice == computer_choice:
            result = "It's a draw!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "🎉 You win!"
        else:
            result = "😞 You lose!"

        # Show results
        st.write(f"**Your choice:** {user_choice}")
        st.write(f"**Computer's choice:** {computer_choice}")
        st.success(result)

# Run the game
if __name__ == "__main__":
    play_rps()
