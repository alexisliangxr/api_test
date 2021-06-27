import http.client
import subprocess
import json
import os

# request_token = "curl -s --location --request POST 'https://api-demo.airwallex.com/api/v1/authentication/login'  --header 'Content-Type: application/json'  --header 'x-client-id: 0b78wd6hRICXIuzuRzekqw'  --header 'x-api-key: dfca479aba6b9dfa96b56afcf52cee9e026e292e1e83050de3f4e50d86a4dec7798d286ed721a9c999ab69f00de1ddfa' --data-raw ''"

def request_get(url, dir, body, headers):
    conn = http.client.HTTPSConnection(url)
    conn.request("POST", dir, body=body, headers=headers)
    res = conn.getresponse()
    data = res.read()
    status = res.status
    data = data.decode("utf-8")
    return data, status

def exec_shell(shell_str):
    try:
        res = os.popen(shell_str).read() 
        return res
    except Exception as e:
        print("error is: %s" % e)

def token_get(request_token):
    result = ""
    try:
        res = exec_shell(request_token)
        if "token" in res:
            result = res.split(":")[1].split("}")[0].strip('"')
            return result
    except Exception as e:
        print("Request token failed, error is: %s" % e)
        return result


