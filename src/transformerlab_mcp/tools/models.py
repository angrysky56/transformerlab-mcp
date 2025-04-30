"""
Model Management Tools for Transformerlab MCP

Provides MCP tools for listing, downloading, and managing models.
"""

from typing import Dict, List, Any
from mcp.server.fastmcp import FastMCP


def register_model_tools(mcp: FastMCP, client) -> None:
    """
    Register model-related tools with the MCP server.
    
    Args:
        mcp: The MCP server instance.
        client: The Transformerlab client wrapper.
    """
    
    @mcp.tool()
    def list_models() -> List[Dict[str, Any]]:
        """
        List all available models in Transformerlab.
        
        Returns:
            A list of model information dictionaries.
        """
        return client.list_models()

    @mcp.tool()
    def get_model_info(model_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific model.
        
        Args:
            model_id: The ID of the model to retrieve information for.
            
        Returns:
            A dictionary containing model details.
        """
        return client.get_model_info(model_id)

    @mcp.tool()
    def download_model(model_id: str) -> Dict[str, Any]:
        """
        Download a model from Hugging Face Hub to Transformerlab.
        
        Args:
            model_id: The Hugging Face model ID to download.
            
        Returns:
            A dictionary with the status of the download operation.
        """
        result = client.download_model(model_id)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "result": result}
