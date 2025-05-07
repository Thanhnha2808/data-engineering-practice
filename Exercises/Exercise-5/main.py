import psycopg2  
import csv       

def create_tables(cur):
    """
    Tạo lại 3 bảng cơ sở dữ liệu: accounts, products và transactions.
    Xoá bảng cũ nếu đã tồn tại để tránh lỗi trùng schema hoặc dữ liệu.
    """
    # Xoá bảng 
    cur.execute("DROP TABLE IF EXISTS transactions;")
    cur.execute("DROP TABLE IF EXISTS products;")
    cur.execute("DROP TABLE IF EXISTS accounts;")

    # Tạo bảng 'accounts' chứa thông tin khách hàng
    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            customer_id INT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            address_1 TEXT,
            address_2 TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            join_date DATE
        );
    """)

    # Tạo bảng 'products' chứa thông tin sản phẩm
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY,
            product_code TEXT,
            product_description TEXT
        );
    """)

    # Tạo bảng 'transactions' chứa thông tin giao dịch
    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            transaction_date DATE,
            product_id INT,
            product_code TEXT,
            product_description TEXT,
            quantity INT,
            account_id INT,
            FOREIGN KEY (product_id) REFERENCES products(product_id),     -- Khóa ngoại liên kết với bảng products
            FOREIGN KEY (account_id) REFERENCES accounts(customer_id)    -- Khóa ngoại liên kết với bảng accounts
        );
    """)

def insert_csv_data(cur, conn, table_name, file_path):
    """
    Chèn dữ liệu từ file CSV vào bảng chỉ định.
    Nếu xảy ra xung đột (ví dụ trùng khóa chính), sẽ bỏ qua dòng đó.
    """
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)  

        for row in reader:
            placeholders = ', '.join(['%s'] * len(row))  
            sql = f"INSERT INTO {table_name} VALUES ({placeholders}) ON CONFLICT DO NOTHING"
            cur.execute(sql, row)  
        conn.commit()  # Ghi thay đổi vào database

def main():
    """
    Hàm chính: kết nối tới PostgreSQL, tạo bảng, rồi nạp dữ liệu từ các file CSV tương ứng.
    """
   
    host = "postgres"
    database = "airflow"
    user = "airflow"
    pas = "airflow"

    # Kết nối tới PostgreSQL
    conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    cur = conn.cursor()

    create_tables(cur)

    # Nạp dữ liệu từ các file CSV vào bảng tương ứng
    insert_csv_data(cur, conn, 'accounts', 'data/accounts.csv')
    insert_csv_data(cur, conn, 'products', 'data/products.csv')
    insert_csv_data(cur, conn, 'transactions', 'data/transactions.csv')

    print("Hoàn thành nạp dữ liệu.")

    # Đóng kết nối sau khi hoàn thành
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()  # Gọi hàm main nếu script được chạy trực tiếp
