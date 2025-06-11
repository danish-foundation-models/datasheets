from pathlib import Path

from git import Repo

from .paths import repo_path


def get_current_revision(repo_path: Path = repo_path) -> str:
    repo = Repo(repo_path)
    commit_id = repo.head.object.hexsha
    return commit_id


def get_latest_revision(path: Path, repo_path=repo_path) -> str | None:
    repo = Repo(repo_path)

    if not path.exists():
        raise ValueError("path does not exist.")

    try:
        last_commit_for_file = next(repo.iter_commits(paths=path, max_count=1))
        return last_commit_for_file.hexsha
    except StopIteration:
        return None


def check_is_ancestor(ancestor_rev: str, rev: str | None, repo_path=repo_path) -> bool:
    if rev is None:  # e.g. when cases are not submitted yet
        return False
    repo = Repo(repo_path)
    return repo.is_ancestor(repo.commit(ancestor_rev), repo.commit(rev))
