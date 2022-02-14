from flask import Flask , request , abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('gTOh/tDUvFimvDs1DG0LyGazyqA7kujVyodFABa6ixnN57/vf5ii8oNZttIAKl9j8fQRHcaoOaoI2NRhMyX6gOAzzc3U/WdI3ZYG4xCawR+KRAAkKvh4dO3QJONQLyR6vRZMYNdfRWgXNtkCTj0VkwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('36ada6b9ffec37062f2692fbf01f287f')

@app.route('/webhook' , methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success',200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)