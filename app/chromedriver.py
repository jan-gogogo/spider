from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class ChromeDriver:

    def __init__(self, window_w=None, window_h=None, wait_sec=None):
        """
        构建chrome driver
        :param window_w: 设置窗口宽度
        :param window_h: 设置窗口高度
        :param wait_sec: 最大等待时间，单位：秒
        """
        # dirver_path = "/Users/jan/spider/chromedriver"  # driver的目录
        dirver_path = "/opt/python/chromedriver"  # driver的目录
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')  # 无界面运行，必须
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dirver_path)
        driver.set_window_size(window_w, window_h)
        driver.implicitly_wait(wait_sec)
        self.driver = driver
