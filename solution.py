from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def predict(report: str | Dict[str, Any]) -> Dict[str, Any]:
    """
    Predict specialty, urgency, and follow-up need for a medical report.
    
    Args:
        report: The medical report text, either as a string or a dictionary with a 'text' field
               If dictionary, should have format: {"text": str}
    
    Returns:
        Dictionary with predictions
            {
                "specialty": str,  # One of: ["cardiology", "endocrinology", "rheumatology", "neurology", "internal_medicine"]
                "urgency": str,    # One of: ["emergency", "urgent", "routine", "non_urgent"]
                "follow_up": str   # One of: ["required", "recommended", "scheduled"]
            }
    
    Example:
        >>> text = "Patient presents with severe chest pain and shortness of breath..."
        >>> predict(text)
        {
            "specialty": "cardiology",
            "urgency": "emergency",
            "follow_up": "required"
        }
        
        >>> report = {"text": "Patient presents with severe chest pain..."}
        >>> predict(report)
        {
            "specialty": "cardiology",
            "urgency": "emergency",
            "follow_up": "required"
        }
    """
    logger.info(f"Received report: {report}")
    logger.info(f"Report type: {type(report)}")
    
    # Handle both string and dictionary inputs
    if isinstance(report, dict):
        if 'text' not in report:
            raise ValueError("Dictionary input must have a 'text' field")
        text = report['text']
    else:
        text = report
    
    if not isinstance(text, str):
        raise ValueError(f"Text must be a string, got {type(text)}")
    
    # Convert to lowercase for case-insensitive matching
    text = text.lower()
    logger.info(f"Lowercase text: {text}")
    
    # Determine specialty based on keywords
    specialty = "internal_medicine"  # default
    if any(word in text for word in ["heart", "chest pain", "cardiac", "ecg", "ekg"]):
        specialty = "cardiology"
    elif any(word in text for word in ["diabetes", "thyroid", "hormone", "blood sugar"]):
        specialty = "endocrinology"
    elif any(word in text for word in ["joint", "arthritis", "inflammation"]):
        specialty = "rheumatology"
    elif any(word in text for word in ["brain", "neuro", "headache", "seizure"]):
        specialty = "neurology"
    logger.info(f"Determined specialty: {specialty}")
    
    # Determine urgency based on critical keywords
    urgency = "routine"  # default
    emergency_keywords = ["severe", "critical", "emergency", "immediate", "stat", "acute", "unstable"]
    urgent_keywords = ["urgent", "concerning", "worrisome", "deteriorating"]
    non_urgent_keywords = ["chronic", "stable", "mild", "moderate", "routine", "well-controlled"]
    
    if any(word in text for word in emergency_keywords):
        urgency = "emergency"
    elif any(word in text for word in urgent_keywords):
        urgency = "urgent"
    elif any(word in text for word in non_urgent_keywords):
        urgency = "non_urgent"
    else:
        urgency = "routine"
    logger.info(f"Determined urgency: {urgency}")
    
    # Determine if follow-up is needed
    follow_up = "recommended"  # default
    required_keywords = ["immediate", "required", "critical", "severe", "emergency"]
    scheduled_keywords = ["schedule", "routine", "well-controlled", "continue"]
    
    if any(word in text for word in required_keywords):
        follow_up = "required"
    elif any(word in text for word in scheduled_keywords):
        follow_up = "scheduled"
    logger.info(f"Determined follow-up: {follow_up}")
    
    result = {
        "specialty": specialty,
        "urgency": urgency,
        "follow_up": follow_up
    }
    logger.info(f"Returning result: {result}")
    return result
