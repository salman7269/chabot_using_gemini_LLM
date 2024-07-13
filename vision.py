#we will use the gemini-pro-vision to generate the details based on the image
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("Google_API_Key"))

# Function to load the gemini pro model to get the response of our chatbot
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="Image Data Generator")
st.header("Image Application")
st.subheader("By: Salman Shaikh")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Upload an Image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploadeded Image",use_column_width=True)
    st.success("Image Uploaded Successfully.")

submit=st.button("Tell me about the image")

#if submit is clicked
if submit:
    response=get_response(input,image)
    st.subheader("The Response is")
    st.write(response)



