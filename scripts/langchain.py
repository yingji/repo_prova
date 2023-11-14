# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:02:34 2023

@author: wuy
"""
import os
import json
import yaml
from tkinter import Tk, filedialog
from langchain.chat_models import ChatOpenAI

CCURENT_FILEPATH = os.path.abspath(__file__)

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


llm = ChatOpenAI(openai_api_key="...")