from selenium import webdriver
from time import sleep
import unittest


class OrangeToolz(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:\selenium\chromedriver_win32\chromedriver.exe')
        cls.driver.get('http://159.89.38.11/login')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_page(self):
        self.driver.get('http://159.89.38.11/login')
        print("User landed into the Login Page")
        self.driver.implicitly_wait(5)

    def test_dashboard_page(self):
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]").send_keys(
            "test@orangetoolz.com")
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]").send_keys(
            "8Kh8nTe*^jdk")
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]").click()
        print("User landed into the Dashboard")
        sleep(5)

    def test_personal_profile(self):
        self.driver.get('http://159.89.38.11/profile')
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li["
            "1]/a[1]").click()
        print("User landed into the Personal Profile information page")
        sleep(5)

    def test_personal_info_update(self):
        # First Name
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]").click()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]").clear()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]").send_keys(
            "Allen")
        sleep(2)
        # Last Name
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]").click()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]").clear()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys(
            "Parker")
        sleep(2)
        # Phone Number
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[4]/div[1]/input[1]").click()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[4]/div[1]/input[1]").clear()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[4]/div[1]/input[1]").send_keys(
            "+1987454987")
        sleep(2)
        # Address
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[5]/div[1]/textarea[1]").click()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[5]/div[1]/textarea[1]").clear()
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[5]/div[1]/textarea[1]").send_keys(
            "12 Madani Ave, Dhaka 1212")
        # Save Changes
        self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div["
            "1]/div[1]/div[1]/form[1]/div[6]/div[1]/button[1]").click()
        print("Update Personal Profile Information")
        sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
