import configuration
import requests
import data
from data import (header_kit, user_body, kit_body)


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=header_kit)

def post_user_kit(kit_body):
    headers = data.header_kit.copy()
    authToken = post_new_user(user_body).json()['authToken']
    headers["Authorization"] = f'Bearer {authToken}'
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

def post_user_kit_empty_body():
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=header_kit,
                         json={})

def kit_verification(kit_body):
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=header_kit)