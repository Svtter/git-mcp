"""mcp client, for testing the server"""

import asyncio
import os

from fastmcp import Client, FastMCP

# Change the working directory to the tests directory
path = os.getcwd()
if not path.endswith("tests"):
  os.chdir(os.path.join(path, "tests"))

# Example transports (more details in Transports page)
server_instance = FastMCP(name="TestServer")  # In-memory server
sse_url = "http://localhost:8000/sse"  # SSE server URL
ws_url = "ws://localhost:9000"  # WebSocket server URL
server_script = os.path.join(path, "my_mcp_server.py")  # Path to a Python server file

# Client automatically infers the transport type
client_in_memory = Client(server_instance)
client_sse = Client(sse_url)
client_ws = Client(ws_url)
client_stdio = Client(server_script)

print(client_in_memory.transport)
print(client_sse.transport)
print(client_ws.transport)
print(client_stdio.transport)
