<<<<<<< HEAD
CREATE TABLE user_events (
    event_date VARCHAR(10),
    timestamp BIGINT,
    user_id VARCHAR(30),
    device JSON,
    geo JSON
)
DUPLICATE KEY(user_id, timestamp)
DISTRIBUTED BY HASH(user_id) BUCKETS 10
PROPERTIES (
    "replication_num" = "3"
);

=======
CREATE TABLE IF NOT EXISTS event_logs.user_events (
    event_date  DATE, 
    user_id     STRING, 
    timestamp   BIGINT, 
    device      JSON,
    geo         JSON,
    event_name  STRING
)
ENGINE=OLAP
>>>>>>> master
