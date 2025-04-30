#!/bin/bash

# Set working directory
cd "$(dirname "$0")"

# Install the package in development mode
uv pip install -e .
