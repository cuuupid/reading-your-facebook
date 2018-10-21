from flask import Flask, request
from pymessenger.bot import Bot
import person

app = Flask(__name__)

ACCESS_TOKEN = ""
VERIFY_TOKEN = ""

bot = Bot(ACCESS_TOKEN)
me = person.load_person()


@app.route("/", methods=['GET', 'POST'])
def speak():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message: str = x['message']['text']
                        if message.startswith('/load'):
                            try:
                                _me = person.load_person(message.split(' ')[1])
                                me = _me
                            except:
                                bot.send_text_message(
                                    recipient_id, ":/ i dont have data for them")
                        else:
                            bot.send_text_message(
                                recipient_id, person.search(me, message))
                    if x['message'].get('attachments'):
                        print("attachment not loading for me :'(")
                else:
                    pass
        return "OK"


if __name__ == "__main__":
    app.run(port=6969, debug=False)
