import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class TestReactAddressBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        os.environ['PATH'] += os.pathsep + '/Users/vinod/Desktop/selenium-drivers'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_should_add_new_contact(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_before = len(elements)

        self.driver.find_element(By.ID, 'name').send_keys('Vinod Kumar K')
        self.driver.find_element(By.NAME, 'email').send_keys('vinod@vinod.co')
        self.driver.find_element(By.CSS_SELECTOR, 'input[type=tel]').send_keys('9731424784')
        self.driver.find_element(By.XPATH, '//input[@type="avatar"]').send_keys('https://avatars.githubusercontent.com/u/14976510?v=4')
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[type=submit]').click()

        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_after = len(elements)

        self.assertEqual(count_after, count_before+1)

    def test_should_not_add_contact_without_name(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_before = len(elements)

        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[type=submit]').click()
        alert = Alert(self.driver)  # from selenium.webdriver.common.alert import Alert
        # print(alert.text) # --> "Name is mandatory"
        alert.accept()  # dismiss the alert dialog by clicking on the "OK" button

        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_after = len(elements)

        self.assertEqual(count_after, count_before)

    def test_should_delete_first_contact(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_before = len(elements)

        # //button[@class="btn text-danger btn-link"]
        # button.btn.btn-link.text-danger
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-link.text-danger').click()
        confirm_dialog = Alert(self.driver)
        confirm_dialog.accept()

        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_after = len(elements)

        self.assertEqual(count_after, count_before-1)

    def test_should_not_delete_first_contact(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_before = len(elements)

        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-link.text-danger').click()
        confirm_dialog = Alert(self.driver)
        confirm_dialog.dismiss()

        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.card-body > h5.card-title')
        count_after = len(elements)

        self.assertEqual(count_after, count_before)


if __name__ == '__main__':
    unittest.main()
