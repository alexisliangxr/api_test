import pytest
import os
import sys
import json
from ..apitest import api_framework
from ..apitest import request_get

def setup_function():
    """ init setup """
    sys.argv = [__file__]
    print("-------setup------")

def test_swift_code_positive():
    payload = api_framework.generate_payload(account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="SWIFT")
    headers = api_framework.generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    dict_data = json.loads(data)

    assert status == 201

def test_aba_positive():
    payload = api_framework.generate_payload(account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = api_framework.generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    dict_data = json.loads(data)
    
    if dict_data['beneficiary']['bank_details']['bank_country_code'] == "US":
        assert dict_data['beneficiary']['bank_details']['account_routing_type1'] == "aba"
        assert len(dict_data['beneficiary']['bank_details']['account_routing_value1']) == 9
    assert status == 201

def test_bsb_positive():
    payload = api_framework.generate_payload(account_name="Lee Da Ming", account_number="12750852", account_routing_type1="bsb", account_routing_value1="083064", \
                               bank_country_code="AU", bank_name="National Australia Bank", payment_methods="LOCAL")
    headers = api_framework.generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    
    dict_data = json.loads(data)
    assert status == 201
    if "beneficiary" in dict_data.keys():
        if dict_data['beneficiary']['bank_details']['bank_country_code'] == "AU":
            assert dict_data['beneficiary']['bank_details']['account_routing_type1'] == "bsb"
            assert len(dict_data['beneficiary']['bank_details']['account_routing_value1']) == 6

    