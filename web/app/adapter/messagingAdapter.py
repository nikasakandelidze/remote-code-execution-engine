import aioredis
import json

HOST = "redis"
PORT = 6379
CHANNEL = "execution.code.language"


class MessagingAdapter:
    def __init__(self):
        self.redis_client = aioredis.from_url(f"redis://{HOST}:{PORT}")

    async def publish_message(self, language: str = "", content: str = ""):
        if len(language) == 0 or len(content) == 0:
            return
        else:
            print('Publishing message to pub-sub queue.')
            await self.redis_client.publish(CHANNEL, json.dumps({"language": language, "content": content}))