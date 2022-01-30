# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.154.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && xargs apt-get -y --no-install-recommends install vim \
    && apt-get autoremove -y && apt-get clean -y 
