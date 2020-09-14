import requests
from bs4 import BeautifulSoup

musicians = input("Welcome! This script will tell you something about your favourite musician! Who knows if it is true or invented though :) Enter your favourite musician : ")
#musicians = "ringo-starr"

Error = True
while Error:

        url = "https://www.biography.com/musician/" + musicians
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        if soup.find_all(lambda tag: "404 Error" in tag.text) :
                musicians = input("I could not find this! Input another musician: ")
        else:
                Error = False

bio = soup.find('p').get_text()

with open("musician-bio.txt", "w") as file:
        file.write(bio)
