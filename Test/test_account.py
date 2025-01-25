import  pytest
from account import account_data
from pathlib import Path
import os
import json


def test_account_data(tmp_path):
    # Setup: Create a temporary account folder
    account_folder = tmp_path/"accounts"
    account_folder.mkdir()

    # Add a valid mock JSON file
    first_user = {
        "uuid": "0110c686-c6a0-4250-8dc5-832256a24f3d",
        "account": {
            "user": {
                "employmentStatus": "FT_EMPLOYED",
                "id": "1418",
                "bankName": "CAPITEC"
            }
        }
    }
    valid_file1 = account_folder/"user1.json"

    with open(valid_file1, 'w') as f:
        json.dump(first_user, f)

    second_user = {
        "uuid": "0220c345-d4a0-4250-8dc5-832256a24f3d",
        "account": {
            "user": {
                "employmentStatus": "T_EMPLOYED",
                "id": "5038",
                "bankName": "CITY BANK"
            }
        }
    }
    valid_file2 = account_folder/"user2.json"

    with open(valid_file2, 'w') as f:
        json.dump(second_user, f)


    # Execute: Run account_data with the temporary folder
    extracted_data = account_data(account_folder)

    # Assert: Verify the extracted data
    assert extracted_data[0]["uuid"] == "0110c686-c6a0-4250-8dc5-832256a24f3d"
    assert extracted_data[0]["employmentstatus"] == "FT_EMPLOYED"
    assert extracted_data[0]["userID"] == "1418"
    assert extracted_data[0]["bankname"] == "CAPITEC"



