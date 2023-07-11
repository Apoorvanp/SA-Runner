import random
import requests
import time

while True:
    for community in range(1,10):
        for house in range(1,5):
            consumption = random.uniform(2, 10)
            payload = {"communityId": community,"houseId": house,"energyNeed":  consumption}
            response = requests.post(url='http://host.docker.internal:8080/api/v1/inventory:consume', json=payload)
            print(f'Consume {consumption} for community: {community}, house: {house} was {response.text}')
    time.sleep(2)