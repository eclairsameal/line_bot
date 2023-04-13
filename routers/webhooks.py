import os
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel
from fastapi import Request, HTTPException, APIRouter, Header
import openai

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
load_dotenv()
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)

openai.api_key = os.getenv("OPENAPI_KEY")
conversation = []

class ChatGPT:
    def __int__(self):
        pass
        self.messages = conversation
        self.model = "gpt-3.5-turbo"

    def get_response(self, user_input):
        conversation.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        print("AI回答內容：")
        print(response['choices'][0]['message']['content'].strip())
        return response['choices'][0]['message']['content'].strip()


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


chatgpt = ChatGPT()

@router.post("/line")
# 驗證跟接收 LINE 的資訊(Verify and receive LINE information)
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'

# 當收到文字訊息時
@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print(event)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    reply_msg = chatgpt.get_response(event.message.text)
    print(reply_msg)
    print("!!!!!!!!!!!!!!!!!!!!!!")
    line_bot_api.reply_message(  # 只能用在接收到其他 LINE 使用者的時候回覆信息，而不能用在主動推送信息
        event.reply_token,
        TextSendMessage(text=reply_msg)
    )