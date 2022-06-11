from db import create_clientChecks, create_client, create_end_points
from datetime import datetime
import requests

result = {'computer_name': 'test',
        'system_version': None,
        'antivirus_installed': None,
        'antivirus_enabled': None,
        'antivirus_up_to_date': None,
        'windows_firewall_is_active': None,
        'max_pass_age': None,
        'min_pass_len': None,
        'number_of_connected_doks': None,
        'chrome_version': None,
        'failed_login_event': None}


def chrome_version(json_before):
    currunt_chrome_version = str(json_before.chrome_version)
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.request("GET", url)
    octat_response = response.text.split(".")
    octat_json = currunt_chrome_version.split(".")
    if json_before.chrome_version == response.text:
        result['chrome_version'] = True
    else:
        result['chrome_version'] = False
    for i in range(len(octat_json)):
        if int(octat_response[i]) < int(octat_json[i]):
            result['chrome_version'] = True
            break




def failed_login_event(json_before):
    today = datetime.today().strftime('%Y-%m-%d')
    counter_date = json_before.failed_login_event.count(today)
    if counter_date < 10:
        result['failed_login_event'] = True
    else:
        result['failed_login_event'] = False


def system_version(json_before):

    if json_before.system_version == '10':
        result['system_version'] = True
    else:
        result['chrome_version'] = False


def anti_virus(json_before):
    result["antivirus_installed"] = json_before.antivirus_installed
    result["antivirus_enabled"] = json_before.antivirus_enabled
    result["antivirus_up_to_date"] = json_before.antivirus_up_to_date


def windows_firewall_is_acvitve(json_before):
    result["windows_firewall_is_active"] = json_before.windows_firewall_is_active


def check_num_of_errors(result: dict):
    count = 0
    for val in result.values():
        if val == True:
            count = count + 1
    return count


def process_json(json_from_agent):
    json_before = json_from_agent
    if json_before.system_version == '10':
        result['system_version'] = True
    else:
        result['system_version'] = False
    if json_before.max_pass_age <= 30:
        result['max_pass_age'] = True
    else:
        result['max_pass_age'] = False
    if json_before.min_pass_len <= 8:
        result['min_pass_len'] = True
    else:
        result['min_pass_len'] = False
    if json_before.number_of_connected_doks == 0:
        result['number_of_connected_doks'] = True
    else:
        result['number_of_connected_doks'] = False

    chrome_version(json_before)
    failed_login_event(json_before)
    system_version(json_before)
    anti_virus(json_before)
    windows_firewall_is_acvitve(json_before)
    my_dict = {'1': result['system_version'],
               '2': result['antivirus_installed'],
               '3': result['antivirus_enabled'],
               '4': result['antivirus_up_to_date'],
               '5': result['windows_firewall_is_active'],
               '6': result['max_pass_age'],
               '7': result['min_pass_len'],
               '8': result['number_of_connected_doks'],
               '9': result['chrome_version'],
               '10': result['failed_login_event']}
    create_clientChecks('mix', json_before.computer_name, my_dict)
    error_number = check_num_of_errors(my_dict)
    create_client(json_before.computer_name, error_number, json_before.ip_add, 'mix')
    create_end_points('mix')





