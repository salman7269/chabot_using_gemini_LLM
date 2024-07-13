from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("Google_API_Key"))

# Function to load the gemini pro model to get the response of our chatbot
model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)
    return response.text

# Initializing the Streamlit application
st.set_page_config(page_title="Robochat", page_icon="🤖", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: black;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .header {
        font-size: 3em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .subheader {
        font-size: 1.5em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .stTextInput>div>div>input {
        color: white;
        background-color: #333333;
        border: 1px solid #4CAF50;
    }
    .stTextInput>div>div>input:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown('<p class="header">Robochat 🤖</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">By: Salman Shaikh</p>', unsafe_allow_html=True)

# Input section
input = st.text_input("Enter your question here:", key="input", help="Type your question and press Enter or click 'Get Response'")

# Get Response button
submit = st.button("Get Response")

# Display response
if submit:
    if input.strip() != "":
        with st.spinner('Generating response...'):
            response = get_response(input)
            st.success('Response generated successfully!')
            st.markdown(f"**Response:**\n\n{response}")
    else:
        st.error("Please enter a valid question.")
