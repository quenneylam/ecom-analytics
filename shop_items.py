import json
import requests
import pandas as pd


def get_shopid(file_path):
    df = pd.read_csv(file_path)
    return df.shopid.to_list()


def get_shop_items(shopid, data_df):
    r = requests.get(
        f'https://shopee.vn/api/v4/search/search_items?by=pop&entry_point=ShopByPDP&limit=100&match_id={shopid}&newest=0&order=desc&page_type=shop&pdp_l3cat=100290&scenario=PAGE_OTHERS&version=2')
    d = r.json()
    result = d['items']
    df = pd.DataFrame.from_dict(result)
    item = pd.DataFrame.from_records(df['item_basic'])
    itemdf = item[['itemid', 'shopid', 'name', 'stock', 'ctime',
                'historical_sold', 'liked_count', 'view_count', 'catid',
                'brand', 'cmt_count', 'price']]
    # 'item_rating.rating_star'
    # 'item_rating.rating_count','item_rating.rcount_with_context','item_rating.rcount_with_image']
    data_df = pd.concat([data_df, itemdf])
    return data_df



if __name__ == '__main__':
    id_list = get_shopid("C:/Users/ASUS/PycharmProjects/ecomview/table/shop_detail.csv")
    default_df = pd.DataFrame()
    for shopid in id_list:
        try:
            default_df = get_shop_items(shopid, default_df)
        except:
            pass
        #breakpoint()
    #print(default_df)
    default_df.to_csv('shop_items.csv')
