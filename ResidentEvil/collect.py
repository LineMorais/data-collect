# %%
import requests
from bs4 import BeautifulSoup

# %%
url = 'https://residentevildatabase.com/personagens/alex-wesker/'
headers = {
    'authority': 'www.residentevildatabase.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

resp = requests.get(url, headers=headers)

# %%
resp.status_code

# %%
resp.text

# %% Deixa estruturado para html
soup = BeautifulSoup(resp.text)
soup

# %% Buscar algo 
div_page = soup.find('div', class_='td-page-content')

# %%
paragrafo = div_page.find_all('p')[1]
paragrafo

# %%
ems  = paragrafo.find_all('em')
ems
# %%
data = {}
for i in ems:
    chave, valor = i.text.split(':')
    chave = chave.strip(' ')
    data[chave] = valor.strip(' ')

data
# %%
ems[0].text

# %%
data['Tipo sanguíneo']
# %%
