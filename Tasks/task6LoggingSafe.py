import logging

logging.basicConfig(level=logging.INFO)

username = input("Username: ")
password = input("Password: ")  # Used but not logged

logging.info(f"Login attempt by user: {username}")
# Never log passwords!
