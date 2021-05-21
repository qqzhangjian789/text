# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from data_ccxt.async_support.base.exchange import Exchange

# -----------------------------------------------------------------------------

try:
    basestring  # Python 3
except NameError:
    basestring = str  # Python 2
import hashlib
import math
from data_ccxt.base.errors import ExchangeError
from data_ccxt.base.errors import AuthenticationError
from data_ccxt.base.errors import ArgumentsRequired
from data_ccxt.base.errors import InsufficientFunds
from data_ccxt.base.errors import InvalidOrder
from data_ccxt.base.errors import OrderNotFound
from data_ccxt.base.errors import DDoSProtection
from data_ccxt.base.errors import ExchangeNotAvailable


class tidex(Exchange):

    def describe(self):
        return self.deep_extend(super(tidex, self).describe(), {
            'id': 'tidex',
            'name': 'Tidex',
            'countries': ['UK'],
            'rateLimit': 2000,
            'version': '3',
            'userAgent': self.userAgents['chrome'],
            'has': {
                'cancelOrder': True,
                'CORS': False,
                'createMarketOrder': False,
                'createOrder': True,
                'fetchBalance': True,
                'fetchCurrencies': True,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrderBooks': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTrades': True,
                'withdraw': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/30781780-03149dc4-a12e-11e7-82bb-313b269d24d4.jpg',
                'api': {
                    'web': 'https://gate.tidex.com/api',
                    'public': 'https://api.tidex.com/api/3',
                    'private': 'https://api.tidex.com/tapi',
                },
                'www': 'https://tidex.com',
                'doc': 'https://tidex.com/exchange/public-api',
                'referral': 'https://tidex.com/exchange/?ref=57f5638d9cd7',
                'fees': [
                    'https://tidex.com/exchange/assets-spec',
                    'https://tidex.com/exchange/pairs-spec',
                ],
            },
            'api': {
                'web': {
                    'get': [
                        'currency',
                        'pairs',
                        'tickers',
                        'orders',
                        'ordershistory',
                        'trade-data',
                        'trade-data/{id}',
                    ],
                },
                'public': {
                    'get': [
                        'info',
                        'ticker/{pair}',
                        'depth/{pair}',
                        'trades/{pair}',
                    ],
                },
                'private': {
                    'post': [
                        'getInfoExt',
                        'getInfo',
                        'Trade',
                        'ActiveOrders',
                        'OrderInfo',
                        'CancelOrder',
                        'TradeHistory',
                        'CoinDepositAddress',
                        'WithdrawCoin',
                        'CreateCoupon',
                        'RedeemCoupon',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'taker': 0.1 / 100,
                    'maker': 0.1 / 100,
                },
            },
            'commonCurrencies': {
                'DSH': 'DASH',
                'EMGO': 'MGO',
                'MGO': 'WMGO',
            },
            'exceptions': {
                'exact': {
                    '803': InvalidOrder,  # "Count could not be less than 0.001."(selling below minAmount)
                    '804': InvalidOrder,  # "Count could not be more than 10000."(buying above maxAmount)
                    '805': InvalidOrder,  # "price could not be less than X."(minPrice violation on buy & sell)
                    '806': InvalidOrder,  # "price could not be more than X."(maxPrice violation on buy & sell)
                    '807': InvalidOrder,  # "cost could not be less than X."(minCost violation on buy & sell)
                    '831': InsufficientFunds,  # "Not enougth X to create buy order."(buying with balance.quote < order.cost)
                    '832': InsufficientFunds,  # "Not enougth X to create sell order."(selling with balance.base < order.amount)
                    '833': OrderNotFound,  # "Order with id X was not found."(cancelling non-existent, closed and cancelled order)
                },
                'broad': {
                    'Invalid pair name': ExchangeError,  # {"success":0,"error":"Invalid pair name: btc_eth"}
                    'invalid api key': AuthenticationError,
                    'invalid sign': AuthenticationError,
                    'api key dont have trade permission': AuthenticationError,
                    'invalid parameter': InvalidOrder,
                    'invalid order': InvalidOrder,
                    'Requests too often': DDoSProtection,
                    'not available': ExchangeNotAvailable,
                    'data unavailable': ExchangeNotAvailable,
                    'external service unavailable': ExchangeNotAvailable,
                },
            },
            'options': {
                'fetchTickersMaxLength': 2048,
            },
            'orders': {},  # orders cache / emulation
        })

    async def fetch_currencies(self, params={}):
        response = await self.webGetCurrency(params)
        #
        #     [
        #         {
        #             "id":2,
        #             "symbol":"BTC",
        #             "type":2,
        #             "name":"Bitcoin",
        #             "amountPoint":8,
        #             "depositEnable":true,
        #             "depositMinAmount":0.0005,
        #             "withdrawEnable":true,
        #             "withdrawFee":0.0004,
        #             "withdrawMinAmount":0.0005,
        #             "settings":{
        #                 "Blockchain":"https://blockchair.com/bitcoin/",
        #                 "TxUrl":"https://blockchair.com/bitcoin/transaction/{0}",
        #                 "AddrUrl":"https://blockchair.com/bitcoin/address/{0}",
        #                 "ConfirmationCount":3,
        #                 "NeedMemo":false
        #             },
        #             "visible":true,
        #             "isDelisted":false
        #         }
        #     ]
        #
        result = {}
        for i in range(0, len(response)):
            currency = response[i]
            id = self.safe_string(currency, 'symbol')
            precision = self.safe_integer(currency, 'amountPoint')
            code = self.safe_currency_code(id)
            visible = self.safe_value(currency, 'visible')
            active = visible is True
            withdrawEnable = self.safe_value(currency, 'withdrawEnable')
            depositEnable = self.safe_value(currency, 'depositEnable')
            canWithdraw = withdrawEnable is True
            canDeposit = depositEnable is True
            if not canWithdraw or not canDeposit:
                active = False
            name = self.safe_string(currency, 'name')
            fee = self.safe_number(currency, 'withdrawFee')
            result[code] = {
                'id': id,
                'code': code,
                'name': name,
                'active': active,
                'precision': precision,
                'funding': {
                    'withdraw': {
                        'active': canWithdraw,
                        'fee': fee,
                    },
                    'deposit': {
                        'active': canDeposit,
                        'fee': 0.0,
                    },
                },
                'limits': {
                    'amount': {
                        'min': None,
                        'max': math.pow(10, precision),
                    },
                    'price': {
                        'min': math.pow(10, -precision),
                        'max': math.pow(10, precision),
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                    'withdraw': {
                        'min': self.safe_number(currency, 'withdrawMinAmount'),
                        'max': None,
                    },
                    'deposit': {
                        'min': self.safe_number(currency, 'depositMinAmount'),
                        'max': None,
                    },
                },
                'info': currency,
            }
        return result

    def calculate_fee(self, symbol, type, side, amount, price, takerOrMaker='taker', params={}):
        market = self.markets[symbol]
        key = 'quote'
        rate = market[takerOrMaker]
        cost = float(self.cost_to_precision(symbol, amount * rate))
        if side == 'sell':
            cost *= price
        else:
            key = 'base'
        return {
            'type': takerOrMaker,
            'currency': market[key],
            'rate': rate,
            'cost': cost,
        }

    async def fetch_markets(self, params={}):
        response = await self.publicGetInfo(params)
        #
        #     {
        #         "server_time":1615861869,
        #         "pairs":{
        #             "ltc_btc":{
        #                 "decimal_places":8,
        #                 "min_price":0.00000001,
        #                 "max_price":3.0,
        #                 "min_amount":0.001,
        #                 "max_amount":1000000.0,
        #                 "min_total":0.0001,
        #                 "hidden":0,
        #                 "fee":0.1,
        #             },
        #         },
        #     }
        #
        markets = response['pairs']
        keys = list(markets.keys())
        result = []
        for i in range(0, len(keys)):
            id = keys[i]
            market = markets[id]
            baseId, quoteId = id.split('_')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': self.safe_integer(market, 'decimal_places'),
                'price': self.safe_integer(market, 'decimal_places'),
            }
            limits = {
                'amount': {
                    'min': self.safe_number(market, 'min_amount'),
                    'max': self.safe_number(market, 'max_amount'),
                },
                'price': {
                    'min': self.safe_number(market, 'min_price'),
                    'max': self.safe_number(market, 'max_price'),
                },
                'cost': {
                    'min': self.safe_number(market, 'min_total'),
                },
            }
            hidden = self.safe_integer(market, 'hidden')
            active = (hidden == 0)
            takerFee = self.safe_number(market, 'fee')
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': active,
                'taker': takerFee / 100,
                'precision': precision,
                'limits': limits,
                'info': market,
            })
        return result

    async def fetch_balance(self, params={}):
        await self.load_markets()
        response = await self.privatePostGetInfoExt(params)
        balances = self.safe_value(response, 'return')
        result = {'info': balances}
        funds = self.safe_value(balances, 'funds', {})
        currencyIds = list(funds.keys())
        for i in range(0, len(currencyIds)):
            currencyId = currencyIds[i]
            code = self.safe_currency_code(currencyId)
            balance = self.safe_value(funds, currencyId, {})
            account = self.account()
            account['free'] = self.safe_number(balance, 'value')
            account['used'] = self.safe_number(balance, 'inOrders')
            result[code] = account
        return self.parse_balance(result)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        if limit is not None:
            request['limit'] = limit  # default = 150, max = 2000
        response = await self.publicGetDepthPair(self.extend(request, params))
        market_id_in_reponse = (market['id'] in response)
        if not market_id_in_reponse:
            raise ExchangeError(self.id + ' ' + market['symbol'] + ' order book is empty or not available')
        orderbook = response[market['id']]
        return self.parse_order_book(orderbook)

    async def fetch_order_books(self, symbols=None, limit=None, params={}):
        await self.load_markets()
        ids = None
        if symbols is None:
            ids = '-'.join(self.ids)
            # max URL length is 2083 symbols, including http schema, hostname, tld, etc...
            if len(ids) > 2048:
                numIds = len(self.ids)
                raise ExchangeError(self.id + ' has ' + str(numIds) + ' symbols exceeding max URL length, you are required to specify a list of symbols in the first argument to fetchOrderBooks')
        else:
            ids = self.market_ids(symbols)
            ids = '-'.join(ids)
        request = {
            'pair': ids,
        }
        if limit is not None:
            request['limit'] = limit  # default = 150, max = 2000
        response = await self.publicGetDepthPair(self.extend(request, params))
        result = {}
        ids = list(response.keys())
        for i in range(0, len(ids)):
            id = ids[i]
            symbol = self.safe_symbol(id)
            result[symbol] = self.parse_order_book(response[id])
        return result

    def parse_ticker(self, ticker, market=None):
        #
        #   {   high: 0.03497582,
        #         low: 0.03248474,
        #         avg: 0.03373028,
        #         vol: 120.11485715062999,
        #     vol_cur: 3572.24914074,
        #        last: 0.0337611,
        #         buy: 0.0337442,
        #        sell: 0.03377798,
        #     updated: 1537522009          }
        #
        timestamp = self.safe_timestamp(ticker, 'updated')
        symbol = None
        if market is not None:
            symbol = market['symbol']
            if not market['active']:
                timestamp = None
        last = self.safe_number(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_number(ticker, 'high'),
            'low': self.safe_number(ticker, 'low'),
            'bid': self.safe_number(ticker, 'buy'),
            'bidVolume': None,
            'ask': self.safe_number(ticker, 'sell'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': self.safe_number(ticker, 'avg'),
            'baseVolume': self.safe_number(ticker, 'vol_cur'),
            'quoteVolume': self.safe_number(ticker, 'vol'),
            'info': ticker,
        }

    async def fetch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        ids = self.ids
        if symbols is None:
            numIds = len(ids)
            ids = '-'.join(ids)
            # max URL length is 2048 symbols, including http schema, hostname, tld, etc...
            if len(ids) > self.options['fetchTickersMaxLength']:
                maxLength = self.safe_integer(self.options, 'fetchTickersMaxLength', 2048)
                raise ArgumentsRequired(self.id + ' has ' + str(numIds) + ' markets exceeding max URL length for self endpoint(' + str(maxLength) + ' characters), please, specify a list of symbols of interest in the first argument to fetchTickers')
        else:
            ids = self.market_ids(symbols)
            ids = '-'.join(ids)
        request = {
            'pair': ids,
        }
        response = await self.publicGetTickerPair(self.extend(request, params))
        result = {}
        keys = list(response.keys())
        for i in range(0, len(keys)):
            id = keys[i]
            market = self.safe_market(id)
            symbol = market['symbol']
            result[symbol] = self.parse_ticker(response[id], market)
        return self.filter_by_array(result, 'symbol', symbols)

    async def fetch_ticker(self, symbol, params={}):
        tickers = await self.fetch_tickers([symbol], params)
        return tickers[symbol]

    def parse_trade(self, trade, market=None):
        timestamp = self.safe_timestamp(trade, 'timestamp')
        side = self.safe_string(trade, 'type')
        if side == 'ask':
            side = 'sell'
        elif side == 'bid':
            side = 'buy'
        price = self.safe_number_2(trade, 'rate', 'price')
        id = self.safe_string_2(trade, 'trade_id', 'tid')
        orderId = self.safe_string(trade, 'order_id')
        marketId = self.safe_string(trade, 'pair')
        symbol = self.safe_symbol(marketId, market)
        amount = self.safe_number(trade, 'amount')
        type = 'limit'  # all trades are still limit trades
        takerOrMaker = None
        fee = None
        feeCost = self.safe_number(trade, 'commission')
        if feeCost is not None:
            feeCurrencyId = self.safe_string(trade, 'commissionCurrency')
            feeCurrencyCode = self.safe_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrencyCode,
            }
        isYourOrder = self.safe_value(trade, 'is_your_order')
        if isYourOrder is not None:
            takerOrMaker = 'taker'
            if isYourOrder:
                takerOrMaker = 'maker'
            if fee is None:
                fee = self.calculate_fee(symbol, type, side, amount, price, takerOrMaker)
        cost = None
        if amount is not None:
            if price is not None:
                cost = amount * price
        return {
            'id': id,
            'order': orderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': type,
            'side': side,
            'takerOrMaker': takerOrMaker,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
            'info': trade,
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        response = await self.publicGetTradesPair(self.extend(request, params))
        if isinstance(response, list):
            numElements = len(response)
            if numElements == 0:
                return []
        return self.parse_trades(response[market['id']], market, since, limit)

    async def create_order(self, symbol, type, side, amount, price=None, params={}):
        if type == 'market':
            raise ExchangeError(self.id + ' allows limit orders only')
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'pair': market['id'],
            'type': side,
            'amount': self.amount_to_precision(symbol, amount),
            'rate': self.price_to_precision(symbol, price),
        }
        price = float(price)
        amount = float(amount)
        response = await self.privatePostTrade(self.extend(request, params))
        id = None
        status = 'open'
        filled = 0.0
        remaining = amount
        if 'return' in response:
            id = self.safe_string(response['return'], 'order_id')
            if id == '0':
                id = self.safe_string(response['return'], 'init_order_id')
                status = 'closed'
            filled = self.safe_number(response['return'], 'received', 0.0)
            remaining = self.safe_number(response['return'], 'remains', amount)
        timestamp = self.milliseconds()
        return {
            'id': id,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'status': status,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'cost': price * filled,
            'amount': amount,
            'remaining': remaining,
            'filled': filled,
            'fee': None,
            # 'trades': self.parse_trades(order['trades'], market),
            'info': response,
            'clientOrderId': None,
            'average': None,
            'trades': None,
        }

    async def cancel_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'order_id': int(id),
        }
        return await self.privatePostCancelOrder(self.extend(request, params))

    def parse_order_status(self, status):
        statuses = {
            '0': 'open',
            '1': 'closed',
            '2': 'canceled',
            '3': 'canceled',  # or partially-filled and still open? https://github.com/ccxt/ccxt/issues/1594
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        id = self.safe_string(order, 'id')
        status = self.parse_order_status(self.safe_string(order, 'status'))
        timestamp = self.safe_timestamp(order, 'timestamp_created')
        marketId = self.safe_string(order, 'pair')
        symbol = self.safe_symbol(marketId, market)
        remaining = None
        amount = None
        price = self.safe_number(order, 'rate')
        if 'start_amount' in order:
            amount = self.safe_number(order, 'start_amount')
            remaining = self.safe_number(order, 'amount')
        else:
            remaining = self.safe_number(order, 'amount')
        fee = None
        return self.safe_order({
            'info': order,
            'id': id,
            'clientOrderId': None,
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'type': 'limit',
            'timeInForce': None,
            'postOnly': None,
            'side': self.safe_string(order, 'type'),
            'price': price,
            'stopPrice': None,
            'cost': None,
            'amount': amount,
            'remaining': remaining,
            'filled': None,
            'status': status,
            'fee': fee,
            'average': None,
            'trades': None,
        })

    async def fetch_order(self, id, symbol=None, params={}):
        await self.load_markets()
        request = {
            'order_id': int(id),
        }
        response = await self.privatePostOrderInfo(self.extend(request, params))
        id = str(id)
        result = self.safe_value(response, 'return', {})
        order = self.safe_value(result, id)
        return self.parse_order(self.extend({'id': id}, order))

    async def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        request = {}
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['pair'] = market['id']
        response = await self.privatePostActiveOrders(self.extend(request, params))
        #
        #     {
        #         "success":1,
        #         "return":{
        #             "1255468911":{
        #                 "status":0,
        #                 "pair":"spike_usdt",
        #                 "type":"sell",
        #                 "amount":35028.44256388,
        #                 "rate":0.00199989,
        #                 "timestamp_created":1602684432
        #             }
        #         },
        #         "stat":{
        #             "isSuccess":true,
        #             "serverTime":"00:00:00.0000826",
        #             "time":"00:00:00.0091423",
        #             "errors":null
        #         }
        #     }
        #
        # it can only return 'open' orders(i.e. no way to fetch 'closed' orders)
        orders = self.safe_value(response, 'return', [])
        return self.parse_orders(orders, market, since, limit)

    async def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        await self.load_markets()
        market = None
        # some derived classes use camelcase notation for request fields
        request = {
            # 'from': 123456789,  # trade ID, from which the display starts numerical 0(test result: liqui ignores self field)
            # 'count': 1000,  # the number of trades for display numerical, default = 1000
            # 'from_id': trade ID, from which the display starts numerical 0
            # 'end_id': trade ID on which the display ends numerical ∞
            # 'order': 'ASC',  # sorting, default = DESC(test result: liqui ignores self field, most recent trade always goes last)
            # 'since': 1234567890,  # UTC start time, default = 0(test result: liqui ignores self field)
            # 'end': 1234567890,  # UTC end time, default = ∞(test result: liqui ignores self field)
            # 'pair': 'eth_btc',  # default = all markets
        }
        if symbol is not None:
            market = self.market(symbol)
            request['pair'] = market['id']
        if limit is not None:
            request['count'] = int(limit)
        if since is not None:
            request['since'] = int(since / 1000)
        response = await self.privatePostTradeHistory(self.extend(request, params))
        trades = self.safe_value(response, 'return', [])
        return self.parse_trades(trades, market, since, limit)

    async def withdraw(self, code, amount, address, tag=None, params={}):
        self.check_address(address)
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'coinName': currency['id'],
            'amount': float(amount),
            'address': address,
        }
        # no docs on the tag, yet...
        if tag is not None:
            raise ExchangeError(self.id + ' withdraw() does not support the tag argument yet due to a lack of docs on withdrawing with tag/memo on behalf of the exchange.')
        response = await self.privatePostWithdrawCoin(self.extend(request, params))
        return {
            'info': response,
            'id': response['return']['tId'],
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api]
        query = self.omit(params, self.extract_params(path))
        if api == 'private':
            self.check_required_credentials()
            nonce = self.nonce()
            body = self.urlencode(self.extend({
                'nonce': nonce,
                'method': path,
            }, query))
            signature = self.hmac(self.encode(body), self.encode(self.secret), hashlib.sha512)
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Key': self.apiKey,
                'Sign': signature,
            }
        elif api == 'public':
            url += '/' + self.implode_params(path, params)
            if query:
                url += '?' + self.urlencode(query)
        else:
            url += '/' + self.implode_params(path, params)
            if method == 'GET':
                if query:
                    url += '?' + self.urlencode(query)
            else:
                if query:
                    body = self.json(query)
                    headers = {
                        'Content-Type': 'application/json',
                    }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # fallback to default error handler
        if 'success' in response:
            #
            # 1 - The exchange only returns the integer 'success' key from their private API
            #
            #     {"success": 1, ...} httpCode == 200
            #     {"success": 0, ...} httpCode == 200
            #
            # 2 - However, derived exchanges can return non-integers
            #
            #     It can be a numeric string
            #     {"sucesss": "1", ...}
            #     {"sucesss": "0", ...}, httpCode >= 200(can be 403, 502, etc)
            #
            #     Or just a string
            #     {"success": "true", ...}
            #     {"success": "false", ...}, httpCode >= 200
            #
            #     Or a boolean
            #     {"success": True, ...}
            #     {"success": False, ...}, httpCode >= 200
            #
            # 3 - Oversimplified, Python PEP8 forbids comparison operator(==) of different types
            #
            # 4 - We do not want to copy-paste and duplicate the code of self handler to other exchanges derived from Liqui
            #
            # To cover points 1, 2, 3 and 4 combined self handler should work like self:
            #
            success = self.safe_value(response, 'success', False)
            if isinstance(success, basestring):
                if (success == 'true') or (success == '1'):
                    success = True
                else:
                    success = False
            if not success:
                code = self.safe_string(response, 'code')
                message = self.safe_string(response, 'error')
                feedback = self.id + ' ' + body
                self.throw_exactly_matched_exception(self.exceptions['exact'], code, feedback)
                self.throw_exactly_matched_exception(self.exceptions['exact'], message, feedback)
                self.throw_broadly_matched_exception(self.exceptions['broad'], message, feedback)
                raise ExchangeError(feedback)  # unknown message
