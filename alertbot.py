import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import requests

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


#tehdään muuttujat ja otetaan tiedot niihin em. taulukon viimeisestä rivistä
rsivalue = f"rsi arvo {last_row['RSI_14']:.2f}"
adxvalue = f"adx arvo {last_row['ADX_14']:.2f}"
macdLvalue = f"macdL arvo {last_row['MACD_14_28_9']:.2f}"
macdHvalue = f"macdH arvo {last_row['MACDh_14_28_9']:.2f}"


#nyt voidaan tehdä haluttu logiikka jonka perusteella lähetetään viesti
#esimerkkitapauksessa pingataan käyttäjää jos macdLvalue > macdHvalue, muuten ei pingata
if macdLvalue > macdHvalue:
    message = ( DISCORD_USERID +"  " + pair + " on nousemassa  " + rsivalue +"  " + macdLvalue + "  " + macdHvalue + " https://www.tradingview.com/chart/?symbol=BINANCE%3ALUNAUSDT")

else:   
    message = ("Ei nousua " + pair + " " + rsivalue +"  " + macdLvalue + "  " + macdHvalue)

#tulostetaan muuttujat lopuun
print(rsivalue)
print(macdHvalue)
print(macdLvalue)
#tulostetaan viesti
print("viesti" , message)

#asetetaan viesti yhdeksi paketiksi
payload = {
"username": "Kaapo bot", 
"content": message
}

#lähetetään viesti käyttäen aiemmin syötettyjä tietoja.
requests.post(WEBHOOK_URL, payload)