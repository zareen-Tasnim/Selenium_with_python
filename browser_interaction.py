from selenium import webdriver


class BrowserInteraction():

    def web_info(self):
        baseurl = "https://ultimateqa.com/automation"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.maximize_window()
        title = driver.title
        url = driver.current_url
        print(f"Title of the page is {title}")
        print(f"Url of the page is {url}")
        driver.implicitly_wait(2)
        driver.quit()


if __name__ == "__main__":
    BrowserInteraction().web_info()

