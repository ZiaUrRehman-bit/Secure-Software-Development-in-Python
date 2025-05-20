import subprocess
from pathlib import Path

filename = input("Enter filename to delete: ")

if Path(filename).exists():
    subprocess.run(["rm", filename])
else:
    print("File does not exist.")
