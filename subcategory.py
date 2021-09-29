import requests
import json
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
#import plotly.express as px
from bs4 import BeautifulSoup

# Read file
with open('C:/Users/ASUS/PycharmProjects/ecomview/data/subcat_list.html','r', encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
cat_list = []

for cat in soup.find_all('a', class_="_2xdbPh"):
     cat_dict = {
            'catid' : cat.get('href')[-8:],
            'subcat_name' : cat.string,
            'subcat_link' : 'https://shopee.vn'+ cat.get('href')
     }
     cat_list.append(cat_dict)
#cat_list
cat_df = pd.DataFrame(cat_list)
#cat_df
subcat_list = []
for subcat in soup.find_all('a',class_="_12uvse"):
    subcat_dict = {
            'catid' : subcat.get('href')[-17:-9],
            'subcatid' : subcat.get('href')[-8:],
            'subcat_name' : subcat.string,
            'subcat_link' : 'https://shopee.vn'+ subcat.get('href')
    }
    subcat_list.append(subcat_dict)
#subcat_list
subcat_df = pd.DataFrame(subcat_list)
#subcat_df
cat = pd.merge(  cat_df,subcat_df , on ='catid', how ='inner')
#cat
#cat.columns
cat.rename(columns={"subcat_name_x": "cat_name", "subcat_link_x": "cat_link",'subcat_name_y':'subcat_name','subcat_link_y':'subcat_link'})
#cat.to_csv('cat_table.csv',index=False)
print(cat)