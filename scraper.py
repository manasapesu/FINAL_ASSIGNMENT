from bs4 import BeautifulSoup
import pandas as pd
import urllib.request

main_sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/assignment.html")
main_soup = BeautifulSoup(main_sauce,'html.parser')

# Loop that creates all 49 csv files
k = 0
for i in main_soup.find_all("a",href=True):
    data = []
    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/"+i.get("href"))
    soup = BeautifulSoup(sauce,'html.parser')
    if k==0:
        th = [j.text for j in soup.find_all("th")]
        k=1
    tr = soup.find_all("tr")
    for j in range(1,len(tr)):
        data.append([h.text for h in tr[j].find_all("td")])
    df = pd.DataFrame(data ,columns=th)
    df.to_csv(i.text+'.csv',index=False)