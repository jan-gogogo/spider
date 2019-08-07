import os
import time

from bs4 import BeautifulSoup

from app.chromedriver import ChromeDriver


def fetch_detail_urls(url):
    # 设置浏览器窗口大小分别为width,height
    # 高度设置为10000，是因为页面内容是懒加载，所以需要把他们全部加载出来
    # 请求时间最长90秒
    # 避免页面的JS未执行完就关闭了浏览器，这里适当sleep2秒
    # 优化获取回来的HTML代码
    driver = ChromeDriver(1000, 10000, 90).driver
    driver.get(url)
    time.sleep(2)
    source = BeautifulSoup(driver.page_source, 'lxml')

    urls = []
    a_list = source.select('a[href*="/mycryptoheroes/"]')
    for a in a_list:
        if a.find('div') is None:
            continue
        print(a['href'])
        urls.append(a['href'])

    return urls


def resolving():
    urls = fetch_detail_urls('https://medium.com/@asano_62722')
    driver = ChromeDriver(1000, 12000, 90).driver
    try:
        for url in urls:
            driver.get('https://medium.com' + url)
            time.sleep(2)
            source = BeautifulSoup(driver.page_source, 'lxml')
            section = source.find('article').find_all('section')[1]

            # 获取标题
            h1 = section.find('h1')
            if h1 is None:
                title = section.find("strong").text
            else:
                title = h1.text if (h1.find('strong') is None) else h1.find('strong').text

            print("标题:", title)
            # 获取内容
            content = str(section)
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()  # 退出浏览器
        os.system('ps -ef | grep chrome | grep -v grep | awk \'{print "kill -9 "$2}\'|sh')  # 强制杀掉进程


resolving()
