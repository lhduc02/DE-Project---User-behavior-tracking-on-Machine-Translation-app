# Sử dụng image chính thức của Python
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy toàn bộ mã nguồn vào container
COPY . .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng 8501 cho Streamlit
EXPOSE 8501

# Chạy ứng dụng Streamlit
CMD ["streamlit", "run", "Interface.py", "--server.port=8501", "--server.address=0.0.0.0"]
