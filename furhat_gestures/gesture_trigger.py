import requests

headers = {
    'Content-type': 'application/json',
}

base_url = "http://localhost"
port = "54321"


def trigger_custom_gesture(gesture_def):
    api_url = "furhat/actions/gesture"
    curl_url = base_url + ":" + port + "/" + api_url

    response = requests.post(curl_url, headers=headers, data=gesture_def)
    # print(response)
    return response


def trigger_predef_gesture(gesture_type):
    api_url = "furhat/actions/gesture?name"
    curl_url = base_url + ":" + port + "/" + api_url + "=" + gesture_type

    response = requests.post(curl_url, headers=headers)

    return response


