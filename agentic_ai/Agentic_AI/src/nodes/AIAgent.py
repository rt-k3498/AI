from ..LLM import LLMWithTools
from ..state import AgentState
from ..tools.search import search
from ..tools.scrape import scrape


llm = LLMWithTools(tools=[search, scrape])


def node(state: AgentState):
    return {"messages": llm.prompt(state["messages"])}
