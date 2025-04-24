# Git MCP

A MCP tool to using git, built with [FastMCP](https://gofastmcp.com/getting-started/welcome).

## Usage

Set up your repos folder on your own disk.

```bash
REPO_DIR=<your repo dir>
```

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