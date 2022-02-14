from traceback import print_tb
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'oPcOCZSd8Q8MTzesCpPFN031TZz8+MaS0jhOnbqir7puFTLB3+VwuRYHYzUZ7Ek7/n2qeRidHKqkGSShLOEHkxVX0oyFDM3NDOfz6cbFudqiRV65EqbKqO6MoivYT4q2lh2xezm3ZMgxGYayygXKZwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d81be6831b95489f999e3bb6e411cc90')


@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if text == '1':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text),
            notification_disabled=True)



if __name__ == "__main__":
    app.run(debug=True)
