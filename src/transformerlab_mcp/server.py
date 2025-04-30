"""
Transformerlab MCP Server

Main module that initializes and runs the MCP server for Transformerlab.
"""

import os
import logging
from mcp.server.fastmcp import FastMCP

# Import the client wrapper
from transformerlab_mcp.client import TransformerLabWrapper

# Import tool registration functions
from transformerlab_mcp.tools.models import register_model_tools
from transformerlab_mcp.tools.datasets import register_dataset_tools
from transformerlab_mcp.tools.training import register_training_tools
from transformerlab_mcp.tools.evaluation import register_evaluation_tools
from transformerlab_mcp.tools.rag import register_rag_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("transformerlab_mcp")


def create_server():
    """
    Create and configure the MCP server with all tools.
    
    Returns:
        The configured MCP server instance.
    """
    # Initialize the MCP server
    mcp = FastMCP("TransformerLabMCP")
    
    # Get Transformerlab API URL from environment
    transformerlab_api_url = os.environ.get("TRANSFORMERLAB_API_URL", "http://localhost:8338")
    
    # Initialize the client wrapper
    client = TransformerLabWrapper(server_url=transformerlab_api_url)
    logger.info(f"Connecting to Transformerlab API at {transformerlab_api_url}")
    
    # Register all tools
    register_model_tools(mcp, client)
    register_dataset_tools(mcp, client)
    register_training_tools(mcp, client)
    register_evaluation_tools(mcp, client)
    register_rag_tools(mcp, client)
    
    logger.info("All Transformerlab MCP tools registered")
    return mcp


def main():
    """
    Main entry point for running the MCP server.
    """
    logger.info("Starting Transformerlab MCP Server")
    server = create_server()
    server.run()


if __name__ == "__main__":
    main()
