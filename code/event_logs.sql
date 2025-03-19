CREATE TABLE IF NOT EXISTS user_events (
    event_date  DATE, 
    timestamp   BIGINT, 
    user_id     STRING, 
    device      JSON,
    geo         JSON,
    event_name  STRING
)
ENGINE=OLAP;
