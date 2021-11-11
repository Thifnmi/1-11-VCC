from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread, Lock
import concurrent.futures
# from multiprocessing import Process
import time
import csv
import re


# browser = None
links = []
urls = []
lock = Lock()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")

browser = webdriver.Chrome(
    executable_path='chromedriver.exe', chrome_options=options)
browser.maximize_window()


def gen_url(num):
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc/trang-"+str(num)+".htm"
    print(url)
    urls.append(url)


def get_total_page(browser, options):
    url = "https://bizflycloud.vn/tin-tuc/tin-tuc.htm"
    browser = webdriver.Chrome(
        executable_path='chromedriver.exe', chrome_options=options)
    browser.get(url)
    browser.maximize_window()
    total_page = browser.find_element_by_class_name("total-page").text
    return int(total_page)


def get_link(browser, url):
    with lock:
        browser.get(url)
        print(url)
        # posts = browser.find_elements_by_class_name("blog-highlight")
        # for post in posts:
        link_tag = browser.find_elements_by_class_name("entry-title")
        for link in link_tag:
            if link.get_attribute("href") not in links:
                print(f'get {link.get_attribute("href")} from {url}')
                links.append(link.get_attribute("href"))


def get_link1(browser, url):
    # global browser
    browser.get(url)
    print(url)
    # posts = browser.find_elements_by_class_name("blog-highlight")
    # for post in posts:
    link_tag = browser.find_elements_by_class_name("entry-title")
    for link in link_tag:
        if link.get_attribute("href") not in links:
            print(f'get {link.get_attribute("href")} from {url}')
            links.append(link.get_attribute("href"))


def get_linkkk(browser, options, links):
    print("runnnnnn")
    for i in range(1, int(get_total_page(browser, options))+1):
        url = "https://bizflycloud.vn/tin-tuc/tin-tuc/trang-"+str(i)+".htm"
        print(url)
        browser.get(url)
        link_tag = browser.find_elements_by_class_name("entry-title")
        for link in link_tag:
            if link.get_attribute("href") not in links:
                links.append(link.get_attribute("href"))
    print(len(links))


def write_file(file_name, data):
    print(f"Start write file name {file_name}")
    header = ['name', 'title', 'content', 'created date', 'url']
    with open(file_name, "w", encoding="utf-8", newline="") as file:
        write_hander = csv.writer(file)
        write_hander.writerow(header)
        write_hander.writerow(data)
    # file.close()
    print(f"Done file {file_name}")


# name/title, content, created date, url
def crawler(browser, link):
    print(f"recived link: {link}")
    with lock:
        print(f"get link: {link}")
        browser.get(link)
        title = browser.find_element_by_class_name("page-title-content").text
        # delimiters = '. ', ' ', '?', '! ', '(', ')', ': ', ' - ', '"', '/', ' | '
        # regex_pattern = "|".join(map(re.escape, title))
        # file_name = "_".join(re.split(regex_pattern, title))
        file_name = re.sub('\W+', '', title)
        # file_name = "".join(e for e in title if e.isalnum())
        file_name = "result\\" + file_name + ".csv"
        name = browser.find_element_by_class_name("author").text
        created_date = browser.find_element_by_class_name("read-time").text
        content_tag = browser.find_element_by_class_name("detail-content")
        contents = content_tag.find_elements_by_tag_name("p")
        contents = (content.text for content in contents)
        content = " ".join(content for content in contents if content)
        data = (name, title, content, created_date, link)
        write_file(file_name, data)


def crawler1(browser, link):
    print(f"recived link: {link}")
    print(f"get link: {link}")
    browser.get(link)
    title = browser.find_element_by_class_name("page-title-content").text
    file_name = re.sub('\W+', '', title)
    # file_name = "".join(e for e in title if e.isalnum())
    file_name = "result\\" + file_name + ".csv"
    name = browser.find_element_by_class_name("author").text
    created_date = browser.find_element_by_class_name("read-time").text
    content_tag = browser.find_element_by_class_name("detail-content")
    contents = content_tag.find_elements_by_tag_name("p")
    contents = (content.text for content in contents)
    content = " ".join(content for content in contents if content)
    data = (name, title, content, created_date, link)
    write_file(file_name, data)


def crawler_with_thread(browser, links):
    threads = []
    t1 = time.perf_counter()
    for link in links:
        t = Thread(target=crawler1, args=(browser, link, ))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print(f"Done crawler with thread in {time.perf_counter() - t1} second(s)")


get_linkkk(browser, options, links)
crawler_with_thread(browser, links)


def pro():
    # total_page = int(get_total_page(options))+1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gen_url, range(1, get_total_page(browser, options)+1))
        # executor.map(gen_url, range(1, get_total_page(options)+1))
        # for page in total_page:
        #     executor.submit(gen_url, str(page))

    # for url in urls:
    #     print(url)
    # urls = [url for url in urls]
    with concurrent.futures.ProcessPoolExecutor() as executor1:
        executor1.map(get_link1, browser, urls)
        # for url in urls:
        #     executor1.submit(get_link, url)
    print(urls)
    print(links)
    # print(len(urls), len(links))

    t1 = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor2:
        executor2.map(crawler1, browser, links)
        # for link in links:
        #     executor2.submit(crawler, link)

    print(f"{time.perf_counter() - t1} seconds")


def thre():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(gen_url, range(1, get_total_page(options)+1))

    with concurrent.futures.ThreadPoolExecutor() as executor1:
        for url in urls:
            executor1.submit(get_link, args=(browser, url))
    print(urls)
    print(links)
    print(len(urls), len(links))

    t1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor2:
        for link in links:
            executor2.submit(crawler, args=(browser, url))

    print(f"{time.perf_counter() - t1} seconds")


# pro()
# thre()
