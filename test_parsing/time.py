from pybit.unified_trading import HTTP
import logging
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)
session = HTTP(
    recv_window=60000
)
r = session.get_orderbook(category="linear", symbol="BTCUSDT")
print(r)
