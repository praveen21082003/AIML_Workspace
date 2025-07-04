from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
import os


file_path = f"{input("enter a file name:")}.xlsx"


if os.path.exists(file_path):
    print("File already \n existsSkipping data extraction again .")
    exit()

driver = webdriver.Edge()
driver.get(input("enter your link:"))
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
driver.quit()

table = soup.find("table", id="chapterListTable")

headers = [th.text.strip() for th in table.find("thead").find_all("th")]

# Initialize dictionary for each header
data = {header: [] for header in headers}

# Extract rows and fill data
rows = table.find("tbody").find_all("tr")
for row in rows:
    cols = [td.text.strip() for td in row.find_all("td")]
    for i, value in enumerate(cols):
        if i < len(headers):  
            data[headers[i]].append(value)


# data - dtatframes - xlsx
print("Data extracting to excel file")
df = pd.DataFrame(data)
# print(df)
df.to_excel(f"{file_path}", index=False)
print("Exctracted sucessfully")


