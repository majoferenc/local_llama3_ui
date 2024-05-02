from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import initialize_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, AIMessage
from langchain.tools import Tool
from langchain.memory import ConversationBufferWindowMemory

llm = ChatOllama(model='llama3:latest')

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

search = DuckDuckGoSearchRun()

tools = [
    Tool.from_function(
        func=search.run,
        name="Search",
        description="Useful for when you need an answer questions about current events."
    )
]

memory = ConversationBufferWindowMemory(memory_key='chat_history')

PREFIX = '''You are a friendly assistant answering questions from human.
'''

FORMAT_INSTRUCTIONS = """Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of: {tool_names}
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Please respect the order of the steps Thought/Action/Action Input/Observation
"""

SUFFIX = '''
Previous conversation history:
{chat_history}

Human Question: {input}
{agent_scratchpad}
'''
agent = initialize_agent(
    tools=tools,
    llm=llm.bind(stop=["<|eot_id|>"]),
    output_key="result",
    handle_parsing_errors=True,
    max_iterations=2,
    early_stopping_method="generate",
    memory=memory,
    agent="zero-shot-react-description",
    agent_kwargs={
        'prefix': PREFIX, 
        'format_instructions': FORMAT_INSTRUCTIONS,
        'suffix': SUFFIX
    }
)

def process_chat(user_input, chat_history):
    response = agent.invoke({
        "input": user_input
    })
    return response["output"]

if __name__ == '__main__':
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = process_chat(user_input, chat_history)
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response))

        print("Assistant:", response)
