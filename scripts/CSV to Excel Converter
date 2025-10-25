import pandas as pd
import os

folder_path = "path/to/csvs"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder_path, file))
        df.to_excel(os.path.join(folder_path, file.replace(".csv", ".xlsx")), index=False)
        print(f"Converted: {file}")
