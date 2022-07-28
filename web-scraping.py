import requests 
from bs4 import BeautifulSoup
import time

link = input("\nDigite seu user do GitHub: ")
link = "https://github.com/" + link

page = requests.get(link)

if(page.status_code == 404):
    print("Usuário não existe!")
    exit()

#print(page.content) #conteúdo de uma página

soup = BeautifulSoup(page.content, 'html.parser') #instância o BeatSoup na variável com o conteúdo e estrutura o html

#print(soup.prettify()) #conteúdo de uma página

name = soup.find('span', class_='p-name').get_text().strip() #retorna a string da tag na variável

userName = soup.find('span', class_='p-nickname').get_text().strip()
job = soup.find('span', class_='p-org')
local = soup.find('span', class_='p-label')
organization = soup.findAll(attrs={'data-hovercard-type':'organization', 'class':'avatar-group-item'})
contributions = soup.find('div', class_='js-yearly-contributions')
if(contributions):
    contributions = contributions.find('h2', class_='f4')
date = soup.findAll('a', class_='js-year-link')


print("\nNome:",name)
print("\nUser:", userName)

# check if user has github pro
pro = soup.find('span', class_='Label Label--purple text-uppercase')
if pro:
    print("\nUser é PRO")
else:
    print("\nUser não é PRO")

if(job):
   job = job.get_text().strip()
   print("\nEmpresa:", job)
if(local):
    local = local.get_text().strip()
    print("\nLocalidade:", local)
if(contributions):
    contributions = contributions.get_text().strip().split()
    print("\n"+contributions[0] + " contribuições\n")
if(organization):
    print("Organizações:")
    for org in organization:
        print(" - "+org['aria-label'].strip())
if(date):
    date = date[-1].get_text().strip()
    print("\nContribuindo desde "+ date + " XD")






