# Evaluation Metrics

Your submission will be evaluated on the following metrics:

## 1. Accuracy Metrics (70% of total score)

### Specialty Classification (30%)
- **Metric**: Multi-class accuracy
- **Classes**: ["Cardiology", "Neurology", "Oncology", "Internal Medicine", "Emergency Medicine", "Other"]
- **Score**: Number of correct specialty predictions / Total number of reports

### Urgency Assessment (25%)
- **Metric**: Weighted F1-score
- **Classes**: ["Emergency", "Urgent", "Routine"]
- **Weights**: Emergency (0.4), Urgent (0.35), Routine (0.25)
- **Reasoning**: Higher weight on emergency cases due to their critical nature

### Follow-up Prediction (15%)
- **Metric**: Binary F1-score
- **Classes**: [True, False]
- **Score**: Harmonic mean of precision and recall for follow-up predictions

## 2. Performance Metrics (30% of total score)

### Processing Time (15%)
- **Metric**: Average processing time per report
- **Target**: < 1 second
- **Penalty**: -2% for each second over target
- **Maximum**: 5 seconds (submissions exceeding this will fail)

### Resource Usage (15%)
- **Memory Usage (7.5%)**
  - **Target**: < 512MB
  - **Penalty**: -1% for each 50MB over target
  - **Maximum**: 1GB

- **CPU Usage (7.5%)**
  - **Target**: < 50% average CPU utilization
  - **Penalty**: -1% for each 5% over target
  - **Maximum**: 90% (submissions exceeding this will fail)

## Scoring Example

```python
# Example scoring calculation
score = {
    'specialty_accuracy': 0.85,     # 85% correct
    'urgency_f1': 0.78,            # F1 score of 0.78
    'follow_up_f1': 0.90,          # F1 score of 0.90
    'avg_processing_time': 1.5,     # 1.5 seconds per report
    'max_memory_usage': 600,        # 600MB
    'avg_cpu_usage': 55            # 55% CPU utilization
}

# Calculate components
accuracy_score = (
    0.30 * score['specialty_accuracy'] +
    0.25 * score['urgency_f1'] +
    0.15 * score['follow_up_f1']
) * 100

# Calculate penalties
time_penalty = max(0, (score['avg_processing_time'] - 1.0) * 2)
memory_penalty = max(0, (score['max_memory_usage'] - 512) / 50)
cpu_penalty = max(0, (score['avg_cpu_usage'] - 50) / 5)

performance_score = 30 - (time_penalty + memory_penalty + cpu_penalty)

total_score = accuracy_score + performance_score
```

## Additional Notes

1. Your submission must process at least 95% of the test reports successfully to be considered valid
2. Any runtime errors or exceptions will result in a failed submission
3. Predictions must be in the exact format specified
4. The evaluation will be run multiple times and the average score will be used
