import unittest
from time import sleep
from selenium import webdriver
import yaml

url = 'https://testerhome.com/'

class test_testerhome_sy(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(3)
    def tearDown(self):
        print('测试完成现在退出')
        self.driver.quit()
    #def test_1opensy(self):
        #sleep(2)
    def test_2click_gg(self):
        sleep(2)
        #在这里用xpath找不到该元素，
        #self.driver.find_element_by_xpath("/html/body[@class='page-home']/div[@id='main']/div[@class='panel panel-default']/a/img/@src").click()
        #测试xpath是否有效==有效
        #self.driver.find_element_by_xpath("/html/body[@class='page-home']/div[@id='main']/div[@class='row']/div[@class='col-md-9 home-main']/div[@class='home_suggest_topics panel panel-default'][2]/div[@class='panel-heading']/div[@class='pull-right']/a").click()
        #通过tag_name定位
        self.driver.find_element_by_tag_name('img').click()
       #切换到新窗口
       # nowhandle = self.driver.current_window_handle
        #allhandles = self.driver.window_handles
        #for handle in allhandles:
         #   if(handle != nowhandle):
          #      self.driver.switch_to_window(handle)
    def test_3click_Stick(self):
        #点击其中一个帖子

       # Stick_all=self.driver.find_element_by_class_name('panel-body topics row')
        pass



if __name__ =='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_testerhome_sy)
    unittest.TextTestRunner(verbosity=2).run(suite)