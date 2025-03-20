import pandas as pd

def start_end_seq(df, set_user_id, start_item, end_item):
    # Tính toán start_index và end_index
    if start_item == "Select item":
        min_ts = df.groupby("user_id")["timestamp"].min().reset_index()
    else:
        df_filter_by_start_item = df[df["event_name"] == f"{start_item}"]
        min_ts = df_filter_by_start_item.groupby("user_id")["timestamp"].min().reset_index()
    min_ts.rename(columns={"timestamp": "min_ts"}, inplace=True)

    if end_item == "Select item":
        max_ts = df.groupby("user_id")["timestamp"].max().reset_index()
    else:
        df_filter_by_end_item = df[df["event_name"] == f"{end_item}"]
        max_ts = df_filter_by_end_item.groupby("user_id")["timestamp"].max().reset_index()
    max_ts.rename(columns={"timestamp": "max_ts"}, inplace=True)
    min_max_df = pd.merge(min_ts, max_ts, on='user_id', how='inner')

    user_id_st = []
    seq_st = []
    for user_id in set_user_id:
        df_tmp = df[df['user_id'] == user_id]
        min_max_row = min_max_df[min_max_df['user_id'] == user_id]
        
        if min_max_row.empty:
            continue
        
        min_ts = min_max_row['min_ts'].values[0]
        max_ts = min_max_row['max_ts'].values[0]
        
        df_tmp = df_tmp[(df_tmp['timestamp'] >= min_ts) & (df_tmp['timestamp'] <= max_ts)]
        set_timestamp = sorted(set(df_tmp['timestamp']))
        
        seq = ""
        for ts in set_timestamp:
            df_ts = df_tmp[df_tmp['timestamp'] == ts]['event_name'].to_list()
            seq += " | ".join(df_ts) + " -> "
        if len(set_timestamp) > 0:
            seq = f"[{str(len(set_timestamp))}] " + seq[:-4]
        else:
            continue
        user_id_st.append(user_id)
        seq_st.append(seq)
    
    return pd.DataFrame({"user_id": user_id_st, "sequence": seq_st})

