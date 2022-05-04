import requests #lib para requisição
from bs4 import BeautifulSoup #lib de extração de dados
import time

link = input("Digite seu usuário do GitHub: ")
link = "https://github.com/" + link

page = requests.get(link)

#print(page.status_code)

if(page.status_code == 404):
    print("Usuário não existe!")
    exit()

#print(page.content) #conteúdo de uma página

soup = BeautifulSoup(page.content, 'html.parser') #instância o BeatSoup na variável com o conteúdo e estrutura o html

#print(soup.prettify()) #conteúdo de uma página

name = soup.find('span', class_='p-name').get_text().strip() #retorna as string da tag na variável

userName = soup.find('span', class_='p-nickname').get_text().strip()
organization = soup.find('span', class_='p-org')
local = soup.find('span', class_='p-label')

# print("\nAguarde...")
# time.sleep(3)
# print("\nTrazendo informações...")
# time.sleep(1.5)

print("\nNome:",name)
print("\nNome de usuário:", userName)


# check if user has github pro
pro = soup.find('span', class_='Label Label--purple text-uppercase')
if pro:
    print("\nUsuário é PRO")
else:
    print("\nUsuário não é PRO")



if(organization != None):
   organization = organization.get_text().strip()
   print("\nOrganização:", organization)
if(local != None):
    local = local.get_text().strip()
    print("\nLocalidade:", local)

contributions = soup.find('div', class_='js-yearly-contributions')

contributions = contributions.find('h2', class_='f4')

contributions = contributions.get_text().strip().split()

print("\n"+contributions[0] + " contribuições\n")





