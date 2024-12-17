# AI Arena - Medical Report Classification Challenge

Welcome to the Medical Report Classification Challenge! Your task is to develop an AI system that can accurately classify medical reports based on specialty, urgency, and follow-up needs.

## Challenge Overview

You need to implement a prediction system that can:
1. Determine the medical specialty most relevant to the report
2. Assess the urgency level of the case
3. Determine if follow-up care is needed

## Getting Started

1. Fork this repository
2. Implement your solution in `solution.py`
3. Push your changes to trigger evaluation

## Implementation Details

### Input Format
Your `predict` function will receive a dictionary with the following structure:
```python
{
    "report_id": str,          # Unique identifier for the report
    "content": str,            # Medical report text content
    "metadata": Dict[str, Any] # Additional metadata about the report
}
```

### Expected Output
Your function should return a dictionary with the following structure:
```python
{
    "specialty": str,     # One of: ["Cardiology", "Neurology", "Oncology", 
                         #          "Internal Medicine", "Emergency Medicine", "Other"]
    "urgency": str,      # One of: ["Emergency", "Urgent", "Routine"]
    "follow_up": bool    # Whether the patient needs follow-up care
}
```

## Evaluation

Your submission will be evaluated on:
1. **Accuracy**: How well your predictions match the ground truth
2. **Speed**: Processing time per report
3. **Resource Usage**: Memory and CPU efficiency

## Rules

1. You must implement your solution in the `predict` function in `solution.py`
2. Your implementation must be self-contained (no external API calls)
3. You can use any Python packages listed in `requirements.txt`
4. Your function must return predictions in the exact format specified
5. Processing time must not exceed 5 seconds per report

## Sample Implementation

```python
def predict(report):
    # Simple rule-based example
    content = report["content"].lower()
    
    # Detect emergency keywords
    if any(word in content for word in ["severe", "critical", "emergency"]):
        urgency = "Emergency"
    else:
        urgency = "Routine"
        
    # Detect specialty keywords
    if "heart" in content or "chest pain" in content:
        specialty = "Cardiology"
    else:
        specialty = "Internal Medicine"
        
    return {
        "specialty": specialty,
        "urgency": urgency,
        "follow_up": True if "follow" in content else False
    }
```

## Resources

- Sample reports in `examples/`
- Evaluation metrics in `metrics.md`
- Performance benchmarks in `benchmarks.md`

## Questions?

If you have any questions, please open an issue in this repository.
