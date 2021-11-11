from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--headless")


def instance(options, link):
    browser = webdriver.Chrome(
        executable_path='chromedriver.exe', chrome_options=options)
    browser.maximize_window()
    browser.get(link)


img_urls = [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]

print(img_urls[6])
# threads = []
# for url in img_urls:
#     t = Thread(target=instance, args=(options, url, ))
#     t.start()
#     threads.append(t)


# for thread in threads:
#     thread.join()
