CREATE TABLE IF NOT EXISTS user_events (
    event_date  DATE, 
    timestamp   BIGINT, 
    user_id     STRING, 
    device      JSON,
    geo         JSON,
    event_name  STRING
)
ENGINE=OLAP
DUPLICATE KEY(event_date, user_id)
PARTITION BY RANGE (event_date) (
    PARTITION p202403 VALUES LESS THAN ('2024-04-01'),
    PARTITION p202404 VALUES LESS THAN ('2024-05-01'),
    PARTITION p_future VALUES LESS THAN (MAXVALUE)
)
DISTRIBUTED BY HASH(user_id) BUCKETS 4
PROPERTIES (
    "replication_num" = "3"
);
