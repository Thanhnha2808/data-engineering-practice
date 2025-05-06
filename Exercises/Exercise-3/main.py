import requests
import gzip
from io import BytesIO

def get_file(base, key):
    url = base + key
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    return resp

def main():
    s3_base = "https://data.commoncrawl.org/"
    key = "crawl-data/CC-MAIN-2022-05/wet.paths.gz"
    
    # Tải file .gz từ S3
    resp_wet = get_file(s3_base, key)
    
    # Giải nén dữ liệu .gz và lấy URI từ dòng đầu tiên
    with gzip.open(BytesIO(resp_wet.content), 'rt', encoding='utf-8') as f:
        uri_path = f.readline().strip()

    # Tải file WARC từ URI lấy được
    resp_warc = get_file(s3_base, uri_path)
    
    # Lặp qua các dòng trong file WARC và giải mã chuỗi byte thành chuỗi văn bản
    for line in resp_warc.iter_lines(decode_unicode=True):
        if line:
            print(line)

if __name__ == "__main__":
    main()
