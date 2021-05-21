# -*- coding: utf-8 -*-

"""CCXT: CryptoCurrency eXchange Trading Library"""

# MIT License
# Copyright (c) 2017 Igor Kroitor
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ----------------------------------------------------------------------------

__version__ = '1.45.5'

# ----------------------------------------------------------------------------

from data_ccxt.base.exchange import Exchange                     # noqa: F401

from data_ccxt.base.decimal_to_precision import decimal_to_precision  # noqa: F401
from data_ccxt.base.decimal_to_precision import TRUNCATE              # noqa: F401
from data_ccxt.base.decimal_to_precision import ROUND                 # noqa: F401
from data_ccxt.base.decimal_to_precision import DECIMAL_PLACES        # noqa: F401
from data_ccxt.base.decimal_to_precision import SIGNIFICANT_DIGITS    # noqa: F401
from data_ccxt.base.decimal_to_precision import TICK_SIZE             # noqa: F401
from data_ccxt.base.decimal_to_precision import NO_PADDING            # noqa: F401
from data_ccxt.base.decimal_to_precision import PAD_WITH_ZERO         # noqa: F401

from data_ccxt.base import errors
from data_ccxt.base.errors import BaseError                      # noqa: F401
from data_ccxt.base.errors import ExchangeError                  # noqa: F401
from data_ccxt.base.errors import AuthenticationError            # noqa: F401
from data_ccxt.base.errors import PermissionDenied               # noqa: F401
from data_ccxt.base.errors import AccountSuspended               # noqa: F401
from data_ccxt.base.errors import ArgumentsRequired              # noqa: F401
from data_ccxt.base.errors import BadRequest                     # noqa: F401
from data_ccxt.base.errors import BadSymbol                      # noqa: F401
from data_ccxt.base.errors import BadResponse                    # noqa: F401
from data_ccxt.base.errors import NullResponse                   # noqa: F401
from data_ccxt.base.errors import InsufficientFunds              # noqa: F401
from data_ccxt.base.errors import InvalidAddress                 # noqa: F401
from data_ccxt.base.errors import AddressPending                 # noqa: F401
from data_ccxt.base.errors import InvalidOrder                   # noqa: F401
from data_ccxt.base.errors import OrderNotFound                  # noqa: F401
from data_ccxt.base.errors import OrderNotCached                 # noqa: F401
from data_ccxt.base.errors import CancelPending                  # noqa: F401
from data_ccxt.base.errors import OrderImmediatelyFillable       # noqa: F401
from data_ccxt.base.errors import OrderNotFillable               # noqa: F401
from data_ccxt.base.errors import DuplicateOrderId               # noqa: F401
from data_ccxt.base.errors import NotSupported                   # noqa: F401
from data_ccxt.base.errors import NetworkError                   # noqa: F401
from data_ccxt.base.errors import DDoSProtection                 # noqa: F401
from data_ccxt.base.errors import RateLimitExceeded              # noqa: F401
from data_ccxt.base.errors import ExchangeNotAvailable           # noqa: F401
from data_ccxt.base.errors import OnMaintenance                  # noqa: F401
from data_ccxt.base.errors import InvalidNonce                   # noqa: F401
from data_ccxt.base.errors import RequestTimeout                 # noqa: F401
from data_ccxt.base.errors import error_hierarchy                # noqa: F401

