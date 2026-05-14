import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
chatbot = ChatBot("FAQBot")

# Training data (FAQ list)
faq_conversations = [
    "What is your name?",
    "I am FAQBot.",
    "What are your working hours?",
    "Our working hours are 9 AM to 5 PM.",
    "Where is the office?",
    "The office is located in the main building.",
    "How to contact support?",
    "You can contact support at maxfitness@gmail.com."
]

trainer = ListTrainer(chatbot)
trainer.train(faq_conversations)

# Streamlit UI
st.title("FAQBot Chat App")

# Maintain chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_message = st.text_input("You:", "")

if st.button("Send"):
    if user_message.strip() != "":
        # Get bot response
        bot_response = chatbot.get_response(user_message)

        # Save to chat history
        st.session_state.chat_history.append(("You", user_message))
        st.session_state.chat_history.append(("FAQBot", str(bot_response)))

# Display chat history
st.subheader("Chat History")
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"{sender}: {message}")
