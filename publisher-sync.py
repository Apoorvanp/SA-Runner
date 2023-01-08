import random
import requests
import time

while True:
    for community in range(1,10):
        for house in range(1,5):
            production = random.uniform(2, 10)
            payload = {"communityId": community,"houseId": house,"energyProduced":  production}
            response = requests.post(url='http://host.docker.internal:8080/api/v1/marketplace/produce', json=payload)
            print("Produced {} for community: {}, house: {}, {}", production, community, house, response.status_code)
    time.sleep(2)