from data_ccxt.aax import aax                                    # noqa: F401
from data_ccxt.aofex import aofex                                # noqa: F401
from data_ccxt.ascendex import ascendex                          # noqa: F401
from data_ccxt.bequant import bequant                            # noqa: F401
from data_ccxt.bibox import bibox                                # noqa: F401
from data_ccxt.bigone import bigone                              # noqa: F401
from data_ccxt.binance import binance                            # noqa: F401
from data_ccxt.binanceus import binanceus                        # noqa: F401
from data_ccxt.bit2c import bit2c                                # noqa: F401
from data_ccxt.bitbank import bitbank                            # noqa: F401
from data_ccxt.bitbay import bitbay                              # noqa: F401
from data_ccxt.bitcoincom import bitcoincom                      # noqa: F401
from data_ccxt.bitfinex import bitfinex                          # noqa: F401
from data_ccxt.bitfinex2 import bitfinex2                        # noqa: F401
from data_ccxt.bitflyer import bitflyer                          # noqa: F401
from data_ccxt.bitforex import bitforex                          # noqa: F401
from data_ccxt.bitget import bitget                              # noqa: F401
from data_ccxt.bithumb import bithumb                            # noqa: F401
from data_ccxt.bitkk import bitkk                                # noqa: F401
from data_ccxt.bitmart import bitmart                            # noqa: F401
from data_ccxt.bitmax import bitmax                              # noqa: F401
from data_ccxt.bitmex import bitmex                              # noqa: F401
from data_ccxt.bitpanda import bitpanda                          # noqa: F401
from data_ccxt.bitso import bitso                                # noqa: F401
from data_ccxt.bitstamp import bitstamp                          # noqa: F401
from data_ccxt.bitstamp1 import bitstamp1                        # noqa: F401
from data_ccxt.bittrex import bittrex                            # noqa: F401
from data_ccxt.bitvavo import bitvavo                            # noqa: F401
from data_ccxt.bitz import bitz                                  # noqa: F401
from data_ccxt.bl3p import bl3p                                  # noqa: F401
from data_ccxt.bleutrade import bleutrade                        # noqa: F401
from data_ccxt.braziliex import braziliex                        # noqa: F401
from data_ccxt.btcalpha import btcalpha                          # noqa: F401
from data_ccxt.btcbox import btcbox                              # noqa: F401
from data_ccxt.btcmarkets import btcmarkets                      # noqa: F401
from data_ccxt.btctradeua import btctradeua                      # noqa: F401
from data_ccxt.btcturk import btcturk                            # noqa: F401
from data_ccxt.buda import buda                                  # noqa: F401
from data_ccxt.bw import bw                                      # noqa: F401
from data_ccxt.bybit import bybit                                # noqa: F401
from data_ccxt.bytetrade import bytetrade                        # noqa: F401
from data_ccxt.cdax import cdax                                  # noqa: F401
from data_ccxt.cex import cex                                    # noqa: F401
from data_ccxt.chilebit import chilebit                          # noqa: F401
from data_ccxt.coinbase import coinbase                          # noqa: F401
from data_ccxt.coinbaseprime import coinbaseprime                # noqa: F401
from data_ccxt.coinbasepro import coinbasepro                    # noqa: F401
from data_ccxt.coincheck import coincheck                        # noqa: F401
from data_ccxt.coinegg import coinegg                            # noqa: F401
from data_ccxt.coinex import coinex                              # noqa: F401
from data_ccxt.coinfalcon import coinfalcon                      # noqa: F401
from data_ccxt.coinfloor import coinfloor                        # noqa: F401
from data_ccxt.coingi import coingi                              # noqa: F401
from data_ccxt.coinmarketcap import coinmarketcap                # noqa: F401
from data_ccxt.coinmate import coinmate                          # noqa: F401
from data_ccxt.coinone import coinone                            # noqa: F401
from data_ccxt.coinspot import coinspot                          # noqa: F401
from data_ccxt.crex24 import crex24                              # noqa: F401
from data_ccxt.currencycom import currencycom                    # noqa: F401
from data_ccxt.delta import delta                                # noqa: F401
from data_ccxt.deribit import deribit                            # noqa: F401
from data_ccxt.digifinex import digifinex                        # noqa: F401
from data_ccxt.equos import equos                                # noqa: F401
from data_ccxt.eterbase import eterbase                          # noqa: F401
from data_ccxt.exmo import exmo                                  # noqa: F401
from data_ccxt.exx import exx                                    # noqa: F401
from data_ccxt.fcoin import fcoin                                # noqa: F401
from data_ccxt.fcoinjp import fcoinjp                            # noqa: F401
from data_ccxt.flowbtc import flowbtc                            # noqa: F401
from data_ccxt.foxbit import foxbit                              # noqa: F401
from data_ccxt.ftx import ftx                                    # noqa: F401
from data_ccxt.gateio import gateio                              # noqa: F401
from data_ccxt.gemini import gemini                              # noqa: F401
from data_ccxt.gopax import gopax                                # noqa: F401
from data_ccxt.hbtc import hbtc                                  # noqa: F401
from data_ccxt.hitbtc import hitbtc                              # noqa: F401
from data_ccxt.hollaex import hollaex                            # noqa: F401
from data_ccxt.huobijp import huobijp                            # noqa: F401
from data_ccxt.huobipro import huobipro                          # noqa: F401
from data_ccxt.idex import idex                                  # noqa: F401
from data_ccxt.independentreserve import independentreserve      # noqa: F401
from data_ccxt.indodax import indodax                            # noqa: F401
from data_ccxt.itbit import itbit                                # noqa: F401
from data_ccxt.kraken import kraken                              # noqa: F401
from data_ccxt.kucoin import kucoin                              # noqa: F401
from data_ccxt.kuna import kuna                                  # noqa: F401
from data_ccxt.lakebtc import lakebtc                            # noqa: F401
from data_ccxt.latoken import latoken                            # noqa: F401
from data_ccxt.lbank import lbank                                # noqa: F401
from data_ccxt.liquid import liquid                              # noqa: F401
from data_ccxt.luno import luno                                  # noqa: F401
from data_ccxt.lykke import lykke                                # noqa: F401
from data_ccxt.mercado import mercado                            # noqa: F401
from data_ccxt.mixcoins import mixcoins                          # noqa: F401
from data_ccxt.ndax import ndax                                  # noqa: F401
from data_ccxt.novadax import novadax                            # noqa: F401
from data_ccxt.oceanex import oceanex                            # noqa: F401
from data_ccxt.okcoin import okcoin                              # noqa: F401
from data_ccxt.okex import okex                                  # noqa: F401
from data_ccxt.paymium import paymium                            # noqa: F401
from data_ccxt.phemex import phemex                              # noqa: F401
from data_ccxt.poloniex import poloniex                          # noqa: F401
from data_ccxt.probit import probit                              # noqa: F401
from data_ccxt.qtrade import qtrade                              # noqa: F401
from data_ccxt.rightbtc import rightbtc                          # noqa: F401
from data_ccxt.ripio import ripio                                # noqa: F401
from data_ccxt.southxchange import southxchange                  # noqa: F401
from data_ccxt.stex import stex                                  # noqa: F401
from data_ccxt.surbitcoin import surbitcoin                      # noqa: F401
from data_ccxt.therock import therock                            # noqa: F401
from data_ccxt.tidebit import tidebit                            # noqa: F401
from data_ccxt.tidex import tidex                                # noqa: F401
from data_ccxt.timex import timex                                # noqa: F401
from data_ccxt.upbit import upbit                                # noqa: F401
from data_ccxt.vbtc import vbtc                                  # noqa: F401
from data_ccxt.vcc import vcc                                    # noqa: F401
from data_ccxt.wavesexchange import wavesexchange                # noqa: F401
from data_ccxt.whitebit import whitebit                          # noqa: F401
from data_ccxt.xbtce import xbtce                                # noqa: F401
from data_ccxt.xena import xena                                  # noqa: F401
from data_ccxt.yobit import yobit                                # noqa: F401
from data_ccxt.zaif import zaif                                  # noqa: F401
from data_ccxt.zb import zb                                      # noqa: F401

