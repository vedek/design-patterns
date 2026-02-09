from abc import ABC, abstractmethod
import json, sqlite3
from datetime import datetime

class Perobserver(ABC):
    @abstractmethod
    def persist(self, obj):
        pass

class Observable:
    def __init__(self):
        self._perobservers = []

    def attach(self, p):
        self._perobservers.append(p)

    def notify(self):
        for p in self._perobservers:
            p.persist(self)

class Sensor(Observable):
    def __init__(self, name, value=0):
        super().__init__()
        self.name = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.notify()

    def to_dict(self):
        return {"name": self.name, "value": self._value}

class JSONPerobserver(Perobserver):
    def __init__(self, path):
        self.path = path

    def persist(self, obj):
        data = obj.to_dict()
        data["timestamp"] = datetime.utcnow().isoformat()
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
