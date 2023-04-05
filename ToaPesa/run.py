from portalsdk import APIContext, APIMethodType, APIRequest
from time import sleep
import smtplib
import imghdr
from email.message import EmailMessage
from flask import Flask,render_template,json,jsonify,make_response,request
import random
import string
import requests


app = Flask(__name__)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def sendMyMail(head,body):
	EMAIL_ADDRESS = "homemetatz@gmail.com"
	EMAIL_PASSWORD = "dujfsqncjmgnsply"
	Port = 465
	M_Smtp = 'smtp.gmail.com'
	contacts = ['luckiusevodius@gmail.com','alawikajoka5@gmail.com']
	msg = EmailMessage()
	msg['Subject'] = head
	msg['From'] = EMAIL_ADDRESS
	msg['To'] = contacts #'luckiusevodius@gmail.com'
	#msg.set_content(data)
	msg.set_content(body)
	with smtplib.SMTP_SSL(M_Smtp, Port) as smtp:
	    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	    smtp.send_message(msg)



#
def sendAdminSms(message):
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
                "dest_addr": "255753646868",
            },
            {
                    "recipient_id": 2,
                    "dest_addr": "255752711043",
            }
		],
		}),
    headers = {
    	"Content-Type": content_type,
    	"Authorization": "Basic " + api_key + ":" + secret_key2,
        },
    auth=(api_key,secret_key),verify=False)
    #print(first_request.status_code)


def sendClientSms(phoneNo,message):
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



@app.route("/",methods=['GET', 'POST'])
def index():
	return render_template("index.html")


@app.route("/addmoney",methods=['GET', 'POST'])
def addmoney():
	return render_template("addMoney.html")



