# ------------------
# Only for running this script here
import logging
import sys
from os.path import dirname

sys.path.insert(1, f"{dirname(__file__)}/../../..")
logging.basicConfig(level=logging.DEBUG)
# ------------------

# export SLACK_API_TOKEN=xoxb-***
# python3 integration_tests/samples/readme/async_script.py

import asyncio
import os
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.errors import SlackApiError

client = AsyncWebClient(token=os.environ["SLACK_API_TOKEN"])


async def post_message():
    try:
        response = await client.chat_postMessage(channel="#random", text="Hello world!")
        assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")


asyncio.run(post_message())
