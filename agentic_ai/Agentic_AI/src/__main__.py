from .state import AgentState
from .nodes.AIAgent import node as ai_agent_node, llm as ai_agent
from .nodes.AIReview import node as ai_review_node
from .conditionals import conditional_router, review_router

from langgraph.graph import StateGraph, START
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode

checkpointer = InMemorySaver()

graph_builder = StateGraph(AgentState)
graph_builder.add_node("AIAgent", ai_agent_node)
graph_builder.add_node("tools", ToolNode(ai_agent.get_tools()))
graph_builder.add_node("AIReview", ai_review_node)

graph_builder.add_edge(START, "AIAgent")
graph_builder.add_conditional_edges("AIAgent", conditional_router)
graph_builder.add_conditional_edges("tools", conditional_router)
graph_builder.add_conditional_edges("AIReview", review_router)


graph = graph_builder.compile(checkpointer=checkpointer)


if __name__ == "__main__":
    while True:
        user_message = input("User: ")
        if user_message.strip().lower() == "exit":
            break
        res = graph.invoke(
            {"messages": user_message}, config={"configurable": {"thread_id": "1"}}
        )
        print(res["messages"][-1].content)
