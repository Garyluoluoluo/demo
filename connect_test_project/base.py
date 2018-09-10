# -*- coding: gb2312 -*- 
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Action(object):

    #��ʼ��driver��url����
    def __init__(self, selenium_driver, base_url, pagetitle):
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.driver = selenium_driver
     
     #��ҳ�棬У��ҳ�������Ƿ������ȷ
    def _open(self, url, pagetitle):
     #ʹ��get�򿪷������ӵ�ַ
        self.driver.get(url)
        self.driver.maximize_window()
     #ʹ��assert����У�飬�򿪵����ӵ�ַ�Ƿ������õĵ�ַһ�¡�����on_page()����
        assert self.on_page(pagetitle), u"�򿪿�ҳ��ʧ�� %s"% url
     
     #��дԪ�ض�λ����
    def find_element(self,*loc):
     #return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print(u"%s ҳ����δ���ҵ� %s Ԫ��"%(self, loc))
     
     #��дswitch_frame����
    def switch_frame(self,*loc):
        self.driver.switch_to.frame(self.find_element(*loc))
     #����open����������_open()���д�����
     
    def open(self):
        self._open(self.base_url, self.pagetitle)
     
     #ʹ��current_url��ȡ��ǰ����Url��ַ�����������õ�ַ���Ƚϣ����رȽϽ����True False��
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title
     
     #����script����������ִ��js�ű�����Χִ�н��
    def script(self, src):
        self.driver.execute_script(src)
     
     #��д����send_keys����
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self,"_%s"% loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except:
         print (u"%s ҳ����δ���ҵ� %s Ԫ��"%(self, loc))