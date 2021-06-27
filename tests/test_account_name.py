import pytest
import os
import sys
from ..apitest.api_framework import generate_payload, generate_headers
from ..apitest import request_get

def setup_function():
    """ init setup """
    sys.argv = [__file__]
    print("-------setup------")

def test_account_name_positive():
    payload = generate_payload(account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 201

def test_account_name_negative1():
    payload = generate_payload(account_name="A", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    assert status == 400

def test_account_name_negative2():
    payload = generate_payload(account_name="AAAAAAAAAAB11111110", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                               bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL")
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    print(data)
    assert status == 400


