from pycoingecko import CoinGeckoAPI
import json

def get_price(coin_id):

    cg = CoinGeckoAPI()
    price = cg.get_price(ids=coin_id, vs_currencies='usd')
    return price[coin_id]['usd']




