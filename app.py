from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()    # gets the msg what we send in the whatsapp
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    url = "https://youtube-search-and-download.p.rapidapi.com/search"
    querystring = {"query":incoming_msg,"hl":"en","type":"v"}
    headers = {
    'x-rapidapi-host': "youtube-search-and-download.p.rapidapi.com",
    'x-rapidapi-key': "b751d01955mshbf18e87fd06f850p119f91jsn9e1723d142b6"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text.encode('utf-8')
    data = json.loads(data)
    # print(data["contents"][0]["video"]["videoId"]) used https://rapidapi.com/h0p3rwe/api/youtube-search-and-download/ API to fetch data

    required_url = "https://www.youtube.com/watch?v="+data["contents"][0]["video"]["videoId"]
    msg.body(required_url)
    responded = True

    if not responded:
        msg.body('Please type the video name correctly so that i can send you the correct video')
    return str(resp)


if __name__ == '__main__':
    app.run()