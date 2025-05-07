import os           
import json         
import csv         
from glob import glob  

def flatten_json(y):
    """Làm phẳng JSON lồng nhau: chuyển các trường lồng nhau thành dạng phẳng"""
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            # Nếu là dict, gọi đệ quy trên từng cặp key-value
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif type(x) is list:
            # Nếu là list, lặp qua từng phần tử và gọi đệ quy
            for i, a in enumerate(x):
                flatten(a, f'{name}{i}_')
        else:
            # Nếu là giá trị cuối (kiểu primitive), lưu lại vào từ điển với key đã được làm phẳng
            out[name[:-1]] = x

    flatten(y)
    return out

def convert_json_to_csv(json_file):
    """Chuyển một tệp JSON sang CSV sau khi làm phẳng nội dung"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)  # Đọc dữ liệu JSON từ file

    if isinstance(data, dict):
        data = [data]  # Nếu là một dict đơn, đưa vào danh sách để xử lý đồng nhất

    # Làm phẳng từng mục trong danh sách JSON
    flat_data = [flatten_json(item) for item in data]
    
    # Đặt tên file CSV cùng tên với file JSON
    csv_file = json_file.replace('.json', '.csv')

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        # Khởi tạo DictWriter với các trường lấy từ keys của phần tử đầu tiên
        writer = csv.DictWriter(f, fieldnames=flat_data[0].keys())
        writer.writeheader()       
        writer.writerows(flat_data)  

def main():
    # Lấy thư mục hiện tại (dùng __file__ nếu script được chạy từ file)
    base_dir = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
    
    # Xác định đường dẫn đến thư mục "data" chứa các file JSON
    data_dir = os.path.join(base_dir, 'data')
    
    # Tìm tất cả các file JSON trong thư mục "data" và các thư mục con
    json_files = glob(os.path.join(data_dir, '**', '*.json'), recursive=True)

    for json_file in json_files:
        print(f"Converting: {json_file}")  
        convert_json_to_csv(json_file)     

if __name__ == "__main__":
    main()  
