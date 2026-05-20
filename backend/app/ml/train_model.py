import pandas as pd

import joblib

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    classification_report
)

from sklearn.preprocessing import (
    LabelEncoder
)

from xgboost import XGBClassifier

from app.ml.feature_extractor import (
    extract_features
)


# LOAD DATASET
df = pd.read_csv(
    "dataset/urls.csv"
)

# CLEAN
df = df.dropna()

# FEATURES
X = df["url"].apply(
    extract_features
).tolist()

# LABELS
y = df["type"]

# ENCODE LABELS
encoder = LabelEncoder()

y = encoder.fit_transform(y)

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
)

# MODEL
model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    eval_metric="mlogloss"
)

# TRAIN
model.fit(
    X_train,
    y_train
)

# TEST
y_pred = model.predict(
    X_test
)

print(
    classification_report(
        y_test,
        y_pred
    )
)

# SAVE MODEL
joblib.dump(
    {
        "model": model,
        "encoder": encoder
    },
    "app/ml/model.pkl"
)

print(
    "MODEL TRAINED SUCCESSFULLY"
)
