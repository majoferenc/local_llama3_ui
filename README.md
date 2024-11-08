# Local Llama 3 UI
Chat UI for local offline Llama3 Model to chat with.

## Architecture
![Alt text](architecture_solution.png?raw=true "Architecture")

## Streamlit UI
![Alt text](llama3_streamlit.png?raw=true "Streamlit UI")

## Prerequisites
- Install Ollama - https://ollama.com/
- Install Python 3

## Download Llama 3 model 
In your terminal:

  `ollama pull llama3:8b`

## Create Python Virtual Env
Via conda (miniconda):

```
  conda create --name local-llm python=3.12
  conda activate local-llm
```

Or via Python Venv:

```
  python3.12 -m venv env​
  source env/bin/activate​
```
​
To deactivate env after the session run:
  
  `deactivate​`

## Install Python libraries
In your terminal:

  `pip install -r requirements.txt`

## Run the Streamlit app

  `streamlit run streamlit_app_v2.py`

## Create Shell alias (optional)
Add into your `bashrc` or `zshrc` file:

  `alias llama='cd ~/llama3_local; streamlit run streamlit_app_v2.py'`

NOTE: update the `cd ~/llama3_local` with the path, where you've saved this project.

## Run the shell alias to call it from any directory

  `llama`

  
