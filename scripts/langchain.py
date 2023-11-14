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


llm = ChatOpenAI(openai_api_key=config['openai_api_key'])