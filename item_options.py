import json
import requests
import pandas as pd


def get_param(file_path):
    df = pd.read_csv(file_path)
    return list(zip(df.itemid, df.shopid))


def get_item_options(itemid, shopid, data_df):
    r = requests.get('https://shopee.vn/api/v2/item/get',
                     params={'itemid': {itemid}, 'shopid': {shopid}},
                     headers={'User-Agent': 'Google/1.0'})
    '''
    r.raise_for_status()
    if (
            r.status_code != 204 and
            r.headers["content-type"].strip().startswith("application/json")
    ):
        try:
            d = r.json()
        except ValueError:
            print('2121')
            pass
    #print(d)
    '''
    d = r.json()
    data = d['item']['models']
    option_df = pd.DataFrame(data)
    option_df = option_df[['itemid', 'modelid', 'name', 'price', 'sold']]
    data_df = pd.concat([data_df, option_df])
    return data_df


if __name__ == '__main__':
    param_list = get_param("C:/Users/ASUS/PycharmProjects/ecomview/table/shop_items.csv")

    default_df = pd.DataFrame()
    for (item_id, shopid) in param_list:
        try:
            default_df = get_item_options(item_id, shopid, default_df)
        except:
            pass
    print(default_df)
    #default_df.to_csv('item_options.csv')
