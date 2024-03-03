# -*- coding: utf-8 -*-
import os
from PIL import Image
import streamlit as st
from html_templates import css, user_template, bot_template
import base64

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
def main():
    image= Image.open('isaksham_logo.png')
    st.image(image, output_format="auto",width=150,use_column_width=50, clamp = False, channels = "RGB")
    st.title("iSaksham Copilot")
    st.write(css, unsafe_allow_html=True)

    st.session_state.setdefault('chat_history', [])

    os.environ["AZURE_OPENAI_API_KEY"] = ""
    os.environ["AZURE_OPENAI_ENDPOINT"] = ""

    query = st.text_input("Ask your question:", placeholder="Message ChatGPT...")

    if st.button('Submit') and query:
        with st.spinner('generating response...'):
            answer = 'Hi there !'

            st.session_state.chat_history.append(f"{answer}")
            st.session_state.chat_history.append(f"{query}")

            for i, message in enumerate(reversed(st.session_state.chat_history)):
                if i%2 == 0:
                    st.markdown(bot_template.replace("{{MSG}}", message), unsafe_allow_html=True)
                else:
                    st.markdown(user_template.replace("{{MSG}}", message), unsafe_allow_html=True)

if __name__ == "__main__":
    main()