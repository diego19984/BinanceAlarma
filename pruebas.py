from binance.client import Client

with open('credenciales.txt') as f:
    lines = f.readlines()
api_key = str(lines[0].replace("\n", " "))
secret_key = str(lines[1].replace("\n", " "))
client = Client(api_key, secret_key)

##########--------------------------------------------------#########################
while (1==1):
    symbol='BTCBUSD'
    vela=client.futures_historical_klines("BTCBUSD",client.KLINE_INTERVAL_1DAY,"3 day ago UTC")
    pOpen=float(vela[0][1])
    pHigh=float(vela[0][2])
    pLow=float(vela[0][3])
    pActual=float(vela[0][4])
    variacion=round(100*(pOpen-pActual)/pOpen,2)
    Criptomonedas=['BTCBUSD','ETHBUSD','APEBUSD']

    print(pOpen)
    print(pHigh)
    print(pLow)
    print(pActual)
    print(variacion)
    print(vela)
    print("-----------------------------------------------------")