@app.route("/apiSandBox/<data>",methods=['GET', 'POST'])
def apiSandBox(data):
    if request.method == "POST":
        data_list = data.split("=")
        print(data_list)
        # Public key on the API listener used to encrypt keys
        public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArv9yxA69XQKBo24BaF/D+fvlqmGdYjqLQ5WtNBb5tquqGvAvG3WMFETVUSow/LizQalxj2ElMVrUmzu5mGGkxK08bWEXF7a1DEvtVJs6nppIlFJc2SnrU14AOrIrB28ogm58JjAl5BOQawOXD5dfSk7MaAA82pVHoIqEu0FxA8BOKU+RGTihRU+ptw1j4bsAJYiPbSX6i71gfPvwHPYamM0bfI4CmlsUUR3KvCG24rB6FNPcRBhM3jDuv8ae2kC33w9hEq8qNB55uw51vK7hyXoAa+U7IqP1y6nBdlN25gkxEA8yrsl1678cspeXr+3ciRyqoRgj9RD/ONbJhhxFvt1cLBh+qwK2eqISfBb06eRnNeC71oBokDm3zyCnkOtMDGl7IvnMfZfEPFCfg5QgJVk1msPpRvQxmEsrX9MQRyFVzgy2CWNIb7c+jPapyrNwoUbANlN8adU1m6yOuoX7F49x+OjiG2se0EJ6nafeKUXw/+hiJZvELUYgzKUtMAZVTNZfT8jjb58j8GVtuS+6TM2AutbejaCV84ZK58E2CRJqhmjQibEUO6KPdD7oTlEkFy52Y1uOOBXgYpqMzufNPmfdqqqSM4dU70PO8ogyKGiLAIxCetMjjm6FCMEA3Kc8K0Ig7/XtFm9By6VxTJK1Mg36TlHaZKP6VzVLXMtesJECAwEAAQ=='
        api_context = APIContext()

        MSISDN_Number = data_list[0]
        short_code = "000000"
        amount = data_list[1]
        thirdPartID = "asvui02e5958774f7ba228d83d0d"+id_generator()
        reference_no = id_generator()+"+"+data_list[0]
        ItemDescription = "Software service payments"

        api_context.api_key = 'fIpIa9R3Nr9ge4E8DLJUwFWyq58rYYIf'
        #api_context.api_key = 'bNtMLyXXwXh0nLnEJXBdH65xg8WWjGMQ'

        api_context.public_key = public_key
        # Use ssl/https
        api_context.ssl = True
        api_context.method_type = APIMethodType.GET
        api_context.address = 'openapi.m-pesa.com'
        api_context.port = 443
        api_context.path = '/sandbox/ipg/v2/vodacomTZN/getSession/'
        #api_context.path = '/openapi/ipg/v2/vodacomTZN/getSession/'

        # Add/update headers
        api_context.add_header('Origin', '*')

        #Do the API call and put result in a response packet
        api_request = APIRequest(api_context)

        # Do the API call and put result in a response packet
        result = None
        try:
            result = api_request.execute()
        except Exception as e:
            print('Call Failed: ' + e)

        if result is None:
            raise Exception('SessionKey call failed to get result. Please check.')

        # Display results
        #print(reference_no)
        #print(result.status_code)
        #print(result.headers)
        #print(result.body)

        # The above call issued a sessionID which will be used as the API key in calls that needs the sessionID
        api_context = APIContext()
        api_context.api_key = result.body['output_SessionID']
        api_context.public_key = public_key
        api_context.ssl = True
        api_context.method_type = APIMethodType.POST
        api_context.address = 'openapi.m-pesa.com'
        api_context.port = 443
        api_context.path = '/sandbox/ipg/v2/vodacomTZN/c2bPayment/singleStage/'
        #api_context.path = '/openapi/ipg/v2/vodacomTZN/c2bPayment/singleStage/'

        api_context.add_header('Origin', '*')

        api_context.add_parameter('input_Amount', amount)
        api_context.add_parameter('input_Country', 'TZN')
        api_context.add_parameter('input_Currency', 'TZS')
        api_context.add_parameter('input_CustomerMSISDN', MSISDN_Number)
        api_context.add_parameter('input_ServiceProviderCode', short_code)
        api_context.add_parameter('input_ThirdPartyConversationID', thirdPartID)
        api_context.add_parameter('input_TransactionReference', reference_no)
        api_context.add_parameter('input_PurchasedItemsDesc', ItemDescription)

        api_request = APIRequest(api_context)

        # SessionID can take up to 30 seconds to become 'live' in the system and will be invalid until it is
        sleep(1)

        result = None
        try:
            result = api_request.execute()
        except Exception as e:
            print('Call Failed: ' + e)

        if result is None:
            raise Exception('API call failed to get result. Please check.')

        print(result.status_code)
        #print(result.headers)
        print((result.body).output_ResponseDesc) 
        response = jsonify({'code': result.status_code,'body':result.body})
        return response




