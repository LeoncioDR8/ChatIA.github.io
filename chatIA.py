import streamlit as st

st.title('Chat AI')


if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

def generate_response(user_input):

    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "help" in user_input.lower():
        return "Sure, tell me what you need, and I'll be happy to help."
    elif "thanks" in user_input.lower():
        return "You're welcome! I'm here to help whenever you need."
    else:
        return "I'm sorry, I am not sure how to help with that. Could you provide more details?"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hello! How can I assist you?")
    st.session_state.messages.append({"role": "assistant", "content": "Hello! How can I assist you?"})
    st.session_state.first_message = False


if user_input := st.chat_input("How can I assist you?"):

    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = generate_response(user_input)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})



