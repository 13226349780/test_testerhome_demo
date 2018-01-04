import unittest
from time import sleep

from selenium import webdriver

url = 'https://testerhome.com/'


class test_testerhome_sy(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        driver.get(url)

    def test_opensy(self):
        sleep(3)
        #driver = webdriver.Chrome()
        #driver.get(url)
    def test_click_gg(self):
        pass
    def tearDown(self):
        print('测试完成现在退出')
        quit()



if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_testerhome_sy)
    unittest.TextTestRunner(verbosity=2).run(suite)