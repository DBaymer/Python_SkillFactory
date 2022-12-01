# Имея входные данные в виде словаря "events" вывести цикличным методом значения, заданные в методе "Event":
class Event:
    def __init__(self, timestamp, events_type, session_id):
        self.timestamp = timestamp
        self.type = events_type
        self.session_id = session_id


events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]

for event in events:
    events_obj = Event(timestamp=event.get("timestamp"),
                       events_type=event.get("type"),
                       session_id=event.get("session_id"))
    print(events_obj.timestamp)
    print(events_obj.type)
    print(events_obj.session_id)
