from ..LLM import LLMWithStructuredOutput
from ..state import AgentState
from langchain_core.messages import AIMessage
from pydantic import BaseModel, Field


class ReviewOutputSchema(BaseModel):
    score: int = Field(description="The quality score of the output, between 1 and 10")
    relevance: int = Field(
        description="The relevance of the output to the query, between 1 and 10"
    )
    feedback: str = Field(
        description="Feedback on the output, including suggestions for improvement or corrections"
    )
    id: str | None = Field(description="Do not interact or set this field")

class AIReviewMessage(AIMessage):
    def __init__(self, content: str):
        super().__init__(content=content)


llm = LLMWithStructuredOutput(output_schema=ReviewOutputSchema)


def node(state: AgentState):
    last_message = state["messages"][-1] if state["messages"] else None
    if not isinstance(last_message, AIMessage):
        return {"needs_review": False}

    prompt = f"""You are an AI agent that reviews the output of another AI agent. Your task is to evaluate the output and provide feedback on its quality (provide a score between 1 and 10), and relevance (provide a score between 1 and 10). You should also suggest improvements or corrections if necessary.
    messages: {state["messages"]}
"""
    response = llm.prompt(prompt)
    last_message_id = last_message.id
    response.id = last_message_id
    if response.score < 5 or response.relevance < 5:
        return {
            "messages": AIReviewMessage(
                content=(
                    "Revise your previous answer using this reviewer feedback. "
                    f"Quality score: {response.score}/10. "
                    f"Relevance score: {response.relevance}/10. "
                    f"Feedback: {response.feedback}"
                )
            ),
            "needs_review": True,
        }

    return {"needs_review": False}
