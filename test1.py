#! /usr/bin/env python
import re, os
<<<<<<< HEAD
from datetime import datetime

print("Hello Python!")
print(datetime.now().strftime("%y年%m月%d日 %H時%M分%S秒"))
print(os.getenv("HOME"),os.path.exists(".git"))
ss = re.sub('\((.+?)\)', r'[\1]', '(name) (address) (telno)') # 2nd param: raw string
print(ss)
=======
print("Hello Python!")
>>>>>>> 238b2fb (Starting here ...)
