import requests
from requests.auth import HTTPBasicAuth
import json

class MpesaCredential:
    consumer_key = "7TTD0aMGv0ARkAjMFCAdblAUDBvTdpcM"
    consumer_secret = "HL32esQQ6Fn0twr9"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

class MpesaToken:
    r = requests.get(MpesaCredential.api_URL, auth=HTTPBasicAuth(MpesaCredential.consumer_key, MpesaCredential.consumer_secret))

    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']