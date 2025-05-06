import requests
import pandas as pd
from bs4 import BeautifulSoup
import os


def main():
    url_base = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    response = requests.get(url_base)
    if response.status_code != 200:
        print(f"Không thể truy cập trang: {response.status_code}")
        return
    soup = BeautifulSoup(response.text,'html.parser')
    ds_tr = soup.find_all('tr')
    output = []
    for i in ds_tr[3:-1]:
        last_modified = i.find_all('td')[1].text.strip()
        if last_modified == "2024-01-19 10:27":
            key = i.find('a')['href']
            url = url_base + key
            resq = requests.get(url)
            if resq.status_code == 200:
                with open(key,'wb') as file:
                    file.write(resq.content)
                df = pd.read_csv(key,low_memory = False)
                df['HourlyDryBulbTemperature'] = pd.to_numeric(df['HourlyDryBulbTemperature'], errors='coerce')
                output.append([f"{key}" ,df['HourlyDryBulbTemperature'].max()])
                os.remove(key)
    df = pd.DataFrame(output,columns = ['file name','Hourly Dry Bulb Temperature max'])
    df.to_csv('output.csv',index = False)
    print(df)
    

if __name__ == "__main__":
    main()
