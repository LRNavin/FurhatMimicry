import requests
from utilities import constants


def trigger_custom_gesture(gesture_def):
    api_url = "furhat/actions/gesture"
    curl_url = constants.base_url + ":" + constants.port + "/" + api_url

    response = requests.post(curl_url, headers=constants.headers, data=gesture_def)
    return response


def trigger_predef_gesture(gesture_type):
    api_url = "furhat/actions/gesture?name"
    curl_url = constants.base_url + ":" + constants.port + "/" + api_url + "=" + gesture_type

    response = requests.post(curl_url, headers=constants.headers)
    return response


