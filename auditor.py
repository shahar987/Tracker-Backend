
from db import create_clientChecks
from datetime import datetime
import requests

dict1 = {'computer_name': 'SHAHAR-PC',
        'system_version': '10',
        'antivirus_installed': False,
        'antivirus_enabled': True,
        'antivirus_up_to_date': True,
        'windows_firewall_is_active': True,
        'max_pass_age': 42,
        'min_pass_len': 0,
        'number_of_connected_doks': 3,
        'chrome_version': '100.0.4896.127',
        'failed_login_event': ['2022-04-30', '2022-04-27','2022-04-24']}


def chrome_version(json_before):
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.request("GET", url)
    if json_before['chrome_version'] == response.text:
        json_before['chrome_version'] = True
    else:
        json_before['chrome_version'] = False

def failed_login_event(json_before):
    today = datetime.today().strftime('%Y-%m-%d')
    counter_date = json_before['failed_login_event'].count(today)
    if counter_date < 10:
        json_before['failed_login_event'] = True
    else:
        json_before['failed_login_event'] = False

def system_version(json_before):

    if json_before['system_version'] == '10':
        json_before['system_version'] = True
    else:
        json_before['chrome_version'] = False


def process_json(json_before):
    if json_before['system_version'] == '10':
        json_before['system_version'] = True
    else:
        json_before['system_version'] = False
    if json_before['max_pass_age'] <= 30:
        json_before['max_pass_age'] = True
    else:
        json_before['max_pass_age'] = False
    if json_before['max_pass_age'] <= 30:
        json_before['max_pass_age'] = True
    else:
        json_before['max_pass_age'] = False
    if json_before['min_pass_len'] <= 8:
        json_before['min_pass_len'] = True
    else:
        json_before['min_pass_len'] = False
    if json_before['number_of_connected_doks'] == 0:
        json_before['number_of_connected_doks'] = True
    else:
        json_before['number_of_connected_doks'] = False
    chrome_version(json_before)
    failed_login_event(json_before)
    system_version(json_before)


my_dict = {'1' : dict1['system_version'],
        '2' : dict1['antivirus_installed'],
        '3' : dict1['antivirus_enabled'],
        '4' : dict1['antivirus_up_to_date'],
        '5' : dict1['windows_firewall_is_active'],
        '6' : dict1['max_pass_age'],
        '7' : dict1['min_pass_len'],
        '8' : dict1['number_of_connected_doks'],
        '9' : dict1['chrome_version'],
        '10' : dict1['failed_login_event']}

if __name__ == '__main__':

    create_clientChecks('Microsoft', dict1['computer_name'], my_dict)
    process_json(dict1)


#here you put only auditor code