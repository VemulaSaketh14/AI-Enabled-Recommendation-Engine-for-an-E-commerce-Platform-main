import pandas as pd
import numpy as np

data = pd.read_csv("clean_data.csv")

# 
data['ProdID'] = data['ProdID'].replace('-2147483648', np.nan)
data["User's ID"] = data["User's ID"].replace('-2147483648', np.nan)

data = data.dropna(subset=["User's ID"])
data["User's ID"] = data["User's ID"].astype('int64')

data = data.dropna(subset=['ProdID'])
data['ProdID'] = data['ProdID'].astype('int64')

data['Review Count'] = data['Review Count'].astype('int64')

data['Category'] = data['Category'].fillna('')
data['Brand'] = data['Brand'].fillna('')
data['Description'] = data['Description'].fillna('')
data['Tags'] = data['Tags'].fillna('')

# To clean image data by choose only first URL before the '|'
if 'ImageURL' in data.columns:
    data['ImageURL'] = data['ImageURL'].fillna('').apply(lambda x: str(x).split('|')[0] if pd.notnull(x) else x)
elif 'Image URL' in data.columns:
    data['Image URL'] = data['Image URL'].fillna('').apply(lambda x: str(x).split('|')[0] if pd.notnull(x) else x)

data.to_csv("cleaned_data.csv", index=False)
