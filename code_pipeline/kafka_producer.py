from kafka import KafkaProducer
import generate_data
import json
import time

# Thông tin Kafka
KAFKA_BROKER = "localhost:9092"
TOPIC_1 = "topic_1"
TOPIC_2 = "topic_2"
TOPIC_3 = "topic_3"

# Khởi tạo Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print(f"Kafka Producer started, sending messages to topic 1, topic 2 or topic 3 based on event type...")

# Gửi dữ liệu 10 lần
for _ in range(1700):
    event_date = generate_data.gen_event_date()
    timestamp = generate_data.gen_timestamp()
    user_id = generate_data.gen_user_id()
    device = generate_data.gen_device()
    geography = generate_data.gen_geography()
    event_name = generate_data.gen_event_name()

    # Gộp tất cả dữ liệu thành một JSON object
    data = {**event_date, **timestamp, **user_id, **device, **geography, **event_name}

    # Kiểm tra event_name và gửi vào topic phù hợp
    event = event_name["event_name"]
    print("---------------------")
    print(event)
    if event[:3] == "ev1":
        producer.send(TOPIC_1, value=data)
        print(f"🛒 Sent to topic_1: {json.dumps(data, indent=4)}")
    elif event[:3] == "ev2":
        producer.send(TOPIC_2, value=data)
        print(f"🔥 Sent to topic_2: {json.dumps(data, indent=4)}")
    elif event[:3] == "ev3":
        producer.send(TOPIC_3, value=data)
        print(f"🤖 Sent to topic_3: {json.dumps(data, indent=4)}")

    # Chờ 1 giây trước khi gửi tiếp
    time.sleep(0.001)

# print("✅ Kafka Producer finished sending 10 messages.")

