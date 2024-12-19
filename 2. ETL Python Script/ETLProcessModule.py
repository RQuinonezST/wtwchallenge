from ETLConfigModule import read_config
import pyodbc

def get_connection(driver, server, database):
    connection_string = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        'Trusted_Connection=yes;'
        'Encrypt=yes;'
        'TrustServerCertificate=yes;'
    )
    return pyodbc.connect(connection_string)

def get_db_connection(config_section):
    driver = config_section["driver"]
    server = config_section["server"]
    database = config_section["database"]

    return get_connection(driver, server, database);

def extract_data(source_conn, offset, batch_size):
    cursor = source_conn.cursor()
    select_query = (
                f"SELECT EmployeeID, FirstName, LastName, Department, Salary "
                f"FROM dbo.Employees "
                f"ORDER BY EmployeeID "
                f"OFFSET {offset} ROWS FETCH NEXT {batch_size} ROWS ONLY"
            )
    cursor.execute(select_query)
    return cursor.fetchall()
    
def transform_data(data):
    # FirstName and LastName are combined into a single string and then shortened to a maximum of 100 characters.
    # Annual Salary is calculated by multiplying the Salary by 12
    return [
                (
                f"{row.EmployeeID}", 
                f"{row.FirstName} {row.LastName}"[:100], 
                f"{row.Department}", 
                row.Salary * 12
                )
                for row in data
            ]

def load_data(target_conn, data):
    cursor = target_conn.cursor()
     # Step 3: Load employess in batches with existence check
    for record in data:
        employee_id = record[0]
        # Check if the employeed was already transferred
        check_query = "SELECT COUNT(1) FROM dbo.[TransformedEmployees] WHERE EmployeeID = ?"
        cursor.execute(check_query, employee_id)
        exists = cursor.fetchone()[0]

        if not exists:
            # Insert the employee transformed record if it does not exist
            insert_query = (
                "INSERT INTO dbo.[TransformedEmployees] (EmployeeID, FullName, Department, AnnualSalary) "
                "VALUES (?, ?, ?, ?)"
            )
            cursor.execute(insert_query, record)

    # Commit after each batch
    target_conn.commit()    


def etl_employees_batch(batch_size=100):

    config = read_config()

    try:
        # Connect to Source and Destination
        source_conn = get_db_connection(config["SourceDB"])
        target_conn = get_db_connection(config["TargetDB"])

        # Step 1: Fetch data in batches
        offset = 0
        while True:
            
            rows = extract_data(source_conn, offset, batch_size)

            if not rows:  # Exit loop when no more data is fetched
                break

            transformed_data = transform_data(rows)

            load_data(target_conn, transformed_data)

            print(f"Processed batch of {len(rows)} records (Offset: {offset})")
            offset += batch_size

        print("ETL process completed successfully!")

    except pyodbc.Error as e:
        print(f"Error: {e}")

    finally:
        # Close connections
        if source_conn:
            source_conn.close()
        if target_conn:
            target_conn.close()
