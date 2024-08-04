import requests
import time
import os


api_key = 'cc027af3f742ed98a3bd943c274c0127a6f72cfbb99cb93d80489b9e72efe508'
url = 'https://www.virustotal.com/api/v3/files'

def virus_scanning(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file)}
        headers = {'x-apikey': api_key}
        response = requests.post(url, files=files, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        data_id = json_response['data']['id']
        print(f"File uploaded successfully. Data ID: {data_id}")
    else:
        print(f"Failed to upload file. Status Code: {response.status_code}")
        exit()

    report_url = f'https://www.virustotal.com/api/v3/analyses/{data_id}'

    while True:
        response = requests.get(report_url, headers=headers)
        json_response = response.json()
        if json_response['data']['attributes']['status'] == 'completed':
            print("Analysis completed.")
            break
        else:
            print("Analysis in progress. Waiting for 10 seconds before retrying...")
            time.sleep(10)

    scan_results = json_response['data']['attributes']['results']
    checks = 0

    for engine, result in scan_results.items():
        if result['category'] == 'malicious':
            checks += 1

    if checks > 0:
        print("The file is a Virus.")
    else:
        print("The file is clean from Viruses.")


def scan_directory(directory_name):
    for dirpath, dirnames, filenames in os.walk(directory_name):
        print(f'Scanning directory: {dirpath}')
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(f'Scanning file: {file_path}')
            virus_scanning(file_path)


def main():
    scan_directory("jjj")


if __name__ == '__main__':
    main()