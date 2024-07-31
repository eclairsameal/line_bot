# LINE bot

Use FastAPI to connect LINE bot to ChatGPT.

## Architecture

![Architecture](/image/Architecture.png)


## Development

```
pip install -r requirements.txt
```

## Environment Variable

.env
```
LINE_CHANNEL_ACCESS_TOKEN=
LINE_CHANNEL_SECRET=
OPENAPI_KEY=
```

## ngrok
https://ngrok.com/


* install
```
brew cask install ngrok
```

* run
```
ngrok http --authtoken [Authtoken] --host-header=rewrite 8080
```

![ngrok](/image/ngrok.png)


## Webhook settings

![Webhook settings](/image/webhook%20setting.png)
