# -- coding: utf-8 --
# A_Jian


import data_ccxt

exchange = data_ccxt.binance({
            'apiKey': 'm3ZMAJK2ZVyoC1SIyirAlQJV8xkkBysRKezwe6wmJRWblh213JdWsV8C4nHtHVZ7',
            'secret': 'FJqhdM5gdvMMenhDTe5y0dDd3pWV0Uv6SClnz1dT0NaJjPIUmyKcoyZT8hQSgiBi',
})


def get_now_data(symbol:str):
    try:
        data = exchange.fapiPrivateGetPositionRisk({
            'symbol':symbol
        })
    except:
        data = exchange.fapiPrivateGetPositionRisk({
            'symbol': symbol
        })
    print(data[0]['notional'])
    return 'ok'

get_now_data(symbol = 'DOGEUSDT')