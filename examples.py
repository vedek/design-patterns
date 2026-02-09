from perobserver import (
    Sensor,
    JSONPerobserver,
    MemoryPerobserver,
    SQLitePerobserver
)

sensor = Sensor("temperature", 25)

sensor.attach(JSONPerobserver("sensor.json"))
sensor.attach(MemoryPerobserver())
sensor.attach(SQLitePerobserver())

sensor.value = 30
sensor.value = 31
