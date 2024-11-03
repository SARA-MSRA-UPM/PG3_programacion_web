# external imports
import requests
# internal imports


MAIN_URL = "http://127.0.0.1:8000"


if __name__ == '__main__':
    response = requests.get(MAIN_URL).json()
    print(type(response))