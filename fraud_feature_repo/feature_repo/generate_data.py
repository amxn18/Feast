import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
rows = []
base_time = datetime.now()

for user in range(1, 51): # 50 users
    for day in range(30): # 30 days
        rows.append({
            "user_id": user,
            "event_timestamp": base_time + timedelta(days=day),
            "transaction_amount": np.random.uniform(10, 1000),
            "is_fraud": np.random.choice([0, 1], p=[0.95, 0.05]) 
        })

df = pd.DataFrame(rows)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
rows = []
base_time = datetime.now()

for user in range(1, 51): # 50 users
    for day in range(30): # 30 days
        rows.append({
            "user_id": user,
            "event_timestamp": base_time + timedelta(days=day),
            "transaction_amount": np.random.uniform(10, 1000),
            "is_fraud": np.random.choice([0, 1], p=[0.95, 0.05]) 
        })

df = pd.DataFrame(rows)
df.to_parquet("data/transactions.parquet", index=False)
print("Data generated and saved to data/transactions.parquet")