@app.route("/openAPI/<data>",methods=['GET', 'POST'])
def openAPI(data):
    if request.method == "POST":
        data_list = data.split("=")
        print(data_list)
        # Public key on the API listener used to encrypt keys
        public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAietPTdEyyoV/wvxRjS5pSn3ZBQH9hnVtQC9SFLgM9IkomEX9Vu9fBg2MzWSSqkQlaYIGFGH3d69Q5NOWkRo+Y8p5a61sc9hZ+ItAiEL9KIbZzhnMwi12jUYCTff0bVTsTGSNUePQ2V42sToOIKCeBpUtwWKhhW3CSpK7S1iJhS9H22/BT/pk21Jd8btwMLUHfVD95iXbHNM8u6vFaYuHczx966T7gpa9RGGXRtiOr3ScJq1515tzOSOsHTPHLTun59nxxJiEjKoI4Lb9h6IlauvcGAQHp5q6/2XmxuqZdGzh39uLac8tMSmY3vC3fiHYC3iMyTb7eXqATIhDUOf9mOSbgZMS19iiVZvz8igDl950IMcelJwcj0qCLoufLE5y8ud5WIw47OCVkD7tcAEPmVWlCQ744SIM5afw+Jg50T1SEtu3q3GiL0UQ6KTLDyDEt5BL9HWXAIXsjFdPDpX1jtxZavVQV+Jd7FXhuPQuDbh12liTROREdzatYWRnrhzeOJ5Se9xeXLvYSj8DmAI4iFf2cVtWCzj/02uK4+iIGXlX7lHP1W+tycLS7Pe2RdtC2+oz5RSSqb5jI4+3iEY/vZjSMBVk69pCDzZy4ZE8LBgyEvSabJ/cddwWmShcRS+21XvGQ1uXYLv0FCTEHHobCfmn2y8bJBb/Hct53BaojWUCAwEAAQ=='
        api_context = APIContext()
        MSISDN_Number = data_list[0]
        short_code = "305533"
        amount = data_list[1]
        thirdPartID = "asvui02e5958774f7ba228d83d0d"+id_generator()
        reference_no = "Pesa_Cash_"+id_generator()
        #reference_no = id_generator()+"+"+data_list[0]
        ItemDescription = "Software service payments"
        api_context.api_key = '6jk0eDdtcvnDCytsg11nTRv2yvRB4oyA'
        api_context.public_key = public_key
        # Use ssl/https
        api_context.ssl = True
        api_context.method_type = APIMethodType.GET
        api_context.address = 'openapi.m-pesa.com'
        api_context.port = 443
        api_context.path = '/openapi/ipg/v2/vodacomTZN/getSession/'
        #api_context.path = '/openapi/ipg/v2/vodacomTZN/getSession/'
        api_context.add_header('Origin', '*')
        api_request = APIRequest(api_context)
        # Do the API call and put result in a response packet
        result = None
        try:
            result = api_request.execute()
        except Exception as e:
            print('Call Failed: ' + e)

        if result is None:
            raise Exception('SessionKey call failed to get result. Please check.')

        print(result.body)
        # The above call issued a sessionID which will be used as the API key in calls that needs the sessionID
        response = jsonify({'code': result.status_code,'body':result.body,'sessionID':result.body['output_SessionID']})
        return response








