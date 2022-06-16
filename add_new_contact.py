import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    os.environ['PATH'] += os.pathsep + '/Users/vinod/Desktop/selenium-drivers'
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000')

    # get a reference to the input element with id 'name'
    name_tf = driver.find_element(By.ID, 'name')
    name_tf.send_keys('Vinod Kumar K')

    email_tf = driver.find_element(By.NAME, 'email')
    email_tf.send_keys('vinod@vinod.co')

    phone_tf = driver.find_element(By.CSS_SELECTOR, 'input[type=tel]')
    phone_tf.send_keys('9731424784')

    avatar_tf = driver.find_element(By.XPATH, '//input[@type="avatar"]')
    avatar_tf.send_keys('https://avatars.githubusercontent.com/u/14976510?v=4')

    submit_btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[type=submit]')
    submit_btn.click()

    time.sleep(10)




if __name__ == '__main__':
    main()
