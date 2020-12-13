from flask import Flask, Response, request
from flask_ngrok import run_with_ngrok
from dotenv import load_dotenv
import json
import telnyx
import os
import requests

app = Flask(__name__)
run_with_ngrok(app)

# Get Environment Variables
load_dotenv()
TELNYX_MMS_S3_BUCKET = os.getenv("TELNYX_MMS_S3_BUCKET")
telnyx.api_key = os.getenv("TELNYX_API_KEY")
TELNYX_APP_PORT = os.getenv("TELNYX_APP_PORT")

@app.route("/webhooks", methods=["POST"])
def webhooks():
    # Load JSON data
    body = json.loads(request.data)

    # On message Recieved, abstract data
    if body['data']['event_type'] == 'message.received':
        to_number = body["data"]["payload"]["to"][0]["phone_number"]
        from_number = body["data"]["payload"]["from"]["phone_number"]
        text = body["data"]["payload"]["text"]
        
        # Check text message for valid responses
        response = check_response(text)

        # Create and send response message
        try:
            telnyx_response = telnyx.Message.create(
                from_=to_number,
                to=from_number,
                text=response
            )
        
        # Log any Errors
        except Exception as e:
            print('Error sending message')
            print(e)
        return Response(status=200)

    # Return status 200 if request is not inbound message
    else: 
        return Response(status=200)

# Check text content and create response
def check_response(text):
    # Set input to lowercase
    text = text.lower()

    if text == 'pizza':
        response = 'Chicago pizza is the best'
    elif text == 'ice cream':
        response = 'I prefer gelato'
    else: 
        response = 'Please send either the word ‘pizza’ or ‘ice cream’ for a different response'
    return response


if __name__ == "__main__": 
    app.run()