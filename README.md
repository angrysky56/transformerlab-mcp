# Transformerlab MCP Server

An MCP (Model Context Protocol) server that provides an interface for AI assistants to interact with Transformerlab functionality.

## Overview

This project implements an MCP server that wraps the Transformerlab API, allowing AI assistants like Claude to interact with Transformerlab's features. This includes model management, training, dataset operations, evaluation, and RAG capabilities.

## Prerequisites

- Python 3.10 or higher
- A running Transformerlab API server (default: http://localhost:8338)
- UV (Python package manager)
- MCP SDK
- Transformerlab client library

## Project Structure

```
transformerlab-mcp/
├── pyproject.toml          # Project configuration
├── README.md               # Documentation
├── src/
│   └── transformerlab_mcp/
│       ├── __init__.py     # Package initialization
│       ├── client.py       # Client wrapper for Transformerlab
│       ├── server.py       # MCP server implementation
│       └── tools/          # Folder for tool implementation
│           ├── __init__.py
│           ├── models.py   # Model management tools
│           ├── datasets.py # Dataset management tools
│           ├── training.py # Training and fine-tuning tools 
│           ├── evaluation.py # Evaluation tools
│           └── rag.py      # RAG tools
├── install_dev.sh          # Script to install in development mode
└── run.sh                  # Script to run the server
```

## Installation

1. Ensure UV is installed (if not, install it following the instructions at https://github.com/astral-sh/uv)

2. Create a Python environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install "mcp[cli]" transformerlab-client
   ```

3. Install the package in development mode:
   ```bash
   ./install_dev.sh
   ```

## Usage

1. Ensure Transformerlab is running and accessible at the configured URL (default: http://localhost:8338)

2. Start the MCP server:
   ```bash
   ./run.sh
   ```

3. To test the server with the MCP Inspector:
   ```bash
   mcp dev -m transformerlab_mcp.server
   ```

4. To use with Claude Desktop or other MCP clients, add the following to the Claude Desktop config file (typically located at `~/.config/Claude Desktop/claude_desktop_config.json` on Linux or similar locations on other platforms):
   ```json
   {
     "mcpServers": {
       "TransformerLabMCP": {
         "command": "uv",
         "args": ["--directory", "/absolute/path/to/transformerlab-mcp", "run", "-m", "transformerlab_mcp.server"]
       }
     }
   }
   ```

## Supported Features

The MCP server provides tools for:

- **Model Management**: Listing, downloading, and getting information about models
- **Training & Fine-tuning**: Starting and monitoring training jobs
- **Dataset Management**: Listing, importing, and getting information about datasets
- **Evaluation**: Running evaluations and retrieving results
- **RAG**: Adding documents, listing collections, and performing RAG queries

## Configuration

The server uses the following environment variables:

- `TRANSFORMERLAB_API_URL`: The URL of the Transformerlab API server (default: http://localhost:8338)

## License

AGPL-3.0 (matching Transformerlab's license)
