from django.shortcuts import render
from API.models import Code
import requests
from requests.auth import HTTPBasicAuth
import json
from django.http import HttpResponse
from .mpesa import MpesaToken
# Create your views here.
def index(request):
    qr = Code.objects.all()
    context = {
        'qr' : qr,
    }
    return render(request, 'API/index.html', context)

def getToken(request):
    consumer_key = "7TTD0aMGv0ARkAjMFCAdblAUDBvTdpcM"
    consumer_secret = "HL32esQQ6Fn0twr9"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)

def Balance(request):
    access_token = MpesaToken.validated_mpesa_access_token

    api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = { "Initiator":"georgeey",
      "SecurityCredential":"TRU6o8vGrgE5qd5uveWKB/RAnRaFQofrG/oSuu3q6Lw7LXDKcZfK6Cum6fUAm+A17DSyq+2YjIpWBoGAa/AICSrN0eD4rDU0qs9UUeDLc8tTOi2GZoGxcjg1XzUtav5EC5IOmznr0wtFOLcW/abgRWgjLyykn7LlVCKNieWciaFkpsyUiHXJy+C/Cv35QatL5YeAN4HddnaduKMbrMf+hahbQSsrjBD+PdHZeqPuHXBiLy1EcRTVrGFXMftqhT8+TpJHq8TGg/zbJuctb2WcaGAhpqjgIJvg5KjwnbB65gFbxFGBBdedS58b/IAXyqLdio0BrPWvlT9rKxB6sebDcg==",
      "CommandID":"AccountBalance",
      "PartyA":"174379",
      "IdentifierType":"4",
      "Remarks":"first trial is a success",
      "QueueTimeOutURL":"http://portfoliombugua.herokuapp.com/",
      "ResultURL":"http://portfoliombugua.herokuapp.com/"
      }

    response = requests.post(api_url, json = request, headers=headers)
    return HttpResponse(response.text)