@app.route("/openAPIResult/<data>",methods=['GET', 'POST'])
def openAPIResult(data):
    if request.method == "POST":
        data_list = data.split("=")
        print(data_list)
        public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAietPTdEyyoV/wvxRjS5pSn3ZBQH9hnVtQC9SFLgM9IkomEX9Vu9fBg2MzWSSqkQlaYIGFGH3d69Q5NOWkRo+Y8p5a61sc9hZ+ItAiEL9KIbZzhnMwi12jUYCTff0bVTsTGSNUePQ2V42sToOIKCeBpUtwWKhhW3CSpK7S1iJhS9H22/BT/pk21Jd8btwMLUHfVD95iXbHNM8u6vFaYuHczx966T7gpa9RGGXRtiOr3ScJq1515tzOSOsHTPHLTun59nxxJiEjKoI4Lb9h6IlauvcGAQHp5q6/2XmxuqZdGzh39uLac8tMSmY3vC3fiHYC3iMyTb7eXqATIhDUOf9mOSbgZMS19iiVZvz8igDl950IMcelJwcj0qCLoufLE5y8ud5WIw47OCVkD7tcAEPmVWlCQ744SIM5afw+Jg50T1SEtu3q3GiL0UQ6KTLDyDEt5BL9HWXAIXsjFdPDpX1jtxZavVQV+Jd7FXhuPQuDbh12liTROREdzatYWRnrhzeOJ5Se9xeXLvYSj8DmAI4iFf2cVtWCzj/02uK4+iIGXlX7lHP1W+tycLS7Pe2RdtC2+oz5RSSqb5jI4+3iEY/vZjSMBVk69pCDzZy4ZE8LBgyEvSabJ/cddwWmShcRS+21XvGQ1uXYLv0FCTEHHobCfmn2y8bJBb/Hct53BaojWUCAwEAAQ=='
        #api_context = APIContext()
        MSISDN_Number = data_list[0]
        short_code = "305533"
        amount = data_list[1]
        thirdPartID = "asvui02e5958774f7ba228d83d0d"+id_generator()
        reference_no = "Pesa_Cash_"+id_generator()
        #reference_no = id_generator()+"+"+data_list[0]
        ItemDescription = "Software service payments"
        #api_context.api_key = '6jk0eDdtcvnDCytsg11nTRv2yvRB4oyA'
        # The above call issued a sessionID which will be used as the API key in calls that needs the sessionID
        api_context = APIContext()
        api_context.api_key = data_list[3] #result.body['output_SessionID']
        api_context.public_key = public_key
        api_context.ssl = True
        api_context.method_type = APIMethodType.POST
        api_context.address = 'openapi.m-pesa.com'
        api_context.port = 443
        api_context.path = '/openapi/ipg/v2/vodacomTZN/c2bPayment/singleStage/'
        #api_context.path = '/openapi/ipg/v2/vodacomTZN/c2bPayment/singleStage/'
        api_context.add_header('Origin', '*')
        api_context.add_parameter('input_Amount', amount)
        api_context.add_parameter('input_Country', 'TZN')
        api_context.add_parameter('input_Currency', 'TZS')
        api_context.add_parameter('input_CustomerMSISDN', MSISDN_Number)
        api_context.add_parameter('input_ServiceProviderCode', short_code)
        api_context.add_parameter('input_ThirdPartyConversationID', thirdPartID)
        api_context.add_parameter('input_TransactionReference', reference_no)
        api_context.add_parameter('input_PurchasedItemsDesc', ItemDescription)
        api_request = APIRequest(api_context)
        # SessionID can take up to 30 seconds to become 'live' in the system and will be invalid until it is
        sleep(1)
        result = None
        try:
            result = api_request.execute()
        except Exception as e:
            print('Call Failed: ' + e)

        if result is None:
            raise Exception('API call failed to get result. Please check.')

        print(result.status_code)
        #print(result.headers)
        print(result.body)
        body_result = result.body

        
        if result.status_code == 201:
            mhead = data_list[0]+" Ametoa Pesa Tshs "+data_list[1]
            mbody = body_result['output_TransactionID'] + " Imethibitishwa mteja mwenye namba "+data_list[0]+" ametoa kiasi cha Tshs "+data_list[1]+" kutoka kwa HOME-META wakala no "+data_list[2]
        else:
            mhead = data_list[0]+" Ametoa Pesa Tshs "+data_list[1]
            mbody = "Imethibitishwa mteja mwenye namba "+data_list[0]+" ametoa kiasi cha Tshs "+data_list[1]+" kutoka kwa HOME-META wakala no "+data_list[2]
        response = jsonify({'code': result.status_code,'body':result.body,'message':mbody,'number':data_list[0],'head':mhead})
        return response



@app.route("/notifications/<data>",methods=['GET', 'POST'])
def notifications(data):
    if request.method == "POST":
        data_list = data.split("=")
        cbody = "Asante kwa kuchagua HOME-META na karibu tena"
        mhead = data_list[1]
        mbody = data_list[2]
        sendMyMail(mhead,mbody)
        sendAdminSms(mbody)
        sendClientSms(data_list[0],cbody)
        return jsonify({'code': 201})





