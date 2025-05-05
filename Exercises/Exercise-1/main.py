import os
import requests
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # lỗi URL
]

def download_and_extract_file(url, save_dir="downloads"):
    os.makedirs(save_dir, exist_ok=True)
    filename = url.split("/")[-1]
    file_path = os.path.join(save_dir, filename)

    try:
        print(f"Tải xuống: {filename}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✔️ Đã tải: {filename}")

        # Giải nén nếu là file zip
        if zipfile.is_zipfile(file_path):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(save_dir)
            os.remove(file_path)
            print(f"📦 Đã giải nén và xoá: {filename}")
        else:
            print(f"⚠️ Không phải file zip: {filename}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error for {filename}: {http_err}")
    except Exception as err:
        print(f"❌ Lỗi khác cho {filename}: {err}")

def main():
    for url in download_uris:
        download_and_extract_file(url)

if __name__ == "__main__":
    main()
