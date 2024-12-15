# Import Libraries
import openai
import streamlit as st
from streamlit_chat import message
import os

# OpenAI API Key
try:
    openai.api_key = st.secrets["OPEN_API_KEY"]
except KeyError:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        st.error("API key not found. Please set it in .streamlit/secrets.toml or as an environment variable.")
        st.stop()

# Generating responses using the ChatCompletion endpoint
def generate_response(prompt):
    try:
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if desired
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.5,
        )
        messages = completions.choices[0].message["content"].strip()
        return messages
    except Exception as e:
        return f"Error generating response: {e}"

# Set custom modern purple theme and rebranding
st.set_page_config(
    page_title="PlutoAI by songfurina",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Apply custom CSS for modern purple theme and styling
st.markdown(
    """
    <style>
        /* General Body Styling */
        body {
            background-color: #F7F3FF; /* Light lavender background */
            color: #4B0082; /* Dark purple text */
        }

        /* Title Styling with Bright Outlined Font */
        .stTitle {
            font-family: "Arial Black", sans-serif;
            font-size: 2.5rem;
            text-align: center;
            color: white;
            text-shadow: 2px 2px 0 #A333FF, -2px -2px 0 #A333FF, 2px -2px 0 #A333FF, -2px 2px 0 #A333FF;
        }

        /* Input Field Styling */
        .stTextInput > div > div > input {
            background-color: #E9D6FF; /* Purple input box */
            color: #4B0082; /* Input text color */
            border: 2px solid #A333FF; /* Highlighted purple border */
            border-radius: 8px; /* Rounded corners */
        }
        .stTextInput > div > div > input::placeholder {
            color: black; /* Black placeholder text for 'Press Enter to Apply' */
        }
        .stTextInput > div > div > input:focus {
            border-color: #8000FF; /* Darker purple focus effect */
        }

        /* Chat Button Styling */
        .stButton > button {
            background-color: #A333FF;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 16px;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #8000FF;
        }

        /* Footer Styling (Fixed at Bottom) */
        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            font-size: 10px;
            text-align: center;
            color: #4B0082;
            background-color: #F7F3FF;
            padding: 5px 0;
            border-top: 1px solid #A333FF;
            z-index: 1000;
        }

        /* Chat History Styling (Preserved as Requested) */
        .stChatMessage {
            font-family: "Courier New", monospace;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with rebranding
st.title("✨ PlutoAI : One Chat at a Time.")
st.caption("by songfurina")  # Small branding below the title

# Storing the input and output in session state
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

# Input field for user input
def get_text():
    input_text = st.text_input(
        "You: ", 
        st.session_state['user_input'], 
        key="input", 
        placeholder="Press Enter to Apply"  # Custom placeholder
    )
    return input_text

# Generate response and update session state
user_input = get_text()

if user_input:
    output = generate_response(user_input)

    # Store the user input and bot output in session state
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    st.session_state['user_input'] = ""  # Clear the input box

# Display the chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')

# Add a clear button to reset the chat
if st.button("Clear Chat"):
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['user_input'] = ""  # Clear the input box
    st.experimental_rerun()  # Refresh the app to reflect changes

# Footer for branding
st.markdown(
    """
    <footer>
        Powered by OpenAI · Designed by songfurina · PlutoAI © 2024
    </footer>
    """,
    unsafe_allow_html=True,
)