@app.route("/openAPIDeposit/<data>",methods=['GET', 'POST'])
def openAPIDeposit(data):
    if request.method == "POST":
        data_list = data.split("=")
        print(data_list)
        MSISDN_Number = data_list[0]
        short_code = "305533"
        amount = data_list[1]
        thirdPartID = "asvui02e5958774f7ba228d83d0d"+id_generator()
        reference_no = "Pesa_Cash_"+id_generator()
        #reference_no = id_generator()+"+"+data_list[0]
        ItemDescription = "Funds transfers from business"

        # Public key on the API listener used to encrypt keys
        public_key = 'MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAietPTdEyyoV/wvxRjS5pSn3ZBQH9hnVtQC9SFLgM9IkomEX9Vu9fBg2MzWSSqkQlaYIGFGH3d69Q5NOWkRo+Y8p5a61sc9hZ+ItAiEL9KIbZzhnMwi12jUYCTff0bVTsTGSNUePQ2V42sToOIKCeBpUtwWKhhW3CSpK7S1iJhS9H22/BT/pk21Jd8btwMLUHfVD95iXbHNM8u6vFaYuHczx966T7gpa9RGGXRtiOr3ScJq1515tzOSOsHTPHLTun59nxxJiEjKoI4Lb9h6IlauvcGAQHp5q6/2XmxuqZdGzh39uLac8tMSmY3vC3fiHYC3iMyTb7eXqATIhDUOf9mOSbgZMS19iiVZvz8igDl950IMcelJwcj0qCLoufLE5y8ud5WIw47OCVkD7tcAEPmVWlCQ744SIM5afw+Jg50T1SEtu3q3GiL0UQ6KTLDyDEt5BL9HWXAIXsjFdPDpX1jtxZavVQV+Jd7FXhuPQuDbh12liTROREdzatYWRnrhzeOJ5Se9xeXLvYSj8DmAI4iFf2cVtWCzj/02uK4+iIGXlX7lHP1W+tycLS7Pe2RdtC2+oz5RSSqb5jI4+3iEY/vZjSMBVk69pCDzZy4ZE8LBgyEvSabJ/cddwWmShcRS+21XvGQ1uXYLv0FCTEHHobCfmn2y8bJBb/Hct53BaojWUCAwEAAQ=='
        api_context = APIContext()
        #newAPIKey S6BKOtJM4PORDdwVFYIrNieE8EMPO8FL
        api_context.api_key = 'S6BKOtJM4PORDdwVFYIrNieE8EMPO8FL'
        api_context.public_key = public_key
        api_context.ssl = True
        api_context.method_type = APIMethodType.GET
        api_context.address = 'openapi.m-pesa.com'
        api_context.port = 443
        api_context.path = '/openapi/ipg/v2/vodacomTZN/getSession/'

        api_context.add_header('Origin', '*')

        api_request = APIRequest(api_context)
        result = None
        try:
            result = api_request.execute()
        except Exception as e:
            print('Call Failed: ' + e)

        if result is None:
            raise Exception('SessionKey call failed to get result. Please check.')

        print(result.status_code)
        print(result.headers)
        print(result.body)

        api_context = APIContext()
        api_context.api_key = result.body['output_SessionID']
        api_context.public_key = public_key
        api_context.ssl = True
        api_context.method_type = APIMethodType.POST
        api_context.address = 'openapi.m-pesa.com'
        api_context.port = 443
        api_context.path = '/openapi/ipg/v2/vodacomTZN/b2cPayment/'

        api_context.add_header('Origin', '*')

        api_context.add_parameter('input_Amount', amount)
        api_context.add_parameter('input_Country', 'TZN')
        api_context.add_parameter('input_Currency', 'TZS')
        api_context.add_parameter('input_CustomerMSISDN', MSISDN_Number)
        api_context.add_parameter('input_ServiceProviderCode', short_code)
        api_context.add_parameter('input_ThirdPartyConversationID', thirdPartID)
        api_context.add_parameter('input_TransactionReference', reference_no)
        api_context.add_parameter('input_PaymentItemsDesc', ItemDescription)
        
        api_request = APIRequest(api_context)

        # SessionID can take up to 30 seconds to become 'live' in the system and will be invalid until it is
        sleep(1)

        result = None
        try:
            result = api_request.execute()
        except Exception as e:
            print('Call Failed: ' + e)

        if result is None:
            raise Exception('API call failed to get result. Please check.')


        print(result.status_code)
        print(result.headers)
        print(result.body)
        if result.status_code == 201:
            mhead = data_list[0]+" Amewekewa Pesa Tshs "+data_list[1]
            mbody = "Mteja mwenye namba "+data_list[0]+" amewekewa kiasi cha Tshs "+data_list[1]+" kutoka kwa wakala "+data_list[2]
            sendMyMail(mhead,mbody) 
        response = jsonify({'code': result.status_code,'body':result.body})
        return response




if __name__ == "__main__":
	app.run(debug=True)