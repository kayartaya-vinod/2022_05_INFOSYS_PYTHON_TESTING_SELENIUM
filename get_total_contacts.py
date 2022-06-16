from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def main():
    os.environ['PATH'] += os.pathsep + '/Users/vinod/Desktop/selenium-drivers'
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('http://localhost:3000')

    # XPATH --> //div[@class="card-body"]/h5[@class="card-title"]
    # CSS   --> div.card-body > h5.card-title
    # elements = driver.find_elements(By.XPATH, '//div[@class="card-body"]/h5[@class="card-title"]')

    elements = driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
    print(f'Type of elements is {type(elements)}')
    print(f'There are {len(elements)} contacts in our addressbook')

    driver.quit()


if __name__ == '__main__':
    main()
