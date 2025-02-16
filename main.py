from account import account_data
from report import read_reports
from pathlib import Path
import pandas as pd
import numpy as np
import os

#Path to the files in account folder

account_folder = Path("bulk-reports/accounts")

report_folder = Path("bulk-reports/reports")


# calling the account data functoin to process the files and retrieve specific data
#output is a list of dictionaries
account_summary = account_data(account_folder)


#converting the list of dictionaries into a pandas Dataframe
account_df = pd.DataFrame(account_summary)

print(account_df.head())

# calling the report data function to process the files and retrieve specific data
#output is a list of dictionaries
report_summary = read_reports(report_folder)

# Convert to DataFrame for analysis
report_df = pd.DataFrame(report_summary)


# Using left join to merge account_df with report_df
merged_df = pd.merge(report_df, account_df, on="uuid", how="left")

# Convert credit_score column to integer
merged_df['credit_score'] = merged_df['credit_score'].astype(int)

# Task 1: Average Credit Score
average_credit_score = merged_df['credit_score'].mean()

#Task 2: Number of users grouped by their employment status
unique_users_by_employment_status = merged_df.groupby('employmentstatus')['uuid'].nunique()

# Task 3:  Number of users in score ranges
latest_reports = merged_df.sort_values(['uuid', 'year', 'month'], ascending=[True, False, False]).drop_duplicates('uuid')

# Define bins for score ranges (0-50, 51-100, ...)
score_bins = np.arange(0, latest_reports['credit_score'].max() + 51, 50)
score_labels = [f"{int(b)}-{int(b + 49)}" for b in score_bins[:-1]]

# Create score ranges
latest_reports['score_range'] = pd.cut(latest_reports['credit_score'], bins=score_bins, labels=score_labels, right=False)

latest_reports[['uuid', 'credit_score', 'score_range']]

# Task 4: Enriched bank data exported as csv
bank_data = latest_reports[['uuid', 'employmentstatus', 'bankname', 'active_bank_accounts', 'total_outstanding_balance']]

## Export the bank_data as csv
output_folder = "output"
output_file = "bank_data.csv"

# Export the DataFrame to CSV
output_path = os.path.join(output_folder, output_file)
bank_data.to_csv(output_path, index=False)

print(f"CSV file saved successfully at: {output_path}")
