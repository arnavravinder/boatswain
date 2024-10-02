from .airtable import AirtableManager
from dotenv import load_dotenv
import os

load_dotenv()


class Environment:
    def __init__(self):
        self.slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
        self.slack_user_token = os.environ.get("SLACK_USER_TOKEN")
        self.slack_signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
        self.slack_support_channel = os.environ.get("SLACK_SUPPORT_CHANNEL")
        self.slack_request_channel = os.environ.get("SLACK_REQUEST_CHANNEL")
        self.airtable_api_key = os.environ.get("AIRTABLE_API_KEY")
        self.airtable_base_id = os.environ.get("AIRTABLE_BASE_ID")

        self.port = os.environ.get("PORT", 3000)

        if not self.slack_bot_token:
            raise Exception("SLACK_BOT_TOKEN is not set")
        if not self.slack_user_token:
            raise Exception("SLACK_USER_TOKEN is not set")
        if not self.slack_signing_secret:
            raise Exception("SLACK_SIGNING_SECRET is not set")
        if not self.slack_support_channel:
            raise Exception("SLACK_SUPPORT_CHANNEL is not set")
        if not self.slack_request_channel:
            raise Exception("SLACK_REQUEST_CHANNEL is not set")
        if not self.airtable_api_key:
            raise Exception("AIRTABLE_API_KEY is not set")
        if not self.airtable_base_id:
            raise Exception("AIRTABLE_BASE_ID is not set")

        self.airtable = AirtableManager(
            api_key=self.airtable_api_key, base_id=self.airtable_base_id
        )


env = Environment()
