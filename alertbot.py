import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import requests

exchange = ccxt.binance()

bars = exchange.fetch_ohlcv('LUNA/USDT', timeframe='1m', limit=40)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

ema = ta.ema(df['close'],14)

df = pd.concat([df, adx,macd,rsi,ema], axis=1)

WEBHOOK_URL = "https://discord.com/api/webhooks/889265250875080725/nAh5DI_8uI6QDQYWW3GtQ4c1rUtK766mvDX9QTKyBseZiDOfMQR16iXGbPk--KGMY-Ts"

#print (df)


last_row = df.iloc[-1]

print(last_row)


emavalue = f"ema arvo {last_row['EMA_14']:.2f}"

rsivalue = f"rsi arvo {last_row['RSI_14']:.2f}"

message = (rsivalue +"    " +emavalue)

print(rsivalue)
print (emavalue)
print("viesti" , message)

payload = {
"username": "alertbot", 
"content": message
}

requests.post(WEBHOOK_URL, payload)


"""

WEBHOOK_URL = "https://discord.com/api/webhooks/889249553142927430/MaXiE0SJXnu50xNyAVbOXqRIQGBX86S8lkU6lzV3S21CEyQuldb-CJZdTW2a2fX3bNMze"

if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: The ADX is {last_row['ADX_14']:.2f}"
    if last_row['DMN_14'] > last_row['DMP_14']:
        message = f"STRONG DOWNTREND: The ADX is {last_row['ADX_14']:.2f}"

    payload = {
        "username": "Cryptobot",
        "content": message
    }

    requests.post(WEBHOOK_URL, json=payload)

if last_row['ADX_14'] < 25:
    message = f"NO TREND: The ADX is {last_row['ADX_14']:.2f}"

    payload = {
        "username": "alertbot",
        "content": message
    }

    requests.post(WEBHOOK_URL, json=payload)
"""