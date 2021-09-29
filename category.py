import requests
import json
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np

# Get all Category

# https://shopee.vn/api/v2/category_list/get

r = requests.get(f'https://shopee.vn/api/v2/category_list/get')
d = r.json()
all_category = d['data']['category_list']
category_df = pd.DataFrame(all_category)
category_df = category_df[['display_name', 'catid']]
category_df.to_csv('categories_list.csv', index=False)
#print(category_df)