exchanges = [
    'aax',
    'aofex',
    'ascendex',
    'bequant',
    'bibox',
    'bigone',
    'binance',
    'binanceus',
    'bit2c',
    'bitbank',
    'bitbay',
    'bitcoincom',
    'bitfinex',
    'bitfinex2',
    'bitflyer',
    'bitforex',
    'bitget',
    'bithumb',
    'bitkk',
    'bitmart',
    'bitmax',
    'bitmex',
    'bitpanda',
    'bitso',
    'bitstamp',
    'bitstamp1',
    'bittrex',
    'bitvavo',
    'bitz',
    'bl3p',
    'bleutrade',
    'braziliex',
    'btcalpha',
    'btcbox',
    'btcmarkets',
    'btctradeua',
    'btcturk',
    'buda',
    'bw',
    'bybit',
    'bytetrade',
    'cdax',
    'cex',
    'chilebit',
    'coinbase',
    'coinbaseprime',
    'coinbasepro',
    'coincheck',
    'coinegg',
    'coinex',
    'coinfalcon',
    'coinfloor',
    'coingi',
    'coinmarketcap',
    'coinmate',
    'coinone',
    'coinspot',
    'crex24',
    'currencycom',
    'delta',
    'deribit',
    'digifinex',
    'equos',
    'eterbase',
    'exmo',
    'exx',
    'fcoin',
    'fcoinjp',
    'flowbtc',
    'foxbit',
    'ftx',
    'gateio',
    'gemini',
    'gopax',
    'hbtc',
    'hitbtc',
    'hollaex',
    'huobijp',
    'huobipro',
    'idex',
    'independentreserve',
    'indodax',
    'itbit',
    'kraken',
    'kucoin',
    'kuna',
    'lakebtc',
    'latoken',
    'lbank',
    'liquid',
    'luno',
    'lykke',
    'mercado',
    'mixcoins',
    'ndax',
    'novadax',
    'oceanex',
    'okcoin',
    'okex',
    'paymium',
    'phemex',
    'poloniex',
    'probit',
    'qtrade',
    'rightbtc',
    'ripio',
    'southxchange',
    'stex',
    'surbitcoin',
    'therock',
    'tidebit',
    'tidex',
    'timex',
    'upbit',
    'vbtc',
    'vcc',
    'wavesexchange',
    'whitebit',
    'xbtce',
    'xena',
    'yobit',
    'zaif',
    'zb',
]

base = [
    'Exchange',
    'exchanges',
    'decimal_to_precision',
]

__all__ = base + errors.__all__ + exchanges
