#! /usr/bin/env python
import re, os
from datetime import datetime

def main():
  print("Hello Python!")
  print(datetime.now().strftime("%y年%m月%d日 %H時%M分%S秒"))
  print(os.getenv("HOME"),os.path.exists(".git"))
  ss = re.sub('\((.+?)\)', r'[\1]', '(name) (address) (telno)') # 2nd param: raw string
  print(ss)
  print("Hello Python!")

  print(datetime.now().strftime("%y年%m月%d日 %H時%M分%S秒"))
  print(f"current time & date: {datetime.now()}")


# this line was added at remote site. 2023/2/2(Thr)

if __name__ == '__main__':
  main()