import joblib

from app.ml.feature_extractor import (
    extract_features
)

saved = joblib.load(
    "app/ml/model.pkl"
)

model = saved["model"]

encoder = saved["encoder"]


def predict_url(url):

    features = extract_features(url)

    prediction = model.predict(
        [features]
    )[0]

    probabilities = model.predict_proba(
        [features]
    )[0]

    confidence = max(probabilities) * 100

    predicted_label = encoder.inverse_transform(
        [prediction]
    )[0]

    # SAFE ONLY FOR BENIGN
    if predicted_label == "benign":
        final_prediction = "safe"
    else:
        final_prediction = "phishing"

    return {
        "prediction": final_prediction,
        "confidence": round(
            float(confidence),
            2
        )
    }
