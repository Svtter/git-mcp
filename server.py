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

  @staticmethod
  def get_repo_path(repo_name: str):
    return os.path.join(RepoContext.repodir(), repo_name)


class RepoHandler(object):
  def __init__(self, repo_name: str):
    self.repo_name = repo_name
    self.repo_path = RepoContext.get_repo_path(repo_name)
    self.repo = gitRepo(self.repo_path)

  def status(self) -> str:
    import subprocess

    output = subprocess.run(
      ["git", "status"], cwd=self.repo_path, capture_output=True, text=True
    )
    return output.stdout


def create_repo(repo_name: str) -> gitRepo:
  """
  Create a gitpython.Repo object.
  repo_name: The name of the repository to create.
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
  repo_name: The name of the repository to add the changes to.
  """
  repo = create_repo(repo_name)
  repo.index.add(repo.untracked_files)
  repo.index.write()


@mcp.tool()
def status(repo_name: str):
  """
  Get the status of the repository.
  repo_name: The name of the repository to get the status of.
  """
  rh = RepoHandler(repo_name)
  return rh.status()


@mcp.resource("files://{repo_name}/{file_path}")
def get_file(repo_name: str, file_path: str):
  """
  Get the file content from the repository.
  repo_name: The name of the repository to get the file content from.
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
  repo_name: The name of the repository to get the diff of.
  """
  repo = create_repo(repo_name)
  return repo.index.diff()


@mcp.tool()
def branch(repo_name: str):
  """
  Get the branch of the repository.
  repo_name: The name of the repository to get the branch of.
  """
  repo = create_repo(repo_name)
  return repo.active_branch.name


@mcp.tool()
def checkout(repo_name: str, branch: str):
  """
  Checkout the branch of the repository.
  repo_name: The name of the repository to checkout the branch of.
  branch: The branch to checkout.
  """
  repo = create_repo(repo_name)
  repo.git.checkout(branch)


@mcp.tool()
def pull(repo_name: str):
  """
  Pull the changes from the repository.
  repo_name: The name of the repository to pull the changes from.
  """
  repo = create_repo(repo_name)
  repo.remotes.origin.pull()


@mcp.tool()
def commit(repo_name: str, message: str):
  """
  Commit the changes to the repository.
  repo_name: The name of the repository to commit the changes to.
  message: The message to commit the changes with.
  """
  repo = create_repo(repo_name)
  repo.index.commit(message)


if __name__ == "__main__":
  mcp.run("sse", host="0.0.0.0", port=8000)
