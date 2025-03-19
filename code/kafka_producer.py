from kafka import KafkaProducer
import generate_data
import json
import time

# Thông tin Kafka
KAFKA_BROKER = "localhost:9092"
TOPIC_1 = "topic_1"
TOPIC_2 = "topic_2"

# Khởi tạo Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

print(f"Kafka Producer started, sending 10 messages to {TOPIC_1} or {TOPIC_2} based on event type...")

# Gửi dữ liệu 10 lần
<<<<<<< HEAD
for _ in range(100):
=======
for _ in range(1000):
>>>>>>> master
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
    if event in {"view", "click"}:
        producer.send(TOPIC_1, value=data)
        print(f"🔥 Sent to {TOPIC_1}: {json.dumps(data, indent=4)}")
    elif event == "purchase":
        producer.send(TOPIC_2, value=data)
        print(f"🛒 Sent to {TOPIC_2}: {json.dumps(data, indent=4)}")

    # Chờ 1 giây trước khi gửi tiếp
<<<<<<< HEAD
    time.sleep(0.001)
=======
    time.sleep(0.00001)
>>>>>>> master

# print("✅ Kafka Producer finished sending 10 messages.")

