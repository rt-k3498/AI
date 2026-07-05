from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

client = MultiServerMCPClient({
    "math":{
        "url": "http://127.0.0.1:8000",
        "transport": "http",
        "headers": {
            "Authorization": "Bearer <YOUR_API_KEY>",
            "X-API-Key": "<YOUR_API_KEY>"
        }
    }
    #other servers can be added here in the same format
})

async def get_tools(client: MultiServerMCPClient):
    return await client.get_tools() # these tools can be bind to the llm and added to the toolNode in the stategraph

asyncio.run(get_tools(client)) # run the get tools function asynchronously