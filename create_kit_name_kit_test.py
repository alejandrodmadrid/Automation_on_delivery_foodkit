import data
import sender_stand_request
from data import kit_body, five_hun_twelve_name, special_symbol_name


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body['name'] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_user_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == name
    # kit_table_response = sender_stand_request.kit_verification(kit_body)
    # str_kit = (kit_body["name"] + "," + kit_body["card"] + ","
    #           + kit_body["productList"] + "," + kit_body["id"] + ','
    #           + kit_body["productsCount"])
    # assert kit_table_response.text.count(str_kit) == 1

def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_user_kit(kit_body)
    assert kit_response.status_code == 400
    assert kit_response.json['name'] == name

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.one_letter_name)

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.five_hun_eleven_letter_name)

def test_create_kit_empty_name_get_error_response():
    negative_assert(data.empty_name)

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert(five_hun_twelve_name)

def test_create_kit_special_char_in_name_get_success_response():
    positive_assert(special_symbol_name)

def test_create_kit_name_with_spaces_get_success_response():
    positive_assert(data.name_with_space)

def test_create_kit_name_with_number_as_str_get_success_response():
    positive_assert(data.numeric_str_name)

def test_create_kit_name_with_number_as_int_get_error_response():
    negative_assert(data.numeric_name_type)

def test_create_kit_with_no_body():
    kit_response = sender_stand_request.post_user_kit_empty_body()
    assert kit_response.status_code == 400


