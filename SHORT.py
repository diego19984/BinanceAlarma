import time
from binance.client import Client

api_key = "pIMO1FnZYXDevEq0VQcEMtLUsSPKgCPXyBv7SCzG7exVWXfXNBGg8xcJtRfKVYTs"
secret_key = "4kJiJPBlb5sKSQmDJvJLYsntiNtiePPFGk1BqgzSu23PW3XWpwTXslDqZqOwvxjG"
client = Client(api_key, secret_key)
n=0

##########--------------------------------------------------#########################

symbol='BTC'

#gananciaMin=

precioCompra=100000
precioMin=100000
futureBalance = client.futures_account_balance()
Apuesta=round(float(input("Apuesta = ")),4)
Ganancia=round(float(input("Ganancia para cerrar = ")),4)
precioMax=round(float(input("PRECIO MAX= ")),4)
margen = round(0.1 * precioMax, 4)
precioVenta = round(precioMax - margen, 4)
quantity = round((Apuesta*10)/precioVenta)
print("USDT ", futureBalance[6].get('balance'))
print("BUSD ", futureBalance[9].get('balance'))
print("-----------------------------------------------------")

Posicion=0

while (1==1):

    p=True
    while p == True:
        try:
            time.sleep(1)
            kline = client.futures_historical_klines(symbol, client.KLINE_INTERVAL_1MINUTE, "1 minute ago UTC")
            precioActual = round(float(kline[0][4]),4)
            infOrder = client.futures_position_information(symbol=symbol)
            Posicion = round(float(infOrder[0].get('positionAmt')), 4)
            p = False
        except:
            print("ERROR!!!")
            print("ERROR!!!")
            print("ERROR!!!")
            print("-----------------------------------------------------")

    if (Posicion == 0):
        if(precioMax <= precioActual ):
            precioMax=precioActual
            margen = round(0.1 * precioMax,4)
            precioVenta=round(precioMax-margen,4)
            quantity = round((Apuesta*10)/precioVenta)
        print("Numero de veces = ",n)
        print(" NO HAY POSICIONES ")
        print("Precio Max       = ",precioMax)
        print("Precio de Venta  = ",precioVenta)
        print("Precio Actual    = ",precioActual)
        print("Margen",margen)

        print("-----------------------------------------------------")

        if(precioActual <= precioVenta):
            client.futures_create_order(symbol=symbol, side='SELL', type='MARKET', quantity=quantity)
            precioVenta=precioVenta
            print(" ---- ALERTA ----- ")
            print("-----------------------------------------------------")
            n=n+1
    else:
        Posicion        = round(float(infOrder[0].get('positionAmt')), 4)
        PrecioEntrada   = round(float(infOrder[0].get('entryPrice')),4)
        PrecioActualPos = round(float(infOrder[0].get('markPrice')),4)
        PnL             = round(float(infOrder[0].get('unRealizedProfit')), 4)
        Apalancamiento  = int(infOrder[0].get('leverage'))

        print("Precio de Venta = ", precioVenta)
        print("Precio Actual   = ", precioActual)
        print("Simbolo\t\t\t Posicion\t Entrada \t precio \t PnL")
        print(symbol, "x", Apalancamiento, "\t", Posicion, "\t", PrecioEntrada, "\t", PrecioActualPos, "\t", PnL)
        print("Precio de Compra = ", precioCompra)

        if(precioActual>precioVenta):#cancelar
            client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=quantity)

        if(precioActual< precioVenta*0.995 ):#aseguré ganancias
            if(precioActual <= precioMin):
                precioMin=precioActual

        if(PnL >= Ganancia):#GANE,RESETEA EL PROGRAMA
            client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=quantity)
            precioMax=0
            precioMin=100000
            precioCompra=100000
        print("-----------------------------------------------------")

    infOrder = client.futures_position_information(symbol=symbol)
    Posicion = round(float(infOrder[0].get('positionAmt')), 4)
    if(Posicion < -quantity):
        seguro=Posicion*(-1)
        print(seguro)
        client.futures_create_order(symbol=symbol, side='BUY', type='MARKET', quantity=seguro)
        quit()
    if (Posicion > quantity):
        seguro = Posicion
        print(seguro)
        client.futures_create_order(symbol=symbol, side='SELL', type='MARKET', quantity=seguro)
        quit()