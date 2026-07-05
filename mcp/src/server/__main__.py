from .tools import add, multiply, subtract, divide

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

add = mcp.tool()(add)
multiply = mcp.tool()(multiply)
subtract = mcp.tool()(subtract)
divide = mcp.tool()(divide)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
