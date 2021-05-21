# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from data_ccxt.ascendex import ascendex


class bitmax(ascendex):

    def describe(self):
        return self.deep_extend(super(bitmax, self).describe(), {
            'id': 'bitmax',
            'name': 'BitMax',
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/66820319-19710880-ef49-11e9-8fbe-16be62a11992.jpg',
                'api': 'https://bitmax.io',
                'test': 'https://bitmax-test.io',
                'www': 'https://bitmax.io',
                'doc': [
                    'https://bitmax-exchange.github.io/bitmax-pro-api/#bitmax-pro-api-documentation',
                ],
                'fees': 'https://bitmax.io/#/feeRate/tradeRate',
                'referral': 'https://bitmax.io/#/register?inviteCode=EL6BXBQM',
            },
        })
