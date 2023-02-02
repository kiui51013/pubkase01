## git command output without pager
```
$ git --no-pager <git command> <options>
or
$ export GIT_PAGER=cat
or 
$ LESS="-F -X $LESS"
```
--

## how to know python version in ipython.
> get_ipython().system("python --version")

## scrapy for nipponkyo
```
Python WebDriver:
 geckodriver exists in /usr/local/bin
 chromedriver exists in /usr/local/bin
```

```
from selenium import webdriver
driver = webdriver.Firefox() # loaded from search path
driver.get(_url)
```
