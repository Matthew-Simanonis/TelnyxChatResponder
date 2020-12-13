# TelnyxChatResponder

This app automatically responds to texts using the Telnyx API, Flask and ngrok.


## Getting Started

Be sure to install all the requirements in requirements.txt.

Set up a messaging profile on Telnyx and assign a new phone number to your messaging profile.

Find your Telnyx API Key and Telnyx Public Key and add them to the .env file. Feel free to change the port if needed.

Start the Flask server by running 'python application.py' in the terminal.

This will automatically run ngrok as a forwarding URL.

Copy the &lt;ngrokURL&gt; from the newly logged ngrok Forwarding URL and paste in the inbound webhook URL on the Telnyx Dashboard followed by /webhooks

i.e.: "&lt;ngrokURL&gt;/webhooks"

*Access this menu from the Telnyx Dasboard -> Messaging -> Inbound Settings


Send a text to your Messaging profile phone number and automatically recieve a response.

*Feel free to change any of the available inputs and responses in the check_response() function in application.py.
