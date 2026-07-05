from langgraph.types import interrupt

def get_user_input(query: str) -> str:
    """Tool to get user input. It is used to get input from the user in a conversational manner. It should be used to get input from the user when you want to ask a question or get information from the user.

    Args:
        query (str): The query to be asked to the user.

    Returns:
        str: The user's input.
    """

    user_input = interrupt({"query": query})
    return user_input["data"]