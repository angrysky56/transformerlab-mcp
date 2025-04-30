"""
RAG Tools for Transformerlab MCP

Provides MCP tools for Retrieval-Augmented Generation (RAG).
"""

import os
from typing import Dict, List, Any
from mcp.server.fastmcp import FastMCP


def register_rag_tools(mcp: FastMCP, client) -> None:
    """
    Register RAG-related tools with the MCP server.
    
    Args:
        mcp: The MCP server instance.
        client: The Transformerlab client wrapper.
    """
    
    @mcp.tool()
    def add_document_to_rag(
        file_path: str,
        collection_name: str = "default"
    ) -> Dict[str, Any]:
        """
        Add a document to the RAG system in Transformerlab.
        
        Args:
            file_path: The path to the document file.
            collection_name: The name of the RAG collection to add the document to.
            
        Returns:
            A dictionary with the result of the operation.
        """
        if not os.path.exists(file_path):
            return {"status": "error", "message": f"File not found: {file_path}"}
        
        result = client.add_document_to_rag(file_path, collection_name)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "document_id": result.get("document_id", ""), "details": result}

    @mcp.tool()
    def list_rag_collections() -> List[Dict[str, Any]]:
        """
        List all RAG collections in Transformerlab.
        
        Returns:
            A list of RAG collection information dictionaries.
        """
        return client.list_rag_collections()

    @mcp.tool()
    def rag_query(
        query: str,
        model_id: str,
        collection_name: str = "default",
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> Dict[str, Any]:
        """
        Perform a RAG query using a specific model and collection.
        
        Args:
            query: The query text.
            model_id: The ID of the model to use for generation.
            collection_name: The name of the RAG collection to search.
            temperature: The temperature for generation.
            max_tokens: The maximum number of tokens to generate.
            
        Returns:
            A dictionary with the RAG response.
        """
        config = {
            "query": query,
            "model_id": model_id,
            "collection_name": collection_name,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        result = client.rag_query(config)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {
            "status": "success", 
            "response": result.get("response", ""),
            "sources": result.get("sources", []),
            "details": result
        }
