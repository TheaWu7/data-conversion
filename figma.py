import requests
from bs4 import BeautifulSoup


def crawler():
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

  response = requests.get('https://releases.figma.com/', headers=headers).content
  soup = BeautifulSoup(response, 'html.parser')

  file = open('./figma.txt', 'a')

  # 一次更新内容
  updateLogs = soup.find_all('div', class_="date-outer")
  for updateLog in updateLogs:
    # 更新时间
    times = updateLog.find_all("h2")
    for time in times:
      timeData = time.text
      file.write(timeData)

    # 更新 wrapper
    updateWrappers = updateLog.find_all('div',class_='post')
    for updateWrapper in updateWrappers:
      # 标题信息 
      titles = updateWrapper.find_all('h3')
      for title in titles:
        # 标题名称
        titleData = title.text
        file.write(titleData)

      # 更新内容
      contents = updateWrapper.find_all('div', class_="post-body")
      for content in contents:
        contentData = content.text
        file.write(contentData)
        file.write('------')
        file.write('\n\n')

crawler()
