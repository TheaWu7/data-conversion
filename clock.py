import datetime
import time

from pixso import crawler

# 这里可以设置每天爬取的时间
def main(h=19, m=46):
 while True:
  now = datetime.datetime.now()
  print(now.hour, now.minute)
  if now.hour == h and now.minute == m:
   break
  time.sleep(60)
 crawler()

main()
