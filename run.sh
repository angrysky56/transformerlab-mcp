#!/bin/bash

# Set working directory
cd "$(dirname "$0")"

# Run the MCP server using uv
uv run -m transformerlab_mcp.server
