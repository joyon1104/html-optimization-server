from mcp.server.fastmcp import FastMCP # Parameter is not strictly needed now, but good practice to keep if you add more complex params later

# Create the FastMCP instance with stdio transport
mcp = FastMCP()

# Define the tool using the @mcp.tool() decorator
@mcp.tool()
def get_capital_city(city: str) -> str:
   """
   Returns weather of the city

   :param city: The city to get the weather for
   """
   return f"{city} weather is good"

# The tool is automatically added to the mcp instance by the decorator

# Run the server if the script is executed directly
if __name__ == "__main__":
   print("Starting MCP server...")
   mcp.run(transport="stdio")
