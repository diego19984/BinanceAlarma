from binance.client import Client
from datetime import datetime

with open('credenciales.txt') as f:
    lines = f.readlines()
api_key = str(lines[0].replace("\n", " "))
secret_key = str(lines[1].replace("\n", " "))
client = Client(api_key, secret_key)

symbol='BTCUSDT'

kline = client.futures_historical_klines(symbol, client.KLINE_INTERVAL_1HOUR, "100 hour ago UTC")

rango=float(input("Introduzca un Rango : "))
cont=0
for i in range(len(kline)):
    var = (float(kline[i][1]) - float(kline[i][4]))/float(kline[i][1])
    if var>rango or var<-rango:
        dt_object = datetime.fromtimestamp(int(kline[i][0]) / 1000)
        print("FECHA ", dt_object)
        cont = cont + 1
print(cont)