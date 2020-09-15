# doing necessary imports
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS, cross_origin
import requests
import pymongo
import json
import os
import random
from saveConversation import Conversations
import urllib
from MLDepressionTest import flask_api

from sendEmail import EMailClient


app = Flask(__name__)  # initialising the flask app with the name 'app'


# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST', 'GET'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    res = processRequest(req)
    print(res)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):
    dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
    log = Conversations.Log()
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    intent = result.get("intent").get('displayName')
    parameters = result.get("parameters")
    cust_name = parameters.get("cust_name")
    cust_phone = parameters.get("cust_phone")
    cust_email = parameters.get("cust_email")
    cust_reason = parameters.get('cust_reason')

    db = configureDataBase()

    if intent == 'Quotes':
        message = makeAPIRequest()
        print(message)
        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            message
                        ]

                    }
                },

            ]
        }
    elif intent == 'Need_Help':
        log.saveConversations(sessionID, cust_reason, intent, db, cust_email, cust_name, cust_phone)
        prepareEmail(cust_email)
    elif intent == 'Depression_workplace':
        val = Depression_test(result)
        if val == 1:
            print("visit")
            return {

                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "It is advisable to visit a psychiatrist"
                            ]

                        }
                    },

                ]
            }
        else:
            print("don't visit")
            return {

                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "You are alright! Take care !!"
                            ]

                        }
                    },

                ]
            }

    else:
        return {
            "fulfillmentText": "something went wrong,Lets start from the begning, Say Hi",
        }


def configureDataBase():
    mongo_uri = "mongodb+srv://Bot_Admin:" + urllib.parse.quote_plus("Bhanu@2001") + "@cluster0.ylac8.mongodb.net/test?retryWrites=true&w=majority"
    db = pymongo.MongoClient(mongo_uri)

    return db.get_database('User_details')


def makeAPIRequest():
    URL = 'https://type.fit/api/quotes'
    response = requests.get(URL)
    js = json.loads(response.text)

    quote = js[random.randint(0, len(js))]['text']
    author = js[random.randint(0, len(js))]['author']
    message1 = quote + "\n\t\t\t\t" + author
    return message1

def prepareEmail(contact_email):
    mailclient = EMailClient.GMailClient()
    mailclient.sendEmail(contact_email)


def Depression_test(result):
    depress_value = flask_api.Depress()
    return depress_value.Inputs(result)


if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
"""if __name__ == "__main__":
    app.run()""""