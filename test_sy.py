import unittest
from time import sleep

from selenium import webdriver

url = 'https://testerhome.com/'


class test_testerhome_sy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
    def tearDown(self):
        print('测试完成现在退出')
        self.driver.quit()
    def test_opensy(self):
        sleep(3)
    def test_click_gg(self):
        self.driver.find_element_by_xpath("/html/body[@class='page-home']/div[@id='main']/div[@class='panel panel-default']/a/img/@src").click()





if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_testerhome_sy)
    unittest.TextTestRunner(verbosity=2).run(suite)