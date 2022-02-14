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
    'gTOh/tDUvFimvDs1DG0LyGazyqA7kujVyodFABa6ixnN57/vf5ii8oNZttIAKl9j8fQRHcaoOaoI2NRhMyX6gOAzzc3U/WdI3ZYG4xCawR+KRAAkKvh4dO3QJONQLyR6vRZMYNdfRWgXNtkCTj0VkwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('36ada6b9ffec37062f2692fbf01f287f')


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
