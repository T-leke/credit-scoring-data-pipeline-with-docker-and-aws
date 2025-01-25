import os
import json
import pytest
from pathlib import Path
from report import read_reports


@pytest.fixture
def mock_report_folder(tmp_path):
    # Create a mock report folder structure
    base_dir = tmp_path / "bulk-reports" / "reports"
    base_dir.mkdir(parents=True)

    # Create year and month folders
    year_dir = base_dir / "2024"
    month_dir = year_dir / "12"
    month_dir.mkdir(parents=True)

    # Add valid JSON file
    file_folder = month_dir / "folder1"
    file_folder.mkdir()
    valid_file = file_folder / "report1.json"
    with open(valid_file, "w") as f:
        json.dump({
            "account-id": "12345",
            "user-uuid": "uuid123",
            "report": {
                "ScoreBlock": {
                    "Delphi": [{"Score": 750}]
                },
                "Summary": {
                    "Payment_Profiles": {
                        "CPA": {
                            "Bank": {
                                "Total_number_of_Bank_Active_accounts_": 3,
                                "Total_outstanding_balance_on_Bank_active_accounts": 15000
                            }
                        }
                    }
                }
            }
        }, f)

    # Add an empty folder
    empty_folder = month_dir / "folder2"
    empty_folder.mkdir()

    return base_dir


def test_read_reports(mock_report_folder):
    # Call the function with the mock folder
    result = read_reports(mock_report_folder)

    # Assertions
    assert len(result) == 2  # One valid file + one empty folder
    # Validate extracted data from the JSON file
    assert result[0]["account-id"] == "12345"
    assert result[0]["uuid"] == "uuid123"
    assert result[0]["credit_score"] == 750
    assert result[0]["active_bank_accounts"] == 3
    assert result[0]["total_outstanding_balance"] == 15000
    assert result[0]["year"] == "2024"
    assert result[0]["month"] == "12"
    # Validate empty folder entry
    assert result[1]["account-id"] is None
    assert result[1]["uuid"] is None
    assert result[1]["credit_score"] == 0
    assert result[1]["active_bank_accounts"] == 0
    assert result[1]["total_outstanding_balance"] == 0
    assert result[1]["year"] == "2024"
    assert result[1]["month"] == "12"
