from bs4 import BeautifulSoup
import requests
import csv

page = 1
file = open("data.csv", 'w')
writer = csv.writer(file)
writer.writerow(["POLITICIAN", "BUY/SELL", "COMPANY", "SIZE OF OPTION"])


while page < 10:
    page_to_scrape = requests.get(f"https://www.capitoltrades.com/trades?page={page}&sortBy=-txDate").text


    soup = BeautifulSoup(page_to_scrape, "html.parser")

    politician = soup.find_all("h2", "q-fieldset politician-name text-[13px] text-foreground")
    stock = soup.find_all("a", "hover:no-underline text-txt-interactive")
    buy_or_sell = soup.find_all("td", "q-td q-column--txType")
    size = soup.find_all("span", "mt-1 text-size-2 text-txt-dimmer hover:text-foreground")    

    for p,s,b,sz in zip(politician,stock,buy_or_sell,size):
        writer.writerow([p.text, b.text, s.text, sz.text])

    page = page + 1
file.close()








