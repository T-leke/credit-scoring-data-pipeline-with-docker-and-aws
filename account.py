from pathlib import Path
import os
import json
import pandas as pd


#Path to the files in account folder

account_folder = Path("bulk-reports/accounts")


#function to load the json file

def load_json(file_path):
    with open(file_path, 'r') as file:

        data = json.load(file)

        print(f"Processing file: {file_path}")
        
        return data
    
def account_data(folder_path):  # this functions iterates through the accounts folder to process the json files
    #List to store selected data for reporting for further processing
    extracted_data = []
    
    for file in os.listdir(folder_path): #iterating through files in the account folder
        if file.endswith(".json"): # this condition ensures only json files are processed
            file_path = os.path.join(folder_path, file)
        
        try:
            json_data = load_json(file_path)

            #Extract only the necessary fields
            uuid = json_data.get("uuid")
            employment_status = json_data.get("account", {}).get("user", {}).get("employmentStatus")
            user_id = json_data.get("account", {}).get("user", {}).get("id")
            bank_name = json_data.get("account", {}).get("user", {}).get("bankName")

            extracted_data.append({
                "uuid": uuid,
                "employmentstatus": employment_status,
                "userID": user_id,
                "bankname": bank_name
            })
            print(f"Processed: {file}")

        except Exception as e:
            print(f"Error processing file {file}: {e}")

    return extracted_data



