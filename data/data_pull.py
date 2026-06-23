import kagglehub
import pandas as pd

path = kagglehub.dataset_download("aleespinosa/apple-watch-and-fitbit-data")
df = pd.read_csv(f"{path}/aw_fb_data.csv")
print("Shape:", df.shape)
#column names
#print("Column Names:", df.columns.tolist())

print(df.head())
