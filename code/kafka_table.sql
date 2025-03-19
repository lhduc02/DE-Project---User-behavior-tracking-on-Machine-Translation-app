CREATE TABLE kafka_events (
    event_date  DATE, 
    timestamp   BIGINT, 
    user_id     STRING, 
    device      JSON, 
    geo         JSON, 
    event_name  STRING
)
ENGINE=KAFKA
PROPERTIES (
    "kafka_broker_list" = "localhost:9092",
    "kafka_topic" = "topic_1,topic_2",
    "kafka_partitions" = "0,1",
    "kafka_offsets" = "OFFSET_BEGINNING",
    "kafka_format" = "json",
    "kafka_jsonpaths" = "[\"$.event_date\", \"$.timestamp\", \"$.user_id\", \"$.device\", \"$.geo\", \"$.event_name\"]",
    "kafka_current_timestamp" = "false"
);