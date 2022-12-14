import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="index-auth-form"]/div[1]/a[2]').click()
        time.sleep(2)

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

        while True:
            print('Обновляем..\n')
            time.sleep(3)
            for account in block_accounts.find_elements(By.CLASS_NAME, 'item'):
                if account.get_attribute('style') == 'display: block;':

                    account.click()
                    time.sleep(2)

                    user_id = account.get_attribute('data-user-id')
                    textarea = driver.find_element(By.ID, 'textarea-message-' + user_id)
                    massage = 'Hello. I am preparing a christmas tree gift for you. For a long time I thought what to give you and decided that the best gift for you will be me. Now I am looking for a suitable box to climb into it)'
                    textarea.send_keys(massage)
                    textarea.send_keys(Keys.ENTER)
                    break


Sender = SenderService('lali_pap30@ukr.net', 'Masya1')
Sender.login()

Sender.scanning()



