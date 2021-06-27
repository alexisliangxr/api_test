import pytest
import os
import sys
import json
from ..apitest.api_framework import generate_payload, generate_headers
from ..apitest import request_get

def setup_function():
    """ init setup """
    sys.argv = [__file__]
    print("-------setup------")

def test_payment_nethod_positive1():
    payload = generate_payload(account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 201

def test_payment_nethod_positive2():
    payload = generate_payload(account_name="John Walker", account_number="AAaa19A", account_routing_type1="bsb", account_routing_value1="021000021", \
                               bank_country_code="AU", bank_name="JP Morgan Chase Bank", payment_methods="SWIFT", swift_code="NATAAU3302S")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 201

def test_payment_nethod_negative1():
    payload = generate_payload(account_name="John Walker", account_number="AAaa19A", account_routing_type1="bsb", account_routing_value1="021000021", \
                               bank_country_code="AU", bank_name="JP Morgan Chase Bank", payment_methods="AAA", swift_code="NATAAU3302S")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    dict_data = json.loads(data)
    if status == 400:
        assert dict_data['code'] == 'invalid_argument'
        assert dict_data['message'] == 'No enum constant com.airwallex.domain.transaction.payment.PaymentMethod.AAA'
        assert dict_data['source'] == 'payment_methods'
    assert status == 400

def test_payment_nethod_negative2():
    payload = generate_payload(account_name="John Walker", account_number="AAaa19A", account_routing_type1="bsb", account_routing_value1="021000021", \
                               bank_country_code="AU", bank_name="JP Morgan Chase Bank", payment_methods="", swift_code="NATAAU3302S")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    dict_data = json.loads(data)
    # print(dict_data)
    if status == 400:
        assert dict_data['code'] == 'invalid_argument'
        assert dict_data['message'] == 'No enum constant com.airwallex.domain.transaction.payment.PaymentMethod.'
        assert dict_data['source'] == 'payment_methods'
    assert status == 400