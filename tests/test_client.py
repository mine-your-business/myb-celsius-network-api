import pytest
import os
import datetime
import json

from celsius_network import CelsiusNetworkApi

@pytest.fixture(scope='module')
def client():
    return CelsiusNetworkApi(
        celsius_partner_token=os.environ.get('CELSIUS_NETWORK_PARTNER_TOKEN'),
        user_api_key=os.environ.get('CELSIUS_NETWORK_API_KEY'),
        api_url="https://wallet-api.staging.celsius.network"
    )

# At this time, I cannot find a way to generate Staging credentials to run these tests in an
# automated fashion, so they are commented out

@pytest.mark.usefixtures('client')
class TestClient(object):

    # def test_get_balance_summary_gets_summary(self, client):
    #     balance_summary = client.get_balance_summary()
    #     print(json.dumps(balance_summary, indent=2))
    #     assert balance_summary is not None
    #     # Spot-check a couple of crypto
    #     assert balance_summary.get('balance') is not None
    #     assert balance_summary['balance'].get('eth') is not None
    #     assert balance_summary['balance'].get('btc') is not None
    
    # def test_get_balance_coin_gets_balance(self, client):
    #     coin = 'ETH'
    #     balance_coin = client.get_balance_coin(coin)
    #     print(json.dumps(balance_coin, indent=2))
    #     assert balance_coin is not None
    #     assert balance_coin.get('amount') is not None
    #     assert balance_coin.get('amount_in_usd') is not None
    
    # def test_get_transactions_summary_gets_summary(self, client):
    #     page = 1
    #     per_page = 2
    #     transactions_summary = client.get_transactions_summary(page, per_page)
    #     print(json.dumps(transactions_summary, indent=2))
    #     assert transactions_summary is not None
    #     assert transactions_summary.get('pagination') is not None
    #     assert transactions_summary['pagination'].get('current') == page
    #     assert transactions_summary['pagination'].get('per_page') == per_page
    #     assert transactions_summary.get('record') is not None
    
    # def test_get_transactions_for_coin_gets_transactions(self, client):
    #     coin = 'ETH'
    #     page = 999
    #     transactions_coin = client.get_transactions_for_coin(coin, page)
    #     print(json.dumps(transactions_coin, indent=2))
    #     assert transactions_coin is not None
    #     assert transactions_coin.get('pagination') is not None
    #     assert transactions_coin['pagination'].get('current') == page
    #     assert transactions_coin.get('record') is not None
    
    # def test_get_deposit_address_for_coin_gets_deposit_address(self, client):
    #     coin = 'ETH'
    #     deposit_address = client.get_deposit_address_for_coin(coin)
    #     print(json.dumps(deposit_address, indent=2))
    #     assert deposit_address is not None
    #     assert deposit_address.get('address') is not None
    
    # def test_withdraw_coin_succeeds(self, client):
    #     ""

    # def test_get_withdrawal_transaction_id_succeeds(self, client):
    #     ""

    # This test doesn't require authentication - auth headers are ignored
    def test_get_interest_rates_gets_rates(self, client):
        rates = client.get_interest_rates()
        print(json.dumps(rates, indent=2))
        assert rates is not None
        assert rates.get('interestRates') is not None
        # Verify an arbitrary rate        
        assert rates['interestRates'][0].get('coin') is not None
        assert rates['interestRates'][0].get('rate') is not None
        assert rates['interestRates'][0].get('currency') is not None
        assert rates['interestRates'][0]['currency'].get('id') is not None
        assert rates['interestRates'][0]['currency'].get('name') is not None
        assert rates['interestRates'][0]['currency'].get('short') is not None
        assert rates['interestRates'][0]['currency'].get('image_url') is not None
