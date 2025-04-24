"""
A MCP server for using git
"""

import ast
import os

# from fastapi import FastAPI
from fastmcp import FastMCP
from git import Repo as gitRepo

__version__ = "1.0.0"


class RepoContext(object):
  @staticmethod
  def repodir():
    return os.environ.get("REPO_DIR", "/home/svtter/work/project")

  def get_repo_path(self, repo_name: str):
    return os.path.join(self.repodir(), repo_name)


def create_repo(repo_name: str) -> gitRepo:
  """
  Create a gitpython.Repo object.
  """
  repo_path = RepoContext.get_repo_path(repo_name)
  repo = gitRepo(repo_path)
  return repo


def get_mcp():
  if ast.literal_eval(os.environ.get("MCP_WITH_INSTRUCTIONS", "True")):
    mcp = FastMCP(
      name="Git MCP",
      version=__version__,
      dependencies=["gitpython"],
      instructions="This is a MCP server for using git",
    )
  else:
    mcp = FastMCP("Git MCP", __version__, dependencies=["gitpython"])
  return mcp


mcp = get_mcp()


# Static resource returning simple text
@mcp.resource("config://app-version")
def get_app_version() -> str:
  """Returns the application version."""
  return __version__


@mcp.tool()
def add(repo_name: str):
  """
  Add the changes to the repository.
  """
  repo = create_repo(repo_name)
  repo.index.add(repo.untracked_files)
  repo.index.write()


@mcp.tool()
def status(repo_name: str):
  """
  Get the status of the repository.
  """
  repo = create_repo(repo_name)
  return repo.index.status()


@mcp.resource("files://{repo_name}/{file_path}")
def get_file(repo_name: str, file_path: str):
  """
  Get the file content from the repository.
  file_path: The path to the file to get the content of, relative to the root of the repository.
  """
  file_path = os.path.join(repo_name, file_path)
  if not os.path.exists(file_path):
    raise FileNotFoundError(f"File {file_path} not found")

  with open(file_path, "r") as f:
    data = f.read()

  return {"filename": file_path, "content": data}


@mcp.tool()
def diff(repo_name: str):
  """
  Get the diff of the repository.
  """
  repo = create_repo(repo_name)
  return repo.index.diff()


@mcp.tool()
def branch(repo_name: str):
  """
  Get the branch of the repository.
  """
  repo = create_repo(repo_name)
  return repo.active_branch.name


@mcp.tool()
def checkout(repo_name: str, branch: str):
  """
  Checkout the branch of the repository.
  """
  repo = create_repo(repo_name)
  repo.git.checkout(branch)


@mcp.tool()
def pull(repo_name: str):
  """
  Pull the changes from the repository.
  """
  repo = create_repo(repo_name)
  repo.remotes.origin.pull()


@mcp.tool()
def commit(repo_name: str, message: str):
  """
  Commit the changes to the repository.
  """
  repo = create_repo(repo_name)
  repo.index.commit(message)


if __name__ == "__main__":
  mcp.run("sse", host="0.0.0.0", port=8000)
