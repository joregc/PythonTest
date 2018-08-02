import json
import httplib2
import time
from ConnInitializer import ConnInitializer


ticker = "ticker/"
ethOrderBook = "?book=eth_mxn"
bitso_api_key = ""
tickerUrl = ""
request = httplib2.Http()


def intializeRequest(orderBook):
    tickerUrl = url + ticker + orderBook  


def getCurrentCriptoCurrencyStat():
    result = json.loads(self.initializer.request.request(initializer.urlApi,'GET')[1])
    print(result['payload']['last'])

def Main():
    initializer = ConnInitializer(ethOrderBook)
    while (True):
        getCurrentCriptoCurrencyStat()
        sleep(2)
        #branch enterprise
Main()