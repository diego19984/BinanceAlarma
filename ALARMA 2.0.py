
import time
from binance.client import Client
from pygame import mixer


with open('credenciales.txt') as f:
    lines = f.readlines()
api_key = str(lines[0].replace("\n", " "))
secret_key = str(lines[1].replace("\n", " "))
client = Client(api_key, secret_key)

rango=float(input("Introduzca el Rango: "))

symbol='BTCUSDT'

futureBalance = client.futures_account_balance()
balance=round(float(futureBalance[6].get('balance')),3)

print("USDT ",balance)
print("-----------------------------------------------------")


mixer.init()
mixer.music.load("ALARMA.mp3")

while (1==1):
    p=True
    while p == True:
        try:
            kline = client.futures_historical_klines(symbol, client.KLINE_INTERVAL_1HOUR, "1 HOUR ago UTC")
            var = round(100*((float(kline[0][1]) - float(kline[0][4]))/float(kline[0][2])),2)
            if var>rango or var<-rango:
                print("ALLERT var ")
                print(var)
                mixer.music.play()
                time.sleep(30)
            print(var)

        except:
            print("ERROR!!!")
            print("ERROR!!!")
            print("ERROR!!!")
            print("---------------------------------------------------")