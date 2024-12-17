import subprocess
import sys

def install_pyodbc():
    try:
        # Check if pyodbc is installed
        import importlib.util
        if importlib.util.find_spec("pyodbc") is None:
            print("Installing pyodbc...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
            print("pyodbc installed successfully.")
    except Exception as e:
        print(f"An error occurred while installing pyodbc: {e}")

# Run the installation check/install process
install_pyodbc()

import os
import configparser
import pyodbc


def etl_employees_batch(batch_size=100):

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to config.ini
    config_path = os.path.join(script_dir, "config.ini")

    # Read configuration from config.ini
    config = configparser.ConfigParser()
    config.read(config_path)

    # Source Database connection details
    source_driver = config["SourceDB"]["driver"]
    source_server = config["SourceDB"]["server"]
    source_database = config["SourceDB"]["database"]

    # Target Database connection details
    target_driver = config["TargetDB"]["driver"]
    target_server = config["TargetDB"]["server"]
    target_database =  config["TargetDB"]["database"]
    
    # Source SQL Server connection string
    source_conn_str = (
        f'DRIVER={source_driver};'
        f'SERVER={source_server};'
        f'DATABASE={source_database};'
        'Trusted_Connection=yes;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )

    # Target SQL Server connection string
    target_conn_str = (
        f'DRIVER={target_driver};'
        f'SERVER={target_server};'
        f'DATABASE={target_database};'
        'Trusted_Connection=yes;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )

    try:
        # Connect to Source and Destination
        source_conn = pyodbc.connect(source_conn_str)
        target_conn = pyodbc.connect(target_conn_str)

        source_cursor = source_conn.cursor()
        target_cursor = target_conn.cursor()

        # Step 1: Fetch data in batches
        offset = 0
        while True:
            select_query = (
                f"SELECT EmployeeID, FirstName, LastName, Department, Salary "
                f"FROM dbo.Employees "
                f"ORDER BY EmployeeID "
                f"OFFSET {offset} ROWS FETCH NEXT {batch_size} ROWS ONLY"
            )
            source_cursor.execute(select_query)
            rows = source_cursor.fetchall()

            if not rows:  # Exit loop when no more data is fetched
                break

            # Step 2: Transform data
            # FirstName and LastName are combined into a single string and then shortened to a maximum of 100 characters.
            # Annual Salary is calculated by multiplying the Salary by 12
            transformed_data = [
                (
                    f"{row.EmployeeID}", 
                    f"{row.FirstName} {row.LastName}"[:100], 
                    f"{row.Department}", 
                    row.Salary * 12
                )
                for row in rows
            ]

            # Step 3: Load employess in batches with existence check
            for record in transformed_data:
                employee_id = record[0]
                # Check if the employeed was already transferred
                check_query = "SELECT COUNT(1) FROM dbo.[TransformedEmployees] WHERE EmployeeID = ?"
                target_cursor.execute(check_query, employee_id)
                exists = target_cursor.fetchone()[0]

                if not exists:
                    # Insert the employee transformed record if it does not exist
                    insert_query = (
                        "INSERT INTO dbo.[TransformedEmployees] (EmployeeID, FullName, Department, AnnualSalary) "
                        "VALUES (?, ?, ?, ?)"
                    )
                    target_cursor.execute(insert_query, record)
            
            # Commit after each batch
            target_conn.commit()


            print(f"Processed batch of {len(rows)} records (Offset: {offset})")
            offset += batch_size

        print("ETL process completed successfully!")

    except pyodbc.Error as e:
        print(f"Error: {e}")

    finally:
        # Close connections
        if source_cursor:
            source_cursor.close()
        if target_cursor:
            target_cursor.close()
        if source_conn:
            source_conn.close()
        if target_conn:
            target_conn.close()


if __name__ == "__main__":
    etl_employees_batch(batch_size=100)  # Adjust batch size as needed
