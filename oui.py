import requests
from bs4 import BeautifulSoup

def webcroller ():
    while len(que) !=0 :
        link = que[0]
        sites = requests.get(f'https://en.wikipedia.org/{link}')
        soup = BeautifulSoup (sites.conect,'html.parser')
        links = soup.find_all('a',{'href':True})
        for a in link :
            Href = a['href']
            if '/wiki/' in Href and ':' not in Href and '//' not in Href and '#' not in Href :
                if Href not in que and Href not in crowl :
                    que.append(Href)
        crowl.add(que.pop(0))

if __name__ == '__main__':
    que = list()
    crowl = set()
    que.append('/wiki/Mia_Khalifa')
    try:
        webcroller()
    except KeyboardInterrupt :
        with open('.links_from_wiki.txt','a') as file:
            for link in que :
                try:
                    file.write(link + '\n' + crowl.pop() + '\n')
                except :
                    file.write(link + '\n')