from .LLM import LLM
from ..retrieval.__main__ import retrieve_context

query = "what is federated learning?"
context_documents = retrieve_context(query)

llm = LLM()
prompt = f"""
Question: {query}
Context: {context_documents}
Answer the question based on the context provided. If the answer is not present in the context, respond with "I don't know."
"""
ans = llm.prompt(prompt)

"""
output = {
    "query": query,
    "context": context_documents,
    "answer": ans
}
"""

output = ans
print(output)
