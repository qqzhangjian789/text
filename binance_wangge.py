# -- coding: utf-8 --
# A_Jian


import data_ccxt as ccxt
from dingtalkchatbot.chatbot import DingtalkChatbot



class Binance_wangge:

    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': 'm3ZMAJK2ZVyoC1SIyirAlQJV8xkkBysRKezwe6wmJRWblh213JdWsV8C4nHtHVZ7',
            'secret': 'FJqhdM5gdvMMenhDTe5y0dDd3pWV0Uv6SClnz1dT0NaJjPIUmyKcoyZT8hQSgiBi'
        })
        self.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=d6c6b417940c932c5cc43c7a0f75bb93ad3054ccc795edf6619c25f30ad9b828'

    def send_data(self,message):
        xiaoding = DingtalkChatbot(self.webhook)
        xiaoding.send_text(msg=message, is_at_all=False)

    def get_now_data(self, symbol: str):
        try:
            data = self.exchange.fapiPrivateGetPositionRisk({
                'symbol': symbol
            })
        except:
            data = self.exchange.fapiPrivateGetPositionRisk({
                'symbol': symbol
            })
        return data

    def create_order_buy(self, symbol, price):
        order = self.exchange.fapiPrivatePostOrder(params={
            'symbol': symbol,
            'side': 'BUY',
            'type': 'LIMIT',
            'quantity': 50,
            'price': price,
            'timeInForce': 'GTC'})
        return order

    def create_order_sell(self, symbol, price):
        order = self.exchange.fapiPrivatePostOrder(params={
            'symbol': symbol,
            'side': 'SELL',
            'type': 'LIMIT',
            'quantity': 50,
            'price': price,
            'timeInForce': 'GTC'})

        return order

    def get_order(self, symbol, orderId):
        try:
            get_order = self.exchange.fapiPrivateGetOrder(params={
                'symbol': symbol,
                'orderId': orderId
            })
        except:
            get_order = self.exchange.fapiPrivateGetOrder(params={
                'symbol': symbol,
                'orderId': orderId
            })
        return get_order

    def clear_order(self, symbol, orderId):
        print('撤销订单,订单id：', orderId)
        try:
            clear_order = self.exchange.fapiPrivateDeleteOrder(params={
                'symbol': symbol,
                'orderId': orderId,
            })
        except:
            clear_order = self.exchange.fapiPrivateDeleteOrder(params={
                'symbol': symbol,
                'orderId': orderId,
            })
        return clear_order


if __name__ == '__main__':

    import time

    bian = Binance_wangge()
    price = 0.36
    symbol = 'DOGEUSDT'
    wave = 0.005
    switch = True
    list = []

    while True:

        if switch:
            try:
                buy = bian.create_order_buy(symbol=symbol, price=round(float(price) - wave, 4))
                sell = bian.create_order_sell(symbol=symbol, price=round(float(price) + wave, 4))
                list.append(buy['orderId'])
                list.append(sell['orderId'])
                print('订单列表：', list)
                switch = False
            except:
                print('有问题，跳过')
                time.sleep(5)
                continue

        else:
            buy_data = bian.get_order(symbol, list[0])
            sell_data = bian.get_order(symbol, list[1])

            if buy_data['executedQty'] == buy_data['origQty']:
                data_1 = bian.get_now_data(symbol)
                number = data_1[0]['notional']
                print('买单成交，id：', sell_data['orderId'], 'price:', buy_data['price'])
                bian.send_data("买单成交，价格：'%s',数量：'%s'" % (buy_data['price'],number))
                bian.clear_order(symbol, sell_data['orderId'])
                price = float(buy_data['price'])
                list.clear()
                switch = True

            if sell_data['executedQty'] == sell_data['origQty']:
                data_1 = bian.get_now_data(symbol)
                number = data_1[0]['notional']
                print('卖单成交，id：', buy_data['orderId'], 'price:', sell_data['price'])
                bian.clear_order(symbol, buy_data['orderId'],)
                bian.send_data("卖单成交，价格：'%s',数量：'%s'" % (sell_data['price'], number))
                price = float(sell_data['price'])
                list.clear()
                switch = True
        time.sleep(6)
