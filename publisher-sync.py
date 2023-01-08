import random
import requests

while True:
    for(community in range(1,10)):
        for(house in range(1,5)):
            production = random.uniform(2, 10)
            payload = {"communityId": community,"houseId": house,"energyProduced":  production}
            response = requests.post(url='host.docker.internal:8080/api/v1/marketplace/produce', data=payload)
            print("Produced {} for community: {}, house: {}, {}", production, community, house response.status_code)
    time.sleep(2)