from ibapi.client import *
from ibapi.wrapper import *
from ibapi.utils import *

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        mycontract = Contract()
        mycontract.exchange = "SMART"
        mycontract.conId = 503837694
        #self.reqMarketDataType(1)
        self.reqMktData(orderId, mycontract, "100, 101, 104, 105, 106", 0, 0, [])

    #def tickPrice(self, reqId, tickType, price, attrib):
    #    print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}", file=open('output.txt', 'a'))
    #    print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.BID}, price: {price}, attribs: {attrib}")


    def tickPrice(self, reqId, tickType, price, attrib):
        print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(tickType)}, price: {price}, attribs: {attrib}")
    

    def tickOptionComputation(self, reqId: TickerId, tickType: TickType, tickAttrib: int,
                                   impliedVol: float, delta: float, optPrice: float, pvDividend: float,
                                   gamma: float, vega: float, theta: float, undPrice: float):
             super().tickOptionComputation(reqId, tickType, tickAttrib, impliedVol, delta,
                                           optPrice, pvDividend, gamma, vega, theta, undPrice)
             print("TickOptionComputation. TickerId:", reqId, "TickType:", tickType,
                   "TickAttrib:", tickAttrib,
                   "ImpliedVolatility:", impliedVol, "Delta:", delta, "OptionPrice:",
                   optPrice, "pvDividend:", pvDividend, "Gamma: ", gamma, "Vega:", vega,
                  "Theta:", theta, "UnderlyingPrice:", undPrice)
    
    def tickSize(self, reqId: TickerId, tickType: TickType, size):
             super().tickSize(reqId, tickType, size)
             print("TickSize. TickerId:", reqId, "TickType:", tickType, "Size: ", size)


app = TestApp()
app.connect("127.0.0.1", 7496, 1000)
app.run()

