import requests
import json

def get_access_token_fortnite(authorization_code):
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        #Below is fortnitePcClient Authorization
        "Authorization": f"Basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ=" 
    }
    data = {
        "grant_type": "authorization_code",
        "code": f"{authorization_code}"
    }

    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.content)
    # print("fortnite Access token")
    # print(data)
    access_token = data['access_token']
    return access_token

def create_exchange_code(access_token):
    url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    # print("Exchange Code")
    # print(data)
    exchange_code = data["code"]
    return exchange_code

def get_access_token(exchange_code):
    url = 'https://api.epicgames.dev/epic/oauth/v2/token'
    headers = {
        'Accept-Encoding': 'deflate, gzip',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization': 'Basic MTJjNDI3OTg2MmFiNDQ2MGEyNWMyZTlmYTUzNWZiN2U6eEZEZnN5QkhXdllXWXZGWkxodXlqamhGNFVEUEZUNms=',
        'X-Epic-Correlation-ID': 'EOS-7Xy9sxln5k6-kd-09Q8ouQ-GmEbSTmd6UmlCwuKAdQF_w',
        'User-Agent': 'EOS-SDK/1.16.0-25515828 (Windows/10.0.22621.2506.64bit) Dauntless/1.0.0',
        'X-EOS-Version': '1.16.0-25515828'
    }
    data = {
            "grant_type": "exchange_code",
            "exchange_code": f"{exchange_code}"
        }

    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.content)
    # print("Trials token")
    # print(data)
    session_token = data['access_token']
    return session_token

def get_session_token(trials_token):
    url = 'https://gamesession-prod.steelyard.ca/gamesession/epiceos'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'Authorization': f'BEARER {trials_token}',
        'Content-Type': 'application/json; charset=utf-8',
        'X-Archon-Console': '(Windows)',
        'User-Agent': 'Archon/++dauntless+rel-1.14.6-CL-615145 Windows/10.0.22621.1.768.64bit'
    }

    response = requests.put(url, headers=headers)
    data = json.loads(response.content)
    # print("Session Token")
    # print(data)
    session_token = data["payload"]["sessiontoken"]
    return session_token

def get_trials_leaderboard(session_token):
    url = "https://leaderboards-prod.steelyard.ca/trials/leaderboards/all"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "deflate, gzip",
        "Authorization": f"BEARER {session_token}",
        "Content-Type": "application/json; charset=utf-8",
        "X-Archon-Console": "(Windows)",
        "User-Agent": "Archon/++dauntless+rel-1.14.6-CL-615145 Windows/10.0.22621.1.768.64bit"
    }
    data = {
            "difficulty": 1,
            "page": 0,
            "page_size": 100,
            "trial_id": "Arena_MatchmakerHunt_Elite_New_0057",
            "target_platforms": []
        } # Put your JSON data here if needed
    response = requests.post(url, headers=headers, json=data)
    data = json.loads(response.content)
    return data


if __name__ == "__main__":
    authorization_code = "814b7651e24d4b78a005e720ad25d2c9"  # <--------   Paste Authorization code here
    fr_access_token = get_access_token_fortnite(authorization_code)
    exchange_code = create_exchange_code(fr_access_token)
    access_token = get_access_token(exchange_code)
    session_token = get_session_token(access_token)
    trials_leaderboard = get_trials_leaderboard(session_token)
    print(trials_leaderboard)