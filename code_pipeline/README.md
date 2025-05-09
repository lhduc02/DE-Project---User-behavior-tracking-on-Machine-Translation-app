# 1. Khởi chạy các docker compose
## 1.1. Tải Docker image của StarRocks và chạy
```cmd
docker pull starrocks/allin1-ubuntu
docker run -d --name starrocks-allin1 \
  -p 8030:8030 \    # Web UI (FE)
  -p 9030:9030 \    # MySQL port
  -p 8040:8040 \    # BE web UI
  -p 9050:9050 \    # BE thrift
  starrocks/allin1-ubuntu
```
Thông tin đăng nhập của StarRocks
* host: 127.0.0.1 (nếu chạy dưới local)
* port: 9030
* username: "root"
* password: ""    #Không có mật khẩu

## 1.2. Chạy docker-compose để khởi tạo Kafka, Prometheus, Grafana
Trên terminal, vào folder chứa docker-compose.yml
```cmd
sudo docker-compose up -d
```

---
# 2. Chạy các components
## 2.1. Chạy file create_topic.py để tạo các topics
```cmd
python -u /path/to/create_topic.py
```

## 2.2. Chạy file kafka_consumer.py để bắt đầu nhận event từ Kafka Cluster, sau đó chuyển vào StarRocks database
```cmd
python -u /path/to/kafka_consumer.py
```

## 2.3. Chạy file kafka_producer.py để bắt đầu bắn dữ liệu vào Kafka Cluster
```cmd
python -u /path/to/kafka_producer.py
```

## 2.4. Chạy Airflow
* Chạy airflow server
```cmd
airflow webserver --port 8081
```

* Chạy airflow scheduler
```cmd
airflow scheduler
```


