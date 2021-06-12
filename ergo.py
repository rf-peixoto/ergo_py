from pycoingecko import CoinGeckoAPI
import requests
import json

class ErgoAPI:
    def __init__(self) -> None:
        """ Initialize API """
        self.coingecko = CoinGeckoAPI()
        self.main_url = 'https://api.ergoplatform.com'
        self.address_url = '/api/v0/addresses/'
        self.issuing_boxes_url = '/api/v0/assets/issuingBoxes'
        self.tx_url = '/api/v0/transactions/'
        self.block_url = '/api/v0/blocks/'
        self.info_url = '/api/v0/info'
        self.status_url = '/api/v0/stats'
        self.tokens_url = '/api/v1/tokens'
        self.boxes_unspent_byTokenId = '/api/v1/boxes/unspent/byTokenId/'
        self.boxes_byTokenId = '/api/v1/boxes/byTokenId/'
        self.donate_address = '9ftyziirHpu7PqPkdTG8jvxNDhb44tGL34mbHan2aKWCP4vfrDX'
        self.ergo_links = {'site':'https://ergoplatform.org/', 'documents':'https://ergoplatform.org/en/documents/',
                           'forum':'https://www.ergoforum.org/', 'faq':'https://ergoplatform.org/en/faq/',
                           'mining':'https://ergoplatform.org/en/mining/', 'get_started':'https://ergoplatform.org/en/about/',
                           'basics':'https://ergoplatform.org/en/basics/', 'wallets':'https://ergoplatform.org/en/wallets/',
                           'news':'https://ergoplatform.org/en/news/', 'blog':'https://ergoplatform.org/en/blog/',
                           'code':'https://github.com/ergoplatform', 'awesome-ergo':'https://github.com/ergoplatform/awesome-ergo',
                           'explorer':'https://explorer.ergoplatform.com/en/'}
        
    def get_current_price(self, symbol:str) -> float:
        """ Get ERG price
        :param str symbol: Currency symbol. Ex: 'usd', 'eur', 'jpy', 'btc'... """
        try:
            return self.coingecko.get_price(ids='ergo', vs_currencies=symbol)['ergo'][symbol]
        except Exception as error:
            print(error)

    def get_historical_data(from_ts:str, to_ts:str, symbol:str) -> dict:
        """ Get historical data
        :param str from_ts: Initial date in timestamp
        :param str to_s: End date in timestamp
        :param str symbol: Currency symbol (usd, eur...) """
        try:
            return json.loads(ergo.coingecko.get_coin_market_chart_range_by_id(id='ergo', vs_currency=symbol,
                                                                               from_timestamp=from_ts,
                                                                               to_timestamp=to_ts))
        except Exception as error:
            print(error)

    def get_complete_address(self, address:str) -> dict:
        """ Get complete info about a address
        :param str address: Address """
        try:
            url = self.main_url + self.address_url
            response = requests.get(url + address)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_address_balance(self, address:str) -> dict:
        """ Get address confirmed balance
        :param str address: Address """
        try:
            url = self.main_url + self.address_url
            response = requests.get(url + address)
            return json.loads(response.content.decode())['transactions']['confirmedBalance']
        except Exception as error:
            print(error)

    def get_transaction(self, transaction:str) -> dict:
        """ Get transaction data
        :param str transaction: Transaction Hash """
        try:
            url = self.main_url + self.tx_url
            response = requests.get(url + transaction)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_transaction_confirmations(self, transaction:str) -> int:
        """ Get number of confirmations of a transaction
        :param str transaction: Transaction Hash """
        try:
            url = self.main_url + self.tx_url
            response = requests.get(url + transaction)
            return json.loads(response.content.decode())['summary']['confirmationsCount']
        except Exception as error:
            print(error)

    def get_complete_block(self, block:str) -> dict:
        """ Get block data
        :param str block: Block """
        try:
            url = self.main_url + self.block_url
            response = requests.get(url + block)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_block_ref(self, block:str) -> dict:
        """ Get block references
        :param str block: Block """
        try:
            url = self.main_url + self.block_url
            response = requests.get(url + block)
            return json.loads(response.content.decode())['references']
        except Exception as error:
            print(error)

    def get_blockchain_info(self) -> dict:
        """ Get blockchain info like hashrate, supply, etc"""
        try:
            response = requests.get(self.main_url + self.info_url)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_tokens(self) -> dict:
        """ Get tokens"""
        try:
            response = requests.get(self.main_url + self.tokens_url)
            return json.loads(response.content.decode())['items']
        except Exception as error:
            print(error)

    def get_total_tokens(self) -> int:
        """ Get total number of tokens"""
        try:
            response = requests.get(self.main_url + self.tokens_url)
            return json.loads(response.content.decode())['total']
        except Exception as error:
            print(error)

    def get_hash_rate(self) -> int:
        """ Get actual hashrate"""
        try:
            response = requests.get(self.main_url + self.info_url)
            return json.loads(response.content.decode())['hashRate']
        except Exception as error:
            print(error)

    def get_issuing_boxes(self) -> dict:
        """ Get issuing boxes"""
        try:
            response = requests.get(self.main_url + self.issuing_boxes_url)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_supply(self) -> int:
        """ Get actual supply"""
        try:
            response = requests.get(self.main_url + self.info_url)
            return json.loads(response.content.decode())['supply']
        except Exception as error:
            print(error)

    def get_boxes_unspent_byTokenId(self, TokenId:str) -> dict:
        """ Get complete info about unspent boxes by TokenId
        :param str TokenId: TokenId """
        try:
            url = self.main_url + self.boxes_unspent_byTokenId
            response = requests.get(url + TokenId)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)

    def get_boxes_byTokenId(self, TokenId:str) -> dict:
        """ Get complete info about boxes by TokenId
        :param str TokenId: TokenId """
        try:
            url = self.main_url + self.boxes_byTokenId
            response = requests.get(url + TokenId)
            return json.loads(response.content.decode())
        except Exception as error:
            print(error)
