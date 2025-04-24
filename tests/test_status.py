from server import RepoHandler


def test_status():
  rh = RepoHandler("git-mcp")
  assert rh.status() != ""
