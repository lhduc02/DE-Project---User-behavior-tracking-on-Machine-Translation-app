from kafka.admin import KafkaAdminClient, NewTopic

# Thông tin Kafka
KAFKA_BROKER = "localhost:9092"
TOPIC_LIST = ["topic_1", "topic_2"]

# Kết nối Kafka Admin
admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER)

# Kiểm tra topic đã tồn tại chưa
existing_topics = admin_client.list_topics()
new_topics = [
    NewTopic(name=topic, num_partitions=3, replication_factor=1)
    for topic in TOPIC_LIST
    if topic not in existing_topics
]

# Tạo topic nếu chưa tồn tại
if new_topics:
    admin_client.create_topics(new_topics=new_topics)
    print(f"Created topics: {', '.join(TOPIC_LIST)}")
else:
    print(f"Topics already exist: {', '.join(TOPIC_LIST)}")

# Đóng kết nối
admin_client.close()

