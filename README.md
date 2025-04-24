# Git MCP

A MCP tool to using git, built with [FastMCP](https://gofastmcp.com/getting-started/welcome).

## Usage

Start server.py

```bash
uv run server.py
```

This will start a MCP server on your machine.

## Config

Config your MCP application

```json
{
  "mcpServers": {
    "git": {
      "url": "http://<your_host>:8000/sse"
    }
  }
}
```

For example,

```json
{
  "mcpServers": {
    "git": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```