import poe
import logging
import time
import json
from typing import List, Union, Dict, Any, Optional


class PoeCaller:
    def __init__(self, token, max_messages_per_minute=10):
        self.client = poe.Client(token)
        self.conversation_history = []
        self.max_messages_per_minute = max_messages_per_minute
        self.last_message_time = 0
        self.get_bots()

    def get_bots(self):
        data = self.client.bot_names
        self.available_bot_names = list(data.keys())
        return self.available_bot_names

    def _check_bot(self, bot_codename):
        return bot_codename in self.available_bot_names

    def chat(self, bot_codename: str, messages: Union[str, List[str]]):
        if not isinstance(messages, list):
            messages = [messages]

        assert self._check_bot(
            bot_codename
        ), f"Bot {bot_codename} does not exist in POE"

        responses = []
        for message in messages:
            # Handle rate limits.
            current_time = time.time()
            if (
                current_time - self.last_message_time
                < 60 / self.max_messages_per_minute
            ):
                time.sleep(60 / self.max_messages_per_minute)

            # Try sending the message and getting a response.
            try:
                response = self.client.send_message(bot_codename, message)
            except Exception as e:
                logging.error(f"Failed to send message: {e}")
                return None
            for chunk in self.client.send_message(bot_codename, message):
                pass
            response = chunk["text"]
            # If successful, add the message and response to the conversation history.
            self.conversation_history.append(
                {
                    "role": "system" if message.startswith("system:") else "user",
                    "content": message,
                }
            )
            self.conversation_history.append({"role": "assistant", "content": response})
            responses.append(response)

            # Update the last message time.
            self.last_message_time = time.time()

        # Return all responses from the bot.
        return responses

    def get_conversation(self):
        return self.conversation_history

    def reset_conversation(self):
        self.conversation_history = []

    def create_bot(
        self,
        handle,
        prompt="",
        base_model="chinchilla",
        description="",
        intro_message="",
        prompt_public=True,
        pfp_url=None,
        linkification=False,
    ):
        try:
            self.client.create_bot(
                handle,
                prompt,
                base_model,
                description,
                intro_message,
                prompt_public,
                pfp_url,
                linkification,
            )
        except Exception as e:
            logging.error(f"Failed to create bot: {e}")
