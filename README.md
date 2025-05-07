# 🧪 LAB 08 - Data Engineering: ETL Pipeline Cơ Bản

## 👨‍💻 Thông tin sinh viên

- Họ tên: Võ Thanh Nhã  
- MSSV: 23709251
- Lớp: DHKHDL19B

---

## 🎯 Mục tiêu của Lab

- Hiểu quy trình xây dựng một pipeline ETL cơ bản.  
- Thực hành trích xuất dữ liệu từ nguồn file và cơ sở dữ liệu.  
- Làm sạch, biến đổi dữ liệu với Python + Pandas.  
- Nạp dữ liệu vào PostgreSQL.  
- Áp dụng Docker để triển khai môi trường linh hoạt.  
- Giới thiệu về Airflow cho tự động hóa.

---

## 🛠️ Công cụ sử dụng

- Python, Pandas  
- MySQL, PostgreSQL  
- Docker  
- Apache Airflow  
- CSV file (dữ liệu mẫu)  
- DBeaver / PgAdmin (truy vấn DB)

---

## 📌 Quy trình thực hiện

### 1. Extract
- Tải dữ liệu từ file CSV và cơ sở dữ liệu MySQL.
- Dùng Python để đọc dữ liệu từ cả hai nguồn.

### 2. Transform
- Dùng Pandas để xử lý thiếu dữ liệu, chuẩn hóa định dạng, đổi tên cột.
- Kết hợp các bảng dữ liệu nếu cần.

### 3. Load
- Kết nối PostgreSQL bằng SQLAlchemy.
- Nạp dữ liệu đã xử lý vào các bảng tương ứng.

### 4. Orchestrate
- Viết DAG trong Airflow gồm các task: extract → transform → load.
- Chạy pipeline tự động theo lịch định sẵn (daily).

---

## 📈 Kết quả

- Dữ liệu được trích xuất và xử lý thành công.
- Nạp dữ liệu vào PostgreSQL đúng định dạng.
- Pipeline ETL chạy mượt thông qua Airflow.
- Có thể mở rộng cho các tập dữ liệu lớn hơn.

---


#Lab 9
# 🧪 Các Bài Tập Python cho Data Engineering

Đây là 5 bài tập thực hành sử dụng Python mô phỏng các công việc phổ biến trong lĩnh vực Data Engineering như tải file, web scraping, xử lý dữ liệu từ AWS S3, chuyển đổi JSON, và tương tác với PostgreSQL.

---

## ✅ Bài 1 – Tải File bằng Python

Sử dụng thư viện `requests` để tải 10 file `.zip` từ internet, sau đó giải nén thành các file `.csv` và lưu vào thư mục `downloads` (được tạo tự động bằng Python). Mỗi file được đặt đúng tên gốc và file `.zip` được xóa sau khi giải nén.  
➡️ **Kỹ năng**: làm việc với HTTP request, xử lý file và thư mục, giải nén dữ liệu.

---

## ✅ Bài 2 – Web Scraping và Tải File

Web scrape trang dữ liệu thời tiết của NOAA để tìm file có ngày sửa đổi là `2024-01-19 10:27`. Dùng Python phân tích HTML để lấy đúng tên file, sau đó tải về và dùng Pandas để tìm bản ghi có **nhiệt độ khô cao nhất**.  
➡️ **Kỹ năng**: web scraping, xử lý HTML, dùng Pandas để phân tích dữ liệu.

---

## ✅ Bài 3 – Làm việc với AWS S3 qua Boto3

Dùng thư viện `boto3` để tải file `.gz` từ bucket S3 `commoncrawl`, giải nén để lấy URL từ dòng đầu tiên và tiếp tục tải file dữ liệu tương ứng. Dữ liệu được in ra từng dòng bằng phương pháp **streaming** (không tải toàn bộ vào RAM).  
➡️ **Kỹ năng**: thao tác với AWS S3, đọc file nén `.gz`, xử lý file lớn hiệu quả.

---

## ✅ Bài 4 – Chuyển JSON sang CSV trong thư mục phức tạp

Duyệt toàn bộ thư mục `data` (có cấu trúc không đồng đều) để tìm file `.json`. Sau đó, làm phẳng các trường dữ liệu lồng nhau (như `{"coordinates": [...]}`) và chuyển đổi từng file JSON thành file `.csv` tương ứng.  
➡️ **Kỹ năng**: đọc & ghi JSON/CSV, xử lý thư mục phức tạp, flatten dữ liệu.

---

## ✅ Bài 5 – Mô Hình Dữ Liệu với Postgres và Python

Phân tích 3 file CSV trong thư mục `data` để viết câu lệnh `CREATE TABLE` với đầy đủ **kiểu dữ liệu**, **khóa chính/khóa ngoại**, và **index**. Dùng thư viện `psycopg2` để kết nối PostgreSQL, tạo bảng và chèn dữ liệu từ file CSV vào.  
➡️ **Kỹ năng**: thiết kế schema, tạo bảng SQL, chèn dữ liệu vào PostgreSQL bằng Python.

---

## 🛠 Công Nghệ Sử Dụng

- Python 3
- requests, aiohttp, boto3, pandas, psycopg2
- Docker & Docker Compose
- PostgreSQL
- HTML parsing (web scraping)
