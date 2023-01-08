# from influxdb_client import InfluxDBClient, Point, WriteOptions
import json

# from paho import mqtt
import paho.mqtt.client as mqtt

# # Connect to InfluxDB
# client = InfluxDBClient(url="localhost:8086", token="C4UnUor3ZirUVgTbefW_iX_biCT7XIm0baBjFYY6aq98OMrwrJKDXgyHS0jD1u-TWBriihFg4hmAOWQvnZQ-lA==", org="SE$GD")
# write_api = client.write_api(write_options=WriteOptions(batch_size=1, flush_interval=1000))

# Connect to MQTT broker
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883)

# Subscribe to topics
topics = ["production", "consumption", "radiation"]
for topic in topics:
    mqtt_client.subscribe(topic)

def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")
    payload = json.loads(payload)
    print(payload)
    # if "t1b1" in payload:
    #     t1b1 = payload["t1b1"]
    #     if topic == "temperature":
    #         temperature = t1b1
    #         # print("temp:", temperature)
    #         point = Point("temperature").field("value", temperature)
    #         write_api.write(bucket="Coldchain", record=point)
    #     elif topic == "humidity":
    #         humidity = t1b1
    #         # print("humidity:", humidity)
    #         point = Point("humidity").field("value", humidity)
    #         write_api.write(bucket="Coldchain", record=point)
    #     elif topic == "pressure":
    #         pressure = t1b1
    #         # print("pressure:", pressure)
    #         point = Point("pressure").field("value", pressure)
    #         write_api.write(bucket="Coldchain", record=point)
    # print("Writing data to InfluxDB:", point)






# Set callback
mqtt_client.on_message = on_message

# Loop forever
mqtt_client.loop_forever()
