import pytest


class Repo(object):
  def __call__(self, repo_name: str):
    return repo_name


def test_call():
  with pytest.raises(TypeError):
    Repo("test")
