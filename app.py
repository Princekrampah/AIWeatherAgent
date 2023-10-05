import streamlit as st
from ai_functionality import generate_ai_reponse


# set initial message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there, how can I help you"}
    ]


with st.sidebar:
    # language
    selected_language = st.selectbox(
        'Select A Language',
        ("English", "Swahili", "French"))

    # json_result_fields
    traits = st.multiselect(
        "Select Behaviour traits You Are Interested In",
        ['Funny', 'rude',
         'normal', 'black',
         "white", "news reporter",
         "childish", "mature",
         "charismatic", "compassion",
         "agreeableness", "creative",
         "optimism", "confident",
         "ambitious"],
        ['Funny', 'charismatic']
    )


# display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# get user input
user_prompt = st.chat_input()


if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response, context = generate_ai_reponse(
                user_prompt=user_prompt,
                traits=traits,
                language=selected_language)
            st.write(ai_response)
            st.write(context)

    new_ai_message = {"role": "user", "content": ai_response}
    st.session_state.messages.append(new_ai_message)
