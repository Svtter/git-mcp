# Git MCP

A MCP tool to using git

## Usage

Start server.py

```bash
uv run server.py
```

Config your MCP application

```json
{
  "mcpServers": {
    "git": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```