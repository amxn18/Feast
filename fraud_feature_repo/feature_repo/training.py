from feast import FeatureStore
import pandas as pd
from sklearn.linear_model import LogisticRegression
from feast import FeatureStore
from sklearn.metrics import classification_report
import joblib

# 1) Connect to the feature store
store = FeatureStore(repo_path=".")

# 2) Load Raw data
df = pd.read_parquet("data/transactions.parquet")

# 3) Create an entity dataframe for historical features retrieval
entity_df = df[["user_id", "event_timestamp", "is_fraud"]]

# 4) Retrieve historical features for training
trainingData = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_transaction_features:transaction_amount",
    ],
).to_df()

print(trainingData.head())
print("Total rows:", len(trainingData))

# 5) Model training
X = trainingData[["transaction_amount"]]
y = trainingData["is_fraud"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Evaluate quickly
preds = model.predict(X)
print(classification_report(y, preds))

# Save model
joblib.dump(model, "fraud_model.pkl")

print("Model trained and saved.")