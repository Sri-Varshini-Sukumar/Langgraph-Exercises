from typing import Annotated, TypedDict, Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage  #The foundational class for all the messages in LangGraph
from langchain_core.messages import ToolMessage #Passes data back to LLM after it calls a tool such as the content
#and tool_call_id
from langchain_core.messages import SystemMessage  #Message for providing instructions to the LLM
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
load_dotenv()

#Annotated - Provides additional context without affecting the type itself
# email = Annotated[str,"This has to be a valid email format"]
# print(email.__metadata__)

#Sequence - To automatically handle the state updates for sequences such as by adding new messages to the
#chat history

#Reducer Function
#Rule that controls how updates from nodes are combined with the existing state
#Tells us how to merge new data to the current state
#Without a reducer, updates would have replaced the existing value entirely

#sequence[basemessage] is the datatype
class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage],add_messages]
#we are going to use a decorator

@tool
def add(a:int, b:int):
    """This is an addition function that adds two numbers"""
    return a+b

@tool
def subtract(a:int, b:int):
    return a-b

@tool
def multiply(a:int, b:int):
    return a*b

@tool
def divide(a:int, b:int):
    return a/b
tools = [add,subtract,multiply,divide]

#pythons inbuilt function
model = ChatOpenAI("gpt-4o").bind_tools(tools)

def model_call(state:AgentState)->AgentState:
    system_prompt = SystemMessage(content="You are my AI Assistant, please answer my query to the best of your ability")
    response = model.invoke([system_prompt] + state["messages"])
    return {"message" : [response]}

def should_continue(state:AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"

graph = StateGraph(AgentState)
graph.add_node("our_agent",model_call)
tool_node = ToolNode(tools=tools)
graph.add_node("tools",tool_node)
graph.set_entry_point("our_agent")
graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue" : "tools",
        "end" : END,
    },
)
#from the tool node back to the agent
graph.add_edge("tools","our_agent")
app = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message,tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages" : [("user","Add 3+4.")]}
print_stream(app.stream(inputs,stream_node="values"))