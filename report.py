from pathlib import Path
import os
import json
import pandas as pd

#Path to the files in report folder
report_folder = Path("bulk-reports/reports")

# function to read all JSON files
def read_reports(report_folder):
    extracted_data = []  # To store extracted data

    # Iterate over years
    for year in os.listdir(report_folder):
        year_path = os.path.join(report_folder, year)
        
        # Ensure year_path is a directory
        if not os.path.isdir(year_path):
            continue

        # Iterate over months
        for month in os.listdir(year_path):
            month_path = os.path.join(year_path, month)

            # Ensure month_path is a directory
            if not os.path.isdir(month_path):
                continue

            # Iterate over files in the month directory
            for file_folder in os.listdir(month_path):
                file_folder_path = os.path.join(month_path, file_folder)

                # Ensure file_folder_path is a directory
                if not os.path.isdir(file_folder_path):
                    continue

                files = os.listdir(file_folder_path)

                if not files:  #If the folder is empty and there is no file
                        extracted_data.append({
                            "account-id": None,
                            "uuid": None,
                            "year": year,
                            "month": month,
                            "credit_score": 0,
                            "active_bank_accounts": 0,
                            "total_outstanding_balance": 0
                        })
                        continue
                
                for file in files:

                    file_path = os.path.join(file_folder_path, file)

                    # If the file exists and is in json format
                    if file.endswith(".json"):
                        try:
                            with open(file_path, "r") as f:
                                json_data = json.load(f)

                                # Extracting account id and other necessary fields
                                account_id = json_data.get("account-id")
                                uuid = json_data.get("user-uuid")
                                credit_score = json_data.get("report", {}).get("ScoreBlock", {}).get("Delphi", [{}])[0].get("Score", 0)

                                total_active_accounts = json_data.get("report", {}).get("Summary", {}).get(
                                "Payment_Profiles", {}).get("CPA", {}).get("Bank", {}).get("Total_number_of_Bank_Active_accounts_", 0)

                                total_outstanding_balance = json_data.get("report", {}).get("Summary", {}).get(
                                "Payment_Profiles", {}).get("CPA", {}).get("Bank", {}).get("Total_outstanding_balance_on_Bank_active_accounts", 0)
                                
                                extracted_data.append({
                                    "account-id": account_id,
                                    "uuid": uuid,
                                    "year": year,
                                    "month": month,
                                    "credit_score": credit_score,
                                    "active_bank_accounts": total_active_accounts,
                                    "total_outstanding_balance": total_outstanding_balance

                                })
                                
                                print(f"Processed file: {file_path}")
                        except Exception as e:
                            print(f"Error reading file {file_path}: {e}")

    return extracted_data
