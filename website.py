from selenium import webdriver

class Website:
    ancList = []
    url = "" 
    i = 0
    def __init__(self):
        pass

    def goto(self):
        """
        Goes to website
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)
        self.navigate()

class LusakaTimes(Website):
    url =  "https://www.lusakatimes.com/"
    def __init__(self):
        super().__init__()
        self.goto()

    def navigate(self):
        driver = self.driver
        element = driver.find_elements_by_tag_name('h3')
        while self.i < 4:
            anchorElement = element[self.i].find_element_by_tag_name('a')
            text = element[self.i].text
            href = anchorElement.get_attribute("href")
            ancDict = {'text': text, 'href': href}
            self.ancList.append(ancDict)
            self.i+=1

class ZambianWatchdog(Website):
    url =  "https://www.zambiawatchdog.com/"
    def __init__(self):
        super().__init__()
        self.goto()

    def navigate(self):
        driver = self.driver
        ele = driver.find_elements_by_class_name("item-main")
        while self.i < 7:
            el2 = ele[self.i].find_element_by_class_name("item-content")
            element = el2.find_element_by_class_name("item-title")
            anchorElement = element.find_element_by_tag_name('a')
            ancText = anchorElement.text
            ancHref = anchorElement.get_attribute("href")
            ancDict = {"text": ancText, "href": ancHref}
            self.ancList.append(ancDict)
            self.i+=1

class ZambianObserver(Website):
    url = "https://www.zambianobserver.com/"
    def __init__(self):
        super().__init__()
        self.goto()
    
    def navigate(self):
        driver = self.driver
        eles = driver.find_elements_by_class_name("td-module-thumb")
        for ele in eles:
            anchorElement = ele.find_element_by_tag_name('a')
            title = anchorElement.get_attribute('title')
            href = anchorElement.get_attribute('href')
            ancDict = {"title": title, "href": href}
            self.ancList.append(ancDict)