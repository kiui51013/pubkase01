import sys, re, os, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path

home_dir = 'http://nipponkyo.or.jp/archive/sankankusyu_jisyu/'
max_page = 12 # max page + 1
txt_dir = 'jisyu3'
htm_dir = f'{txt_dir}/htm'
Path(txt_dir).mkdir(exist_ok=True)
Path(htm_dir).mkdir(exist_ok=True)

def file_url(argv):
  if len(argv) == 1:
    print(f'one argument in 1 ~ {max_page} required!')
    exit()
  if not re.search(r'\d{1,2}', argv[1]):
    print(f'parameter must be Numeric in 1 ~ {max_page}')
    exit()
  page = int(argv[1])
  if page < 1 or page > max_page:
    print(f'parameter must be Numeric in 1 ~ {max_page}')
    exit()

  _file = '{}/{:0>3}.txt'.format(txt_dir,page)

# https://nipponkyo.or.jp/archive/sankankusyu_jisyu/2/
  if page == 1:
    _url = home_dir
  else:
    _url = '{}{:d}/'.format(home_dir,page)

  return _file, _url

def file_url_(page):
  _file = '{}/{:0>3}.txt'.format(txt_dir, page)

  if page == 1:
    _url = home_dir
  else:
    _url = '{}{:d}/'.format(home_dir,page)

  return _file, _url

def url2html(_file, _url):
  driver = webdriver.Firefox()
  driver.get(_url)
  ## assert "Python" in driver.title
  elem = driver.find_element_by_name("password_protected_pwd")
  elem.clear()
  elem.send_keys(os.getenv("HANAKAGO"))
  elem.send_keys(Keys.RETURN)
  WebDriverWait(driver=driver, timeout=20).until(EC.presence_of_element_located((By.CLASS_NAME, 'wp-block-group__inner-container')))
  content = driver.find_element_by_class_name('wp-block-group__inner-container')
  print(content)
  # sleep(3)
  html = driver.page_source
  print("length", len(html))
  with open(htm_dir + "/" + os.path.basename(_file).replace(".txt",".htm"), 'w') as f:
    f.write(html)
  
  driver.close()
  driver.quit()
  
  return html

def html2txt(html,file2):
  m = re.search('<div class="wp-block-group__inner-container">(.*?)</div>', html, flags= re.DOTALL|re.MULTILINE)
  data = m.group(1)
  lines = re.findall('<p>(.*?)</p>', data)
  print('>' * 10, datetime.datetime.now())
  with open(file2, 'w') as f:
    for line in lines:
      line = re.sub(r"</{0,1}rp>", "", line)
      ku = re.sub('<rt>(.*?)</rt>',r'(\1)', re.sub(r'<ruby>(.*?)</ruby>', r'\1',line)).replace('<br>', '\n')
      # ku = re.sub('<ruby>(.*?)<rt>(.*?)</rt></ruby>', r'\1(\2)', line).replace('<br>', '\n')
      f.write(ku + '\n')
      f.write('-' * 80 + '\n')

if __name__ == '__main__':
  for page in range(1, max_page + 1):
    _file, _url = file_url_(page)
    # file = re.sub("\.html", ".txt", _file)
    print("_file:", _file, "_url:", _url)
    html = url2html(_file, _url)
    html2txt(html,_file)
