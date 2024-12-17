from typing import Dict, Any

def predict(report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Predict medical report classifications including specialty, urgency, and follow-up need.
    
    Args:
        report: Dictionary containing report data with the following structure:
            {
                "report_id": str,          # Unique identifier for the report
                "content": str,            # Medical report text content
                "metadata": Dict[str, Any] # Additional metadata about the report
            }
    
    Returns:
        Dictionary containing predictions with the following structure:
            {
                "specialty": str,     # One of: ["Cardiology", "Neurology", "Oncology", 
                                     #          "Internal Medicine", "Emergency Medicine", "Other"]
                "urgency": str,       # One of: ["Emergency", "Urgent", "Routine"]
                "follow_up": bool     # Whether the patient needs follow-up care
            }
    
    Example:
        >>> report = {
        ...     "report_id": "12345",
        ...     "content": "Patient presents with severe chest pain and shortness of breath...",
        ...     "metadata": {"age": 65, "gender": "M"}
        ... }
        >>> predict(report)
        {
            "specialty": "Cardiology",
            "urgency": "Emergency",
            "follow_up": True
        }
    """
    # Your implementation here
    # Feel free to use any machine learning models or rule-based systems
    # Just ensure your predictions match the expected format
    
    return {
        "specialty": "Internal Medicine",  # Default prediction
        "urgency": "Routine",             # Default prediction
        "follow_up": False                # Default prediction
    }
