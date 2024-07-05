import requests
import base64

def extract_data(source: list, keys: dict) -> list[dict]:
  """ Returns a new list based on old list"""
  try:
    return [
      {
        'title': i.get(keys.get('title') or 'title'),
        'url': i.get(keys.get('url') or 'url'),
        'image': i.get(keys.get('image`') or 'image'),
        'id': i.get(keys.get('id') or 'id'),
      } for i in source
    ]
  except:
    return []
  

def get_image(url: str, referer: str):
  """ Fetch the chapter image """
  image = requests.get(url, headers={ 'referer': referer })
  return base64.b64encode(image.content).decode('utf-8')