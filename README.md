# **Project Title: Data Analysis of Clearscore User Activity**

---

## **Overview**
This project focuses on analyzing user activity data to derive actionable insights. The implementation includes extraction of files from account and reports folder, merging the files and performing analysis on the combined data

---

## **Documentation**
- All relevant details of the project have been documented in the code and this README.
- The purpose of each module and function is explained using docstrings.

---

## **Project Structure**
The project is organized logically to ensure clarity and ease of navigation:

```plaintext
project-folder/
├── account.py            # Contains data extraction from the account folder
├── report.py             # Contains data extraction from the report folder
├── main.ipynb            # Contains results of the analysis done on the merged data
├── main.py               # Merges both extracted files and exports relevant information as CSV
├── output/
│   └── bank_data.csv     # Result output in CSV
├── tests/
│   ├── test_account.py   # Unit tests for account functionality
│   └── test_report.py    # Unit tests for report functionality
├── bulk-reports/
│   ├── accounts/         # Contains raw account data of users in JSON
│   └── reports/          # Contains raw report data of users arranged in years and months
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

```

---

## **Run Convenience**
To set up and run this project:

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the main script:
    ```bash
    python account.py
    python report.py
    python main.py
    ```
3. Execute tests:
    ```bash
    pytest tests/test_account.py
    pytest tests/test_report.py
    ```
    Alternatively
    ```bash
    python -m pytest Test/test_account.py
    python -m pytest Test/test_report.py
    ```
---

## **Code Quality**
- The code adheres to PEP8 standards for readability.
- Meaningful variable names and consistent formatting have been used.

---

## **Meeting the Requirements**
All core requirements have been implemented successfully. Insights derived align with the project goals.

---

## **Testing**
- Unit tests have been written using the `pytest` framework.
- The `tests/test_account.py` and `tests/test_report.py` file ensures core functionality correctness.

---

## **Deployment steps**
- The project can be dockerized for deployment.

Building the docker image
`sudo docker build -t clearscore-data-app .`

Bind-mounting the bulk-reports folder because it is not part of the docker image
on windows:
`docker run -v C:\Users\admin\Documents\clear score\clearscore assessment\bulk-reports:/app/bulk-reports clearscore-data-app`
on WS:
`docker run -v /mnt/c/Users/admin/Documents/clear\ score/clearscore\ assessment/bulk-reports:/app/bulk-reports clearscore-data-app`

Run the docker container
`sudo docker run -d --name clearscore-app clearscore-data-app`

Alternatively, mount and run at thesame time
`sudo docker run -d --name clearscore-app -v /mnt/c/Users/admin/Documents/clear\ score/clearscore\ assessment/bulk-reports:/app/bulk-reports clearscore-data-app`

to check logs and the output of the execution
`docker logs clearscore-app`



- Data pipelines can be scheduled using tools like Apache Airflow.

---

## **Known Issue**
**Empty User Folders**: 
Some user folders in the dataset were empty, which affected the overall accuracy of the results. Given more time, these issues would be flagged through Implementing a data validation pipeline to check for completeness.

---

## **Further Improvements**
1. Implement a CI/CD pipeline to automate testing and deployment.
2. Enhance visualizations to better represent the data.

---

## **Contributors**
Ogidan Toluwaleke

