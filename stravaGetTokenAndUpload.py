import requests
import os

def get_access_token(client_id, client_secret, code):
    token_url = "https://www.strava.com/oauth/token"
    payload:dict = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': code,
    'grant_type': "authorization_code",
    'f': 'json'
    }
    response = requests.post(token_url, data=payload, verify=False)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Error getting access token:", response.text)
        return None

def upload_activities(folder_path, access_token, data_type):
    # Get list of files in the specified folder
    files = os.listdir(folder_path)

    # Iterate through each file and upload to Strava
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            upload_activity(file_path, access_token, data_type)

def upload_activity(file_path, access_token, data_type):
    # Strava upload URL
    upload_url = "https://www.strava.com/api/v3/uploads"

    # Open the file and prepare payload
    with open(file_path, 'rb') as file:
        files = {'file': file}

        # Headers with authorization
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        payload:dict = {
            'data_type': data_type
        }

        # Make the request to upload the activity
        response = requests.post(upload_url, files=files, headers=headers, data=payload)

        # Check response status
        if response.status_code == 201:
            print(f"Successfully uploaded activity: {file_path}")
        else:
            print(f"Failed to upload activity: {file_path}")
            print(f"Response: {response.text}")
            print("Check https://www.strava.com/settings/api for your upload limits")
            exit()

if __name__ == "__main__":

    print("Login to Strava, go to https://www.strava.com/settings/api and create an app.")
    client_id = input("Enter client id: ")
    client_secret = input("Enter client secret: ")
    url = "https://www.strava.com/oauth/authorize?client_id=" + client_id + "&response_type=code&redirect_uri=http%3A%2F%2Flocalhost&scope=activity:write&state=mystate&approval_prompt=force"
    print("Open below url to browser, authorize and copy code from redirect address")
    print(url)
    authorization_code = input("Enter code: ")

    access_token = get_access_token(client_id, client_secret, authorization_code)
    if access_token:
        print("Access Token:", access_token)
    else:
        print("Failed to get access token.")
        exit()

    folder_name = input("Enter folder name containing training data: ")
    data_type = input("Enter data type (fit, fit.gz, tcx, tcx.gz, gpx, gpx.gz): ")

    upload_activities(folder_name, access_token, data_type)
