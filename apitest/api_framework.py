import http.client
import subprocess
import json
import os
from . import request_get
# import request_get

def generate_payload(personal_email="john.walker@gmail.com", city="Seattle", country_code="US", postcode="98104", state="Washington", \
                    street_address="412 5th Avenue", account_currency="USD", local_clearing_system="ACH", company_name="ABC University", \
                    entity_type="COMPANY", nickname="ABC University", **kwargs):
    account_name = kwargs["account_name"]
    account_number = kwargs["account_number"]
    account_routing_type1 = kwargs["account_routing_type1"]
    account_routing_value1 = kwargs["account_routing_value1"]
    bank_country_code = kwargs["bank_country_code"]
    bank_name = kwargs["bank_name"]
    payment_methods = kwargs["payment_methods"]
    
    payload = {
        'beneficiary': {
            'additional_info': {'personal_email': personal_email},
            'address': {
                'city': city,
                'country_code': country_code,
                'postcode': postcode,
                'state': state,
                'street_address': street_address},
            'bank_details': {
                'account_currency': account_currency,
                'account_name': account_name,
                'account_number': account_number,
                'account_routing_type1': account_routing_type1,
                'account_routing_value1': account_routing_value1,
                'bank_country_code': bank_country_code,
                'bank_name': bank_name,
                'local_clearing_system': local_clearing_system},
            'company_name': company_name,
            'entity_type': entity_type},
            'nickname': nickname,
            'payment_methods': [payment_methods]
    }

    if payment_methods == "SWIFT":
        payload['beneficiary']["bank_details"]["swift_code"] = kwargs["swift_code"]

    return json.dumps(payload)

def new_token():
    token_headers = {'Content-Type': 'application/json', 'x-client-id': '0b78wd6hRICXIuzuRzekqw', 'x-api-key': 'dfca479aba6b9dfa96b56afcf52cee9e026e292e1e83050de3f4e50d86a4dec7798d286ed721a9c999ab69f00de1ddfa'}
    token_tmp, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/authentication/login", '', token_headers)
    token = ""
    if "token" in token_tmp:
        token = token_tmp.split(":")[1].split("}")[0].strip('"')
    return token

def generate_headers():
    # token = token_get(request_token)
    token = new_token()
    headers = {
    "Authorization": "Bearer %s" % token,
    "Content-Type": "application/json",
    "headers": """{
    "description": "headers",
    "in": "header",
    "items": {
      "{field_path}": {
      }
    },
    "name": "headers",
    "required": "true"
    }"""
    }
    return headers

def framework_run():
    """api test run"""
    payload = generate_payload(account_name="Lee Da Ming", account_number="12750852", account_routing_type1="bsb", account_routing_value1="083064", \
                               bank_country_code="AU", bank_name="National Australia Bank", payment_methods="SWIFT", swift_code="NATAAU3302S")
    # (account_name="John Walker", account_number="50001121", account_routing_type1="aba", account_routing_value1="021000021", \
                              #  bank_country_code="US", bank_name="JP Morgan Chase Bank", payment_methods="LOCAL") 
    headers = generate_headers()
    data, status = request_get.request_get("api-demo.airwallex.com", "/api/v1/beneficiaries/create", payload, headers)
    print(status)
    dict_data = json.loads(data)
    if "beneficiary" in dict_data.keys():
      print(dict_data['beneficiary']['bank_details']['account_routing_type1'])
    return data

# print(framework_run())
# /Users/liang/Library/Python/3.9/bin/pytest --version
