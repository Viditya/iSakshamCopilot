# Usage
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

tokenizer = LlamaTokenizer.from_pretrained('sarvamai/OpenHathi-7B-Hi-v0.1-Base')
model = LlamaForCausalLM.from_pretrained('sarvamai/OpenHathi-7B-Hi-v0.1-Base', torch_dtype=torch.bfloat16)

prompt = "मैं एक अच्छा हाथी हूँ"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(inputs.input_ids, max_length=30)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

# ----------------------------------------------------------------------------------------------------#

# from langchain.sql_database import SQLDatabase
# from dotenv import load_dotenv, find_dotenv
# import os
# from langchain_community.agent_toolkits import create_sql_agent
# from langchain_openai import ChatOpenAI

# load_dotenv(find_dotenv())

# con_str = os.getenv('CONNECTION_STRING')
# uri = con_str
# db = SQLDatabase.from_uri(uri)

# # print(db.get_table_names())
# print(db.get_table_info(['BuddyTalkTest']))



# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)