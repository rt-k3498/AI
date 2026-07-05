from ..LLM import LLMWithTools
from ..state import AgentState
from ..tools.search import search
from ..tools.scrape import scrape
from ..tools.user_input import get_user_input


llm = LLMWithTools(
    tools=[search, scrape, get_user_input],
    system_rules=(
        "Confirm with the user before using search or scrape. "
        "Use get_user_input to ask for confirmation."
    ),
)


def node(state: AgentState):
    return {"messages": llm.prompt(state["messages"])}
