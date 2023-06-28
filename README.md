
# PoeCaller: A Python Wrapper for Poe API

PoeCaller is a Python wrapper for the Poe API. It allows for easy interaction with Poe's available bots, including sending messages, receiving responses, and even creating new bots.

## Installation

Before using PoeCaller, make sure you have Python 3.7+ installed on your system. You can then clone this repository to your local machine:

```bash
git clone https://github.com/munozariasjm/PoeCaller.git
cd PoeCaller
```

Next, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the PoeCaller, first import it in your Python script:

```python
from poe_caller import PoeCaller
```

Then, initialize a `PoeCaller` instance with your Poe API token:

```python
poe_caller = PoeCaller("YOUR_POE_API_TOKEN")
```

You can send messages to a bot and get its responses:

```python
responses = poe_caller.chat('bot_codename', ['Hello bot!', 'How are you?'])
print(responses)
```

You can also get the full conversation history:

```python
print(poe_caller.get_conversation())
```

And reset the conversation history when you're done:

```python
poe_caller.reset_conversation()
```

Finally, you can create a new bot:

```python
poe_caller.create_bot('my_new_bot', 'Hello, I am a new bot.', 'chinchilla', 'A bot for testing purposes.')
```

## Limitations

This wrapper provides basic functionality and error handling, but there are some limitations:

- The rate limit handling is basic and doesn't take into account the actual rate limit of the Poe API.
- It doesn't handle quotas or other API limits.
- It doesn't handle different types of errors in different ways. For example, it doesn't differentiate between a network error and an API error.

## Contributing

We welcome contributions to PoeCaller! Please submit a pull request with your improvements.

## License

This project is licensed under the terms of the MIT license.

---
