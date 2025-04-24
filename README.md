# Git MCP

A MCP tool to using git, built with [FastMCP](https://gofastmcp.com/getting-started/welcome).

## Usage

You set up your repos folder on your own disk.

### Run from source code

```bash
REPO_DIR=<your repo dir>
```

Start server.py

```bash
uv run server.py
```

This will start a MCP server on your machine.

### Run from Docker

`docker run --rm -t -v $(pwd):/repos -e REPO_DIR=/repos svtter/git-mcp`

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