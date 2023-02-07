import os
import pathlib

DOCKER_DATA_PATH = "/code/data/"


def get_git_root():
    last_cwd = os.getcwd()
    while not os.path.isdir(".git"):
        os.chdir("..")
        cwd = os.getcwd()
        if cwd == last_cwd:
            raise OSError("no .git directory")
        last_cwd = cwd
    return last_cwd


LOCAL_DATA_PATH = str(pathlib.Path(get_git_root()) / "data")


def get_data_path():
    try:
        is_docker = os.environ["DOCKER_ENV_DATA_PROJECT"]
        if is_docker:
            path = DOCKER_DATA_PATH
        else:
            path = LOCAL_DATA_PATH
    except KeyError:
        path = LOCAL_DATA_PATH
    return path


DATA_PATH = get_data_path()
