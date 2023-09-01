import requests
import json

def login(email, password):
    """
    구글 API를 사용하여 구글 아이디로 로그인합니다.

    Args:
        email (str): 구글 아이디
        password (str): 구글 비밀번호

    Returns:
        dict: 로그인 성공 시에는 access_token, expires_in, token_type, refresh_token 등의 정보를 포함하는 dict,
               로그인 실패 시에는 error, error_description 등의 정보를 포함하는 dict
    """

    url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "grant_type": "password",
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "username": email,
        "password": password,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = requests.post(url, data=data, headers=headers)
    response_json = json.loads(response.content)
    return response_json

if __name__ == "__main__":
    email = "YOUR_EMAIL"
    password = "YOUR_PASSWORD"
    response_json = login(email, password)
    print(response_json)
