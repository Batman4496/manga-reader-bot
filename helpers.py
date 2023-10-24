import base64
import requests
import zlib
import random
import os
import io

def encode(input_string):
    # Encode the input string to Base64
    return str(zlib.compress(input_string.encode('utf-8')))

def decode(encoded_string):
    byte_str = encoded_string[2:-1]
    bytes_data = bytes(byte_str, 'utf-8')
    return zlib.decompress(bytes_data, 'utf-8')

def get_key(url: str) -> str:
    key = url.strip().split('/')[-1]
    return key

def download_image(url: str, referer) -> str:
    req = requests.get(url, headers={
        'referer': referer
    })
    name =  str(random.randint(100000, 9999999)) + '.jpg'

    with open(f"temp/{name}", "wb") as f:
        f.write(req.content)

    return name


def remove_image(name: str) -> bool:
    os.remove(f'temp/{name}')
    return True


  

def get_image(url: str, referer: str):
  """ Fetch the chapter image """
  image = requests.get(url, headers={ 'referer': referer })
  base = base64.b64encode(image.content).decode('utf-8')
  _bytes = io.BytesIO(base64.b64decode(base))
  
  return _bytes


if __name__ == '__main__':
  image = get_image('https://avt.mkklcdnv6temp.com/33/a/16-1583494657.jpg', 'https://readmangabat.com/')
  print(image)