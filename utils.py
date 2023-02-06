import os

DOCKER_DATA_PATH = "/code/data/"
LOCAL_DATA_PATH = "./data/"


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
