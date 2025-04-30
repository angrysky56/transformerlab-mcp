#!/usr/bin/env python
"""
Transformerlab MCP Server

This MCP (Model Context Protocol) server provides an interface for AI assistants
to interact with Transformerlab functionality, including model management, 
training, dataset operations, and evaluations.
"""

from mcp.server.fastmcp import FastMCP
from transformerlab_client import TransformerLabClient
from typing import List, Dict, Any, Optional
import os
import json

# Initialize the MCP server
mcp = FastMCP("TransformerLabMCP")

# Create a client instance for Transformerlab
# Default URL is http://localhost:8338, but this can be configured
TRANSFORMERLAB_API_URL = os.environ.get("TRANSFORMERLAB_API_URL", "http://localhost:8338")
tlab_client = TransformerLabClient(base_url=TRANSFORMERLAB_API_URL)

# ----- Model Management Tools -----

@mcp.tool()
def list_models() -> List[Dict[str, Any]]:
    """
    List all available models in Transformerlab.
    
    Returns:
        A list of model information dictionaries.
    """
    try:
        models = tlab_client.list_models()
        return models
    except Exception as e:
        return [{"error": f"Failed to list models: {str(e)}"}]

@mcp.tool()
def get_model_info(model_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific model.
    
    Args:
        model_id: The ID of the model to retrieve information for.
        
    Returns:
        A dictionary containing model details.
    """
    try:
        model_info = tlab_client.get_model_info(model_id)
        return model_info
    except Exception as e:
        return {"error": f"Failed to get model info: {str(e)}"}

@mcp.tool()
def download_model(model_id: str) -> Dict[str, Any]:
    """
    Download a model from Hugging Face Hub to Transformerlab.
    
    Args:
        model_id: The Hugging Face model ID to download.
        
    Returns:
        A dictionary with the status of the download operation.
    """
    try:
        result = tlab_client.download_model(model_id)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ----- Training and Fine-tuning Tools -----

@mcp.tool()
def list_training_jobs() -> List[Dict[str, Any]]:
    """
    List all training jobs in Transformerlab.
    
    Returns:
        A list of training job information dictionaries.
    """
    try:
        jobs = tlab_client.list_training_jobs()
        return jobs
    except Exception as e:
        return [{"error": f"Failed to list training jobs: {str(e)}"}]

@mcp.tool()
def get_training_job_status(job_id: str) -> Dict[str, Any]:
    """
    Get the status of a specific training job.
    
    Args:
        job_id: The ID of the training job to check.
        
    Returns:
        A dictionary with the job status information.
    """
    try:
        status = tlab_client.get_training_job_status(job_id)
        return status
    except Exception as e:
        return {"error": f"Failed to get job status: {str(e)}"}

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
    try:
        config = {
            "model_id": model_id,
            "dataset_id": dataset_id,
            "output_name": output_name,
            "learning_rate": learning_rate,
            "num_epochs": num_epochs,
            "batch_size": batch_size
        }
        
        job_info = tlab_client.start_finetuning_job(config)
        return {"status": "success", "job_id": job_info.get("job_id"), "details": job_info}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def stop_training_job(job_id: str) -> Dict[str, Any]:
    """
    Stop a running training job.
    
    Args:
        job_id: The ID of the training job to stop.
        
    Returns:
        A dictionary with the result of the stop operation.
    """
    try:
        result = tlab_client.stop_training_job(job_id)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ----- Dataset Management Tools -----

@mcp.tool()
def list_datasets() -> List[Dict[str, Any]]:
    """
    List all available datasets in Transformerlab.
    
    Returns:
        A list of dataset information dictionaries.
    """
    try:
        datasets = tlab_client.list_datasets()
        return datasets
    except Exception as e:
        return [{"error": f"Failed to list datasets: {str(e)}"}]

@mcp.tool()
def get_dataset_info(dataset_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific dataset.
    
    Args:
        dataset_id: The ID of the dataset to retrieve information for.
        
    Returns:
        A dictionary containing dataset details.
    """
    try:
        dataset_info = tlab_client.get_dataset_info(dataset_id)
        return dataset_info
    except Exception as e:
        return {"error": f"Failed to get dataset info: {str(e)}"}

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
    try:
        result = tlab_client.import_huggingface_dataset(dataset_name, subset, split)
        return {"status": "success", "dataset_id": result.get("dataset_id"), "details": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ----- Evaluation Tools -----

@mcp.tool()
def list_evaluations() -> List[Dict[str, Any]]:
    """
    List all model evaluations in Transformerlab.
    
    Returns:
        A list of evaluation information dictionaries.
    """
    try:
        evaluations = tlab_client.list_evaluations()
        return evaluations
    except Exception as e:
        return [{"error": f"Failed to list evaluations: {str(e)}"}]

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
    try:
        config = {
            "model_id": model_id,
            "eval_name": eval_name,
            "eval_type": eval_type,
            "dataset_id": dataset_id
        }
        
        eval_info = tlab_client.start_evaluation(config)
        return {"status": "success", "eval_id": eval_info.get("eval_id"), "details": eval_info}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def get_evaluation_results(eval_id: str) -> Dict[str, Any]:
    """
    Get the results of a specific evaluation.
    
    Args:
        eval_id: The ID of the evaluation to get results for.
        
    Returns:
        A dictionary with the evaluation results.
    """
    try:
        results = tlab_client.get_evaluation_results(eval_id)
        return results
    except Exception as e:
        return {"error": f"Failed to get evaluation results: {str(e)}"}

# ----- RAG Tools -----

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
    try:
        if not os.path.exists(file_path):
            return {"status": "error", "message": f"File not found: {file_path}"}
        
        result = tlab_client.add_document_to_rag(file_path, collection_name)
        return {"status": "success", "document_id": result.get("document_id"), "details": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def list_rag_collections() -> List[Dict[str, Any]]:
    """
    List all RAG collections in Transformerlab.
    
    Returns:
        A list of RAG collection information dictionaries.
    """
    try:
        collections = tlab_client.list_rag_collections()
        return collections
    except Exception as e:
        return [{"error": f"Failed to list RAG collections: {str(e)}"}]

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
    try:
        config = {
            "query": query,
            "model_id": model_id,
            "collection_name": collection_name,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        response = tlab_client.rag_query(config)
        return {
            "status": "success", 
            "response": response.get("response"),
            "sources": response.get("sources", []),
            "details": response
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ----- Run the server -----

if __name__ == "__main__":
    print(f"Starting TransformerLab MCP Server - connecting to {TRANSFORMERLAB_API_URL}")
    mcp.run()
