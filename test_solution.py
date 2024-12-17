from sample_solution import predict

def test_cardiology_case():
    report = {
        "report_id": "test1",
        "content": "Patient presents with chest pain and irregular heart rhythm.",
        "metadata": {}
    }
    result = predict(report)
    assert result["specialty"] == "cardiology"
    assert result["urgency"] == "routine"
    assert result["follow_up"] == False

def test_urgent_case():
    report = {
        "report_id": "test2",
        "content": "Emergency: Severe neuro trauma with loss of consciousness. Urgent CT scan needed.",
        "metadata": {}
    }
    result = predict(report)
    assert result["specialty"] == "neurology"
    assert result["urgency"] == "urgent"
    assert result["follow_up"] == False

def test_follow_up_case():
    report = {
        "report_id": "test3",
        "content": "Fractured wrist healing well. Patient should follow up in 2 weeks for repeat X-ray.",
        "metadata": {}
    }
    result = predict(report)
    assert result["specialty"] == "orthopedics"
    assert result["urgency"] == "routine"
    assert result["follow_up"] == True

if __name__ == "__main__":
    test_cardiology_case()
    test_urgent_case()
    test_follow_up_case()
    print("All tests passed!")
