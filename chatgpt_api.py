import time
import os
import flask
import random
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions as SeleniumExceptions
import markdownify


class chatgpt_api():
    
    def __init__(self, token: str = None) -> None:
        
        self.__token = token
    
    def open_browser(self) -> None:
        options = uc.ChromeOptions()
        self.page = uc.Chrome(options=options, enable_cdp_events=True)
        self.page.execute_cdp_cmd('Network.setCookie',
                            {'domain': 'chat.openai.com',
                            'path': '/',
                            'name': '__Secure-next-auth.session-token',
                            'value': self.__token,
                            'httpOnly': True,
                            'secure': True,
                            },
                            )

        self.page.get('https://chat.openai.com/chat')

        try:
            WebDriverWait(self.page, 5).until(
                EC.presence_of_element_located((By.ID, 'headlessui-portal-root'))
            )
            print('Closing intro')
            self.page.execute_script(
                """
            var element = document.getElementById('headlessui-portal-root');
            if (element)
                element.parentNode.removeChild(element);
            """
            )
            print('Intro dismissed')
        except SeleniumExceptions.TimeoutException:
            print('Did not found intro')
            pass

    def send_message(self, message, lang = None) -> str:
        lang_dict = {'en': 'please reply in English', 'zhcn': '請以簡體中文回答', 'zhtw': '請以繁體中文回答'}
        WebDriverWait(self.page, 3).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )
        textbox = self.page.find_element(By.TAG_NAME, 'textarea')
        if lang:
            if lang in lang_dict:
                textbox.send_keys(lang_dict[lang], message)
        else:
            
            textbox.send_keys(message)
        time.sleep(0.3)
        textbox.send_keys(Keys.ENTER)

        WebDriverWait(self.page, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'result-streaming'))
                )
        WebDriverWait(self.page, 150).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, 'result-streaming'))
        )

        response = self.page.find_elements(
                    By.XPATH, '//div[starts-with(@class, "markdown prose w-full break-words")]'
                )[-1]

        msg = markdownify.markdownify(response.get_attribute('innerHTML')).replace(
            'Copy code`', '`'
        )
        return msg
    
    # def clear_all_tab(self):
        
    
    def reset(self) -> None:
        self.page.find_element(By.LINK_TEXT, 'New chat').click()

    def close(self) -> None:
        self.page.close()