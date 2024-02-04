from pybit.unified_trading import HTTP

session = HTTP(api_key="qBld2EceeIo3M8i40v", api_secret="suUB0wP1M9fVo9gDM0hnoUdTuhOeZbUjmUg5")
response = session.get_kline(
    category="linear",
    symbol="BTCUSD",
    interval=60,
    #start=1670601600000,
    #end=1670608800000,
)

# Получаем массив свечей
kline_list = response['result']['list']

# Печатаем длину массива
print(kline_list, len(kline_list))
