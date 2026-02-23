from feast import FeatureStore
import joblib
import pandas as pd

# Connect to feature store
store = FeatureStore(repo_path=".")

# Load trained model
model = joblib.load("fraud_model.pkl")

# Simulate incoming request
entity_rows = [{"user_id": 1}]

# Retrieve online features
online_features = store.get_online_features(
    features=[
        "user_transaction_features:transaction_amount",
    ],
    entity_rows=entity_rows,
).to_df()

print("Retrieved Online Features:")
print(online_features)

# Predict
prediction = model.predict(online_features[["transaction_amount"]])

print("Prediction (1 = Fraud, 0 = Not Fraud):", prediction[0])