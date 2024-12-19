from ETLInstallationModule import install_pyodbc
from ETLProcessModule import etl_employees_batch

# Run the installation check/install process
install_pyodbc()


if __name__ == "__main__":
    etl_employees_batch(batch_size=100)  # Adjust batch size as needed
