from datetime import datetime
import uuid
import threading
from MassageProducer import MessageProducer


class TenThread (threading.Thread):
    message_producer = MessageProducer('localhost:9092', 'input.channel')
    count = 0

    def __init__(self, name, counter, count):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.count = count

    def run(self):
        data = {'product_id': '',
                'quantity': 0,
                'price': 14.02,
                'price_type': str(uuid.uuid4()),
                'expiration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S+00:00")}
        i = 1
        while i <= self.count:
            data['product_id'] = str(uuid.uuid4())
            data['quantity'] = i
            self.message_producer.send_msg(data)
            i = i + 1
