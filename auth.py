import sys
from requests_html import HTMLSession
import os
from dotenv import load_dotenv
import json

load_dotenv()

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

URL = 'https://www.remind.com/v2/access_tokens/confirmed_login'

def main():
    # This is the form data that the page sends when logging in
    login_data = {
        "user": {
            "device_address": EMAIL,
            "password": PASSWORD,
        },
        "persist": False,
    }

    with HTMLSession() as session:
        # Authenticate
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Host': 'www.remind.com',
            'Accept': 'application / json',
            'Accept-Language': 'en-US, en; q = 0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.remind.com/',
            'Remind101-Client-Type': 'Web',
            'Remind101-Client-Name': 'Dashboard',
            'Remind101-Client-Segment': 'desktop_web',
            'Remind101-Client-Version': 'v8039',
            'Remind101-Timezone-Id': 'America/Los_Angeles',
            'Remind101-Timezone-Offset': '-25200',
            'Origin': 'https://www.remind.com',
            'Cookie': 'client_uuid=72e6f80b-7270-444f-b4f9-e78271822bcc; session_uuid=2e4808a4-ab87-4ad6-bc29-e1ddba462d66; _dd_s=logs=1&id=2ea746d8-fcad-43df-95ce-fb5a5e7fb862&created=1664069763577&expire=1664070924968; persist=false; G_ENABLED_IDPS=google'
        }
        r = session.get('https://www.remind.com/log_in/')
        r.html.render()
        print(r.html.find('#id-9', first=True))
        r = session.post(URL, data=json.dumps(login_data), headers=headers)
        print(r.text)
        # Try accessing a page that requires you to be logged in
        r = session.get('https://www.remind.com/v2/access_tokens/confirmed_login', headers=headers)
        print(r.text)

if __name__ == '__main__':
    main()