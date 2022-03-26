from storage.sessionManager import SessionManager
from storage.storage import Storage

import redis
import json

HOST = "redis"
PORT = 6379
CHANNEL = "execution.code.language"

storage = Storage()
session_manager = SessionManager()


class MessagePersisterConsumer:
    def __init__(self):
        self.redis_client = redis.from_url('redis://redis:6379')

    def listen_for_messages(self):
        sub = self.redis_client.pubsub()
        sub.subscribe('execution.code.language')
        for message in sub.listen():
            if message is not None and isinstance(message, dict):
                type = message.get('type')
                if type is not None and type == 'subscribe':
                    print("Got initial subscribe message from pubsub queue.")
                else:
                    print(f"Got message for new execution on redis. Content: {message}.")
                    data = message.get('data').decode("utf-8")
                    dictionary = json.loads(data)
                    lang = dictionary.get('language')
                    content = dictionary.get('content')
                    session = session_manager.get_new_session()
                    try:
                        if lang and content:
                            storage.insert_new_code(session, lang, content)
                    finally:
                        session.close()


if __name__ == '__main__':
    print('starting up persister')
    message_consumer = MessagePersisterConsumer()
    message_consumer.listen_for_messages()