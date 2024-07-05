import requests
from bs4 import BeautifulSoup

REQUEST_URL = "https://m.mangatown.com"

class MangaTown:

  def get_url(self):
    return REQUEST_URL
  
  def get_details_url(self):
    return REQUEST_URL + '/manga'
  
  def search(self, search_keyword: str) -> list[dict]:
    res = requests.get(f"{REQUEST_URL}/search?name={search_keyword}").text
    soup = BeautifulSoup(res, 'lxml')
    container = soup.find('ul', { 'class': 'post-list' })
    items = container.find_all('a', { 'class': 'manga-cover' })
    
    data = []
    for item  in items:
      data.append({
        'title': ' '.join(item.get('rel')),
        'url': REQUEST_URL + item.get('href'),
        'image': item.find('img').get('src'),
      })

    return data
  
  def get_chapters_list(self, url: str) -> list[dict]:
    data = []
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    chapters = soup.find('ul', { 'class', 'detail-ch-list' }).find_all('a')
    
    for index, chapter in enumerate(chapters[::-1]):
      data.append({
        'chapter': index + 1,
        'title': chapter.text,
        'url': REQUEST_URL +  chapter.get('href')
      })
    
    return data

  def get_manga(self, url: str) -> dict:
    data = {}
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    top = soup.find('div', { 'class': 'manga-detail-top' })
    data['url'] = url
    data['title'] = top.find('div', { 'class': 'title' }).text
    data['image'] = top.find('img').get('src')

    paras = top.find('div', { 'class': 'detail-info' }).find_all('p')
    for para in paras:
      splitted = para.text.strip().split()
      
      if len(splitted) < 2:
        continue

      if 'author' in splitted[0].lower():
        data['author'] = splitted[1]
        
      if 'status' in splitted[0].lower():
        data['status'] = splitted[1]
        
    paras = soup.find('div', { 'class': 'detail-info-middle' }).find_all('p')
    for para in paras:
      splitted = para.text.strip().split()
      
      if len(splitted) < 2:
        continue

      if 'alt' in splitted[0].lower():
        data['alt'] = ', '.join(splitted[2:])

      if 'genre' in splitted[0].lower():
        data['genres'] = ', '.join(splitted[1:])
        
      if 'summary' in splitted[0].lower():
        data['description'] = ' '.join(splitted[1:])
      
    data['chapters'] = self.get_chapters_list(url)

    return data
  
  def get_chapter(self, url: str) -> list[dict]:
    data = []
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    select = soup.find('select', { 'class': 'index-page' })
    options = select.find_all('option')

    for option in options:
      r = requests.get(REQUEST_URL + option.get('value')).text
      s = BeautifulSoup(r, 'lxml')
      
      data.append({
        'page': option.text,
        'title': s.find('div', { 'class': 'title' }).text,
        'url': 'https:' + s.find('img', { 'id': "image" }).get('src'),
      })

    return data
    
  def get_hot_mangas(self) -> list[dict]:
    res = requests.get(f"{REQUEST_URL}/hot").text
    soup = BeautifulSoup(res, 'lxml')
    container = soup.find('ul', { 'class': 'post-list' })
    items = container.find_all('a', { 'class': 'manga-cover' })
    
    data = []
    for item  in items:
      data.append({
        'title': ' '.join(item.get('rel')),
        'url': REQUEST_URL + item.get('href'),
        'image': item.find('img').get('src')
      })

    return data
  

def main() -> None:
  m = MangaTown()
  ...