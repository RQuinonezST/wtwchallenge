import subprocess
import sys
import importlib.util

# Check if pyodbc is installed
def install_pyodbc():
    try:
        if importlib.util.find_spec("pyodbc") is None:
            print("Installing pyodbc...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyodbc"])
            print("pyodbc installed successfully.")
    except Exception as e:
        print(f"An error occurred while installing pyodbc: {e}")
