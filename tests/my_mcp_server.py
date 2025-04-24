from fastmcp import FastMCP

if __name__ == "__main__":
  # Create a basic server instance
  mcp = FastMCP(name="MyAssistantServer")

  # You can also add instructions for how to interact with the server
  mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="This server provides data analysis tools. Call get_average() to analyze numerical data.",
  )
