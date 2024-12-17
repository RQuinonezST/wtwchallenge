# WTW Challenge
WTW code challenge: ETL Process with SQL Server and GraphQL

# Project Instructions

## Run SQL Scripts

Open the folder :open_file_folder: "1. SQL Scripts".

There you will find two SQL Scripts:

* :page_with_curl: 1. Create and Populate Employees.sql:\
This script will create the database SourceDB, the table Employees, and populate it with sample data.

* :page_with_curl: "2. Create TransformedEmployees.sql"\
This script will create the database TargetDB and the table TransformedEmployees.

## Run Python ETL Script

Open the folder :open_file_folder: "2. ETL Python Script".

1. **Set up** the config.ini file with the server name or IP. The script is considering a connection using Windows Authentication, so a username and password are not needed.

*Configuration Example:*
~~~~
[SourceDB]
driver = {ODBC Driver 17 for SQL Server}
server = .
database = SourceDB

[TargetDB]
driver = {ODBC Driver 17 for SQL Server}
server = .
database = TargetDB
~~~~

2. **Run** the script: :gem: ETLEmployeesToTransformedEmployees.py

This script will install the pyodbc library if it's missing, then load and transform Employees data in 100-record chunks to avoid excessive memory usage. The transformed data is then saved to TransformedEmployees.

## GraphQL API

Open the folder :open_file_folder: "3. GraphQL API".

Open the solution WTWGraphAcces.sln\
First **Set up** the project WTWGraphAccess.Api as the startup project
Then **Set up** the connection string localed in the file: appsettings.json

*Configuration Example:*
~~~~
"WTWTargetDBConnectionString": "Data Source=.;Initial Catalog=TargetDB;Integrated Security=True;Connect Timeout=30;Encrypt=True;Trust Server Certificate=True;"
~~~~

*Explanation*
- **Data Source**: This setting specifies the database server. In this case, a dot (.) is used to indicate the local server.
- **Windows Authentication**: The connection uses Windows Authentication, which means no explicit username or password is required.

Finally do a full rebuild of the solution and then run the project WTWGraphAccess.Api, you will get the URL pointing to the root that give you access to a playground to work with the graph query.
The URL to consume the API will end in /graphql such as for example: https://localhost:7084/graphql


*Query Examples*

~~~~
query {
  employee {
    employeeID
    fullName
    department
    annualSalary
  }
}


query {
  employeebydepartment(department: "Finance") 
  {
    employeeID
    fullName
    annualSalary
  }
}
~~~~
