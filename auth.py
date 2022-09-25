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
            'Accept': 'application/json',
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
            }
        r = session.get('https://www.remind.com/log_in/')
        r.html.render()
        print(r.html.find('#id-9', first=True))
        r = session.post(URL, data=json.dumps(login_data), headers=headers)
        print(r.text)
        print(r.status_code)
        if r.status_code == 403:
            emailVerify = input("Enter email verification code: ")
            email_data = {
                "address": EMAIL,
                "code": emailVerify,
            }
            emailEndpoint = "https://www.remind.com/v2/devices/outbound_verification"
            verify = session.post(emailEndpoint, data=json.dumps(email_data), headers=headers)
            print(verify.text)

if __name__ == '__main__':
    main()