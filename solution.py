from typing import Dict, Any

def predict(report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Predict specialty, urgency, and follow-up need for a medical report.
    
    Args:
        report: Dictionary containing report data
            {
                "report_id": str,
                "content": str,
                "metadata": Dict[str, Any]
            }
    
    Returns:
        Dictionary with predictions
            {
                "specialty": str,
                "urgency": str,
                "follow_up": bool
            }
    """
    # Extract the report content
    content = report["content"].lower()
    
    # Simple keyword-based classification
    
    # Determine specialty
    specialty = "general"
    if "heart" in content or "cardiac" in content:
        specialty = "cardiology"
    elif "brain" in content or "neuro" in content:
        specialty = "neurology"
    elif "bone" in content or "fracture" in content:
        specialty = "orthopedics"
    
    # Determine urgency
    urgency = "routine"
    urgent_keywords = ["emergency", "urgent", "critical", "severe", "immediately"]
    if any(keyword in content for keyword in urgent_keywords):
        urgency = "urgent"
    
    # Determine follow-up need
    follow_up = False
    follow_up_keywords = ["follow up", "follow-up", "return", "check again", "monitor"]
    if any(keyword in content for keyword in follow_up_keywords):
        follow_up = True
    
    return {
        "specialty": specialty,
        "urgency": urgency,
        "follow_up": follow_up
    }
