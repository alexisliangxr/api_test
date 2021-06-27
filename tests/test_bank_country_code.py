import pytest
import json
import os
import sys
from ..apitest.api_framework import generate_payload, generate_headers
from ..apitest import request_get

def setup_function():
    """ init setup """
    sys.argv = [__file__]
    print("-------setup------")

def test_bank_country_code_positive1():
    payload = generate_payload(account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 201

def test_bank_country_code_positive2():
    payload = generate_payload(account_name="John Walker", account_number="AAaa19A", account_routing_type1="bsb", account_routing_value1="021000021", \
                               bank_country_code="AU", bank_name="JP Morgan Chase Bank", payment_methods="SWIFT", swift_code="NATAAU3302S")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 201

def test_bank_country_code_positive3():
    payload = generate_payload(account_name="John Walker", account_number="44250100003700000259", account_routing_type1="cnaps", account_routing_value1="021000021", \
                               bank_country_code="CN", bank_name="JP Morgan Chase Bank", payment_methods="SWIFT", swift_code="PCBCCNBJSZX")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 201

def test_bank_country_code_negative1():
    payload = generate_payload(account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="USSS", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 400

def test_bank_country_code_negative2():
    payload = generate_payload(account_name="John Walker", account_number="AAaa19A", account_routing_type1="bsb", account_routing_value1="021000021", \
                               bank_country_code="AUUUUU", bank_name="JP Morgan Chase Bank", payment_methods="SWIFT", swift_code="NATAAU3302S")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    dict_data = json.loads(data)
    if status == 400:
        assert dict_data['code'] == 'invalid_argument'
        assert dict_data['message'] == 'AUUUUU is not a valid type'
        assert dict_data['source'] == 'beneficiary.bank_details.bank_country_code'
    assert status == 400