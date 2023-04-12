import os
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel
from fastapi import Request, HTTPException, APIRouter, Header

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

class Line(BaseModel):
    destination: str
    events: List[Optional[None]]

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
    line_bot_api.reply_message(  # 只能用在接收到其他 LINE 使用者的時候回覆信息，而不能用在主動推送信息
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )