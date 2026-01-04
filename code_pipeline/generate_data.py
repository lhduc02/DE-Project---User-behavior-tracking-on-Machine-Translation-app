import os
import pandas as pd
import random
import string
from datetime import datetime


# Lấy thư mục chứa file script (generate_data.py)
script_dir = os.path.dirname(os.path.abspath(__file__))


# Generate event_date
def gen_event_date():
    return {"event_date" : datetime.today().strftime('%Y%m%d')}


# Generate timestamp
def gen_timestamp():
    return {"timestamp" : round(datetime.now().timestamp())}


# Generate user_id
def gen_user_id():
    characters = string.ascii_lowercase + string.digits  # Chứa cả chữ hoa, chữ thường và số
    return {'user_id': ''.join(random.choices(characters, k=24))}


# Generate data device
def gen_device():
    # Tạo đường dẫn tuyệt đối đến data_device.csv
    file_path_device = os.path.join(script_dir, "data_country_device", "data_device.csv")
    # Đọc file
    df_device = pd.read_csv(file_path_device)
    # Tạo ngẫu nhiên một số từ 1 đến 1400 và trả về user properties tương ứng
    random_number = random.randint(1, 1400)
    device_user = df_device.loc[random_number].to_list()
    # Return device_category, device_mobile_brand_name, device_mobile_marketing_name, device_OS, device_OS_version
    return {"device": {"category": device_user[0], "mobile_brand_name": device_user[1], "mobile_marketing_name": device_user[2], "OS": device_user[3], "OS_version": device_user[4]}}


# Generate data geography
def gen_geography():
    # Tạo đường dẫn tuyệt đối đến data_geography.csv
    file_path_geography = os.path.join(script_dir, "data_country_device", "data_geography.csv")
    # Đọc file
    df_geography = pd.read_csv(file_path_geography)
    # Tạo ngẫu nhiên một số từ 1 đến 231 và trả về user properties tương ứng
    random_number = random.randint(1, 231)
    geo_user = df_geography.loc[random_number].to_list()
    # Return theo thứ tự: geo_continent, geo_sub_continent, geo_country
    return {"geo": {"continent": geo_user[0], "sub_continent": geo_user[1], "country": geo_user[2]}}


# Generate event_name
def gen_event_name():
    ev1 = ["ev1_ad_click", "ev1_ad_show", "ev2_user_go_to_IAP_screen", "ev1_in_app_purchase"]
    ev2 = ["ev2_session_start", "ev2_screen_view", "ev2_notification_receive", "ev2_notification_click", "ev2_user_engagement", "ev2_user_rate_app", "ev2_app_remove"]
    ev3 = ["ev3_user_speech2text", "ev3_user_text2speech", "ev3_user_copy_translation", "ev3_machine_text2speech", "ev3_machine_speech2text"]
    return {"event_name": random.choice(ev1+ev2+ev3)}

# ev1 là những event liên quan đến IAA, IAP
# ev2 là những event liên quan đến trải nghiệm của user trên app
# ev3 là những event liên quan đến việc user sử dụng các tính năng trong app

