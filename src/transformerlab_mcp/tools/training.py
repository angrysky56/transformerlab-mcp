"""
Training Tools for Transformerlab MCP

Provides MCP tools for training and fine-tuning models.
"""

from typing import Dict, List, Any
from mcp.server.fastmcp import FastMCP


def register_training_tools(mcp: FastMCP, client) -> None:
    """
    Register training-related tools with the MCP server.
    
    Args:
        mcp: The MCP server instance.
        client: The Transformerlab client wrapper.
    """
    
    @mcp.tool()
    def list_training_jobs() -> List[Dict[str, Any]]:
        """
        List all training jobs in Transformerlab.
        
        Returns:
            A list of training job information dictionaries.
        """
        return client.list_training_jobs()

    @mcp.tool()
    def get_training_job_status(job_id: str) -> Dict[str, Any]:
        """
        Get the status of a specific training job.
        
        Args:
            job_id: The ID of the training job to check.
            
        Returns:
            A dictionary with the job status information.
        """
        return client.get_training_job_status(job_id)

    @mcp.tool()
    def start_finetuning(
        model_id: str, 
        dataset_id: str, 
        output_name: str,
        learning_rate: float = 3e-4,
        num_epochs: int = 3,
        batch_size: int = 8
    ) -> Dict[str, Any]:
        """
        Start a fine-tuning job in Transformerlab.
        
        Args:
            model_id: The ID of the base model to fine-tune.
            dataset_id: The ID of the dataset to use for fine-tuning.
            output_name: The name to give to the fine-tuned model.
            learning_rate: The learning rate for fine-tuning.
            num_epochs: The number of training epochs.
            batch_size: The batch size for training.
            
        Returns:
            A dictionary with information about the created fine-tuning job.
        """
        config = {
            "model_id": model_id,
            "dataset_id": dataset_id,
            "output_name": output_name,
            "learning_rate": learning_rate,
            "num_epochs": num_epochs,
            "batch_size": batch_size
        }
        
        result = client.start_finetuning_job(config)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "job_id": result.get("job_id", ""), "details": result}

    @mcp.tool()
    def stop_training_job(job_id: str) -> Dict[str, Any]:
        """
        Stop a running training job.
        
        Args:
            job_id: The ID of the training job to stop.
            
        Returns:
            A dictionary with the result of the stop operation.
        """
        result = client.stop_training_job(job_id)
        if "error" in result:
            return {"status": "error", "message": result["error"]}
        return {"status": "success", "result": result}
