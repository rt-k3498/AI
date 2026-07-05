from .state import AgentState
from .nodes.AIAgent import node as ai_agent_node, llm as ai_agent
from .nodes.AIReview import node as ai_review_node
from .conditionals import conditional_router, review_router
from .storage_client.supabase import supabase

from langgraph.graph import StateGraph, START
from .memory import MemoryManager
from langchain_core.load.load import loads
from langgraph.prebuilt import ToolNode
from langgraph.types import Command
import json

checkpointer = MemoryManager()

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
    config = {"configurable": {"thread_id": "1"}}
    db_res = supabase.table("chats").select("state").eq("id", "1").maybe_single().execute()
    state_history = None
    if db_res and db_res.data:
        state_history = loads(json.dumps(db_res.data["state"]))
    if state_history:
        graph.update_state(config=config, values=state_history, as_node=START)
    pending_interrupt = False
    while True:
        user_message = input("User: ")
        if user_message.strip().lower() == "exit":
            break

        if pending_interrupt:
            res = graph.invoke(Command(resume={"data": user_message}), config=config)
        else:
            res = graph.invoke({"messages": user_message}, config=config)

        pending_interrupt = "__interrupt__" in res
        if pending_interrupt:
            interrupt_value = res["__interrupt__"][0].value
            print(interrupt_value.get("query", interrupt_value))
            continue

        print(res["messages"][-1].content)
