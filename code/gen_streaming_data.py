import generate_data
import json

event_date = generate_data.gen_event_date()
timestamp = generate_data.gen_timestamp()
user_id = generate_data.gen_user_id()
device = generate_data.gen_device()
geography = generate_data.gen_geography()
event_name = generate_data.gen_event_name()

data = {**event_date, **timestamp, **user_id, **device, **geography, **event_name}

print(json.dumps(data, indent=4))

