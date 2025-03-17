CREATE TABLE IF NOT EXISTS event_logs.user_events (
    event_date  DATE, 
    user_id     STRING, 
    timestamp   BIGINT, 
    device      JSON,
    geo         JSON,
    event_name  STRING
)
ENGINE=OLAP