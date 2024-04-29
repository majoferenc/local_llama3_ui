# Local Llama 3 UI
Chat UI for local offline Llama3 Model to chat with.

## Architecture
![Alt text](architecture.png?raw=true "Architecture")

## Streamlit UI
![Alt text](llama3_streamlit.png?raw=true "Streamlit UI")

## Prerequisites
- Install Ollama - https://ollama.com/
- Install Python 3

## Download Llama 3 model 
In your terminal:

  `ollama pull llama3:latest`

## Install Python libraries
In your terminal:

  `pip install -r requirements.txt`

## Create Shell alias
Add into your `bashrc` or `zshrc` file:

  `alias llama='cd ~/IBM/llama3_local; streamlit run streamlit_app_v2.py'`

NOTE: update the `cd ~/IBM/llama3_local` with the path, where you've saved this project.

## Run the alias

  `llama`
