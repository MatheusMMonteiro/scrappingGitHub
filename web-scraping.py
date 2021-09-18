import requests #lib para requisição
from bs4 import BeautifulSoup #lib de extração de dados
import time

link = input("Digite seu usuário do GitHub: ")
link = "https://github.com/" + link

page = requests.get(link)

#print(page.status_code)

#print(page.content) #conteúdo de uma página

soup = BeautifulSoup(page.content, 'html.parser') #instância o BeatSoup na variável com o conteúdo e estrutura o html

#print(soup.prettify()) #conteúdo de uma página

name = soup.find('span', class_='p-name').get_text().strip() #retorna as string da tag na variável
userName = soup.find('span', class_='p-nickname').get_text().strip()
organization = soup.find('span', class_='p-org').get_text().strip()
local = soup.find('span', class_='p-label').get_text().strip()

print("\nAguarde...")
time.sleep(3)
print("\nTrazendo informações...")
time.sleep(1.5)

print("\nNome:",name)
print("\nNome de usuário:", userName)
print("\nOrganização:", organization)
print("\nLocalidade:", local)

imgs = soup.find_all('img', 'avatar')

