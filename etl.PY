import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"

#Take the html of the page in the url
page = requests.get(url)

#Create soup object by tooked html content
soup = BeautifulSoup(page.content, 'html.parser')

titles_tb = soup.find_all("a", "gem-c-document-list__item-title")

descriptions_tb = soup.find_all("p", "gem-c-document-list__item-description")

titles = []
descriptions = []

for title in titles_tb:
    titles.append(title.string)

for description in descriptions_tb:
    descriptions.append(description.string)

#Store in the file "bd_test.txt"
file = open("bd_test.txt", "w")

file.write("TITLE ==> DESCRIPTION \n\n")
for i in range(len(titles)):
    file.write(f"{titles[i]} ==>{descriptions[i]} \n\n")

file.close()

#Store in an csv file
en_tete = ["Title", "Description"]

with open("bd_test2.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=">")
    
    writer.writerow(en_tete)
    for title,description in zip(titles, descriptions):
        csv_line = [title, description]
        writer.writerow(csv_line)
        writer.writerow(["---------------------------------------", "---------------------------------------"])
        
#Read the csv file
with open("bd_test2.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter='>')

    for line in reader:
        if line["Title"] == "---------------------------------------":
            print("------------------------------------------------------------------------------")
        else:
            print(f"Le titre {line['Title']} a pour description {line['Description']} ")