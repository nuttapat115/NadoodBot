from traceback import print_tb
from flask import Flask, request, abort ,render_template

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


@app.route("/liff")
def test():
    return render_template("login.html")


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
    userid = event.source.user_id
    check_user_res = check_user(userid)
    print(userid)
    if check_user_res :
        text = event.message.text
        if text == '1':
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='https://liff.line.me/1656889718-KMoBB5el'),
                notification_disabled=True)
    else :
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='ท่านยังไม่ได้ลงทะเบียน กรุณากด "เริ่มต้นให้งาน" ที่เมนู'),
                notification_disabled=True)

def check_user (userid):
    return 0
    


if __name__ == "__main__":
    app.run(debug=True)
