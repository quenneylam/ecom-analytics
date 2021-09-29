import json
import requests
import pandas as pd


def get_username(file_path):
    df = pd.read_csv(file_path)
    return df.username.to_list()


def get_shop_details(username, data_df):
    r = requests.get(f'https://shopee.vn/api/v4/shop/get_shop_detail?username={username}')
    d = r.json()
    df = pd.json_normalize(d['data'])
    df = df[["account.username", "shopid", "mtime",
             "country", "rating_normal", "rating_bad", "rating_good",
             "description", "rating_star", "item_count",
             "follower_count", "response_rate", "shop_location"]]
    data_df = pd.concat([data_df, df])
    return data_df


if __name__ == '__main__':
    usernames = get_username("C:/Users/ASUS/PycharmProjects/ecomview/table/cat_shops.csv")
    default_df = pd.DataFrame()
    for username in usernames:
        try:
            default_df = get_shop_details(username, default_df)
        except:
            pass
        #breakpoint()
    #print(default_df)
    default_df.to_csv('shop_detail.csv')
