from perobserver import Sensor, JSONPerobserver

sensor = Sensor("temperature", 25)
sensor.attach(JSONPerobserver("sensor.json"))

sensor.value = 30
sensor.value = 31
