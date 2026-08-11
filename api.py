import requests

def get_crypto(crypto_id):

  url = "https://api.coingecko.com/api/v3/coins/markets"

  params = {
    "vs_currency": "usd",
    "ids": crypto_id
  }

  try:
    response = requests.get(url, params= params, timeout= 10)
    response.raise_for_status()

    data = response.json()

    if not data:
      return None
    
    crypto = data[0]

    return{
       "name" : crypto["name"],
       "symbol" : crypto["symbol"],
       "price" : crypto["current_price"],
       "market Cap" : crypto["market_cap"],
       "24h change" : crypto["price_change_percentage_24h"]
    }
  except requests.exceptions.RequestException:
    return None
