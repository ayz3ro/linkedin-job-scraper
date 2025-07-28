import os

import pandas as pd


def save_to_csv(data, filename="linkedin_jobs.csv", folder="data"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False, encoding="utf-8")
    print(f"✅ Saved {len(df)} jobs to {path}")
