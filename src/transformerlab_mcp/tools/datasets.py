"""
Dataset Management Tools for Transformerlab MCP

Provides MCP tools for listing, importing, and managing datasets.
"""

from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP


def register_dataset_tools(mcp: FastMCP, client) -> None:
    """
    Register dataset-related tools with the MCP server.
    
    Args:
        mcp: The MCP server instance.
        client: The Transformerlab client wrapper.
    """
    
    @mcp.tool()
    def list_datasets() -> List[Dict[str, Any]]:
        """
        List all available datasets in Transformerlab.
        
        Returns:
            A list of dataset information dictionaries.
        """
        return client.list_datasets()

    @mcp.tool()
    def get_dataset_info(dataset_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific dataset.
        
        Args:
            dataset_id: The ID of the dataset to retrieve information for.
            
        Returns:
            A dictionary containing dataset details.
        """
        return client.get_dataset_info(dataset_id)

    @mcp.tool()
    def import_huggingface_dataset(
        dataset_name: str, 
        subset: Optional[str] = None,
        split: str = "train"
    ) -> Dict[str, Any]:
        """
        Import a dataset from Hugging Face Hub to Transformerlab.
        
        Args:
            dataset_name: The name of the Hugging Face dataset.
            subset: Optional subset of the dataset.
            split: The split to use (train, test, validation).
            
        Returns:
            A dictionary with information about the imported dataset.
        """
        result = client.import_huggingface_dataset(dataset_name, subset, split)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "dataset_id": result.get("dataset_id", ""), "details": result}
