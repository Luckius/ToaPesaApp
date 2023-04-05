import requests
from flask import Flask,request,jsonify,json


def sendSms(phoneNo,message):
	URL = "https://apisms.beem.africa/v1/send"
	api_key = "4b983184ce90ce55"
	secret_key = "M2I0MDI3YTAxYzQwY2RiNWFmODNkMGUxMzE5ZGQ4ZGVkOTEzNTIzODRiM2QzZmJjOTYwNjRiZWVmZTU5YTNiOA=="
	secret_key2 = "NWYwOTU4ZDM1ZDgwM2ZlYzpNamhsTUdGbFkyWXpObUk1TVRZd01qZzRZamhtWW1GbU5HSTJOakZsTnprMU16WXlaRFJsTTJOa09HWXdZamd3TlRZeU1HUm1aRFUwTldGa05qSTBOZz09"
	content_type = "application/json"
	source_addr = "INFO"
	apikey_and_apisecret = api_key + ":" + secret_key
	first_request = requests.post(url = URL,data = json.dumps({
		"source_addr": source_addr,
		"schedule_time": "",
		"encoding": 0,
		"message": message,
		"recipients": [
		{
			"recipient_id": 1,
			"dest_addr": phoneNo,
		},
		],
		}),
    headers = {
    	"Content-Type": content_type,
    	"Authorization": "Basic " + api_key + ":" + secret_key2,
        },
    auth=(api_key,secret_key),verify=False)
    #print(first_request.status_code)

#sendSms("255753646868","Testing")