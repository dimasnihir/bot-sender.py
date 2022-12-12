import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SenderService:
    _PAUSE = 2
    _Black_list = []
    _Turn = []

    def __init__(self, email, password):
        self.email = email,
        self.password = password

        self.driver = webdriver.Chrome('./driver/chromedriver.exe')

    def login(self):
        driver = self.driver
        time.sleep(self._PAUSE)

        driver.get('https://victoriyaclub.com/')
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="index-auth-form"]/div[1]/a[2]').click()
        time.sleep(3)

        input_name = driver.find_element(By.XPATH, '//*[@id="index-auth-form"]/div[3]/form/div[1]/input')
        input_pass = driver.find_element(By.XPATH, '//*[@id="index-auth-form"]/div[3]/form/div[2]/input')
        input_name.send_keys(self.email)
        input_pass.send_keys(self.password)

        driver.find_element(By.XPATH, '//*[@id="index-auth-form"]/div[3]/form/button').click()
        time.sleep(5)

    def scanning(self):
        driver = self.driver

        driver.find_element(By.XPATH, '//*[@id="top-header"]/header/div[3]/div/a[1]').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        block_accounts = driver.find_element(By.XPATH, '//*[@id="newchat-online-list"]/div[2]')

        for account in block_accounts.find_elements(By.CLASS_NAME, 'item'):
            print(account.get_attribute('style'))



Sender = SenderService('lali_pap30@ukr.net', 'Masya1')
Sender.login()
Sender.scanning()



