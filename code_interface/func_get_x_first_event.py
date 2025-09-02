import pandas as pd
import read_data

conn = read_data.connect_to_starrocks()

def get_x_first_event(sequence_length):
    query = f"""
    WITH RankedEvents AS (
        SELECT 
            user_id, 
            timestamp, 
            event_name,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp ASC) AS event_rank
        FROM user_events
    )
    SELECT user_id, timestamp, event_name
    FROM RankedEvents
    WHERE event_rank <= {sequence_length};
    """
    df = pd.read_sql(query, conn)
    return df

