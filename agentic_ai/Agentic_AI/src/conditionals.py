from .state import AgentState
from langgraph.graph import END
from langchain_core.messages import AIMessage, ToolMessage
    


def conditional_router(state: AgentState):
    last_message = state["messages"][-1] if state["messages"] else ""
    match last_message:
        case AIMessage():
            if last_message.tool_calls:
                return "tools"
            return "AIReview"
        case ToolMessage():
            return "AIAgent"
        case _:
            return END


def review_router(state: AgentState):
    if state.get("needs_review"):
        return "AIAgent"
    return END
