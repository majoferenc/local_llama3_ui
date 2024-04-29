# Local Llama 3 UI
Chat UI for local offline Llama3 Model to chat with.

## Prerequisites
Install Ollama - https://ollama.com/
Install Python 3

## Download Llama 3 model 

  ollama pull llama3:latest

## Install Python libraries

  pip install -r requirements.txt

## Create Shell alias

  alias llama='cd ~/IBM/llama3_local; streamlit run streamlit_app_v2.py'

NOTE: update the `cd ~/IBM/llama3_local` with the path, where you've saved this project.

## Run the alias

  llama
