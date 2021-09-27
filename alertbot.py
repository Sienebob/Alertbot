import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import requests
import datetime

#asetetaan haluttu exchange, pari, aikaväli ja kuinka monta askelta taakse katsotaan.
exchange = ccxt.binance()
pair = 'LUNA/USDT'
bars = exchange.fetch_ohlcv(pair, timeframe='5m', limit=100)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

#linkitetään halutut muuttujat
adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

#Discordin webhook url sekä user ID jota halutaan pingata
WEBHOOK_URL = "https://discord.com/api/webhooks/889265250875080725/nAh5DI_8uI6QDQYWW3GtQ4c1rUtK766mvDX9QTKyBseZiDOfMQR16iXGbPk--KGMY-Ts"
DISCORD_USERID = "<@606915182459093032>"

#haetaan taulukkoon viimeiset 100 muuttujaa ja mitä arvoja niistä haetaan
df = pd.concat([df, adx,macd,rsi], axis=1)

#haetaan em taulukosta viimeinen rivi
last_row = df.iloc[-1]

#tulostetaan viimeinen rivi
print(last_row)

#Otetaan unix timestamp ja muutetaan se ihmismuotoon
Timestamp = last_row['time']
#täytyy jakaa 1000 koska käytetään windowsia

ts = int(Timestamp/1000)
#tulostetaan haluttuun muotoon
realtime = datetime.datetime.fromtimestamp(int(ts)).strftime('%d-%m %H:%M')
print(realtime)

#tehdään muuttujat ja otetaan tiedot niihin em. taulukon viimeisestä rivistä


rsivalue = f"rsi {last_row['RSI_14']:.2f}"
adxvalue = f"adx {last_row['ADX_14']:.2f}"
macd1 = f"macd {last_row['MACD_14_28_9']:.2f}" #oranssi
macd2 = f"macd ero  {last_row['MACDh_14_28_9']:.2f}" 
macd3 = f"macd-Signal  {last_row['MACDs_14_28_9']:.2f}" #sininen


#nyt voidaan tehdä haluttu logiikka jonka perusteella lähetetään viesti
#esimerkkitapauksessa pingataan käyttäjää jos macdLvalue > macdHvalue, muuten ei pingata
if macd1  > macd3 :
    message = ( DISCORD_USERID +"  " + pair + " nousee  " + rsivalue +"  " + macd1 + "  " + macd3+ "  " + realtime +" https://www.tradingview.com/chart/?symbol=BINANCE%3ALUNAUSDT")

else:   
    message = ("Ei nousua " + pair + " " + rsivalue +"  " + macd1 + "  " + macd3 + "  " + realtime)

#tulostetaan muuttujat lopuun
print(rsivalue)

print(macd1)
print(macd2)
print(macd3)

#tulostetaan viesti
print("viesti" , message)

#asetetaan viesti yhdeksi paketiksi
payload = {
"username": "Kaapo bot", 
"content": message
}

#lähetetään viesti käyttäen aiemmin syötettyjä tietoja.
requests.post(WEBHOOK_URL, payload)