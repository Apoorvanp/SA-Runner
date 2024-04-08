import random
import requests
import time

while True:
    for community in range(1,10):
        for house in range(1,5):
            production = random.uniform(2, 10)
            payload = {"communityId": community,"houseId": house,"energyProduced":  production}
            response = requests.post(url='http://host.docker.internal:8080/api/v1/productions', json=payload)
            print(f'Produced {production} for community: {community}, house: {house}')
    time.sleep(2)