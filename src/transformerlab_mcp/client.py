"""
Transformerlab Client Wrapper

This module provides a wrapper around the Transformerlab client to handle
exceptions and provide consistent error handling.
"""

import os
import logging
from typing import Any, Dict, List, Optional, Union

# Import the correct client class from the transformerlab_client package
from transformerlab_client.client import TransformerLabClient

logger = logging.getLogger(__name__)

class TransformerLabWrapper:
    """
    Wrapper around TransformerLabClient with consistent error handling.
    """
    
    def __init__(self, server_url: Optional[str] = None):
        """
        Initialize the Transformerlab client wrapper.
        
        Args:
            server_url: Optional URL to the Transformerlab API. 
                      If not provided, uses the TRANSFORMERLAB_API_URL
                      environment variable, defaulting to http://localhost:8338.
        """
        self.server_url = server_url or os.environ.get(
            "TRANSFORMERLAB_API_URL", "http://localhost:8338"
        )
        self.client = TransformerLabClient(server_url=self.server_url)
        logger.info(f"Initialized Transformerlab client at {self.server_url}")
    
    def _handle_request(self, func_name: str, *args, **kwargs) -> Dict[str, Any]:
        """
        Wrapper to handle requests with standardized error handling.
        
        Args:
            func_name: The name of the function to call on the client.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.
            
        Returns:
            The result of the function call, or an error dictionary.
        """
        try:
            func = getattr(self.client, func_name)
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Error in {func_name}: {str(e)}", exc_info=True)
            return {"error": f"Failed in {func_name}: {str(e)}"}
    
    # Model Management Methods
    
    def list_models(self) -> Union[List[Dict[str, Any]], Dict[str, str]]:
        """List all available models."""
        return self._handle_request("list_models")
    
    def get_model_info(self, model_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific model."""
        return self._handle_request("get_model_info", model_id)
    
    def download_model(self, model_id: str) -> Dict[str, Any]:
        """Download a model from Hugging Face Hub."""
        return self._handle_request("download_model", model_id)
    
    # Training and Fine-tuning Methods
    
    def list_training_jobs(self) -> Union[List[Dict[str, Any]], Dict[str, str]]:
        """List all training jobs."""
        return self._handle_request("list_training_jobs")
    
    def get_training_job_status(self, job_id: str) -> Dict[str, Any]:
        """Get the status of a specific training job."""
        return self._handle_request("get_training_job_status", job_id)
    
    def start_finetuning_job(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Start a fine-tuning job."""
        return self._handle_request("start_finetuning_job", config)
    
    def stop_training_job(self, job_id: str) -> Dict[str, Any]:
        """Stop a running training job."""
        return self._handle_request("stop_training_job", job_id)
    
    # Dataset Management Methods
    
    def list_datasets(self) -> Union[List[Dict[str, Any]], Dict[str, str]]:
        """List all available datasets."""
        return self._handle_request("list_datasets")
    
    def get_dataset_info(self, dataset_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific dataset."""
        return self._handle_request("get_dataset_info", dataset_id)
    
    def import_huggingface_dataset(
        self, dataset_name: str, subset: Optional[str] = None, split: str = "train"
    ) -> Dict[str, Any]:
        """Import a dataset from Hugging Face Hub."""
        return self._handle_request(
            "import_huggingface_dataset", dataset_name, subset, split
        )
    
    # Evaluation Methods
    
    def list_evaluations(self) -> Union[List[Dict[str, Any]], Dict[str, str]]:
        """List all model evaluations."""
        return self._handle_request("list_evaluations")
    
    def start_evaluation(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Start a model evaluation job."""
        return self._handle_request("start_evaluation", config)
    
    def get_evaluation_results(self, eval_id: str) -> Dict[str, Any]:
        """Get the results of a specific evaluation."""
        return self._handle_request("get_evaluation_results", eval_id)
    
    # RAG Methods
    
    def add_document_to_rag(
        self, file_path: str, collection_name: str = "default"
    ) -> Dict[str, Any]:
        """Add a document to the RAG system."""
        return self._handle_request("add_document_to_rag", file_path, collection_name)
    
    def list_rag_collections(self) -> Union[List[Dict[str, Any]], Dict[str, str]]:
        """List all RAG collections."""
        return self._handle_request("list_rag_collections")
    
    def rag_query(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Perform a RAG query."""
        return self._handle_request("rag_query", config)
