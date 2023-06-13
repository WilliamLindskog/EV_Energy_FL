import json
import pandas as pd

df = pd.read_csv('./data/fever.csv')

# Drop fuel_date
df = df.drop(['fuel_date'], axis=1)

# Encode all object columns
# Store cat codes and its corresponding categories
cat_codes = {}
for col in df.columns:
    if df[col].dtypes == 'object':
        df[col] = df[col].astype('category')
        cat_codes[col] = dict(enumerate(df[col].cat.categories))
        df[col] = df[col].cat.codes

# Save cat codes
with open('./data/cat_codes.json', 'w') as f: 
    json.dump(cat_codes, f)

# put quantity(kWh) as first column
cols = list(df.columns)
cols.insert(0, cols.pop(cols.index('quantity(kWh)')))
df = df[cols]

# Save encoded data
df.to_csv('./data/fever_encoded.csv', index=False, header=False)
