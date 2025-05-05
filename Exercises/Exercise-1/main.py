import os
import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",  # lỗi URL
]

def download_file(url, save_dir="downloads"):
    os.makedirs(save_dir, exist_ok=True)
    filename = url.split("/")[-1]
    file_path = os.path.join(save_dir, filename)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Gây lỗi nếu HTTP status code != 200

        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error for {filename}: {http_err}")
    except Exception as err:
        print(f"Other error for {filename}: {err}")

def main():
    for url in download_uris:
        download_file(url)

if __name__ == "__main__":
    main()
