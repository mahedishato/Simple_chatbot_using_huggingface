from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os


#create a function 
def get_openai_response(quastion):
    llm = OpenAI(openai_api_key = os.getenv('OPEN_API_KEY'),model_name = 'text-davinci-003', temperature=0.6)
    response = llm(quastion)
    return response

##initialze our app

st.set_page_config(page_title="QNA DEMO")
st.header("langchain app")
input = st.text_input('Input: ', key="input")
response=get_openai_response(input)

stramlit = st.button("Ask the Question")

if stramlit:
    st.subheader("the response is ")
    st.write(response)