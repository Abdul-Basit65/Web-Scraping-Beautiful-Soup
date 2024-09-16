import requests
from bs4 import BeautifulSoup
import pandas as pd

web = requests.get("https://www.iplt20.com/auction/2022")
soup = BeautifulSoup(web.content, "html.parser")

# Find all tables with the specified class
tables = soup.find_all("table", class_="ih-td-tab auction-tbl")

# Assuming there's only one table, you can access it like this
if len(tables) > 0:
    table = tables[0]
    
    # Find all 'th' elements with the specified class in the table
    title = table.find_all("th", class_="skip-filter")
    
    header = []
    for i in title:
        name = i.text.strip()  # Strip whitespace around text
        header.append(name)
    
    # print(header)
else:
    print("No table found with the specified class.")

df=pd.DataFrame(columns=header)
# print(df)

rows= table.find_all("tr")
# print(rows)

for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    row= [tr.text for tr in data]
    row.insert(0,first_td)
    l= len(df)
    df.loc[l]=row
print(df)

df.to_csv("TATA IPL Auction Stats.csv")

