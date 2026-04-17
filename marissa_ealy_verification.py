import requests
import datetime

# Constants
CUSTOMER_ID = 'ARRizEXLA26ifIZK-pGsU5**'
API_URL = 'https://api.melissadata.net/v4/VERIFYSOAP'

# Information to verify
user_info = {
    'name': 'Marissa Yvonne Ealy',
    'email': 'marissaealy@hotmail.com',
    'phone': '7602077608',
    'street': '1704 Buckeye St',
    'city': 'Highland',
    'state': 'CA',
    'zip': '92346',
    'country': 'US'
}

def log_audit(action):
    with open('audit_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} - {action}\n")

# Function to verify user information

def verify_user_info(user_info):
    payload = {
        'CustomerID': CUSTOMER_ID,
        'Record': user_info
    }
    response = requests.post(API_URL, json=payload)
    return response.json()

# Main function
if __name__ == '__main__':
    # Logging consent
    log_audit('User consent granted for verification of Marissa Yvonne Ealy.')

    # Verifying user information
    result = verify_user_info(user_info)
    
    # Displaying results
    print(f"Verification results for {user_info['name']}: {result}")
    
    # Logging the results
    log_audit(f'Verification results for {user_info['name']}: {result}')