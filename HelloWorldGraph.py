from typing import Dict,TypedDict
from langgraph.graph import StateGraph  
from  IPython.display import Image,display
#StateGraph is a framework that helps you to design and manage the flow of t
#the tasks in your application using a graph ds

class AgentState(TypedDict): #Our state schema
    message : str

def greeting_node(state:AgentState) -> AgentState:
    """This is a simple node that adds a greeting node to the state"""
    state["message"] = "Hey" + state["message"] + ", How is your day going?"
    return state
graph = StateGraph(AgentState)
graph.add_node("Greeter",greeting_node)
graph.set_entry_point("Greeter")
graph.set_finish_point("Greeter")
app = graph.compile()
display(Image(app.get_graph().draw_mermaid_png()))