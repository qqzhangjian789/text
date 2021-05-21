import data_ccxt as ccxt


class binance_U_EOS_W():

    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': 'm3ZMAJK2ZVyoC1SIyirAlQJV8xkkBysRKezwe6wmJRWblh213JdWsV8C4nHtHVZ7',
            'secret': 'FJqhdM5gdvMMenhDTe5y0dDd3pWV0Uv6SClnz1dT0NaJjPIUmyKcoyZT8hQSgiBi',
        })

    def create_buy_order(self, symbol, price):
        data = self.exchange.dapiPrivatePostOrder(params={
            'symbol': symbol,
            'side': 'BUY',
            'type': 'LIMIT',
            'quantity': 10,
            'price': price,
            'timeInForce': 'GTC'
        })
        return data

    def create_sell_order(self, symbol, price):
        data = self.exchange.dapiPrivatePostOrder(params={
            'symbol': symbol,
            'side': 'SELL',
            'type': 'LIMIT',
            'quantity': 10,
            'price': price,
            'timeInForce': 'GTC'
        })
        return data

    def get_order(self, symbol, orderId):
        try:
            data = self.exchange.dapiPrivateGetOrder(params={
                'symbol': symbol,
                'orderId': orderId
            })
        except:
            data = self.exchange.dapiPrivateGetOrder(params={
                'symbol': symbol,
                'orderId': orderId
            })
        return data

    def clear_order(self, symbol, orderId):
        print('撤销订单,订单id：', orderId)
        try:
            clear_order = self.exchange.dapiPrivateDeleteOrder(params={
                'symbol': symbol,
                'orderId': orderId,
            })
        except:
            clear_order = self.exchange.dapiPrivateDeleteOrder(params={
                'symbol': symbol,
                'orderId': orderId,
            })
        return clear_order

if __name__ == '__main__':
    import time
    exchange = binance_U_EOS_W()
    symbol = 'EOSUSD'
    price = 10
    wave = 0.2
    switch = True
    list = []

    while True:

        if switch:
            try:
                buy = exchange.create_buy_order(symbol=symbol, price=round(float(price) - wave,3))
                sell = exchange.create_sell_order(symbol=symbol, price=round(float(price) + wave,3))
                list.append(buy['orderId'])
                list.append(sell['orderId'])
                print('订单列表：',list)
                switch = False
            except:
                print('有问题，跳过')
                time.sleep(5)
                continue

        else:
            buy_data = exchange.get_order(symbol, list[0])
            sell_data = exchange.get_order(symbol, list[1])

            if buy_data['executedQty'] == buy_data['origQty']:
                print('买单成交，撤销卖单，id：', sell_data['orderId'])
                exchange.clear_order(symbol, sell_data['orderId'])
                price = buy_data['price']
                list.clear()
                switch = True

            elif sell_data['executedQty'] == sell_data['origQty']:
                print('卖单成交，撤销买单，id：',buy_data['orderId'])
                exchange.clear_order(symbol, buy_data['orderId'])
                price = sell_data['price']
                list.clear()
                switch = True
        time.sleep(6)
