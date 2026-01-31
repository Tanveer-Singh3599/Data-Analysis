import numpy as np
import pandas as pd

np.random.seed(42)

def generate_food_delivery(n=50):
    df = pd.DataFrame({
        "order_id": np.arange(1000, 1000+n),
        "estimated_time_min": np.random.randint(25, 50, n),
        "distance_km": np.round(np.random.uniform(1, 12, n), 1),
        "order_hour": np.random.randint(9, 23, n),
        "weather_condition": np.random.choice(["Clear", "Cloudy", "Rainy", "Storm"], n, p=[0.4,0.3,0.2,0.1]),
        "restaurant_rating": np.round(np.random.uniform(3.2, 4.9, n), 1),
        "is_festival": np.random.choice([0,1], n, p=[0.75,0.25])
    })

    noise = np.random.normal(0, 5, n)
    df["delivery_time_min"] = (
        df["estimated_time_min"]
        + df["distance_km"] * 2
        + df["is_festival"] * 12
        + (df["weather_condition"] == "Rainy") * 8
        + (df["weather_condition"] == "Storm") * 15
        + noise
    ).astype(int)

    # 🔥 Leakage: post-delivery KPI
    df["actual_delay_flag"] = (df["delivery_time_min"] > df["estimated_time_min"]).astype(int)

    return df

food_delivery = generate_food_delivery()

food_delivery.to_csv("food_delivery.csv", index=False)