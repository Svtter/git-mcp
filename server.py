"""
A MCP server for using git
"""

import os

from fastmcp import FastMCP
from git import Repo

__version__ = "1.0.0"

mcp = FastMCP("Git MCP", __version__, dependencies=["gitpython"])


@mcp.tool()
def add(repo_path: str):
  """
  Add the changes to the repository.
  """
  repo = Repo(repo_path)
  repo.index.add(repo.untracked_files)
  repo.index.write()


@mcp.tool()
def status(repo_path: str):
  """
  Get the status of the repository.
  """
  repo = Repo(repo_path)
  return repo.index.status()


@mcp.tool()
def get_file(repo_path: str, file_path: str):
  """
  Get the file content from the repository.
  file_path: The path to the file to get the content of, relative to the root of the repository.
  """
  file_path = os.path.join(repo_path, file_path)
  if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} not found")
  with open(file_path, "r") as f:
    return f.read()


@mcp.tool()
def diff(repo_path: str):
  """
  Get the diff of the repository.
  """
  repo = Repo(repo_path)
  return repo.index.diff()


@mcp.tool()
def branch(repo_path: str):
  """
  Get the branch of the repository.
  """
  repo = Repo(repo_path)
  return repo.active_branch.name


@mcp.tool()
def checkout(repo_path: str, branch: str):
  """
  Checkout the branch of the repository.
  """
  repo = Repo(repo_path)
  repo.git.checkout(branch)


@mcp.tool()
def pull(repo_path: str):
  """
  Pull the changes from the repository.
  """
  repo = Repo(repo_path)
  repo.remotes.origin.pull()


@mcp.tool()
def commit(repo_path: str, message: str):
  """
  Commit the changes to the repository.
  """
  repo = Repo(repo_path)
  repo.index.commit(message)


if __name__ == "__main__":
  mcp.run()
