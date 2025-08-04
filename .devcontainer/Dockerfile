FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:18

# Install Python
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3.11 python3.11-venv python3-pip \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install global tools
RUN npm install -g @vscode/vsce typescript ts-node markdownlint-cli

# Create Python virtual environment
ENV VIRTUAL_ENV=/workspace/venv
RUN python3.11 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Switch to non-root user
USER node
WORKDIR /workspace

# Create cache directories
RUN mkdir -p /home/node/.vscode-server/extensions \
    /home/node/.vscode-server-insiders/extensions

# VS Code specific settings
ENV SHELL=/bin/bash \
    VSCODE_EXTENSIONS="/home/node/.vscode-server/extensions" \
    VSCODE_TEST_WORKSPACE="/workspace/test-workspace"
