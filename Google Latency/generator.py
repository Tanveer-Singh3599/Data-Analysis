import numpy as np
import pandas as pd

np.random.seed(42)
N = 100_000

latency = pd.DataFrame({
    "request_id": np.arange(N),
    "region": np.random.choice(["US","EU","ASIA"], p=[0.45,0.35,0.20], size=N),
    "device_type": np.random.choice(["mobile","desktop"], p=[0.7,0.3], size=N),
    "variant": np.random.choice(["control","treatment"], size=N)
})

# Base latency (infra normal behavior)
base = np.random.normal(90, 12, int(N*0.88))

# Tail latency (network congestion, cold cache, failures)
tail = np.random.normal(280, 60, int(N*0.12))

latency_vals = np.concatenate([base, tail])
np.random.shuffle(latency_vals)

latency["latency_ms"] = latency_vals

# Inject treatment effect (infra optimization)
latency.loc[latency["variant"]=="treatment", "latency_ms"] *= 0.96

latency.to_csv("dataset.csv", index=False)