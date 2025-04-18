CREATE DATABASE IF NOT EXISTS event_logs;

CREATE TABLE IF NOT EXISTS event_logs.user_events (
    event_date  INT,
    timestamp   BIGINT,
    user_id     STRING,
    device      JSON,
    geo         JSON,
    event_name  STRING
)
ENGINE=OLAP;
