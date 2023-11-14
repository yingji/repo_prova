# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:02:34 2023

@author: wuy
"""
import os
import json
import yaml
import pycurl
import certifi
import requests
from tkinter import Tk, filedialog

from openai import OpenAI
from langchain.chat_models import ChatOpenAI


CURRENT_FILEPATH = os.path.abspath(__file__)

## init
root = Tk() ; root.withdraw()
filename = filedialog.askopenfilename(
    parent=root, 
    initialdir='.', 
    filetypes=[("config files", "*.json; *.yaml")]
)
if filename.endswith('.json'):
    with open(filename, 'r') as json_data_file: # os.path.join(os.getcwd(), 'config/config.json')
        config = json.load(json_data_file)
else: #yaml
    with open(filename, 'r') as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.FullLoader)
headers = {
    "Authorization": f"Bearer {config['openai_api_key']}"
    }
model="gpt-3.5-turbo"
# endpoint = "https://api.openai.com/v1/completions" # Legacy models: text-davinci-003, text-davinci-002, davinci, curie, babbage, ada
endpoint = "https://api.openai.com/v1/chat/completions" # gpt4 turbo

#%% chat text-generation
# for json format:
#     model="gpt-3.5-turbo-1106"
#     response_format={ "type": "json_object" }
client = OpenAI(api_key=config['openai_api_key'])
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
     "role": "system", 
     "content": "You are a helpful assistant designed to output JSON."
     },
    {
     "role": "user", 
     "content": "Name 5 most trendy houseplants"
     },
    {
     "role": "assistant", 
     "content": "trendyHouseplants: Monstera deliciosa, Fiddle leaf fig, Snake plant, Pilea peperomioides, Calathea orbifolia"
     },
    {
     "role": "user", 
     "content": "Name 3 most common pets now, and tell me their taxonomy"
     },
    {
     "role": "assistant", 
     "content": """"
     commonPets: "Cats", "Dogs", "Fish"

     taxonomy:
     - Cats
       - Kingdom: Animalia
       - Phylum: Chordata
       - Class: Mammalia
       - Order: Carnivora
       - Family: Felidae
       - Genus: Felis
       - Species: catus

     - Dogs
       - Kingdom: Animalia
       - Phylum: Chordata
       - Class: Mammalia
       - Order: Carnivora
       - Family: Canidae
       - Genus: Canis
       - Species: lupus familiaris

     - Fish
       - Kingdom: Animalia
       - Phylum: Chordata
       - Class: Actinopterygii
       """
     },
    {
     "role": "user", 
     "content": "Who is the most famous cat? and what is it famous for?"
     }
    
    ]
)
for c in response.choices: # len=1
    print(c.message.content)

