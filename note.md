# line_bot

## requirements.txt

fastapi
uvicorn
line-bot-sdk
python-dotenv
jinja2
openai

## 環境變數

[Python - 環境變數設定](http://johnliutw.logdown.com/posts/7831770/python-environment-variable-settings-env-auto-settings)

.env
```
LINE_CHANNEL_ACCESS_TOKEN=
LINE_CHANNEL_SECRET=
OPENAPI_KEY=
API_ENV=developer
```

## ngrok
https://ngrok.com/

[使用 ngrok 讓外網連接你的 API](https://ithelp.ithome.com.tw/articles/10197345)


## line bot

```
@handler.add(MessageEvent, message=TextMessage)
```
當LINE 機器人接收 LINE 的 MessageEvent (信息事件)時該做什麼,message=表示信息內容.

事件：
* MessageEvent (信息事件)
* FollowEvent (加好友事件)、
* UnfollowEvent (刪好友事件)
* JoinEvent (加入聊天室事件)
* LeaveEvent (離開聊天室事件)
* MemberJoinedEvent (加入群組事件)
* MemberLeftEvent (離開群組事件)
* .....[等](https://github.com/line/line-bot-sdk-python#event)

MessageEvent (信息事件)內容：
* TextMessage
* ImageMessage
* VideoMessage
* StickerMessage
* FileMessagec
* .....[等](https://github.com/line/line-bot-sdk-python#message)




[說明](https://ithelp.ithome.com.tw/articles/10217767)

