from feast import Entity, FeatureView, Field
from feast.value_type import ValueType
from feast.types import Float64
from feast.infra.offline_stores.file_source import FileSource
from datetime import timedelta

# Entity Definition
user = Entity(
    name="user",
    join_keys=["user_id"],
    value_type=ValueType.INT64,
)

# Data Source
transactions_source = FileSource(   # Tells feast where the offline data is present
    path="data/transactions.parquet",
    timestamp_field="event_timestamp", # Enables point in time joins
)

# Feature View
user_transaction_features = FeatureView(
    name="user_transaction_features",
    entities=[user],
    ttl=timedelta(days=7),
    schema=[
        Field(name="transaction_amount", dtype=Float64),
    ],
    source=transactions_source,
)