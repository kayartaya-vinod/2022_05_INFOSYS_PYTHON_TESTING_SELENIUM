from selenium import webdriver
import os


if __name__ == '__main__':
    os.environ['PATH'] += os.pathsep + '/Users/vinod/Desktop/selenium-drivers'  # path to executables
    # path += os.pathsep + 'c:\\users\\vinod.kumar\\desktop\\selenium-drivers'

    driver = webdriver.Chrome()  # open chrome browser
    driver.get('https://vinod.co')  # visit this site in the browser
    title = driver.title  # access the current browser's title
    driver.quit()  # close all browser sessions and quit the browser
    print(f'Title of the website visited is "{title}"')
