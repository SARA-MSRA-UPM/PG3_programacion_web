# external imports
import random
from time import sleep
import requests

# internal imports
from src.dataModels.radar_model import RadarModel
from src.actors.stream_reader import StreamReader


BASE_IP = "127.0.0.1"


if __name__ == '__main__':

    # Get Hello World
    response_main = requests.get("")
    print(response_main.text)

    # Environment configuration

    # Select environment to get data

    # Open socket to start stream of detections
