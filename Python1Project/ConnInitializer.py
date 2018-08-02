import httplib2

class ConnInitializer(object):
    """Initialize the connection to the api"""

    request = httplib2.Http()
    urlApiV3 =  "https://bitso.com/api/v3"
    ticker = "/ticker"
    moco = "moco"

    def __init__(self, orderBook):      
        self.orderBook = orderBook
        self.urlApi = self.urlApiV3 + self.ticker + orderBook
