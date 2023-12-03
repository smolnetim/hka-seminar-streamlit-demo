# hka-seminar-streamlit-demo
A seminar work at the [Hochschule Karlsruhe - University of Applied Sciences (HKA)](https://h-ka.de) with the title "Web development with Streamlit and Python".

[[_TOC_]]

## Further reading

| Topic            | Documentation                             |
|------------------|-------------------------------------------|
| backend/hasura   | [README.md](./backend/hasura/README.md)   |

## Used technology

| Technology       | Link                      |
|------------------|---------------------------|
| Streamlit        | <https://streamlit.io/>   |
| Python           | <https://python.org/>     |
| PostgreSQL       | <https://postgresql.org/> |
| Hasura           | <https://hasura.io/>      |

## Prerequisites

| Tool | Version | Comment |
|---|---|---|
| Node.js | 16@latest | It is recommended to use `nvm` to quickly switch between node.js versions |
| Commitizen | latest | `npm install -g commitizen` |

## How to commit

Use the [commitizen cli](https://github.com/commitizen/cz-cli) to commit.

1. Stage your changes
2. Run `git cz` in the terminal
3. Select the proper type
4. Select a scope, e.g.:
    * frontend/...
    * backend/...
5. Write a short description
6. Skip the other options

## NPM Scripts

This project contains some useful _npm scripts_ under `./package.json` for building and running the server. They also automate some processes to enhance development and deployment. Scripts can be executed within the top level directory (`/`) of this repository by executing the following:

```bash
npm run script-name
```

Please use the correct script depending on your OS. Scripts that only run on one OS (e.g. Windows) are suffixed with an abbreviation. No abbreviation means that any OS can run the script.

* `win:` Windows
* `lnx:` Linux
* `mac:` Mac

| Script name            | Description                |
| ---------------------- | ---------------------------|
| `win:init`             | Initializes the repository |
| `lnx:init`             | Initializes the repository |
| `mac:init`             | Initializes the repository |

## DEV SETUP

### **Required** - NPM install

To make sure commitizen works in the root directory you need to install its dependencies inside the root directory.
You will also have to copy the _.env_ files to make sure the environment is set up correctly.
The following steps will guide you threw the initialization process.

#### Step 1: Run init script

Run one of the init scripts from the _package.json_ depending on your operating system. (e.g. `npm run win:init`)

#### Step 2: Configure the `.env` files

Update the .env files with strong auth keys and passwords. (Optional for local development)

### Local Development

For local development you will have to run the docker containers using the given [docker-compose.yml](./docker-compose.yml).
By default it serves the whole application. You can then stop specific containers if you want to develop them manually.
The necessary configuration in that regard will be explained further down.

> Use [Docker Desktop](https://www.docker.com/products/docker-desktop/) to manage and analyze the container with ease.

```sh
docker compose build --no-cache
docker compose up -d
```
