import json
import mysql.connector
from confluent_kafka import Consumer, KafkaError

# Cấu hình Kafka Consumer
consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "my_consumer_group",
    "auto.offset.reset": "earliest"
}

# Kết nối đến StarRocks
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=9030,
    user="root",
    password="",  # Nếu có password thì thêm vào
    database="event_logs"
)
cursor = conn.cursor()

# Tạo Kafka Consumer
consumer = Consumer(consumer_config)
consumer.subscribe(["topic_1", "topic_2", "topic_3"])

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

        # Parse JSON
        event_data = json.loads(msg.value().decode("utf-8"))

        # Chuẩn bị dữ liệu
        event_date = event_data["event_date"]
        timestamp = event_data["timestamp"]
        user_id = event_data["user_id"]
        device = json.dumps(event_data["device"])  # Chuyển dict thành JSON string
        geo = json.dumps(event_data["geo"])        # Chuyển dict thành JSON string
        event_name = event_data["event_name"]

        # Câu lệnh INSERT
        insert_query = """
        INSERT INTO user_events (event_date, timestamp, user_id, device, geo, event_name)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (event_date, timestamp, user_id, device, geo, event_name)

        cursor.execute(insert_query, data)
        conn.commit()

        print(f"Inserted event for user {user_id}: {event_name}")

except KeyboardInterrupt:
    print("\nStopping consumer...")

finally:
    consumer.close()
    cursor.close()
    conn.close()
