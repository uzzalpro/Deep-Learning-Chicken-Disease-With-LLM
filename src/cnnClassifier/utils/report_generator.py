def generate_health_report(prediction, llm_text):
    report = {
        "disease_prediction": prediction,
        "ai_explanation": llm_text,
    }
    return report