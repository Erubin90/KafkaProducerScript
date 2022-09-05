from kafka import KafkaProducer
import json


class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=self.broker,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      acks='all',
                                      retries=3)

    def send_msg(self, msg):
        future = self.producer.send(self.topic, msg)
        self.producer.flush()
        future.get(timeout=60)
