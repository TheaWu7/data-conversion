import requests
from bs4 import BeautifulSoup


def crawler():
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

  response = requests.get('https://pixso.cn/releases/', headers=headers).content
  soup = BeautifulSoup(response, 'html.parser')

  scripts = soup.find_all('script')
  for script in scripts:
    if 'const releaseList = [{' in str(script):
      content = str(script)[31:-9]

  open('./pixsoLog.json','w').write(str(content))
  print(u'开始爬！')
