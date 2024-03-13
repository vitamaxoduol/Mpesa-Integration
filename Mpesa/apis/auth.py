import requests
import traceback

from requests.auth import HTTPBasicAuth


class MpesaBase:
    def __init__(self, env="sandbox",  CONSUMER_KEY="4lLvX2iuvUpu435BA7uMVBqYWuNBlaRBt3GBP4VMZV97szCY", CONSUMER_SECRET="hUJX9nzaqfAG6AEwvFTqr0OQNQGQTRpFwjzCjkUPvt4YB4cGGObcAupynBu4Mxs5", sandbox_url="https://sandbox.safaricom.co.ke", live_url="https://api.safaricom.co.ke"):
        self.env = env
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.sandbox_url = sandbox_url
        self.live_url = live_url
        self.token = None
        self.session = requests.Session()


    def get_access_token(self):
        if self.env == "production":
            base_safaricom_url = self.live_url
        else:
            base_safaricom_url = self.sandbox_url

        authenticate_uri = "oauth/v1/generate?grant_type=client_credentials"
        authenticate_url = f"{base_safaricom_url}/{authenticate_uri}"

        try:
            response = self.session.get(authenticate_url, auth=HTTPBasicAuth(self.CONSUMER_KEY, self.CONSUMER_SECRET))
            response.raise_for_status()
            self.token = response.json().get('acess_token')
            return self.token
        except requests.RequestException as e:
            traceback.print_exec()
            print(f"Error during authentication: {e}")
            return None

