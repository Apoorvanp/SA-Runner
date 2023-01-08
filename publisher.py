import random
import json
import time
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("localhost", 1883)
topics = ["production", "consumption", "radiation"]

while True:
    production = random.uniform(2, 10) 
    consumption = random.uniform(50, 100) 
    radiation = random.uniform(1000, 1100)
    key = 'c' + str(random.randint(1, 10)) + 'h' + str(random.randint(1,5))
    payload = {"production": production, "consumption": consumption, "radiation": radiation}
    for topic, value in payload.items():
        client.publish(topic, json.dumps({key: value}))
    print("Published Payload:", payload)
    time.sleep(2)