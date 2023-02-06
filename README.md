# Install

- [Install docker](https://docs.docker.com/get-docker/) and start the daemon.
- `docker-compose up`  will start the container and print URLs to connect to the jupyter web UI.
	- If you're using VSCode, install the [Remote Development Extensions Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) to easily run code and otherwise work within the docker container. 
	- Attach to the `{repo_name}-notebook-1` container.
	- Be sure to install the VSCode python extension in the *remote* container as well. 

- The Prefect UI is available at `http://localhost:4200/` to view jobs.
- Jupyter notebooks are available at `http://localhost:8888/`. 
  - Ensure that notebooks are "trusted" in the top right corner to display interactive plots.
- Download data: `docker compose exec -i notebook python download_data.py` 

# Usage

You can use poetry to run set up an environment without Docker to save on overhead. 

- Install [poetry](https://python-poetry.org/docs/).
- Configure to create virtual environment in project: `poetry config settings.virtualenvs.in-project true`
- `poetry install` and point your notebooks to the venv.
- To add/remove packages:
  - `poetry {add|remove} {package}` 
  - `poetry export -f requirements.txt --output requirements.txt --without-hashes`. 
  - Run `docker-compose up --build` to rebuild the image with new packages, or for faster turnaround, `docker-compose exec notebook pip install -r /usr/src/app/requirements.txt`

