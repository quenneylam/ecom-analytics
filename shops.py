import json
import requests
import pandas as pd
import time


def get_catid(file_path):
    cat_df = pd.read_csv(file_path)
    return cat_df.catid.to_list()


def get_shop_info(category_id, data_df):
    r = requests.get(
        f'https://shopee.vn/api/v4/official_shop/get_shops_by_category?need_zhuyin=0&category_id={category_id}')
    d = r.json()
    df = pd.DataFrame(d['data']['brands'])
    shop_df = pd.DataFrame()
    for index, row in df.iterrows():
        for x in row['brand_ids']:
            dict1 = {'id': x['shopid'],
                     'name': x['brand_name'],
                     'username': x['username'],
                     'catid': category_id
                     }
            shop_df = shop_df.append(dict1, ignore_index=True)
    data_df = pd.concat([data_df, shop_df])
    return data_df



if __name__ == '__main__':
    catid_list = get_catid("C:/Users/ASUS/PycharmProjects/ecomview/table/categories_list.csv")

    time.sleep(1)

    default_df = pd.DataFrame()
    for id in catid_list:
        try:
            default_df = get_shop_info(id, default_df)
        except:
            pass
        # breakpoint()
    print(default_df)
    default_df.to_csv('cat_shops.csv')
