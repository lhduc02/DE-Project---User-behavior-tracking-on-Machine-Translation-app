from confluent_kafka import Consumer, KafkaError

# Cấu hình Kafka Consumer
consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "my_consumer_group",       # Nhóm consumer
    "auto.offset.reset": "earliest"        # Nhận dữ liệu từ đầu nếu chưa có offset
}

# Tạo Kafka Consumer
consumer = Consumer(consumer_config)
consumer.subscribe(["topic_1", "topic_2"])

print("Listening for messages...")

try:
    while True:
        msg = consumer.poll(1.0)  # Chờ tin nhắn trong 1 giây
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        print(f"Received message: {msg.value().decode('utf-8')}")
        a = msg.value().decode('utf-8')
        print(type(a))

except KeyboardInterrupt:
    print("\nStopping consumer...")

finally:
    consumer.close()
