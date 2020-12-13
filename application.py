from flask import Flask, Response, request
from flask_ngrok import run_with_ngrok
from dotenv import load_dotenv
import telnyx
import os
import requests

app = Flask(__name__)
run_with_ngrok(app)

load_dotenv()

TELNYX_MMS_S3_BUCKET = os.getenv("TELNYX_MMS_S3_BUCKET")
telnyx.api_key = os.getenv("TELNYX_API_KEY")
TELNYX_APP_PORT = os.getenv("TELNYX_APP_PORT")

client = telnyx.http_client.RequestsClient()
telnyx.default_http_client = client

@app.route("/messaging/inbound", methods=["POST"])
def inbound_message():
    body = json.loads(request.data)
    message_id = body["data"]["payload"]["id"]
    print(f"Received inbound message with ID: {message_id}")

    to_number = body["data"]["payload"]["to"][0]["phone_number"]
    from_number = body["data"]["payload"]["from"]["phone_number"]

    response = 'doi'

    try:
        telnyx_response = telnyx.Message.create(
            from_=to_number,
            to=from_number,
            text=response
        )
        print(f"Sent message with id: {telnyx_response.id}")
    except Exception:
        print('error sending message')
    return Response(status=200)


# “pizza” respond with the sentence: “Chicago pizza is the best”
# “Ice cream” respond with the sentence: “I prefer gelato”
 

if __name__ == "__main__": 
    app.run()