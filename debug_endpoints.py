import requests
import json

BASE_URL = "https://restcountries.com"

def construct_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers

def construct_body(data):
    return json.dumps(data)

def send_get_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    headers = construct_headers()
    response = requests.get(url, headers=headers, verify=False)
    return response

def send_post_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    headers = construct_headers()
    body = construct_body(data)
    response = requests.post(url, headers=headers, data=body, verify=False)
    return response

def validate_response(response, expected_status):
    if response.status_code == expected_status:
        print(f"Success: {response.status_code}")
    else:
        print(f"Failed: {response.status_code}")
    print(response.json())

def main():
    endpoints = [
        "/v3.1/all",
        "/v3.1/name/canada",
        "/v3.1/name/united%20states?fullText=true",
        "/v3.1/alpha/US",
        "/v3.1/currency/usd",
        "/v3.1/lang/spanish",
        "/v3.1/region/europe",
        "/v3.1/subregion/southern%20asia"
    ]

    for endpoint in endpoints:
        print(f"Testing GET {endpoint}")
        response = send_get_request(endpoint)
        validate_response(response, 200)

if __name__ == "__main__":
    main()