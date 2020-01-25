import sys
from getpass import getpass

from fedora.client import AuthError
from fedora.client.fas2 import AccountSystem

username = input("Enter your username: ")
password = getpass("Enter your password: ")

try:
    FAS = AccountSystem(username=username, password=password)

    username_query = input("Enter username to query: ")

    response = FAS.person_by_username(username=username_query)

    print(f"\nEmail found: {response['email']}")

except AuthError:
    print("\nYou entered your details wrong.")
    sys.exit(1)

except KeyError:
    print("\nUsername not found. Please enter a valid username.")
