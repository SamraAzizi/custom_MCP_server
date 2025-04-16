from mcp.server.fastmcp import FastMCP


mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b:int) -> int:
    return a+b

@mcp.resource("greeting://{name}")
def get_greeting(name:str) -> str:
    return f"hello, {name}!"