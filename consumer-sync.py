import os
import random
import requests
import time

host = os.environ['HOST']

while True:
    for community in range(1,10):
        for house in range(1,5):
            consumption = random.uniform(2, 10)
            payload = {"communityId": community,"houseId": house,"energyNeed":  consumption}
            response = requests.post(url=f'http://{host}/api/v1/consumptions', json=payload)
            print(f'Consume {consumption} for community: {community}, house: {house} was {response.text}')
    time.sleep(2)