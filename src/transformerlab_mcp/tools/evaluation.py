"""
Evaluation Tools for Transformerlab MCP

Provides MCP tools for evaluating models.
"""

from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP


def register_evaluation_tools(mcp: FastMCP, client) -> None:
    """
    Register evaluation-related tools with the MCP server.
    
    Args:
        mcp: The MCP server instance.
        client: The Transformerlab client wrapper.
    """
    
    @mcp.tool()
    def list_evaluations() -> List[Dict[str, Any]]:
        """
        List all model evaluations in Transformerlab.
        
        Returns:
            A list of evaluation information dictionaries.
        """
        return client.list_evaluations()

    @mcp.tool()
    def start_evaluation(
        model_id: str,
        eval_name: str,
        eval_type: str = "basic",
        dataset_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Start a model evaluation job in Transformerlab.
        
        Args:
            model_id: The ID of the model to evaluate.
            eval_name: The name to give to this evaluation.
            eval_type: The type of evaluation (basic, comprehensive, custom).
            dataset_id: Optional dataset ID to use for evaluation.
            
        Returns:
            A dictionary with information about the created evaluation job.
        """
        config = {
            "model_id": model_id,
            "eval_name": eval_name,
            "eval_type": eval_type
        }
        
        if dataset_id:
            config["dataset_id"] = dataset_id
        
        result = client.start_evaluation(config)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "eval_id": result.get("eval_id", ""), "details": result}

    @mcp.tool()
    def get_evaluation_results(eval_id: str) -> Dict[str, Any]:
        """
        Get the results of a specific evaluation.
        
        Args:
            eval_id: The ID of the evaluation to get results for.
            
        Returns:
            A dictionary with the evaluation results.
        """
        return client.get_evaluation_results(eval_id)
