import configuration
import requests
from data import headers, user_body, kit_body


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=headers)

authToken = post_new_user(user_body).json()['authToken']

header_kit = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {authToken}'
}

def post_user_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=header_kit)

def post_user_kit_empty_body():
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=header_kit,
                         json={})

def kit_verification(kit_body):
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=header_kit)