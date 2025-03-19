import streamlit as st
import read_data
import func_get_x_first_event
import func_get_x_end_event
import func_start_end_seq


# Tạo sidebar
st.sidebar.title("Tùy chọn")
option = st.sidebar.selectbox(
    "Select feature:",
    ["Main", "Sequence", "Compare chart"]
)

# Hiển thị nội dung tương ứng
st.title("Data Platform Interface")

if option == "Main":
    pass

elif option == "Sequence":
    # Đọc dữ liệu từ StarRocks (chỉ chạy nếu chưa có)
    if "df" not in st.session_state:
        st.session_state.df = read_data.connect_to_starrocks()

    a1, a2, a3 = st.columns(3)
    b1, b2 = st.columns(2)

    # Yêu cầu user nhập các thông tin
    with a1:
        sequence_type = st.radio("Sequence type:", ["First sequence", "Last sequence"], key="sequence_type")
    with a2:
        sequence_length_type = st.radio("Sequence length type:", ["Long sequence", "Short sequence"], key="sequence_length_type")
    with a3:
        sequence_length = st.number_input("Sequence length [1,1000]:", min_value=1, max_value=1000, value=10, step=1, key="sequence_length")

    ev1 = ["ev1_ad_click", "ev1_ad_show", "ev2_user_go_to_IAP_screen", "ev1_in_app_purchase"]
    ev2 = ["ev2_session_start", "ev2_screen_view", "ev2_notification_receive", "ev2_notification_click", "ev2_user_engagement", "ev2_user_rate_app", "ev2_app_remove"]
    ev3 = ["ev3_user_speech2text", "ev3_user_text2speech", "ev3_user_copy_translation", "ev3_machine_text2speech", "ev3_machine_speech2text"]
    with b1:
        start_item = st.selectbox("Start item:", ["Select item"]+ev1+ev2+ev3, key="start_item")
    with b2:
        end_item = st.selectbox("End item:", ["Select item"]+ev1+ev2+ev3, key="end_item")

    exclude_items = st.text_input("Exclude items:", "", key="exclude_items")
    exclude_items = [item.strip() for item in exclude_items.split(",") if item.strip()]

    # Giữ lại kết quả cũ nếu chưa ấn "Run"
    if "df_result" not in st.session_state:
        st.session_state.df_result = None

    # Run code
    c1, c2, c3, c4, c5 = st.columns(5)
    with c3:
        run_button1 = st.button("Run Sequence")

    if run_button1:
        if sequence_type == 'First sequence' and sequence_length_type == 'Short sequence':
            st.session_state.df_result = "Do not build 'Short sequence' feature"
        elif sequence_type == 'First sequence' and sequence_length_type == 'Long sequence':
            df = func_get_x_first_event.get_x_first_event(sequence_length)
            set_user_id = set(df['user_id'])
            df_final = func_start_end_seq.start_end_seq(df, set_user_id, start_item, end_item)
            st.session_state.df_result = df_final
        elif sequence_type == 'Last sequence' and sequence_length_type == 'Short sequence':
            st.session_state.df_result = "Do not build 'Short sequence' feature"
        elif sequence_type == 'Last sequence' and sequence_length_type == 'Long sequence':
            df = func_get_x_end_event.get_x_end_event(sequence_length)
            set_user_id = set(df['user_id'])
            df_final = func_start_end_seq.start_end_seq(df, set_user_id, start_item, end_item)
            st.session_state.df_result = df_final

    # Chỉ hiển thị nếu đã có kết quả
    if st.session_state.df_result is not None:
        if isinstance(st.session_state.df_result, str):
            st.write(st.session_state.df_result)
        else:
            st.dataframe(st.session_state.df_result)

            # Hiển thị chart group sequence by user_id
            st.write("The chart below shows group sequence by user_id")
            st.dataframe(st.session_state.df_result.groupby("sequence")['user_id'].count())

    st.write("End process sequence")

elif option == "Compare chart":
    st.write("Not done yet")


