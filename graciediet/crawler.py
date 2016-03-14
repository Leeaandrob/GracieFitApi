# coding: utf-8
from selenium import webdriver
# from pyvirtualdisplay import Display


class CrawlerCalories(object):
    def __init__(self):
        # self.display = Display(visible=0, size=(1024, 768))
        # self.display.start()
        self.browser = webdriver.Chrome()

    def start(self):
        self.browser.get(
            'http://graciediet.com.br/food-groups/index.php')

    def get_all_trs(self):
        elements = self.browser.find_elements_by_xpath('//tr')
        trs = elements[8:][:37]
        return trs

    def prepare_informations(self, trs):
        pre_informations = {}
        list_info = []

        for tr in trs:
            pre_informations.update({
                tr.text.split('\n')[0]: tr.text.split('\n')[1].strip()})

        for j, k in pre_informations.items():
            list_info.append(Calories(activity=j, calories_per_hour=k))

        return list_info

    def save_informations(self, informations):
        Calories.objects.bulk_create(informations)

    def run(self):
        self.start()
        trs = self.get_all_trs()
        info = self.prepare_informations(trs)
        self.save_informations(info)
        self.browser.close()

