# -*- coding: utf-8 -*-
import os
from PIL import Image
import streamlit as st
from html_templates import css, user_template, bot_template
import base64
from langchain_community.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.agents.agent_types import AgentType
import matplotlib.pyplot as plt
import sqlite3
import random
from plotly.graph_objects import Figure
import plotly.express as px
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from streamlit_javascript import st_javascript
from user_agents import parse
import os
from langchain_community.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.memory import ConversationBufferWindowMemory
import streamlit as st
from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers



st.set_page_config(page_title='iSaksham CoPilot')
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("isaksham.png")
img2 = get_img_as_base64("isaksham_logo.png")

page_by_img = f"""
<style>
[data-test-id="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: repeat%;
background-attachment: local;
}}
.chat-message.user::after {{
background-image: url("data:image/png;base64,{img2}");
}}

[data-test-id="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_by_img, unsafe_allow_html=True)

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


def main():
    image= Image.open('isaksham_logo.png')
    st.image(image, output_format="auto",width=150,use_column_width=50, clamp = False, channels = "RGB")
    st.title("iSaksham Copilot")
    st.write(css, unsafe_allow_html=True)

    st.session_state.setdefault('chat_history', [])

    # os.environ["OPENAI_API_KEY"] = ""
    # os.environ["OPENAI_ENDPOINT"] = ""

    input_text=st.text_input("Enter the Blog Topic")

    ## creating to more columns for additonal 2 fields

    col1,col2=st.columns([5,5])

    with col1:
        no_words=st.text_input('No of Words')
    with col2:
        blog_style=st.selectbox('Writing the blog for',
                                ('Researchers','Data Scientist','Common People'),index=0)


    # query = st.text_input("Ask your question:", placeholder="Message ChatGPT...")
    
    if st.button('Submit'):
        with st.spinner('generating response...'):
            answer = getLLamaresponse(input_text,no_words,blog_style)

            st.session_state.chat_history.append(f"{answer}")
            # st.session_state.chat_history.append(f"{query}")

            for i, message in enumerate(reversed(st.session_state.chat_history)):
                if i%2 == 0:
                    st.markdown(bot_template.replace("{{MSG}}", message), unsafe_allow_html=True)
                else:
                    st.markdown(user_template.replace("{{MSG}}", message), unsafe_allow_html=True)

if __name__ == "__main__":
    main()